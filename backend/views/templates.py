from models.schemas import MessageResponse

class ChatResponseTemplate:
    @staticmethod
    def format_response(message_response: MessageResponse) -> dict:
        return {
            "status": "success",
            "data": message_response.dict(),
            "metadata": {
                "version": "1.0"
            }
        }
