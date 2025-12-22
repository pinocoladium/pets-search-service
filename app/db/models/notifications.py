from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, func, String
from sqlalchemy.orm import Mapped, mapped_column

from utils.models.base import BaseModel


class NotificationTable(BaseModel):
    __tablename__ = 'notifications'

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    recipient_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    text: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    is_read: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )
