from deque import Deque

class CompletedDeque(Deque):
    def __init__(self):
        super()
        self._data = []

    def clear(self):
        self._data.clear()

    def exists(self, value):
        for elem in self._data:
            if elem == value:
                return True
        return False

    def peek(self, position, order="asc"):
        if position < 0 or len(self) <= position:
            return None

        direction_correction = 1, 0

        if order == "desc":
            direction_correction = -1, +1
    
        return self._data[direction_correction[0] * position - direction_correction[1]]

if __name__ == "__main__":
    c_deque = CompletedDeque()
    c_deque.push_front(1)
    c_deque.push_front(2)
    print(c_deque)
    c_deque.clear()
    print(c_deque)

    for i in [22, 2, 77, 6, 43, 76, 89, 90]:
        c_deque.push_back(i)

    print(c_deque)

    c_deque.peek(2)
    c_deque.peek(5)
    c_deque.peek(0, "desc")
    c_deque.peek(-1)
    c_deque.peek(8)
