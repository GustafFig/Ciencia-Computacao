def FizzBuzz(n):
    list = []
    for num in range(1, n + 1):
        elem = ""
        if num % 3 == 0:
            elem += "Fizz"
        if num % 5 == 0:
            elem += "Buzz"
        list.append(elem or num)

    return list
