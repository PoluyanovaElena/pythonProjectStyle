class Building:
    total = 0
    def __init__(self):
        Building.total += 1

    def __str__(self):
        s = "Здание "
        s += str(self.total)
        return s


for a in range(40):
    dom = Building()
    print(dom)
