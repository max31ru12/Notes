

## Checkout Session

### Создание сессии

```python
import stripe

stripe.api_key = "api_key"

session = stripe.checkout.Session.create(
	success_url="https://example.com/success",
	line_items=[
		{
			"price": "price_id", 
			"quantity": 2
		}
	],
	mode="payment",
)

# session.status - статус текущей сессии
```

#### mode (required)
- `payment` - одноразовый платеж
- `setup` - сохранение способа оплаты на будущее 
- `subscription` - подписка

#### line_items
- `adjustable_quantity` - Используется тогда, когда надо дать пользователю возможность изменять кол-во товара 
- `price` - ID of the **Price** or **Plan**, используется либо **price**, либо **price_data**
- `metadata` - дополнительная информация, которую можно передать
- `price_data` - генерирует новый объект **Price** на лету, используется либо **price**, либо **price_data**

#### return url
Редирект покупателя после успешного **setup** или **complete**


### Получить сессию