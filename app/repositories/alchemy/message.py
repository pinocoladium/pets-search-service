from dataclasses import asdict
from datetime import datetime

from app.domains import Message
from app.repositories.alchemy.base import BaseAlchemyRepository


class MessageAlchemyRepository(BaseAlchemyRepository[Message]):
    domain_model = Message

    def for_user(self, user: int, updated_domain: Message) -> Message:
        database_instance = self.get(id)
        updated_domain.updated_at = datetime.now()
        updated_domain.created_at = database_instance.created_at

        for key, value in asdict(updated_domain).items():
            setattr(database_instance, key, value)

        self.session.add(database_instance)
        self.session.commit()
        self.session.refresh(database_instance)

        return database_instance
