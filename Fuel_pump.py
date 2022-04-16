
class FuelPump:

    def __init__(self, fuel_type, value_liter, amount_fuel):
        self.__fuel_tipe = fuel_type
        self.__value_liter = value_liter
        self.__amount_fuel = amount_fuel

    def refil_value(self, value):
        old_amount_fuel = self.__amount_fuel
        if value <= (self.__amount_fuel * self.__value_liter):
            self.__amount_fuel -= value
            return value / self.__value_liter
        else:
            self.__amount_fuel = 0
            return old_amount_fuel

    def refil_quantity(self, quantity):
        old_amount_fuel = self.__amount_fuel

        if quantity <= self.__amount_fuel:
            self.__amount_fuel -= quantity
            return quantity * self.__value_liter
        else:
            self.__amount_fuel = 0
            return round(old_amount_fuel * self.__value_liter, 2)

    def change_value_liter(self, value):
        self.__value_liter = value

    def change_fuel_type(self, new_type):
        self.__fuel_tipe = new_type

    def change_amount_fuel(self, amount):
        self.__amount_fuel = amount


fuel_pump1 = FuelPump('Diesel', 10, 200)
print(vars(fuel_pump1))
fuel_pump1.change_fuel_type('Gasoline')
print(vars(fuel_pump1))
fuel_pump1.refil_value(100)
print(vars(fuel_pump1))
a = fuel_pump1.refil_quantity(500)
print(f'R${a}')
print(vars(fuel_pump1))
fuel_pump1.change_amount_fuel(100000)
print(vars(fuel_pump1))
