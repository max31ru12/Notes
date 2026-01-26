

## Ограничение на создание/обновление/удаление веток, подходящих под данный паттерн


![[Pasted image 20260118132522.png]]

**matching refs** - попадающие под паттерн ветки  

## Require linear history

> Prevent merge commits from being pushed to matching refs.

Запрещает merge-коммиты в защищенную ветку, то есть:

```shell
git checkout develop
git merge feature-x
git push
```

GitHub  такое сделать не позволит.

То есть необходимо делать **Squash and merge** или **Rebase and merge** в GitHub.


## Require deployments to succeed

> Choose which environments must be successfully deployed to before refs can be pushed into a ref that matches this rule.

Нельзя замержить PR, пока деплой в указанные environment'ы не прошел успешно

1. Есть GitHub Actions с `environment` (например `staging`, `production`)
2. PR пытаются замержить
3. GitHub проверят? ,sk kb ecgtiysq вуздщн d ye;ysq утмшкщтьуте

Для чего:

- Не нужен, если нет автодеплоя
- Нельзя сломать прод

## Require signed commits

> Commits pushed to matching refs must have verified signatures.

Каждый коммит должен быть криптографически подписан с помощью
- GPG
- SSH
- GitHub verified signature

Проверяет:

- что коммит не подделан
- автор - реальный пользователь

Не подходит для личных проектов.



## Require a pull request before merging

Запрещает прямые пуши в защищенную ветку

![[Pasted image 20260118142540.png]]

### Dismiss stale pull request approvals when new commits are pushed

Есть после `approve` в PR пушат новый коммит, то предыдущий `approve` АННУЛИРУЕТСЯ


### Require review from specific teams

Требовать ревью от какой-то специфичной команды


### Require review from Code Owners

Если файл имеет CODEOWNER, то он ОБЯЗАН одобрить PR


### Require approval of the most recent reviewable push

Последний коммит должен быть быть одобрен кем-то другим

- не подходит для маленьких команд
- сам себе нельзя approve
- CI-поправки тоже требуют review

### Require conversation resolution before merging

Все комментарии в PR должны быть resolved. ✅ Best practice


## Require status checks to pass

Нельзя обновлять ветку (merge / push), пока все обязательные CI-проверки не пройдут успешно.


## Block force pushes

Блокируеn force-push в защищенную ветку

## Require code scanning results

**Запрещает merge**, если **code scanning (security analysis)** не прошёл успешно.

Под code scanning GitHub понимает:

- **CodeQL**
- security-сканеры (уязвимости, инъекции, XSS, unsafe patterns)

### Как это работает

1. У тебя должен быть workflow с CodeQL
2. Он запускается на PR
3. GitHub ждёт **результаты анализа**
4. Если найдены уязвимости → ❌ merge запрещён

## Require code quality results

Блокирует merge, если **анализ качества кода** показывает ошибки определённого уровня

Это **не ESLint**, а внешние системы:

- SonarQube / SonarCloud
- Code Climate
- DeepSource

Лишнее для маленькой команды

## Automatically request Copilot code review

GitHub **автоматически добавляет Copilot** как reviewer в каждый PR

Copilot:
- читает PR
- оставляет комментарии
- указывает на возможные проблемы

### Важно
- **не блокирует merge**
- это именно reviewer, а не check

### Плюсы
- полезно для solo-dev
- ловит очевидные баги
- бесплатно, если есть Copilot

### Минусы
- иногда пишет очевидности
- не заменяет человека


## Manage static analysis tools in Copilot code review (Preview)

Copilot будет **использовать результаты статических анализаторов**  
и включать их в свои комментарии