#!/bin/bash

# Find the process id of the flask server
flask_pid=$(ps aux | grep "todo_list/main.py" | grep -v grep | awk '{print $2}')
# Find the process id of the angular server
angular_pid=$(ps aux | grep "ng serve" | grep -v grep | awk '{print $2}')

# Kill the flask server
kill $flask_pid
# Kill the angular server
kill $angular_pid
