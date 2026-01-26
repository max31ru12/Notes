

```html

<input 
	type="file" 
	id="photo" 
	accept="image/*"
	class=".fileInput"
/> 
<label for="photo">Upload</label>
```

Если `for` в **label** совпадает с `id` в **input**, то клик по **label** === клик по **label**. 


```css
.fileInput {
	display: flex;
}
```