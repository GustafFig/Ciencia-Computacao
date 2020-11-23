def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def avg(list):
    return sum(list) / len(list)


def print_n_lines_square(n):
    for i in range(n):
        print("*" * n)


def bigger_name(list):
    bigger = ""
    for name in list:
        if len(name) > len(bigger):
            bigger = name
    return bigger


def calculate_paint_price(size, ratio_size_can=3, can_size=18, can_price=80):
    if size % (ratio_size_can * can_size) == 0:
        cans = size // (ratio_size_can * can_size)
        return (cans, cans * can_price)
    cans = 1 + size // (ratio_size_can * can_size)
    print(cans)
    return (cans, cans * can_price)


def triangulo_evaluator(*sizes):
    third, second, bigger = sorted(sizes)
    s_bigger, s_second, s_third = bigger ** 2, second ** 2, third ** 2
    print(bigger)
    if bigger >= second + third:
        return "this is not an triangulo"
    if s_bigger == s_second + s_third:
        return "Trinagulo reto"
    if s_bigger < s_second + s_third:
        return "Triangulo agudo"
    if s_bigger > s_second + s_third:
        return "Triangulo obtuso"


def print_triangle(n):
    for i in range(n):
        print(i * "*")


def return_sum(N):
    return sum(range(N + 1))


def calculate_fuel_price(litre, type, gas_price=2.5, alcool_price=1.9):
    if type == "G":
        tax = gas_price
    elif type == "A":
        tax = alcool_price
    return tax * litre
