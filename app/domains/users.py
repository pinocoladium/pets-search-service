from dataclasses import dataclass
from datetime import datetime

from shapely import Point


@dataclass
class User:
    name: str
    username: str
    is_admin: bool
    email: str | None
    phone_number: str
    notifications_enabled: bool
    is_blocked: bool
    created_at: datetime
    updated_at: datetime


@dataclass
class UserPassword:
    user_id: int
    user: User
    password: str
    created_at: datetime
    updated_at: datetime


@dataclass
class UserLocation:
    user_id: int
    user: User
    title: str
    location: Point
