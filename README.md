# todo_list

## Inhalt

1. Prerequirements
2. Setup
3. Quick Start
4. Development

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
1. Führe `poetry run python ./todo_list/main\.py` in einem Terminal aus, um den Backend Server zu starten.
2. Führe `cd ./frontend && ng serve` in einem Terminal aus, um den Frontend Server zu starten.
3. Erreiche das Frontend über [localhost:4200](http://localhost:4200).

## Development
### Run Linters
- `poetry run black todo_list`
- `poetry run flake8 todo_list`

### Directory Tree
#### `todo_list`
todo_list/
│
├── controllers/
│   ├── \_\_init\_\_\.py
│   ├── lists\\.py
│   ├── todos\.py
│   └── validations\.py
│
├── core/
│   ├── \_\_init\_\_\.py
│   └── data_store_manager\.py
│
├── models/
│   │
│   ├── _entities/
│   │   ├── \_\_init\_\_\.py
│   │   ├── base_entity\.py
│   │   ├── lists\.py
│   │   └── todos\.py
│   │
│   ├── \_\_init\_\_\.py
│   ├── lists\.py
│   └── todos\.py
│
├── constants\.py
└── main\.py
#### `frontend`
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
│   │   │   │   ├── README\.md
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
├── README\.md
├── angular.json
├── package-lock.json
├── package.json
├── tailwind.config.js
├── tsconfig.app.json
├── tsconfig.json
└── tsconfig.spec.json
