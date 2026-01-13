# import time
# import json
# from celery import shared_task
# from sqlalchemy.exc import SQLAlchemyError
# # from app.utils.celery_utils import celery, logger
# from app.core.celery_app import celery
# from app.config.database import SessionLocal
# from app.models.testcase_model import TestCase
# from app.schemas.testcase_schema import GeminiTestCaseResponse
# from app.utils.async_utils import run_async_safely
# from app.utils.code_utils import extract_json_from_model_output
# from app.agents.test_case_generator import test_case_gen_agent
# from app.templates.prompts import TESTCASE_GENERATION_PROMPT
# from app.config.logger import AppLogger

# logger = AppLogger.get_logger()


# @celery.task(bind=True, max_retries=3, default_retry_delay=10, name="app.tasks.testcase_tasks.generate_test_cases_task")
# # @shared_task(bind=True, max_retries=3, default_retry_delay=10, name="app.tasks.testcase_tasks.generate_test_cases_task")
# def generate_test_cases_task(self, question_id: str, question_text: str, language: str):
#     """
#     Celery Task:
#     Generate test cases using Test Case Generator Agent for a given coding question.
#     - Runs safely in async context
#     - Retries on transient errors
#     """
#     db = SessionLocal()
#     task_id = self.request.id

#     logger.info(f"[{task_id}] Task received for Question ID: {question_id}")
#     start_time = time.time()

#     try:
#         # -------------------------------
#         # STEP 1: Build Prompt
#         # -------------------------------
#         prompt = TESTCASE_GENERATION_PROMPT.format(
#             question_text=question_text, language=language
#         )
#         logger.info(f"[{task_id}] Sending prompt to Gemini for {language} question")

#         # -------------------------------
#         # STEP 2: Run Gemini Agent safely
#         # -------------------------------
#         response = run_async_safely(test_case_gen_agent.run, prompt)
#         if not hasattr(response, "output"):
#             raise ValueError("Gemini agent returned no output attribute")

#         # -------------------------------
#         # STEP 3: Extract JSON from output
#         # -------------------------------
#         text_output = extract_json_from_model_output(response.output)
#         # text_output = text_output.replace("\n", " ").replace("\'", "'")
#         logger.info(f"text_output-->{text_output}")
#         try:
#             parsed = json.loads(text_output)
#         except json.JSONDecodeError as e:
#             logger.error(f"[{task_id}] Invalid JSON returned from Gemini: {e}")
#             raise ValueError("Gemini returned invalid JSON")

#         if not isinstance(parsed, list):
#             raise TypeError(f"Expected list of test cases, got {type(parsed)}")

#         logger.info(f"[{task_id}] Parsed {len(parsed)} test cases")

#         # -------------------------------
#         # STEP 4: Validate using Pydantic
#         # -------------------------------
#         validated = GeminiTestCaseResponse(test_cases=parsed)
#         logger.info(f"[{task_id}] Pydantic validation successful")



#         # -------------------------------
#         # STEP 5: Save test cases to DB
#         # -------------------------------
#         for case in validated.test_cases:
#             db.add(
#                 TestCase(
#                     question_id=question_id,
#                     input_data=case.input_data,
#                     expected_output=case.expected_output,
#                     reasoning=case.reasoning,
#                     difficulty_level=case.difficulty_level,
#                 )
#             )

#         db.commit()
#         duration = round(time.time() - start_time, 2)
#         logger.info(
#             f"[{task_id}] Saved {len(validated.test_cases)} test cases to DB in {duration}s"
#         )

#         return {
#             "status": "success",
#             "question_id": question_id,
#             "total": len(validated.test_cases),
#             "duration": f"{duration}s",
#         }

#     # -------------------------------
#     # Error Handling
#     # -------------------------------
#     except (SQLAlchemyError, json.JSONDecodeError, ValueError, TypeError) as e:
#         db.rollback()
#         logger.error(f"[{task_id}] Task failed with error: {e}")

#         try:
#             countdown = 5 * (2 ** self.request.retries)
#             logger.info(f"[{task_id}] Retrying in {countdown}s...")
#             raise self.retry(exc=e, countdown=countdown)
#         except self.MaxRetriesExceededError:
#             logger.critical(f"[{task_id}] Max retries exceeded for question {question_id}")
#             return {"status": "error", "message": str(e)}

#     except Exception as e:
#         db.rollback()
#         logger.exception(f"[{task_id}] Unexpected error: {e}")
#         return {"status": "error", "message": str(e)}

#     finally:
#         db.close()

# stable string

import json
import time
import asyncio
from app.core.celery_app import celery
from sqlalchemy.exc import SQLAlchemyError

