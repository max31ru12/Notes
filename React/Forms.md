# Формы

### [Супер-статья про формы в React](https://www.freecodecamp.org/news/how-to-build-forms-in-react/)

- контролируемый input
- множественный input в форме
- валидация форм

### Контролируемый `input`

```js
class Ccomponent extends Component {

    constructor(props){
      super(props)
      this.state = {
        input: ''
      }
      this.handleChange = this.handleChange(this);
    }

    // Так обрабатывается событие onChange input'а
    handleChange(event){
        this.setState({
            input: event.target.value
        })
    }

    // Вариант обработки события onSubmit
    handleSubmit(event){
        // обработчик отправки (предотвращает обновление страницы)
        event.preventDefault();
        this.setState({
            submit: this.state.input
        })
    }

    render() {
        return (
        // Форма
        <div>
            <h5>Controlled input</h5>
            <form onSubmit={this.handleSubmit}>
                <input 
                    value={this.state.input} 
                    placeholder='Search...' 
                    onChange={this.handleChange}>
                </input>
                <button type="submit">Submit!</button>
            </form>
            
            <h3>{this.state.submit}</h3>
        </div>
        )
    }
}
```


### Валидация ошибок

```ts
function MyForm(){
    [inputValue, setInputValue] = useState("")
    [inputError, setInputError] = useState(null)

    function handleInputChange(event) => {
        const value = event.target.value
        setInputValue(value)

        if (value.length >= 5){
            // submit form
        } else {
            setInputError('Input must be lesst than 5 characters')
        }
    }

    return (
        <form>
            <label>
                <input type="text" value={inputValue} onChange={handleInputChange}>
            </label>
            {inputError && <div>{ inputError }</div>}
        </form>
    )
}

```

## Uncontrolled components: хук `useRef`




