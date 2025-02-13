import os

class OpenAIService:
    def __init__(self, api_key: str = os.getenv("OPENAI_API_KEY", "")):
        self.api_key = api_key

    def get_response(self, prompt: str) -> str:
        # ...integration using OpenAI API...
        return "OpenAI response placeholder"

openai_service = OpenAIService()
