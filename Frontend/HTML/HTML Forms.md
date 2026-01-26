
## Пример формы с очисткой 

```html
<form method="POST">  
    <label htmlFor="">Имя: <br/>  
        <input type="text"/>  
    </label>     
    
    <label>Язык програмирования</label>    
    
    <label>        
	    <input type="radio" name="radioGroup" value="C++"/>C++  
    </label>  
    
	<label>        
		<input type="radio" name="radioGroup" value="PHP"/>PHP  
    </label>    
    
    <label>        
	    <input type="radio" name="radioGroup" value="Python"/>Python  
    </label>  
  
    <label htmlFor="additional-info">Дополнительная информация: <br/>  
        <textarea name="" id="additional-info" cols={30} rows={4}></textarea>  
    </label>  
    
    <button type="submit">Подтвердить</button>  
    <button type="reset">Очистить</button>  
  
</form>
```