

## eslint.config.js

### Отключить проверку unused-vars для _ 

В `rules` добавить правило:

```js
"no-unused-vars": ["warn", { "argsIgnorePattern": "^_", "varsIgnorePattern": "^_" }]
```






### Примерное содержание файла

```js
import js from "@eslint/js"  
import globals from "globals"  
import reactHooks from "eslint-plugin-react-hooks"  
import reactRefresh from "eslint-plugin-react-refresh"  
import tseslint from "typescript-eslint"  
import prettier from "eslint-config-prettier"  
  
export default tseslint.config(  
    { ignores: ["dist", "node_modules", "public"] },  
    {  
        extends: [  
            js.configs.recommended,  
            ...tseslint.configs.recommended,  
            prettier,  
        ],  
        files: ["**/*.{ts,tsx}"],  
        languageOptions: {  
            ecmaVersion: 2020,  
            globals: globals.browser,  
        },  
        plugins: {  
            "react-hooks": reactHooks,  
            "react-refresh": reactRefresh,  
        },  
  
        rules: {  
            ...reactHooks.configs.recommended.rules,  
            "react-refresh/only-export-components": ["warn", { allowConstantExport: true }],  
            "no-unused-vars": ["warn", { "argsIgnorePattern": "^_", "varsIgnorePattern": "^_" }],  
            "react/react-in-jsx-scope": "off",  
            "@typescript-eslint/no-explicit-any": "off",  
            semi: ["error", "never"],  
            'react-hooks/rules-of-hooks': 'error',  
            'react-hooks/exhaustive-deps': 'warn',  
        },  
    },  
)
```