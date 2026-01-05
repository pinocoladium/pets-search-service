import logging
import sys

from minio import Minio
from pydantic import AnyUrl, ConfigDict
from pydantic.networks import IPvAnyAddress
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(extra='ignore')  # Игнорирование лишних переменных в env файле

    # Debug
    DEBUG: bool = False
    SENTRY_DSN: str = ''

    # Application
    PORT: int = 8000
    HOST: IPvAnyAddress | AnyUrl = '0.0.0.0'
    WORKERS: int = 4

    # Database
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str

    # Celery
    CELERY_BROKER_URL: str

    # Redis
    REDIS_URL: str

    # Minio
    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    MINIO_ENDPOINT: str

    WEATHER_FORECAST_HOURS_STEP: int = 3
    # Be carefully with this setting, cus open weather may do not support this
    WEATHER_FORECAST_DAYS_STEP: int = 4
    WEATHER_CURRENT_EXPIRE_IN_SECONDS: int = 60 * 60 * 2  # 2 hours

    # Triangulation
    TRIANGULATION_BUFFER_IN_METERS: int = 100_000
    TRIANGULATION_STATIONS_COUNT: int = 3
    TRIANGULATION_MAX_SECONDS_TO_WEATHER: int = 60 * 60 * 6  # 6 hours


settings = Settings(_env_file='.environment')

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)


minio_client = Minio(
    settings.MINIO_ENDPOINT,
    access_key=settings.MINIO_ROOT_USER,
    secret_key=settings.MINIO_ROOT_PASSWORD,
    secure=False,
)
