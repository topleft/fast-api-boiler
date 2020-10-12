#!/bin/bash

echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

ls -la
ls -la app

uvicorn \
  --host ${HOST} \
  --port ${PORT} \
  --workers 1 \
  --reload \
  app.app:app
