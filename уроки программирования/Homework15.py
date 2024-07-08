class House:
    def __init__(self):
        self.numberOfFloors = 0


    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(floors)


dom = House()
print(dom.numberOfFloors)
dom.setNewNumberOfFloors(8)















# class Transport(object):
#     def __init__(self, s, c, m):
#         self.speed = s
#         self.color = c
#         self.made = m
#     def __str__(self):
#         s = "Это объект класса Transport\n"
#         s += "Скорость:" + str(self.speed) + ",цвет:"+ self.color + ",производитель:" + self.made + "\n"
#         return s
#     def go(self):
#         print("Начинает движение ", self.made)
#     def stop(self):
#         print("Остановка ",self.made)
# transport1 = Transport(20, "blue", "Forward")
# transport2 = Transport(180, "white", "Ford")
# transport3 = Transport(100, "red", "МАЗ")
# print(transport1)
# print(transport2)
# print(transport3)
# transport1.go()
# transport2.go()
# transport1.stop()
