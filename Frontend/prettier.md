## Настройка `prettier`

```shell
npm install --save-dev --save-exact prettier

echo {}> .prettierrc.json
```

### Файл `.prettierrc.json`:

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




```js
import globals from "globals";  
import pluginJs from "@eslint/js";  
import tseslint from "typescript-eslint";  
import pluginReact from "eslint-plugin-react";  
import * as react from "typescript-eslint";  
import reactHooks from "eslint-plugin-react-hooks";  
import js from "@eslint/js";  
import importPlugin from "eslint-plugin-import";  
import prettier from "eslint-plugin-prettier";  
import prettierConfig from "eslint-config-prettier";  
  
  
/** @type {import('eslint').Linter.Config[]} */  
export default [  
  {  
    files: ["**/*.{js,mjs,cjs,ts,jsx,tsx}"]  
  },  
  {  
    languageOptions: {  
      globals: globals.browser  
    }  
  },  
  js.configs.recommended,  
  react.configs.recommended,   // Подключаем стандартные правила React  
  react.configs["jsx-runtime"], // Разрешает использовать JSX без импорта React  
  reactHooks.configs.recommended, // Подключаем правила хуков  
  importPlugin.configs.recommended, // Подключает проверку импортов  
  prettierConfig, // Отключает конфликтующие правила ESLint  
  {  
    plugins: {  
      prettier // Включаем Prettier как плагин  
    },  
    rules: {  
      "no-console": "warn",  
      "react/react-in-jsx-scope": "off", // Отключает требование `import React`  
      "react-hooks/rules-of-hooks": "error", // Ошибка при неправильных хуках  
      "react-hooks/exhaustive-deps": "warn",  // Предупреждение при deps useEffect  
      "import/no-unresolved": "error",  // Ошибка, если импорт не найден  
      "import/order": ["warn", { "groups": ["builtin", "external", "internal"] }], // Упорядочивание импортов  
      "prettier/prettier": "warn" // Включаем проверку формата через Prettier  
    }  
  },  
  pluginJs.configs.recommended,  
  ...tseslint.configs.recommended,  
  pluginReact.configs.flat.recommended,  
];