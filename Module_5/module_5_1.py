class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= self.number_of_floors:
            print(new_floor)
        else:
            print('Такого этажа не существует')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h2.go_to(1)
h2.go_to(2)
h1.go_to(3)
h1.go_to(4)
h1.go_to(5)
h2.go_to(10)