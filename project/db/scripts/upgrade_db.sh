#!/usr/bin/env bash

export DB_URI=localhost
export DB_PORT=5433
export DB_NAME=boiler
export DB_USER=boiler_user
export DB_PASSWORD=dev_admin

PYTHONPATH=. alembic upgrade head
