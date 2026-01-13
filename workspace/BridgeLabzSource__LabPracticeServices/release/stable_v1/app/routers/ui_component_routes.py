from fastapi import APIRouter, Depends, Query, status, HTTPException
from app.config.database import get_db
from sqlalchemy.orm import Session
from typing import List
from app.models.ques_model import Programme, QuestionType, AnswerType, Difficulty, Subtopic, Question
from sqlalchemy import func

ui_component_router = APIRouter(prefix="/components", tags=["Ui Components"])

@ui_component_router.get("/mentor-page-dropdown-data")
def get_question_metadata(db: Session = Depends(get_db)):
    try:
        # --------------------------------------------------------
        # Fetch all counts grouped by hierarchy + difficulty
        # --------------------------------------------------------
        raw_counts = (
            db.query(
                Question.programme_id,
                Question.module_id,
                Question.topic_id,
                Question.subtopic_id,
                Question.difficulty,
                func.count(Question.id)
            )
            .group_by(
                Question.programme_id,
                Question.module_id,
                Question.topic_id,
                Question.subtopic_id,
                Question.difficulty
            )
            .all()
        )

        # Lookup maps
        subtopic_map = {}      # sub_id → {difficulty: count}
        topic_map = {}         # topic_id → {difficulty: count}
        module_map = {}        # module_id → {difficulty: count}
        programme_map = {}     # programme_id → {difficulty: count}

        def add_to_map(map_obj, key, difficulty, count):
            if key not in map_obj:
                map_obj[key] = {"EASY": 0, "MEDIUM": 0, "HARD": 0}
            map_obj[key][difficulty] += count

        # Fill maps
        for prog_id, mod_id, topic_id, sub_id, diff, cnt in raw_counts:
            add_to_map(subtopic_map, sub_id, diff.value, cnt)
            add_to_map(topic_map, topic_id, diff.value, cnt)
            add_to_map(module_map, mod_id, diff.value, cnt)
            add_to_map(programme_map, prog_id, diff.value, cnt)

        # --------------------------------------------------------
        # Nested hierarchy response
        # --------------------------------------------------------
        programmes = db.query(Programme).all()

        programme_data = []
        for prog in programmes:

            modules_data = []
            for mod in prog.modules:

                topics_data = []
                for topic in mod.topics:

                    subtopics_data = [
                        {
                            "id": sub.id,
                            "name": sub.name,
                            "question_count": sum(subtopic_map.get(sub.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0}).values()),
                            "difficulty_breakdown": subtopic_map.get(sub.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0})
                        }
                        for sub in topic.subtopics
                    ]

                    topics_data.append({
                        "id": topic.id,
                        "name": topic.name,
                        "question_count": sum(topic_map.get(topic.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0}).values()),
                        "difficulty_breakdown": topic_map.get(topic.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0}),
                        "subtopics": subtopics_data
                    })

                modules_data.append({
                    "id": mod.id,
                    "name": mod.name,
                    "question_count": sum(module_map.get(mod.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0}).values()),
                    "difficulty_breakdown": module_map.get(mod.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0}),
                    "topics": topics_data
                })

            programme_data.append({
                "id": prog.id,
                "name": prog.name,
                "question_count": sum(programme_map.get(prog.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0}).values()),
                "difficulty_breakdown": programme_map.get(prog.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0}),
                "modules": modules_data
            })

        return {
            "message": "Fetched Content for UI",
            "payload": {
                "programmes": programme_data,
                "question_types": [qt.value for qt in QuestionType],
                "answer_types": [at.value for at in AnswerType],
                "difficulty_levels": [d.value for d in Difficulty]
            },
            "status": 200,
        }

    except Exception as e:
        return {
            "message": f"Error in fetching dropdown data: {e}",
            "payload": [],
            "status": 500
        }
