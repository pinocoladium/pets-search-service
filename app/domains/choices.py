from enum import StrEnum


class PetAdoptionNoticeStatusChoice(StrEnum):
    NEW = 'NEW'
    ACTIVE = 'ACTIVE'
    ADOPTED = 'ADOPTED'
    CLOSED = 'CLOSED'
    BLOCKED = 'BLOCKED'


class PetSpeciesChoice(StrEnum):
    DOG = 'DOG'
    CAT = 'CAT'
    BIRD = 'BIRD'
    OTHER = 'OTHER'


class PetSexChoice(StrEnum):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    UNKNOW = 'UNKNOW'


class PetMissingNoticeStatusChoice(StrEnum):
    NEW = 'NEW'
    ACTIVE = 'ACTIVE'
    FOUND = 'FOUND'
    CLOSED = 'CLOSED'
    BLOCKED = 'BLOCKED'


class PetFoundNoticeStatusChoice(StrEnum):
    NEW = 'NEW'
    ACTIVE = 'ACTIVE'
    RETURNED = 'RETURNED'
    CLOSED = 'CLOSED'
    BLOCKED = 'BLOCKED'


class PetHealthConditionChoice(StrEnum):
    HEALTHY = 'HEALTHY'
    WOUNDED = 'WOUNDED'
    SCARED = 'SCARED'


class PetNoticeMatchStatusChoice(StrEnum):
    PENDING = 'PENDING'
    APPROVED = 'APPROVED'
    DECLINED = 'DECLINED'
