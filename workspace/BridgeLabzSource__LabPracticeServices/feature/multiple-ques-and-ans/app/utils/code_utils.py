from app.config.logger import AppLogger
import re
# from app.config.agent_initialization import gemini_agent as code_analyser_agent
from fastapi.responses import JSONResponse
from google.api_core import exceptions as google_exceptions
# from app.utils.github_utils import fetch_github_code
from app.templates.prompts import REVIEW_PROMPT, REVIEW_PROMPT_THEORY
from app.schemas.model_resp_schema import *
import json
from pydantic_ai.settings import ModelSettings
from pydantic_ai.agent import Agent
from app.config.settings import settings
from app.config.agent_initialization import gemini_model
from app.crud.pricing_queries import insert_pricing_data

logger = AppLogger.get_logger()

def generate_model_response(review_results):
    return CodeReviewOutput(
        analysis_output=AnalysisOutput(
            what_worked_well=review_results["Code_Analysis"]["What_worked_well"],
            what_can_be_improved=review_results["Code_Analysis"]["What_can_be_improved"],
        ),
        quality_feedback=QualityFeedback(
            correctness=review_results["Code_Quality_Qualitative"]["Correctness"],
            readability=review_results["Code_Quality_Qualitative"]["Readability"],
            maintainability=review_results["Code_Quality_Qualitative"]["Maintainability"],
            design=review_results["Code_Quality_Qualitative"]["Design"],
            scalability=review_results["Code_Quality_Qualitative"]["Scalability"],
        ),
        quality_scores=QualityScores(
            correctness=review_results["Code_Quality_Quantitative"]["Correctness"],
            readability=review_results["Code_Quality_Quantitative"]["Readability"],
            maintainability=review_results["Code_Quality_Quantitative"]["Maintainability"],
            design=review_results["Code_Quality_Quantitative"]["Design"],
            scalability=review_results["Code_Quality_Quantitative"]["Scalability"],
            overall=review_results["Code_Quality_Quantitative"]["Overall"],
        )
    )

def model_json_error(error_message: str):
    return JSONResponse(
    status_code=500,
    content={"success_status": False, "error_details": str(error_message), "results": None},
    )

def extract_json_from_model_output(text: str) -> str:
    """
    Removes markdown code fences (```json ... ```).
    Returns cleaned JSON string.
    """
    # Remove leading/trailing whitespace and code fences
    cleaned = re.sub(r"^```(?:json)?\n|\n```$", "", text.strip(), flags=re.MULTILINE)
    return cleaned.strip()


async def review_code_with_gemini(db, prompt_str: str, content: list, language: str) -> dict:
    logger.info(f"Reviewing code for language review_code_with_gemini: {language}")
    try:
        # if question_type == "TEXT":
        #     prompt = REVIEW_PROMPT_THEORY.format(language=language, question=prompt, code=code)
        # else:
        #     prompt = REVIEW_PROMPT.format(language=language, question=prompt, code=code)

        def build_qa_block(content_list):
            block = ""
            for item in content_list:
                block += f"""
                    QUESTION ID: {item.question_id}
                    QUESTION: {item.question_text}
                    ANSWER:
                    {item.answer_text}

                    --- END ITEM ---

                """
            return block
        
        formatted_QA = build_qa_block(content)

        prompt = prompt_str.format(
            language="Java",
            ques_ans_content=formatted_QA
        )


        code_analyser_agent = Agent(
            model = gemini_model,
            system_prompt = prompt,
            model_settings = ModelSettings(
                temperature=settings.GEMINI_TEMPERATURE,
                )
        )

        if not code_analyser_agent:
            raise ValueError("code_analyser_agent not initialized")
        else:
            logger.info("code_analyser_agent initialized")

            response = await code_analyser_agent.run(prompt)
            logger.info(f"Code Analysis generated")

            # insert_pricing_data(db, user_id, "Java", prompt, response)
            text_output = extract_json_from_model_output(response.output)

            try:
                parsed = json.loads(text_output)
            except json.JSONDecodeError:
                logger.error(f"code_analyser_agent did not return valid JSON.\nOutput was:\n{text_output}")
                raise ValueError(f"code_analyser_agent did not return valid JSON.\nOutput was:\n{text_output}")
            return parsed

    except google_exceptions.GoogleAPICallError as e:
        logger.error(f"Gemini API error while reviewing code: {str(e)}")
        raise ValueError(f"Gemini API error while reviewing code: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error reviewing code: {str(e)}")
        raise ValueError(f"Unexpected error reviewing code: {str(e)}")