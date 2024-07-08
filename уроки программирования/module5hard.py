class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed


class Plant:
    def __init__(self, name, edible=False):
        self.name = name
        self.edible = edible

class Mammal(Animal):
    def __init__(self, food):
        self.food = food
    def eat(food):



class Predator(Animal):


class Flower(Plant):


class Fruit(Plant):
