#!/bin/bash

echo "Starting Rasa Action Server..."
rasa run actions --port 5055 &

echo "Starting Rasa Server..."
rasa run --enable-api --cors "*" --port 5005 &

echo "Starting Flask Web App..."
gunicorn app:app --bind 0.0.0.0:$PORT