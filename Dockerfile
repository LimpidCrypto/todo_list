FROM mcr.microsoft.com/devcontainers/base:bullseye

# Use bash as default shell
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
    libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev
# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs
# Install Angular CLI
RUN npm install -g @angular/cli
# Install Python3 and pip
RUN apt update && apt install python3 python3-pip -y
# Install pyenv
RUN curl https://pyenv.run | bash
# Add pyenv to PATH
ENV PATH="/root/.pyenv/bin:${PATH}"
# Install poetry
RUN pip install --user poetry
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry completions bash >> ~/.bash_completion
# Install python 3.12.3
RUN pyenv install 3.12.3

EXPOSE 4200
EXPOSE 3000

WORKDIR /app
COPY . .

# Set python 3.12.3 as local python version
RUN pyenv local 3.12.3
# Use python 3.12.3 for poetry
RUN poetry env use $HOME/.pyenv/versions/3.12.3/bin/python
# Install poetry dependencies
RUN poetry install

# Install frontend dependencies
RUN cd frontend && npm install

# Copy start script
RUN chmod +x ./up.sh && chmod +x ./down.sh

# Run servers
CMD ["./up.sh"]
