from dataclasses import dataclass
from typing import TYPE_CHECKING

from app.domains.choices import PetAdoptionNoticeStatusChoice, PetSexChoice, PetSpeciesChoice


if TYPE_CHECKING:
    from app.domains import User


@dataclass
class PetAdoptionNotice:
    status: PetAdoptionNoticeStatusChoice
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
