from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.domains import User


@dataclass
class Message:
    created_at: datetime
    recipient_id: int
    recipient: User
    sender_id: int
    sender: User
    text: str
    is_read: bool
