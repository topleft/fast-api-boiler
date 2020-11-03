#!/usr/bin/env bash

export DB_URI=0.0.0.0
export DB_PORT=5433
export DB_NAME=boiler
export DB_USER=boiler_user
export DB_PASSWORD=dev_admin

PYTHONPATH=. alembic revision --autogenerate
