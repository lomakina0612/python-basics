def cost_delivery(quantity, *items, discount=0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""
    
    result = 0
    if quantity >=1:
        result = 5 + (quantity - 1) * 2
    if discount != 0:
        result *= 1 - discount
    return result

print(cost_delivery(2, 1, 2, 3))
print(cost_delivery(3, 3))
print(cost_delivery(1))
print(cost_delivery(2, 1, 2, 3, discount=0.5))

print(cost_delivery.__doc__)