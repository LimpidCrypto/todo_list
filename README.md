# todo_list

## Inhalt

1. Prerequirements
2. Setup
3. Quick Start

## Prerequirements

1. [VSCode](https://visualstudio.microsoft.com/de/free-developer-offers/)
    1. [Dev Container Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. [Docker](https://www.docker.com/products/docker-desktop/)

## Setup

1. VSCode öffnen
2. `Strg + Shift + P` und nach "Dev Containers: Clone Repository in Container Volume..."
3. Durchnavigieren bis der Repository Name eingegeben werden muss und nach "LimpidCrypto/todo_list" suchen
4. Weiter durchnavigieren
5. VSCode setzt den Devcontainer automatisch auf
6. Warten bis Devcontainer komplett konfiguriert wurde

## Quick Start
1. Führe `poetry run python ./todo_list/main.py` in einem Terminal aus, um den Backend Server zu starten.
2. Führe `cd ./frontend && ng serve` in einem Terminal aus, um den Frontend Server zu starten.
3. Erreiche das Frontend über [localhost:4200](http://localhost:4200).
