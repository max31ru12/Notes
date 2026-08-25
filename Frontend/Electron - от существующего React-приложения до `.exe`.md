

## 0. Что у нас уже есть

Предположим, проект выглядит примерно так:

```text
my-app/
├── main.js
├── preload.js
├── package.json
├── src/
│   ├── App.jsx
│   └── ...
├── public/
└── ...
```

То есть:

```text
React
├── src/           → UI
│
Electron
├── main.js        → запускает Electron
└── preload.js     → мост между React и Electron
```

**Ничего пересоздавать через electron-vite не нужно.**

Сначала только выясни, чем собирается твой React.

Открой `package.json`.

Если:

```json
"scripts": {
  "dev": "vite"
}
```

или есть:

```json
"vite": "..."
```

→ у тебя **Vite**.

Если:

```json
"scripts": {
  "start": "react-scripts start",
  "build": "react-scripts build"
}
```

→ у тебя **Create React App**.

Дальше я буду показывать в основном Vite, а отличия CRA отмечать отдельно.

---

# 1. Как Electron запускает React

В development React работает как обычный web-server:

```text
Vite
 ↓
http://localhost:5173
```

Electron просто открывает этот URL:

```js
// main.js

const { app, BrowserWindow } = require("electron")
const path = require("path")

function createWindow() {
    const win = new BrowserWindow({
        width: 1200,
        height: 800,

        webPreferences: {
            preload: path.join(__dirname, "preload.js"),
            contextIsolation: true,
            nodeIntegration: false,
        },
    })

    if (!app.isPackaged) {
        // development
        win.loadURL("http://localhost:5173")
    } else {
        // production
        win.loadFile(
            path.join(__dirname, "dist", "index.html")
        )
    }
}

app.whenReady().then(createWindow)
```

Если CRA:

```text
http://localhost:3000
```

и production build обычно находится:

```text
build/index.html
```

а не:

```text
dist/index.html
```

---

# 2. Что происходит при сборке

Для Vite:

```bash
npm run build
```

фактически запускает:

```bash
vite build
```

и получается:

```text
dist/
├── index.html
└── assets/
    ├── index-....js
    └── index-....css
```

То есть:

```text
src/
 ↓
Vite
 ↓
dist/
```

Electron в production больше **не запускает Vite server**.

Он просто открывает:

```text
dist/index.html
```

как локальный файл.

---

# 3. Важный момент для Vite + Electron

В `vite.config.js` желательно:

```js
import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"

export default defineConfig({
    plugins: [react()],
    base: "./",
})
```

Почему:

по умолчанию Vite может генерировать:

```html
<script src="/assets/index.js">
```

а Electron открывает:

```text
file:///.../dist/index.html
```

Поэтому для Electron удобнее относительные пути:

```html
<script src="./assets/index.js">
```

Если после сборки Electron показывает **белое окно**, это одна из первых вещей, которые надо проверить.

Если используешь React Router и после упаковки ломается навигация, отдельно проверь `BrowserRouter`: для простого Electron-приложения часто проще использовать `HashRouter`.

---

# 4. Теперь главное: `.env`

Здесь есть **ДВА совершенно разных мира**:

```text
                 ENV

        ┌─────────┴─────────┐
        ↓                   ↓

 React / Vite          Electron main.js

 import.meta.env       process.env
```

И работают они по-разному.

---

# 5. `.env` внутри React / Vite

Создаёшь в корне проекта:

```text
.env
.env.development
.env.production
```

Например:

### `.env.development`

```env
VITE_API_URL=http://localhost:8000
```

### `.env.production`

```env
VITE_API_URL=https://backend.mycompany.local
```

React:

```js
const API_URL = import.meta.env.VITE_API_URL

fetch(`${API_URL}/api/users`)
```

---

## Как Vite вообще находит `.env`

Тебе самому ничего читать не надо.

Когда запускаешь:

```bash
npm run dev
```

Vite запускается в режиме:

```text
development
```

и сам читает:

```text
.env
.env.development
```

Когда запускаешь:

```bash
npm run build
```

Vite работает в:

