# todo_list

## Inhalt

1. [Quick Start](#1-quick-start)
2. [Development](#2-development)
    1. [Voraussetzungen](#i-voraussetzungen)
    2. [Setup](#ii-setup)
    3. [Run Linters](#iii-run-linters)
    4. [Wichtige Dateien und Ordner](#iv-wichtige-dateien-und-ordner)
    5. [Directory Tree](#v-directory-tree)

## 1. Quick Start
1. `docker pull limpidcrypto1/todo_list:latest`
2. `docker run -p 4200:4200 -p 3000:3000 -t limpidcrypto1/todo_list:latest`

## 2. Development

### i. Voraussetzungen

1. [VSCode](https://visualstudio.microsoft.com/de/free-developer-offers/)
    1. [Dev Container Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. [Docker](https://www.docker.com/products/docker-desktop/)


### ii. Setup

#### Dev Container

1. VSCode öffnen
2. `Strg + Shift + P` und nach "Dev Containers: Clone Repository in Container Volume..."
3. Durchnavigieren bis der Repository Name eingegeben werden muss und nach "LimpidCrypto/todo_list" suchen
4. Weiter durchnavigieren
5. VSCode setzt den Devcontainer automatisch auf
6. Warten bis Devcontainer komplett konfiguriert wurde

#### Server Starten

1. Führe `poetry run python ./todo_list/main.py` in einem Terminal aus, um den Backend Server zu starten.
2. Führe `cd ./frontend && ng serve` in einem Terminal aus, um den Frontend Server zu starten.
3. Erreiche das Frontend über [localhost:4200](http://localhost:4200).

### iii. Run Linters

- `poetry run black todo_list`
- `poetry run flake8 todo_list`

### iv. Wichtige Dateien und Ordner
- *./frontend/src/assets/openApi/documentation.yaml* - Die API Dokumentation
- *./data/* - Der Datenspeicher
- *./todo_list/main.py* - Die Hauptdatei der flask-App
- *./todo_list/controllers/* - Die Controller-Funktionen, die die Requests entgegen nehmen
- *./todo_list/models/* - Die Models steuern, wie auf Daten zugegriffen wird
- *./todo_list/core/data_store_manager.py* - liest und bearbeitet den Datenspeicher
- *./Dockerfile* - Die deployment Dockerfile
- *./frontend/src/app/pages/documentation* - Erstellt aus der Doku das Frontend

### v. Directory Tree

#### `todo_list`

```
todo_list/
│
├── controllers/
│   ├── __init__.py
│   ├── lists.py
│   ├── todos.py
│   └── validations.py
│
├── core/
│   ├── __init__.py
│   └── data_store_manager.py
│
├── models/
│   │
│   ├── _entities/
│   │   ├── __init__.py
│   │   ├── base_entity.py
│   │   ├── lists.py
│   │   └── todos.py
│   │
│   ├── __init__.py
│   ├── lists.py
│   └── todos.py
│
├── constants.py
└── main.py
```
#### `frontend`

```
frontend/
│
├── .vscode/
│   ├── extensions.json
│   ├── launch.json
│   └── tasks.json
│
├── src/
│   │
│   ├── app/
│   │   │
│   │   ├── pages/
│   │   │   │
│   │   │   └── documentation/
│   │   │       ├── documentation.component.html
│   │   │       ├── documentation.component.scss
│   │   │       ├── documentation.component.spec.ts
│   │   │       └── documentation.component.ts
│   │   │
│   │   │
│   │   ├── shared/
│   │   │   │
│   │   │   ├── components/
│   │   │   │   │
│   │   │   │   ├── organisms/
│   │   │   │   │   │
│   │   │   │   │   ├── api-documentation/
│   │   │   │   │   │   ├── api-documentation.component.html
│   │   │   │   │   │   ├── api-documentation.component.scss
│   │   │   │   │   │   ├── api-documentation.component.spec.ts
│   │   │   │   │   │   └── api-documentation.component.ts
│   │   │   │   │   │
│   │   │   │   │   └── organisms.module.ts
│   │   │   │   │
│   │   │   │   ├── README.md
│   │   │   │   └── components.module.ts
│   │   │   │
│   │   │   └── shared.module.ts
│   │   │
│   │   ├── app.component.html
│   │   ├── app.component.scss
│   │   ├── app.component.spec.ts
│   │   ├── app.component.ts
│   │   ├── app.config.ts
│   │   └── app.routes.ts
│   │
│   ├── assets/
│   │   │
│   │   ├── openApi/
│   │   │   └── documentation.yaml
│   │   │
│   │   └── .gitkeep
│   │
│   ├── favicon.ico
│   ├── index.html
│   ├── main.ts
│   └── styles.scss
│
├── .editorconfig
├── .gitignore
├── README.md
├── angular.json
├── package-lock.json
├── package.json
├── tailwind.config.js
├── tsconfig.app.json
├── tsconfig.json
└── tsconfig.spec.json
```
