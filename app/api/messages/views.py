from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import authorize, get_session
from app.api.messages.serializers import MessageResponse
from app.domains import User
from app.repositories.alchemy.message import MessageAlchemyRepository


messages_api_router = APIRouter()


@messages_api_router.get(
    '/',
    summary='Получение всех сообщений',
    response_model=list[MessageResponse],
)
def get_messages(
    session: Annotated[Session, Depends(get_session)],
    user: Annotated[User, Depends(authorize)],
):
    """
    Получение всех сообщений
    """
    return MessageAlchemyRepository(session).list()
