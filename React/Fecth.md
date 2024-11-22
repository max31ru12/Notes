# Раюота с API



```js

export default class SomeClass extends Component {

    constructor(props){
        super(prosp)
        state = {
            result = []
        }
    }

    // Этот компонент вызывается сразу после монтирования компонента
    // Тут происходят действия, для которых необходимо наличие DOM-узлов
    componentDidMount() {
        fetch("url")
        .then(res => res.json())
        .then(
            (result) => {
                this.setState({
                    result: result.<key_from_response>
                })
            },
            (error) => {
                this.setState({
                    error: true
                })
            }
        )
    }

    render() {
        const {error, items} = this.state;

        if (error) {
            return <p>Error {error.message}</p>
        } else {
            return (
            <ul>
                {items.map(item => (
                    <li key={item.name}>{item.name}</li>
                ))}
            </ul>
            )
        }
    }
}


```



