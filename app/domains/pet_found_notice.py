from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

from shapely import Point

from app.domains.choices import PetFoundNoticeStatusChoice, PetHealthConditionChoice, PetSexChoice, PetSpeciesChoice


if TYPE_CHECKING:
    from app.domains import User


@dataclass
class PetFoundNotice:
    status: PetFoundNoticeStatusChoice
    finder_id: int | None
    finder: User | None
    title: str
    description: str
    pet_name: str
    pet_species: PetSpeciesChoice
    pet_breed: str
    pet_color: str
    pet_special_marks: str
    pet_sex: PetSexChoice
    pet_age: float
    found_datetime: datetime
    found_location: Point
    pet_was_with_collar: bool
    pet_health_condition: PetHealthConditionChoice
