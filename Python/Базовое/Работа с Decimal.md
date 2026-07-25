

### Decimal в Pydantic

```python
class CreateDonationCheckoutSchema(BaseModel):  
    amount: Decimal = Field(  
        ge=Decimal("5.00"),  
        decimal_places=2,  # максимум две значащие цифры после запятой  
    )
```


### Перевод Decimal значение в целое

`quantize()` приводит число к такой же десятичной структуре, как у переданного образца.

```python

amount = Decimal("12.54")

amount_in_cents = amount.quantize(Decimal("1"), rounding=ROUND_HALF_UP))

# .quantize(Decimal("1")) - приведение к целому числу
# .quantize(Decimal("0.01")) - приведение к числу с двумя знаками почле запятой
```

`rounding=ROUND_HALF_UP` задает привычное школьное округление

```python
Decimal("12.345").quantize( Decimal("0.01"), rounding=ROUND_HALF_UP) 

# Decimal("12.35")
```