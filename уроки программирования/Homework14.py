class House:
    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor

    def go_to(self, new_floor):
        if new_floor >= 1 and new_floor <= int(self.number_of_floors):
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('"Такого этажа не существует"')


dom = House('ЖК Эльбрус,', 30)
print(dom.name, dom.number_of_floors)
dom.go_to(7)
dom.go_to(31)



