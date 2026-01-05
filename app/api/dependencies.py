from collections.abc import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.db.engine import SessionLocal
from app.domains import User


security = HTTPBearer()


def get_session() -> Generator:
    with SessionLocal() as session:
        yield session


def authorize(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    session: Session = Depends(get_session),
) -> User:
    payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=['HS256'])
    user_id = payload['sub']

    user = session.get(User, int(user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Invalid token',
            headers={'WWW-Authenticate': 'Basic'},
        )

    return user
