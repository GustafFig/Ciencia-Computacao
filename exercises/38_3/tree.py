from stack import Stack


class Worst_garage:
    def __init__(self, stack, street):
        self._stack = stack
        self._street = street

    def get_veiculo(self, id):
        searched_car = None

        for car_pos in range(self._stack.size()):
            car = self._stack.pop()
            if car == id:
                searched_car = car
                break
            self._street.push(car)

        self.retrieve_cars()

        return searched_car or None

    def retrieve_cars(self):
        for _car_pos in range(self._street.size()):
            car = self._street.pop()
            self._stack.push(car)

    def insert_veiculo(self, car):
        self._stack.push(car)

    def __str__(self):
        return f"Garagem: {str(self._stack)}, Rua: {str(self._street)}"


if __name__ == "__main__":
    stack = Stack()
    street = Stack()
    garage = Worst_garage(stack, street)

    option = "1"
    while option != "3":
        plate_number = input("Input an plate: ")

        if option == "1":
            garage.insert_veiculo(plate_number)
            print(garage)

        if option == "2":
            car = garage.get_veiculo(plate_number)
            print(car)
            print(garage)

        option = input("Put an option: ")
