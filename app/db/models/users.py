from shapely import Point
from sqlalchemy import Boolean, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from utils.geoalchemy import PointField
from utils.models.base import BaseModel
from utils.models.mixins import MetadataColumnsMixin


class UserTable(MetadataColumnsMixin, BaseModel):
    __tablename__ = 'users'

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    username: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
    )

    is_admin: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(150),
        nullable=True,
    )

    phone_number: Mapped[str] = mapped_column(
        String(11),
        unique=True,
        nullable=False,
    )

    notifications_enabled: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    is_blocked: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )


class UserPasswordTable(MetadataColumnsMixin, BaseModel):
    __tablename__ = 'users_passwords'

    user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'),
        nullable=False,
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )


class UserLocationTable(BaseModel):
    __tablename__ = 'users_locations'

    user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    location: Mapped[Point] = mapped_column(
        PointField,
        nullable=True,
    )

    __table_args__ = (
        UniqueConstraint(
            'user_id',
            'location',
            name='user_id_location_unique_constraint',
        ),
    )
