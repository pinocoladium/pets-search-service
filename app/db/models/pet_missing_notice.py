from datetime import datetime

from shapely import Point
from sqlalchemy import DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models import BaseModel
from app.domains.choices import PetMissingNoticeStatusChoice
from utils.geoalchemy import PointField
from utils.models.mixins import MetadataColumnsMixin, PetNoticeColumnsMixin


class PetMissingNoticeTable(PetNoticeColumnsMixin, MetadataColumnsMixin, BaseModel):
    __tablename__ = 'pet_missing_notices'

    status: Mapped[str] = mapped_column(
        Enum(PetMissingNoticeStatusChoice),
        nullable=False,
    )

    owner_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False,
    )

    lost_datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    lost_location: Mapped[Point] = mapped_column(
        PointField,
        nullable=False,
    )