from app.core.celery_app import celery  # your Celery instance
from app.config.database import SessionLocal
from app.models.testcase_model import TestCase
from app.schemas.testcase_schema import GeminiTestCaseResponse
from app.utils.code_utils import extract_json_from_model_output
# from app.agents.test_case_generator import test_case_gen_agent
from app.agents.test_case_generator import built_test_case_agent
from app.templates.prompts import TESTCASE_GENERATION_PROMPT
from app.config.logger import AppLogger
from app.utils.async_utils import run_async

logger = AppLogger.get_logger()

# KEY_MAP = {
#     "input_data": ["input_data", "input", "inputs", "inputValue", "args", "arguments"],
#     "expected_output": ["expected_output", "output", "result", "results", "answer"],
#     "reasoning": ["reasoning", "explanation", "why", "notes", "thoughts"],
#     "difficulty_level": ["difficulty_level", "difficulty", "level"]
# }

# def normalize_keys(item: dict) -> dict:
#     normalized = {}

#     for target, candidates in KEY_MAP.items():
#         for c in candidates:
#             if c in item:
#                 normalized[target] = item[c]
#                 break

#         # if missing, set default value
#         if target not in normalized:
#             normalized[target] = "" if target != "difficulty_level" else "MEDIUM"

#     return normalized



# @celery.task(
#     bind=True,
#     max_retries=3,
#     default_retry_delay=10,
#     name="app.tasks.testcase_tasks.generate_test_cases_task",
# )
# def generate_test_cases_task(self, question_id: str, question_text: str, language: str):
#     """
#     Celery Task:
#     Generate test cases using Test Case Generator Agent for a given coding question.
#     - Calls Gemini via asyncio.run (no manual event-loop hacks)
#     - Retries on transient/model/JSON issues
#     """
#     db = SessionLocal()
#     task_id = self.request.id

#     logger.info(f"[{task_id}] Task received for Question ID: {question_id}")
#     start_time = time.time()

#     try:
#         # 1) Build prompt
#         prompt = TESTCASE_GENERATION_PROMPT.format(
#             question_text=question_text,
#             language=language,
#         )
#         logger.info(f"[{task_id}] Sending prompt to Gemini for {language} question")

#         # 2) Call Gemini
#         test_case_agent = built_test_case_agent()
#         response = run_async(test_case_agent.run, prompt)

#         if not hasattr(response, "output"):
#             raise ValueError("Gemini agent returned no 'output' attribute")

#         # 3) Extract JSON from output
#         text_output = extract_json_from_model_output(response.output)
#         logger.info(f"text_output -->{text_output}")
#         logger.info(f"[{task_id}] Raw JSON candidate length: {len(text_output)}")

#         try:
#             parsed = json.loads(text_output)
#         except json.JSONDecodeError as e:
#             logger.error(f"[{task_id}] Invalid JSON returned from Gemini: {e}")
#             # treat as transient model error → retry
#             raise ValueError("Gemini returned invalid JSON")

#         if not isinstance(parsed, list):
#             raise TypeError(f"Expected list of test cases, got {type(parsed)}")

#         logger.info(f"[{task_id}] Parsed {len(parsed)} test cases from model")

#         # ------------------ 4) Validate with Pydantic ------------------
#         normalized_cases = []
#         for case in parsed:
#             # Convert input_data to string if not already
#             if not isinstance(case.get("input_data"), str):
#                 case["input_data"] = json.dumps(case["input_data"])

#             # Convert expected_output to string if not already
#             if not isinstance(case.get("expected_output"), str):
#                 case["expected_output"] = json.dumps(case["expected_output"])

#             normalized_cases.append(case)
#         validated = GeminiTestCaseResponse(test_cases=normalized_cases)
#         logger.info(f"[{task_id}] Pydantic validation successful")

#         # ------------------ 5) Save test cases to DB ------------------
#         for case in validated.test_cases:
#             db.add(
#                 TestCase(
#                     question_id=question_id,
#                     input_data=case.input_data,
#                     expected_output=case.expected_output,
#                     reasoning=case.reasoning,
#                     difficulty_level=case.difficulty_level,
#                     # metadata_json=getattr(case, "metadata_json", None),  # if you later add this
#                 )
#             )

#         db.commit()
#         duration = round(time.time() - start_time, 2)
#         logger.info(
#             f"[{task_id}] Saved {len(validated.test_cases)} test cases to DB in {duration}s"
#         )

#         return {
#             "status": "success",
#             "question_id": question_id,
#             "total": len(validated.test_cases),
#             "duration": f"{duration}s",
#         }

#     # ------------ JSON / validation / model / type issues ------------
#     except (json.JSONDecodeError, ValueError, TypeError) as e:
#         db.rollback()
#         logger.error(f"[{task_id}] Task failed with error: {e}")

