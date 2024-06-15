#!/bin/bash

cd /app

alembic upgrade head

cd /app/src

gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000