# Формы


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


