from datetime import datetime

from pydantic import BaseModel


class MessageResponse(BaseModel):
    id: int
    created_at: datetime
    recipient_id: int
    sender_id: int
    text: str
    is_read: bool
