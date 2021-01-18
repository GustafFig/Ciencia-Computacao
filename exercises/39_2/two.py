from deque import Deque


class UnderFlow(OverflowError):
    def __init__(self, value):
        super().__init__()
        pass


class OverDeque(Deque):
    def __init__(self, limit=10):
        super().__init__()
        self._data = []
        self.__limit = limit

    def is_full(self):
        return len(self) >= self.__limit

    def is_empty(self):
        return len(self) == 0

    def push_back(self, elem):
        if self.is_full():
            raise OverflowError(f"{self} out of range")

        super().push_back(elem)

    def push_front(self, elem):
        if self.is_full():
            raise OverflowError(f"{self} out of range")
        super().push_front(elem)

    def pop_front(self):
        if self.is_empty():
            raise UnderFlow(f"{self} under range")
        return super().pop_front()

    def pop_back(self):
        if self.is_empty():
            raise UnderFlow(f"{self} under range")
        return super().pop_back()


if __name__ == "__main__":
    over_deque = OverDeque(2)

    over_deque.push_back(1)
    over_deque.push_back(2)

    print(over_deque.pop_front())
    print(over_deque.pop_front())
    print(over_deque.pop_front())