```text
production
```

и читает:

```text
.env
.env.production
```

Vite автоматически предоставляет frontend-коду переменные с префиксом `VITE_`.

---

# 6. Что значит «env попадает в build»

Допустим:

```env
VITE_API_URL=https://api.example.com
```

Код:

```js
fetch(`${import.meta.env.VITE_API_URL}/users`)
```

Во время:

```bash
npm run build
```

Vite фактически превращает это в что-то вроде:

```js
fetch("https://api.example.com/users")
```

То есть после сборки:

```text
.env.production
       ↓
    Vite build
       ↓
значение вставляется в JS
       ↓
dist/assets/index-xxx.js
```

После этого `.env.production` приложению **больше не нужен**.

Если поменять:

```env
VITE_API_URL=...
```

после сборки — ничего не изменится.

Нужно снова:

```bash
npm run build
```

Vite прямо описывает эти переменные как статически заменяемые во время build.

---

# 7. Если у тебя Create React App

Механизм тот же, только вместо:

```env
VITE_API_URL=...
```

пишется:

```env
REACT_APP_API_URL=...
```

А React читает:

```js
process.env.REACT_APP_API_URL
```

CRA также встраивает это значение **во время build**, а не читает `.env` из установленного приложения.

---

# 8. Когда API URL нормально хранить в `.env.production`

Если у всех установок:

```text
один и тот же backend
```

например:

```text
https://api.mycompany.com
```

то вообще не усложняй.

Делай:

```env
VITE_API_URL=https://api.mycompany.com
```

и:

```js
const API_URL = import.meta.env.VITE_API_URL
```

Получится:

```text
.env.production
       ↓
npm run build
       ↓
React bundle
       ↓
Electron installer
```

Это самый простой вариант.

---

# 9. Когда `.env.production` уже НЕ подходит

Например приложение устанавливается в разных локальных сетях:

```text
Клиент A:
192.168.1.10

Клиент B:
10.10.0.15

Клиент C:
server.company.local
```

Ты не хочешь делать:

```text
build для A
build для B
build для C
```

Тогда API URL должен определяться **после установки приложения**.

Это называется:

```text
runtime configuration
```

---

# 10. Runtime config — как он реально работает

Electron умеет получить директорию, предназначенную для пользовательских данных приложения:

```js
app.getPath("userData")
```

Electron рекомендует это место для конфигурации приложения.

Логика:

```text
MyApp.exe
   ↓
Electron запускается
   ↓
app.getPath("userData")
   ↓
C:\Users\...\AppData\Roaming\MyApp\
   ↓
config.json
```

Например:

```json
{
    "apiBaseUrl": "http://192.168.1.10:8000"
}
```

Это уже **не часть build**.

Пользователь/администратор может поменять файл:

```json
{
    "apiBaseUrl": "http://192.168.1.20:8000"
}
```

Перезапустить приложение — и оно работает с новым сервером.

Пересобирать `.exe` не нужно.

---

# 11. Как читать `config.json`

В `main.js`:

```js
const { app } = require("electron")
const path = require("path")
const fs = require("fs")

function getConfigPath() {
    return path.join(
        app.getPath("userData"),
        "config.json"
    )
}

function loadConfig() {
    const configPath = getConfigPath()

    if (!fs.existsSync(configPath)) {
        const defaultConfig = {
            apiBaseUrl: "http://localhost:8000",
        }

        fs.writeFileSync(
            configPath,
            JSON.stringify(defaultConfig, null, 2)
        )

        return defaultConfig
    }

    return JSON.parse(
        fs.readFileSync(configPath, "utf-8")
    )
}
```

Получаем:

```text
loadConfig()
      ↓
{
    apiBaseUrl: "http://192.168.1.10:8000"
}
```

---

# 12. Но React не должен читать этот файл напрямую

При нормальных настройках:

```js
nodeIntegration: false
```

React не может сделать:

```js
require("fs")
```

и это хорошо.

Поэтому:

```text
React
 ↓
preload
 ↓
main.js
 ↓
config.json
```

---

# 13. Передаём config через preload

