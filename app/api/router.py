from fastapi import APIRouter

from app.api.messages.views import messages_api_router
from app.api.notifications.router import notifications_api_router
from app.api.users.router import users_api_router


api_router = APIRouter(prefix='/api')

api_router.include_router(users_api_router, prefix='/users', tags=['users'])
api_router.include_router(messages_api_router, prefix='/messages', tags=['messages'])
api_router.include_router(notifications_api_router, prefix='/notifications', tags=['notifications'])
