from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Minimalist Chatbot"
    debug: bool = False
    frontend_url: str = "http://localhost:3000"
    
    class Config:
        env_file = ".env"

settings = Settings()
