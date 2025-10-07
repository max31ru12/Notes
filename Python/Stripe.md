
## Создание сессии

```python
session = stripe.checkout.Session.create(  
    mode="payment",  
    line_items=[  
        {  
            "price_data": {  
                "currency": "usd",  
                "product_data": {  
                    "name": membership.name,  
                },  
                "unit_amount": 2000,  # cents
            },  
            "quantity": 1,  
        }  
    ],  
    customer_email=current_user.email,  
    success_url="http://localhost:3000/membership/stripe/success/{CHECKOUT_SESSION_ID}",  
    cancel_url="http://localhost:4242/cancel",  
)
```

## проксировать вебхук

```shell
docker run --rm -it -e STRIPE_API_KEY=${STRIPE_API_KEY} stripe/stripe-cli:latest listen --api-key ${STRIPE_API_KEY} --forward-to http://host.docker.internal:8000/api/membership/stripe/webhook --events checkout.session.completed,payment_intent.succeeded
```