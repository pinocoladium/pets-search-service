from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models import BaseModel
from app.domains.choices import PetNoticeMatchStatusChoice
from utils.models.mixins import MetadataColumnsMixin


class PetNoticeMatchTable(MetadataColumnsMixin, BaseModel):
    __tablename__ = 'pet_notice_matches'

    found_notice_id: Mapped[int] = mapped_column(
        ForeignKey('pet_found_notices.id'),
        nullable=False,
    )

    missing_notice_id: Mapped[int] = mapped_column(
        ForeignKey('pet_missing_notices.id'),
        nullable=False,
    )

    initiator_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=True,
    )

    match_status: Mapped[str] = mapped_column(
        Enum(PetNoticeMatchStatusChoice),
        nullable=False,
    )

    comment: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )
