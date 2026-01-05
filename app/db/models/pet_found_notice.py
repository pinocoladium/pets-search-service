from datetime import datetime

from shapely import Point
from sqlalchemy import Boolean, DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models import BaseModel
from app.domains.choices import PetFoundNoticeStatusChoice, PetHealthConditionChoice
from utils.geoalchemy import PointField
from utils.models.mixins import MetadataColumnsMixin, PetNoticeColumnsMixin


class PetFoundNoticeTable(PetNoticeColumnsMixin, MetadataColumnsMixin, BaseModel):
    __tablename__ = 'pet_found_notices'

    status: Mapped[str] = mapped_column(
        Enum(PetFoundNoticeStatusChoice),
        nullable=False,
    )

    finder_id: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=True,
    )

    found_datetime: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    found_location: Mapped[Point] = mapped_column(
        PointField,
        nullable=False,
    )

    pet_was_with_collar: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
    )

    pet_health_condition: Mapped[str] = mapped_column(
        Enum(PetHealthConditionChoice),
        nullable=False,
    )
