from sqlalchemy.orm import registry, relationship

from app.db.models import (
    MessageTable,
    NotificationTable,
    PetAdoptionNoticeTable,
    PetFoundNoticeTable,
    PetMissingNoticeTable,
    UserLocationTable,
    UserPasswordTable,
    UserTable,
)
from app.domains import (
    Message,
    Notification,
    PetAdoptionNotice,
    PetFoundNotice,
    PetMissingNotice,
    User,
    UserLocation,
    UserPassword,
)


def start_mapping_table_from_domain():
    """
    Регистрирует доменные модели как сущность алхимии.
    Суть в том, что доменная модель никак не изменяет свою работу, но мы
    получаем возможность использовать ее как модель при выполнение запросов.
    Это упрощает работу т.к. не нужно перегонять из ОРМ модели в домен.

    Параметр viewonly=True означает, что при сохранение модели будет использоваться поле {table}_id, а не поле {table}.
    """
    registrator = registry()

    registrator.map_imperatively(
        User,
        UserTable.__table__,
        properties={
            'passwords': relationship(
                UserPassword,
                back_populates='user',
                viewonly=True,
            ),
            'locations': relationship(
                UserLocation,
                back_populates='user',
                viewonly=True,
            ),
            'notifications': relationship(
                Notification,
                back_populates='user',
                viewonly=True,
            ),
            'sent_messages': relationship(
                Message,
                foreign_keys=[MessageTable.sender_id],
                back_populates='sender',
                viewonly=True,
            ),
            'received_messages': relationship(
                Message,
                foreign_keys=[MessageTable.recipient_id],
                back_populates='recipient',
                viewonly=True,
            ),
            'pet_adoption_notices': relationship(
                PetAdoptionNotice,
                foreign_keys=[PetAdoptionNoticeTable.owner_id],
                back_populates='owner',
                viewonly=True,
            ),
            'pet_missing_notices': relationship(
                PetMissingNotice,
                foreign_keys=[PetMissingNoticeTable.owner_id],
                back_populates='owner',
                viewonly=True,
            ),
            'pet_found_notices': relationship(
                PetFoundNotice,
                foreign_keys=[PetFoundNoticeTable.finder_id],
                back_populates='finder',
                viewonly=True,
            ),
        },
    )

    registrator.map_imperatively(
        UserPassword,
        UserPasswordTable.__table__,
        properties={
            'user': relationship(
                User,
                back_populates='passwords',
                viewonly=True,
            ),
        },
    )

    registrator.map_imperatively(
        UserLocation,
        UserLocationTable.__table__,
        properties={
            'user': relationship(
                User,
                back_populates='locations',
                viewonly=True,
            ),
        },
    )

    registrator.map_imperatively(
        Notification,
        NotificationTable.__table__,
        properties={
            'recipient': relationship(
                User,
                back_populates='notifications',
                viewonly=True,
            ),
        },
    )

    registrator.map_imperatively(
        Message,
        MessageTable.__table__,
        properties={
            'sender': relationship(
                User,
                foreign_keys=[MessageTable.sender_id],
                back_populates='sent_messages',
                viewonly=True,
            ),
            'recipient': relationship(
                User,
                foreign_keys=[MessageTable.recipient_id],
                back_populates='received_messages',
                viewonly=True,
            ),
        },
    )

    registrator.map_imperatively(
        PetAdoptionNotice,
        PetAdoptionNoticeTable.__table__,
        properties={
            'owner': relationship(
                User,
                back_populates='pet_adoption_notices',
                viewonly=True,
            ),
        },
    )

    registrator.map_imperatively(
        PetMissingNotice,
        PetMissingNoticeTable.__table__,
        properties={
            'owner': relationship(
                User,
                back_populates='pet_missing_notices',
                viewonly=True,
            ),
        },
    )

    registrator.map_imperatively(
        PetFoundNotice,
        PetFoundNoticeTable.__table__,
        properties={
            'finder': relationship(
                User,
                back_populates='pet_found_notices',
                viewonly=True,
            ),
        },
    )
