from math import sqrt


def quadratic(a, b, c):
    x1 = -b / (2 * a)
    x2 = sqrt(b ** 2 - 4 * a * c) / (2 * a)
    return (x1 + x2), (x1 - x2)


x = [1, 2, 3, 4, 5]

_, *x = x
print(x)
