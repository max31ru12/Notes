# Классовые компоненты

`rcc` - команда для создания классвого компрнента **shortcut**

`rfc` - компонент из функции

`rafc` - компонент из стрелочной функции


### Классовый компонент

`rconst` - создать конструктор

```js
class Ccomponent extends Component {

    // Конструктор
    constructor(props){
        super(props)

      this.state = {
         name: "Alex",
         buttonClicked: 0,
      }
      // Запись нужна, так как в JS метод класс не привязан к контексту (без этого, как минимум, не будет работать setState)
      this.handleClick = this.handleClick.bind(this);
    }

    // создали метод (обработчик)
    handleClick(){
        // setState в классе есть по умолчанию 
        this.setState({
            name: this.state.name,
            buttonClicked: this.state.buttonClicked + 1,
        });
    }

    render() {
        return (
            <div>
                <h1>Class component {this.props.propname}<h1>
            </div>
        )
    }
} 
```


### Изменение `state` (более короткая форма)
```js
handleClick(){
    this.setState(state => ({
        buttonClicked: state.buttonClicked + 1
    }));
}
```

`this.props.propname` - это использование приходящих `props`

