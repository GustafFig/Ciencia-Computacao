from stack import Stack


def revert_in_parentesis(string):
    stack = Stack()
    in_parentesis = False
    final = ""

    for char in string:
        if in_parentesis and char != ")" and char != "(":
            stack.push(char)
            continue
        if char == "(":
            in_parentesis = True
        elif char == ")":
            while not stack.is_empty():
                final += stack.pop()
            in_parentesis = False
        else:
            final += char
    return final


if __name__ == "__main__":
    string = "teste((lagel))"

    print(revert_in_parentesis(string))