### main.js

```js
const {
    app,
    BrowserWindow,
    ipcMain,
} = require("electron")

ipcMain.handle("config:get", () => {
    return loadConfig()
})
```

### preload.js

```js
const {
    contextBridge,
    ipcRenderer,
} = require("electron")

contextBridge.exposeInMainWorld(
    "appConfig",
    {
        get: () => ipcRenderer.invoke("config:get"),
    }
)
```

### React

```js
const config = await window.appConfig.get()

console.log(config.apiBaseUrl)
```

И схема получается:

```text
React
 ↓
window.appConfig.get()
 ↓
preload.js
 ↓
ipcRenderer
 ↓
ipcMain
 ↓
main.js
 ↓
config.json
```

Это и есть нормальная роль `preload.js`: дать renderer только те возможности Electron/Node, которые ты явно разрешил. Electron рекомендует `contextIsolation: true`, `nodeIntegration: false` и ограниченный API через preload.

---

# 14. Теперь про `process.env.MYAPP_API_URL`

Вот это вообще другой механизм.

В Node.js существует:

```js
process.env
```

Это объект с **переменными окружения операционной системы процесса**.

Например в PowerShell:

```powershell
$env:MYAPP_API_URL="http://192.168.1.10:8000"

npm run electron
```

Electron запускается из этого процесса и получает:

```js
console.log(process.env.MYAPP_API_URL)
```

Результат:

```text
http://192.168.1.10:8000
```

Electron main process основан на Node.js и имеет доступ к `process`, включая `process.env`.

---

# 15. Важно: `.env` ≠ `process.env`

Вот здесь чаще всего возникает путаница.

Если просто создать:

```text
.env
```

с:

```env
MYAPP_API_URL=http://localhost:8000
```

то Node/Electron **сам этот файл не прочитает**.

```text
.env file

    ❌

process.env
```

Чтобы `.env` попал в `process.env` именно в `main.js`, нужна, например, библиотека:

```bash
npm install dotenv
```

и:

```js
require("dotenv").config()
```

После этого:

```text
.env
 ↓
dotenv
 ↓
process.env
```

Но для установленного Electron-приложения я бы так runtime-конфиг **не организовывал**.

Почему:

непонятно, куда пользователю класть `.env`, где его менять после установки, как переживать обновления и т.д.

Для этого намного понятнее:

```text
config.json
+
app.getPath("userData")
```

---

# 16. Зачем тогда вообще может пригодиться `process.env`

Например разработчику нужно временно переопределить сервер:

```powershell
$env:MYAPP_API_URL="http://localhost:9000"
npm run electron
```

Тогда можно написать:

```js
function getApiUrl() {
    if (process.env.MYAPP_API_URL) {
        return process.env.MYAPP_API_URL
    }

    return loadConfig().apiBaseUrl
}
```

Получается приоритет:

```text
MYAPP_API_URL из ОС
        ↓ если нет

config.json
        ↓ если нет

default URL
```

Но это **не обязательная часть архитектуры**.

Для начала можешь вообще не использовать `process.env.MYAPP_API_URL`.

---

# 17. Итог по конфигурации

Есть три совершенно разных вещи:

```text
1. .env.production

Vite → React bundle

VITE_API_URL=...
```

Использовать, если URL известен при build и одинаковый для всех.

---

```text
2. config.json

Electron runtime → config

{
    "apiBaseUrl": "..."
}
```

Использовать, если URL нужно менять после установки.

---

```text
3. process.env

Operating System
      ↓
Electron main.js
```

Удобно для разработчика/администратора, но необязательно.

---

# 18. Подключение backend

Теперь можно выбрать один из двух вариантов.

## Вариант A — React напрямую вызывает backend

```text
React
 ↓
fetch()
 ↓
FastAPI
```

Например:

```js
const config = await window.appConfig.get()

const response = await fetch(
    `${config.apiBaseUrl}/api/users`
)
```

Самый простой вариант.

Но запрос идёт из Chromium renderer → значит действуют browser security rules, включая CORS.

---

# 19. Что такое `webSecurity`

