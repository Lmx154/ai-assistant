from models.schemas import MessageDTO, MessageResponse
from services.openai_service import openai_service
import asyncio

class ChatController:
    async def process_chat(self, message: MessageDTO) -> MessageResponse:
        try:
            ai_reply = await asyncio.to_thread(openai_service.get_response, message.text)
        except Exception as e:
            ai_reply = "Error processing your request."
        return MessageResponse(
            text=message.text,
            response=ai_reply
        )

chat_controller = ChatController()
