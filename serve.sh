#!/bin/bash

nohup poetry run python todo_list/main.py > ./logs/flask.log 2>&1 &
cd frontend
nohup ng serve > ./../logs/angular.log 2>&1 &
