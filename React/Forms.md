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

### Правильная типизация `useRef` и `event`

```ts
const inputUsername = useRef<HTMLInputElement>(null);  
const inputPassword = useRef<HTMLInputElement>(null);  
  
function handleSubmit(event: React.FormEvent<HTMLFormElement>): void {  
    event.preventDefault();  
    const formData: AuthData = {  
        username: inputUsername.current?.value ?? "",  
        password: inputPassword.current?.value ?? "",  
  
    }  
}
```

### Пример использования формы с `useRef`:

```ts
export default function SkillCreateForm() {

    const nameRef = useRef<HTMLInputElement>(null)
    const levelRef = useRef<HTMLSelectElement>(null)
    const avatarRef = useRef<HTMLInputElement>(null)

    function handleSubmit(event) {
        event.preventDefault()
        const formData: ICreateSkill = {
            name: nameRef.current?.value ?? "",
            level: Number(levelRef.current?.value) ?? "",
            avatar_url: avatarRef.current?.value ?? "",
        }

        console.log(formData)
        // axios.post("http://127.0.0.1:8000/skills/", )
    }

    return (
    <form action="" onSubmit={handleSubmit}>
        <label htmlFor="skill-name">Skill name: </label>
        <input type="text" id="skill-name" ref={nameRef} placeholder="Type skill name..."/><br />

        <label htmlFor="skill-level">Skill level: </label> 
        <select ref={levelRef} id="skill-level">
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
        </select>
        <br />

        <label htmlFor="skill-avatar">Skill avatar</label>
        <input type="text" id="skill-avatar" ref={avatarRef} placeholder="Type avatar URL..."/><br />

        <button type="submit">Submit</button>
    </form>
    )
}
```


