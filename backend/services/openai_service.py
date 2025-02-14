import os
from openai import OpenAI
from dotenv import load_dotenv
import logging
from services.memories_service import memories_service

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

class OpenAIService:
    def __init__(self):
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
            
            # Build system message with memories
            memories = memories_service.get_memories()
            system_content = "You are a helpful assistant that can answer questions about various topics."
            if memories:
                system_content += "\nPlease keep in mind these important pieces of information:"
                for memory in memories:
                    system_content += f"\n- {memory}"

            response = self.client.chat.completions.create(
                model="gpt-35-turbo-16k",
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            
            logger.debug(f"Full API response: {response}")
            
            if not hasattr(response, 'choices') or not response.choices:
                raise Exception("Invalid response format: 'choices' not found")
                
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
