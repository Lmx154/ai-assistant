from models.schemas import MessageDTO, MessageResponse
from services.chat_service import chat_service

class ChatController:
    async def process_chat(self, message: MessageDTO) -> MessageResponse:
        return await chat_service.process_message(message)

chat_controller = ChatController()
