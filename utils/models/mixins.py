from datetime import datetime

from sqlalchemy import DateTime, Enum, Float, func, String
from sqlalchemy.orm import Mapped, mapped_column

from app.domains.choices import PetSexChoice, PetSpeciesChoice


class MetadataColumnsMixin:
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )


class PetNoticeColumnsMixin:
    title: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    pet_name: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    pet_species: Mapped[str] = mapped_column(
        Enum(PetSpeciesChoice),
        nullable=False,
    )

    pet_breed: Mapped[str] = mapped_column(
        String(50),
        nullable=True,
    )

    pet_color: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    pet_special_marks: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
    )

    pet_sex: Mapped[str] = mapped_column(
        Enum(PetSexChoice),
        nullable=False,
    )

    pet_age: Mapped[float] = mapped_column(
        Float,
        nullable=True,
    )
