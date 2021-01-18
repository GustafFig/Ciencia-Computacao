from deque import Deque


class Pilha:
    def __init__(self):
        self._deque = Deque()

    def push(self, elem):
        self._deque.push_back(elem)

    def peek(self):
        return self._deque.peek_back()

    def pop(self):
        return self._deque.pop_back()

    def __str__(self):
        return f"{self._deque}"


if __name__ == "__main__":
    pilha = Pilha()
    pilha.push(1)
    pilha.push(2)
    print(pilha)
    print(pilha.pop())
    print(pilha)
    print(pilha.peek())
