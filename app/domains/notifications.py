from dataclasses import dataclass
from datetime import datetime

from app.domains import User


@dataclass
class Notification:
    created_at: datetime
    recipient_id: int
    recipient: User
    title: str
    text: str
    is_read: bool
