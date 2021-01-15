class Stack:  # Implementação apresentada no curso
    def __init__(self):
        self._data = list()

    def size(self):
        return len(self._data)

    def is_empty(self):
        return not bool(self.size())

    def push(self, value):
        self._data.append(value)

    def pop(self):
        if self.is_empty():
            return None

        # -1 se refere ao último objeto da pilha.
        # Ou seja, o valor do topo da pilha
        value = self._data[-1]
        del self._data[-1]
        return value

    def peek(self):
        if self.is_empty():
            return None
        value = self._data[-1]
        return value

    def clear(self):
        self._data.clear()

    def __str__(self):
        size = self.size()
        length = f"len={str(size)}, " if size > 0 else ""
        return f"Stack({length}{self.__repr__()})"

    def __repr__(self):
        str_items = ""
        for i in range(self.size()):
            value = self._data[i]
            str_items += str(value)
            if i + 1 < self.size():
                str_items += ", "
        return str_items

    # exercício 1
    def min_value(self):
        if self.is_empty():
            return None

        min_v = self._data[0]
        for elem in self._data:
            if elem < min_v:
                min_v = elem
        return elem

    # implementação minha específico para os exercícios
    def multi_pop(self, qnt):
        if self.size() < qnt:
            return None
        return [self.pop() for i in range(qnt)]


if __name__ == "__main__":
    stack = Stack()

    i = 0
    while i < 10:
        stack.push(i)
        i += 1

    print(stack)

    values = stack.multi_pop(2)
    print(values[1])

    print(stack)
