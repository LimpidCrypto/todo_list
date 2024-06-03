#!/bin/bash

# find frontend server PID
FRONTEND_PID=$(ps aux | grep '[n]g serve' | awk '{print $2}')
# kill frontend server
kill $FRONTEND_PID

# find backend server PID
BACKEND_PID=$(ps aux | grep '[p]oetry run python todo_list/main.py' | awk '{print $2}')
# kill backend server
kill $BACKEND_PID
