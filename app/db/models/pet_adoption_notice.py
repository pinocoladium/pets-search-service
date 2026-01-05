from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models import BaseModel
from app.domains.choices import PetAdoptionNoticeStatusChoice
from utils.models.mixins import MetadataColumnsMixin, PetNoticeColumnsMixin


class PetAdoptionNoticeTable(PetNoticeColumnsMixin, MetadataColumnsMixin, BaseModel):
    __tablename__ = 'pet_adoption_notices'

    status: Mapped[str] = mapped_column(
        Enum(PetAdoptionNoticeStatusChoice),
        nullable=False,
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False,
    )
