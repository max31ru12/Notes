
## Расширения файлов

Распознавание расширений файлов:

```ts
// vite.config.ts
export default defineConfig({  
  plugins: [react()],  
  resolve: {  
    extensions: ['.js', '.jsx', '.ts', '.tsx', '.json']  
  }  
})
```



