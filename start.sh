#!/bin/sh

rasa run actions &
rasa run --enable-api --cors "*" --port $PORT --host 0.0.0.0