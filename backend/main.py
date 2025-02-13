from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(message: Message):
    # Here you would typically integrate with an AI model
    return {"response": f"You said: {message.text}"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