В `BrowserWindow` есть:

```js
webPreferences: {
    webSecurity: true
}
```

Это значение и так `true` по умолчанию.

Оно включает обычные browser security mechanisms Chromium, в том числе **same-origin policy**.

Условно браузер говорит:

```text
React загружен из A

и хочет обратиться в B

→ проверить, разрешает ли B такой запрос
```

Отсюда возникает CORS.

---

# 20. Почему `webSecurity: false` «чинит» CORS

Можно написать:

```js
new BrowserWindow({
    webPreferences: {
        webSecurity: false
    }
})
```

и внезапно запросы начинают работать.

Но происходит это потому, что ты сказал Chromium:

> не применяй normal same-origin security.

То есть это не решение CORS.

Это отключение защиты.

Более того, Electron прямо указывает, что `webSecurity: false` отключает same-origin policy и также включает возможность insecure content, если она отдельно не настроена.

Поэтому:

```text
CORS error

        ↓

❌ webSecurity: false

        ↓

✅ настроить backend
```

---

# 21. Если React ходит напрямую в FastAPI

Настраиваешь CORS на backend.

Например:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Для production origin Electron может отличаться от dev-origin, поэтому это надо проверить уже на packaged приложении.

---

# 22. Альтернатива: отправлять запросы через Electron main

Можно вообще сделать:

```text
React
 ↓
IPC
 ↓
main.js
 ↓
fetch()
 ↓
FastAPI
```

Тогда browser CORS к этим запросам не относится, потому что HTTP-запрос делает Node/Electron main, а не renderer.

Пример:

### preload.js

```js
contextBridge.exposeInMainWorld("api", {
    getUsers: () =>
        ipcRenderer.invoke("api:get-users"),
})
```

### main.js

```js
ipcMain.handle("api:get-users", async () => {
    const config = loadConfig()

    const response = await fetch(
        `${config.apiBaseUrl}/api/users`
    )

    return response.json()
})
```

### React

```js
const users = await window.api.getUsers()
```

---

# 23. Какой вариант я бы выбрал

Если у тебя сейчас обычный React-клиент уже нормально работает с FastAPI:

```text
React → FastAPI
```

**оставь так.**

Не надо переписывать весь API-layer в IPC просто потому, что это Electron.

Если начнутся реальные проблемы с:

```text
CORS
cookies
authentication
secure local token storage
```

тогда уже имеет смысл отдельно решить архитектуру:

```text
React → IPC → Main → Backend
```

---

# 24. Теперь делаем installer

Устанавливаем:

```bash
npm install --save-dev electron-builder
```

Убедись, что в `package.json` есть:

```json
{
    "main": "main.js"
}
```

---

# 25. Настраиваем electron-builder

Создай:

```text
electron-builder.yml
```

Для Vite:

```yaml
appId: com.example.myapp
productName: MyApp

directories:
  output: release

files:
  - main.js
  - preload.js
  - package.json
  - dist/**/*

asar: true

win:
  target:
    - nsis
```

`electron-builder` позволяет хранить конфигурацию именно в `electron-builder.yml`; для Windows стандартным target является NSIS.

Для CRA заменить:

```yaml
- dist/**/*
```

на:

```yaml
- build/**/*
```

---

# 26. Добавляем команды

Vite:

```json
{
    "scripts": {
        "dev": "vite",
        "build": "vite build",

        "electron": "electron .",

        "dist": "npm run build && electron-builder",

        "dist:win": "npm run build && electron-builder --win"
    }
}
```

Теперь:

```bash
npm run build
```

делает:

```text
React source
 ↓
dist/
```

А:

```bash
npm run dist:win
```

делает:

```text
React source
 ↓
Vite
 ↓
dist/
 ↓
electron-builder
 ↓
Windows installer
```

---

# 27. Что получится

Например:

```text
release/
├── MyApp Setup 1.0.0.exe
└── win-unpacked/
```

Для распространения нужен:

```text
MyApp Setup 1.0.0.exe
```

Пользователю не нужны:

```text
Node
npm
Electron
React
исходники
```

---

