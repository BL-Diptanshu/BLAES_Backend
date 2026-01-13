from sqlalchemy.orm import Session
from app.models.ques_model import Question,Programme
from sqlalchemy import func

def get_ques_count_levelwise_for_dropdown(db:Session):
    raw_counts = (
            db.query(
                Question.programme_id,
                Question.module_id,
                Question.submodule_id,
                Question.difficulty,
                func.count(Question.id)
            )
            .group_by(
                Question.programme_id,
                Question.module_id,
                Question.submodule_id,
                Question.difficulty
            )
            .all()
        )

    programme_map = {}   
    module_map = {} 
    submodule_map = {} 

    def add_to(map_obj, key, difficulty, count):
        if key not in map_obj:
            map_obj[key] = {"EASY": 0, "MEDIUM": 0, "HARD": 0}
        map_obj[key][difficulty] += count

    for prog_id, mod_id, sub_id, diff, cnt in raw_counts:
        add_to(programme_map, prog_id, diff.value, cnt)
        add_to(module_map, mod_id, diff.value, cnt)
        add_to(submodule_map, sub_id, diff.value, cnt)

    # --------------------------------------------------------
    # Final nested structure
    # --------------------------------------------------------
    programmes = db.query(Programme).all()

    programme_data = []

    for prog in programmes:
        modules_data = []

        for mod in prog.modules:
            submodules_data = []

            for sub in mod.submodules:
                breakdown = submodule_map.get(sub.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0})

                submodules_data.append({
                    "id": sub.id,
                    "name": sub.name,
                    "question_count": sum(breakdown.values()),
                    "difficulty_breakdown": breakdown
                })

            mod_breakdown = module_map.get(mod.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0})

            modules_data.append({
                "id": mod.id,
                "name": mod.name,
                "question_count": sum(mod_breakdown.values()),
                "difficulty_breakdown": mod_breakdown,
                "submodules": submodules_data
            })

        prog_breakdown = programme_map.get(prog.id, {"EASY": 0, "MEDIUM": 0, "HARD": 0})

        programme_data.append({
            "id": prog.id,
            "name": prog.name,
            "question_count": sum(prog_breakdown.values()),
            "difficulty_breakdown": prog_breakdown,
            "modules": modules_data
        })
    return programme_data