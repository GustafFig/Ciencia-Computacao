from deque import Deque

class OverDeque(Deque):
    def __init__(self, limit = 10):
        super().__init__()
        self._data = []
        self.__limit = limit

    def is_full(self):
        return len(self) <= self.__limit

    def push_back(self, elem);
        if self.is_full():
            raise 

        super().push(elem)
        
