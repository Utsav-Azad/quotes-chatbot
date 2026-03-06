#!/bin/bash

echo "Training Rasa model..."
rasa train

echo "Starting Action Server..."
rasa run actions --port 5055 &

echo "Starting Rasa Server..."
rasa run --enable-api --cors "*" --port 5005 &

echo "Waiting for Rasa to start..."
sleep 30

echo "Starting Flask App..."
gunicorn app:app --bind 0.0.0.0:$PORT