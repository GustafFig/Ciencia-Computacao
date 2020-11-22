a = 10
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)
print(a ** b)

hours = 6

minutes = hours * 60

seconds = hours * 60 * 60

print(minutes, seconds)


def calculatePrice(qnt):
    value = 24.20
    unit_price = value * 0.4
    price_by_products = unit_price * qnt
    transport = 3 + qnt * 0.75
    return price_by_products + transport


print(calculatePrice(60))

set a = 10
