#!/bin/bash

# Start the frontend server in the background
cd /app/frontend
nohup ng serve --host 0.0.0.0 &

# Start the backend server and keep it in the foreground
cd /app
poetry run python todo_list/main.py
