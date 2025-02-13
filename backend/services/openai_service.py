import os
from openai import OpenAI
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.DEBUG)  # Changed to DEBUG for more details
logger = logging.getLogger(__name__)

load_dotenv()

class OpenAIService:
    def __init__(self):
        # Debug environment variables
        api_key = os.getenv("OPENAI_API_KEY")
        api_base = os.getenv("OPENAI_API_BASE")
        logger.debug(f"API Base URL: {api_base}")
        logger.debug(f"API Key (first 4 chars): {api_key[:4] if api_key else 'None'}")
        
        try:
            self.client = OpenAI(
                api_key=api_key,
                base_url=api_base
            )
            logger.info("OpenAI client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {str(e)}")
            raise

    def get_response(self, prompt: str) -> str:
        try:
            logger.info(f"Sending prompt: {prompt[:50]}...")
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0
            )
            
            result = response.choices[0].message.content.strip()
            logger.info(f"Received response: {result[:50]}...")
            return result
            
        except Exception as e:
            logger.error(f"Error in get_response: {str(e)}", exc_info=True)
            raise Exception(f"OpenAI API error: {str(e)}")

# Initialize service with error handling
try:
    openai_service = OpenAIService()
except Exception as e:
    logger.error(f"Failed to create OpenAIService: {str(e)}")
    raise
