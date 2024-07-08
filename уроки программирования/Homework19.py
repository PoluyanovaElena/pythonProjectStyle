class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000
    def horse_powers(self, power):
        return f'Количество лошадиных сил - {power}'


class Nissan(Car):
    vehicle_type = "Nissan-Qashqai"
    price = 800000
    def horse_powers(self, power):
        return super().horse_powers(power)


Qashqai = Nissan()
print(Qashqai.horse_powers(190))
print("Тип автомобиля: ", Qashqai.vehicle_type, 'Цена:', Qashqai.price)
