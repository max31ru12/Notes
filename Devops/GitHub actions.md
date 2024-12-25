
`workflow` - процесс, который запускает одну или несколько `job`, расположены в папке **.github/workflows/**.  

## Workflows

Все workflows хранятся в папке **.github/workflows**. [Дока про написание workflows](https://docs.github.com/en/actions/writing-workflows/about-workflows#understanding-the-workflow-file)


## При каких действиях выполнять `workflow`

```yml
on:  
  push:  
    branches: [ main ]  
  pull_request:  
    branches: [ main ]
```

- при пуше
- при пулл реквесте

## Jobs

Все `job'ы` выполняются параллельно

```yaml
jobs:
  example-job:
    runs-on: ubuntu-latest
    steps:
      - name: Retrieve secret
        env:
          super_secret: ${{ secrets.SUPERSECRET }}
        run: |
          example-command "$super_secret"
```

## Dependent jobs

Для того, чтобы создать зависимую `job'у`, необходимо прописать параметр `needs` и указать имя `job'у` от которой зависит текущая.

```yaml
jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - run: ./setup_server.sh
  build:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - run: ./build_server.sh
  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: ./test_server.sh
```




## FastAPI + docker workflow

```yml


on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  prepare:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@main
      - uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - name: Lint with flake8
        run: |
          # stop the build if there are Python syntax errors or undefined names
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
          flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
      - name: Run tests
        run: |
          pytest

  migrations:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up docker
        run: |
          # Add Docker's official GPG key:
          sudo apt-get update
          sudo apt-get install ca-certificates curl
          sudo install -m 0755 -d /etc/apt/keyrings
          sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
          sudo chmod a+r /etc/apt/keyrings/docker.asc

          # Add the repository to Apt sources:
          echo \
            "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
            $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
            sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
          sudo apt-get update

          sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

          sudo docker run hello-world

      - name: Run docker compose
        run: |
          docker compose -f local.yml up -d

      - name: Run migrations
        run: |
          docker compose -f local.yml run --rm backend alembic upgrade head
```