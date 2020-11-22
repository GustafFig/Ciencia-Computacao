restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]

filtered = [
    restaurant["name"] for restaurant in restaurants if restaurant["nota"] > 3
]

print(filtered)

rating = {6, 8, 5, 9, 10}
last = 10
new = 100

new_rating = [rat * new / last for rat in rating]

print(new_rating)

mult = [
    "Multiplo de 5" if not a else a
    for a in [
        "Múltiplo de 3" if rat % 3 == 0 else rat % 5 == 0 for rat in rating
    ]
]

print(mult)
