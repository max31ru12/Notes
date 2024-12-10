
## Кастомизация колонок в зависимости от записи через `itemProps`

```ts
{  
    key: "value",  
    title: t("Значение"),  
    dataIndex: "value",  
    itemType: "VARCHAR",  
    itemProps: (record: { record: IRow }) => {  
        return {  
            isUpdatable: true,  
            type: record.record.encrypted ? "password" : "text",  
        }  
    },  
},
```