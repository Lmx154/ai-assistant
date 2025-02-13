from typing import Optional
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Minimalist Chatbot"
    debug: bool = False
    frontend_url: str = "http://localhost:3000"
    openai_api_key: str = ""  # new field for OpenAI integration

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
