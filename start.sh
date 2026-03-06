#!/bin/bash

echo "Starting Action Server..."
rasa run actions --port 5055 &

echo "Starting Rasa Server..."
rasa run --enable-api --cors "*" --port 5005 --interface 0.0.0.0 --model models &

echo "Waiting for Rasa to start..."
sleep 25

echo "Starting Flask App..."
gunicorn app:app --bind 0.0.0.0:$PORT