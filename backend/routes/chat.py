from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from models.schemas import MessageDTO, MessageResponse
from controllers.chat_controller import chat_controller

router = APIRouter(prefix="/chat", tags=["chat"])

@router.get("/")
async def root():
    return HTMLResponse("<h1>Minimalist Chatbot API</h1>")

@router.post("/", response_model=MessageResponse)
async def chat(message: MessageDTO):
    return await chat_controller.process_chat(message)

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