# 28. Сначала распространяй приложение максимально тупо

Первый этап:

```text
MyApp Setup.exe
 ↓
общая папка / сайт / сервер / Telegram / etc.
 ↓
пользователь скачивает
 ↓
устанавливает
```

Не надо сразу делать auto-update.

Сначала докажи себе, что работает:

```text
build
 ↓
installer
 ↓
другой компьютер
 ↓
запуск
 ↓
backend работает
```

---

# 29. Потом добавить auto-update

Когда ручное распространение начнёт раздражать:

```bash
npm install electron-updater
```

`main.js`:

```js
const { autoUpdater } = require("electron-updater")

app.whenReady().then(() => {
    autoUpdater.checkForUpdatesAndNotify()
})
```

Например хранишь releases:

```text
https://server.example.com/updates/
```

Builder:

```yaml
publish:
  provider: generic
  url: https://server.example.com/updates/
```

После новой сборки появляются installer + update metadata, например `latest.yml`; updater проверяет metadata и определяет, есть ли новая версия. Generic HTTP(S) server поддерживается напрямую.

---

# 30. Версии

В:

```text
package.json
```

есть:

```json
"version": "1.0.0"
```

Следующий release:

```json
"version": "1.0.1"
```

Дальше:

```text
npm run dist:win
 ↓
MyApp Setup 1.0.1.exe
```

Auto-updater сравнивает release metadata с текущей версией приложения.

---

# 31. Code signing

В самом начале можешь собрать unsigned:

```text
.exe
```

и проверить весь pipeline.

Но Windows может показывать предупреждение о неизвестном издателе.

Перед нормальным распространением клиентам уже разбираешься отдельно с:

```text
Windows Code Signing Certificate
```

А для macOS:

```text
Apple Developer
Code Signing
Notarization
```

---

# 32. Мой рекомендуемый pipeline конкретно для тебя

Сейчас:

```text
[ ] 1. Посмотреть package.json
      Vite или CRA?

[ ] 2. Проверить main.js:
      dev → localhost
      production → dist/index.html

[ ] 3. Если Vite:
      base: "./"

[ ] 4. Запустить React build:
      npm run build

[ ] 5. Проверить, что Electron умеет открыть production build

[ ] 6. Определиться с API URL:

      один URL для всех
          ↓
      .env.production

      разные URL после установки
          ↓
      config.json + app.getPath("userData")

[ ] 7. Оставить:
      webSecurity: true
      contextIsolation: true
      nodeIntegration: false

[ ] 8. Установить electron-builder

[ ] 9. Создать electron-builder.yml

[ ] 10. npm run dist:win

[ ] 11. Установить .exe на другой компьютер

[ ] 12. Проверить:
       React
       backend
       routing
       API URL
       authentication
```

Только после этого:

```text
[ ] HTTPS
[ ] code signing
[ ] auto-update
[ ] CI/CD
```

---

# 33. Самая важная mental model

```text
                    DEVELOPMENT

.env.development
       ↓
      Vite
       ↓
React dev server :5173
       ↑
Electron main.js


                       BUILD

.env.production
       ↓
      Vite
       ↓
dist/index.html + JS
       ↓
electron-builder
       ↓
MyApp Setup.exe


                     RUNTIME

MyApp.exe
   ↓
Electron main.js
   ↓
config.json   ← если нужен runtime config
   ↓
React
   ↓
Backend


                     UPDATE

новый код
   ↓
version 1.0.1
   ↓
npm run dist:win
   ↓
installer + metadata
   ↓
update server
   ↓
electron-updater
```

## Главное, что надо понять про ENV

```text
VITE_API_URL
     ↓
.env.production
     ↓
Vite BUILD
     ↓
вшивается в React JS
```

А:

```text
config.json
     ↓
Electron читает при ЗАПУСКЕ
     ↓
можно менять без rebuild
```

А:

```text
process.env.MYAPP_API_URL
     ↓
переменная ОС / процесса
     ↓
доступна main.js
```

Это **три разных механизма**, и если их не смешивать, вся конфигурация Electron становится намного понятнее.


