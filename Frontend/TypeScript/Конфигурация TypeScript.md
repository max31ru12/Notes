
## Голый TypeScript

- `npm init -y` - инициализация **npm** проекта
- `npm i typescript -D` - установка **TypeScript** (как dev-зависимость, так как в Runtime он не попадает)
- `npx tsc --init` - инициализирует **tsconfig.json**
	- `target` - версия js, в которую будем компилировать
	- `module` - модульная система (то, как будем работать с импортами, экспортами)
	- `strict: true` - всегда в **true** (подсвечивает спорные ошибки)


## Сборщик Vite

`npm create vite@lates` - инициализация vite

Общий **tsconfig.json**, который ссылается на 2 других конфига

