from stack import Stack


def RPN(expression):
    stack = Stack()
    expr = expression.split(" ")

    for char in expr:
        if char == "+":
            value2, value1 = stack.multi_pop(2)
            stack.push(value1 + value2)
        elif char == "*":
            value2, value1 = stack.multi_pop(2)
            stack.push(value1 * value2)
        elif char == "/":
            value2, value1 = stack.multi_pop(2)
            stack.push(value1 / value2)
        elif char == "-":
            value2, value1 = stack.multi_pop(2)
            stack.push(value1 - value2)
        else:
            stack.push(int(char))
    return stack.pop()


if __name__ == "__main__":
    value = RPN("2 3 + 3 * 5 / 3 -")
    print(value)
