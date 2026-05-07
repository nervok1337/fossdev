### Проверка работы через Docker Compose

Команда:

```bash
curl -X POST http://127.0.0.1:8002/orders \
  -H "Content-Type: application/json" \
  -d '{"product_id":"pencil","quantity":3,"promo_code":"STUDENT10"}'
```


Ответ:
``` JSON
{
    "product_id":"pencil",
    "quantity":3,
    "unit_price":1.5,
    "subtotal":4.5,
    "discount_percent":10.0,
    "discount_amount":0.45,
    "total":4.05
}
```
Сервис order-service получил заказ, обратился к product-service за данными о товаре, затем к discount-service за скидкой и после этого рассчитал итоговую стоимость.