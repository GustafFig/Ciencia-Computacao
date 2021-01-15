from stack import Stack


class Limited_Stack(Stack):
    def __init__(self, limit=2):
        super().__init__()
        self.limit = limit

    def is_full(self):
        return super().size() == self.limit

    def push(self, elem):
        if self.is_full():
            raise OverflowError(f"{self} out of range")

        super().push(elem)
        return self.size() + 1


if __name__ == "__main__":
    stack = Limited_Stack(2)

    stack.push(1)
    stack.push(1)
    print(stack)
    stack.push(1)
