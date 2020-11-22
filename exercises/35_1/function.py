def name(*peso, altura):
    print("altura", altura)
    return peso / (altura / 100) ** 2


x = name(10, 185, 20)

print(x)
