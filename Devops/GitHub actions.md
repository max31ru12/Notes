
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