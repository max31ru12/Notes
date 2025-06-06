
[Документация](https://prettier.io/docs/install)

## Настройка `prettier`

```shell
npm install --save-dev --save-exact prettier

npx prettier --write /app  # запустить prettier c автоматическим фиксом (аргумент  --write) в папке /app
```

### Файл `.prettierrc:

```json
{  
  "trailingComma": "es5",  // конечная запятая
  "tabWidth": 4,  // ширина отступа, в пробелах
  "semi": false,  // добавление точек с запятыми в конце инструкций
  "singleQuote": true,
  "endOfLine": "lf", // решает проблему с кодировкой букв в винде
  "printWidth": 100,
}
```
