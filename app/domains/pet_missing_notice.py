from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

from shapely import Point

from app.domains.choices import PetMissingNoticeStatusChoice, PetSexChoice, PetSpeciesChoice


if TYPE_CHECKING:
    from app.domains import User


@dataclass
class PetMissingNotice:
    status: PetMissingNoticeStatusChoice
    owner_id: int
    owner: User
    title: str
    description: str
    pet_name: str
    pet_species: PetSpeciesChoice
    pet_breed: str
    pet_color: str
    pet_special_marks: str
    pet_sex: PetSexChoice
    pet_age: float
    lost_datetime: datetime
    lost_location: Point
