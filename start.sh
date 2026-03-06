#!/bin/sh

rasa run actions &
rasa run --enable-api --cors "*" --port 5005 &
gunicorn app:app --bind 0.0.0.0:$PORT