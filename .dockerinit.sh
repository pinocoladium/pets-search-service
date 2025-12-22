#!/bin/bash

alembic upgrade head || exit 1

gunicorn -c gunicorn_conf.py app.app:app
