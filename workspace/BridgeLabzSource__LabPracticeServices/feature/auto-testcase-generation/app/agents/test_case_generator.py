from app.config.logger import AppLogger
from app.config.settings import settings
from app.templates.prompts import TESTCASE_GENERATION_PROMPT
from pydantic_ai.providers.google_gla import GoogleGLAProvider
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.settings import ModelSettings
from pydantic_ai.agent import Agent

logger = AppLogger.get_logger()

# ---------Pydantic Codeanalyser Agent ---------
def built_test_case_agent():
    provider = GoogleGLAProvider(api_key=settings.GEMINI_API_KEY)
    gemini_model = GeminiModel(
        settings.GEMINI_MODEL,
        provider = provider
        )

    test_case_gen_agent = Agent(
        model = gemini_model,
        system_prompt = TESTCASE_GENERATION_PROMPT,
        model_settings = ModelSettings(
            temperature=settings.GEMINI_TEMPERATURE,
            )
        )

    if not test_case_gen_agent:
        raise ValueError("Test case generator agent not initialized")
    else:
        logger.info("Test case generator agent initialized")
        return test_case_gen_agent