#         # If it’s a "no JSON array" or invalid JSON, you *might* want to NOT retry.
#         # Right now we treat them as transient model errors and retry with backoff.
#         try:
#             countdown = max(10, 5 * (2 ** self.request.retries))
#             logger.info(f"[{task_id}] Retrying in {countdown}s...")
#             raise self.retry(exc=e, countdown=countdown)
#         except self.MaxRetriesExceededError:
#             logger.critical(
#                 f"[{task_id}] Max retries exceeded for question {question_id}"
#             )
#             return {"status": "error", "message": str(e)}

#     # ------------------ DB errors ------------------
#     except SQLAlchemyError as e:
#         db.rollback()
#         logger.error(f"[{task_id}] Database error: {e}")
#         return {"status": "db_error", "message": str(e)}

#     # ------------------ Fallback unexpected errors ------------------
#     except Exception as e:
#         db.rollback()
#         logger.exception(f"[{task_id}] Unexpected error: {e}")
#         return {"status": "error", "message": str(e)}

#     finally:
#         db.close()

@celery.task(
    bind=True,
    max_retries=3,
    default_retry_delay=10,
    name="app.tasks.testcase_tasks.generate_test_cases_task",
)
def generate_test_cases_task(self, question_id: str, question_text: str, language: str):
    """
    Celery Task:
    Generate test cases using Test Case Generator Agent for a given coding question.
    Stores structured JSON test cases using JSON columns.
    """
    db = SessionLocal()
    task_id = self.request.id

    logger.info(f"[{task_id}] Task received for Question ID: {question_id}")
    start_time = time.time()

    try:
        # 1) Build Prompt
        prompt = TESTCASE_GENERATION_PROMPT.format(
            question_text=question_text,
            language=language,
        )
        logger.info(f"[{task_id}] Sending prompt to Gemini for {language} question")

        # 2) Run Gemini async safely
        test_case_agent = built_test_case_agent()
        response = run_async(test_case_agent.run, prompt)

        if not hasattr(response, "output"):
            raise ValueError("Gemini agent returned no 'output' attribute")

        # 3) Extract JSON from AI output
        text_output = extract_json_from_model_output(response.output)
        logger.info(f"text_output --> {text_output}")
        logger.info(f"[{task_id}] Raw JSON candidate length: {len(text_output)}")

        try:
            parsed = json.loads(text_output)
        except json.JSONDecodeError as e:
            logger.error(f"[{task_id}] Invalid JSON returned from Gemini: {e}")
            raise ValueError("Gemini returned invalid JSON")

        if not isinstance(parsed, list):
            raise TypeError(f"Expected list of test cases, got {type(parsed)}")

        logger.info(f"[{task_id}] Parsed {len(parsed)} test cases")

        # 4) Normalize & Validate with Pydantic
        normalized_cases = []
        for case in parsed:
            # Input_data is stored as string
            if not isinstance(case.get("input_data"), str):
                case["input_data"] = json.dumps(case["input_data"])

            # Expected_output is stored as string
            if not isinstance(case.get("expected_output"), str):
                case["expected_output"] = str(case["expected_output"])

            normalized_cases.append(case)

        validated = GeminiTestCaseResponse(test_cases=normalized_cases)
        logger.info(f"[{task_id}] Pydantic validation successful")

        # 5) Save JSON test cases to DB
        for idx, case in enumerate(validated.test_cases, start=1):
            db.add(
                TestCase(
                    question_id=question_id,
                    input_json=case.input_data,  # JSON field
                    expected_output_json=case.expected_output,  # JSON field
                    reasoning=case.reasoning,
                    difficulty_level=case.difficulty_level,
                    case_number=case.case_number or idx,
                )
            )

        db.commit()
        duration = round(time.time() - start_time, 2)
        logger.info(
            f"[{task_id}] Saved {len(validated.test_cases)} test cases to DB in {duration}s"
        )

        return {
            "message":"Test Cases gen and saved to DB successfully",
            "payload":{
                "status": "success",
                "question_id": question_id,
                "total": len(validated.test_cases),
                "duration": f"{duration}s"},
            "status":201
                
        }

    # JSON / Validation / Model Errors
    except (json.JSONDecodeError, ValueError, TypeError) as e:
        db.rollback()
        logger.error(f"[{task_id}] Task failed with error: {e}")

        try:
            countdown = max(10, 5 * (2 ** self.request.retries))
            logger.info(f"[{task_id}] Retrying in {countdown}s...")
            raise self.retry(exc=e, countdown=countdown)
        except self.MaxRetriesExceededError:
            logger.critical(f"[{task_id}] Max retries exceeded for question {question_id}")
            return {"status": "error", "message": str(e)}

    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"[{task_id}] Database error: {e}")
        return {"status": "db_error", "message": str(e)}

    except Exception as e:
        db.rollback()
        logger.exception(f"[{task_id}] Unexpected error: {e}")
        return {"status": "error", "message": str(e)}

    finally:
        db.close()
