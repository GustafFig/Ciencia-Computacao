def print_name(name):
    print(*name, sep="\n")


sum = 0
num = 0

while num is not None:
    num = input("Coloque um numero: ")
    try:
        num = int(num)
        sum += num
        print(sum)
    except ValueError as verr:
        print(f"Erro ao somar valores, {num} é um valor inválido")
        num = None
