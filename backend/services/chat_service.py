from models.schemas import MessageDTO, MessageResponse, Message
from datetime import datetime

class ChatService:
    async def process_message(self, message: MessageDTO) -> MessageResponse:
        # Create a model instance
        chat_message = Message(
            id=1,  # In a real app, this would be from the database
            text=message.text,
            response=f"You said: {message.text}",
            created_at=datetime.now()
        )
        
        # Return DTO
        return MessageResponse(
            text=chat_message.text,
            response=chat_message.response
        )

chat_service = ChatService()
