
## NVM (Гибкое управление версиями Node и npm)

https://github.com/nvm-sh/nvm

1) Скачать
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```
2) Добавить переменную окружения
```bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

### Установить nodejs

```bash nvm install 22.17.0
```



## CI/CD




