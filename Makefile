TAIL=100

define set-default-container
	ifndef c
	c = fastapi
	else ifeq (${c},all)
	override c=
	endif
endef


set-container:
	$(eval $(call set-default-container))
build:
	docker compose -f docker-compose.yml build
up:
	docker compose -f docker-compose.yml up -d
down:
	docker compose -f docker-compose.yml down
logs: set-container
	docker compose -f docker-compose.yml logs --tail=$(TAIL) -f $(c)
restart: set-container
	docker compose -f docker-compose.yml restart $(c)
exec: set-container
	docker compose -f docker-compose.yml exec $(c) /bin/bash

test: set-container
	docker compose -f docker-compose.yml run --rm $(c) python -m pytest

migrate: set-container
	docker compose -f docker-compose.yml run --rm $(c) alembic upgrade head
migrations: set-container
	docker compose -f docker-compose.yml run --rm $(c) alembic revision --autogenerate -m "$(m)"
pre-commit: set-container
	docker compose -f docker-compose.yml run --rm $(c) bash -c 'PRE_COMMIT_HOME=.precomcache pre-commit run --all-files'