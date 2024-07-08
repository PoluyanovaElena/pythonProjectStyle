class Car:
    price = 1000000
    def horse_powers(self, power):
        return f'Автомобиль. Количество лошадиных сил - {power} '

class Nissan(Car):
    price = 800000

    def horse_powers(self, power):
        return f'Nissan. Количество лошадиных сил - {power}'

class Kia(Car):
    price = 600000
    def horse_powers(self, power):
        return f'Kia. Количество лошадиных сил - {power} '

car = Car()
print(car.horse_powers(250))
print("Цена: ", car.price)

nissan = Nissan()
print(nissan.horse_powers(190))
print('Цена: ', nissan.price)

kia = Kia()
print(kia.horse_powers(170))
print('Цена: ', kia.price)