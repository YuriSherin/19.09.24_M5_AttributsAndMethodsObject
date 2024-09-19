class House:
    def __init__(self, name: str, number_of_floors: int):
        """Инициализатор класса"""
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor: int):
        """Метод класса"""
        if 1 <= new_floor <= self.number_of_floors:
            for n in range(new_floor):
                print(n + 1)
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
