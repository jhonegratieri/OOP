
class Equipment:

    def __init__(self, screen_size, screen_type):
        self.__screen_size = screen_size
        self.__screen_type = screen_type

    @property
    def screen_size(self):
        return self.__screen_size

    @property
    def screen_type(self):
        return self.__screen_type

    @screen_size.setter
    def screen_size(self, value):
        self.__screen_size = value

    @screen_type.setter
    def screen_type(self, screen_type):
        self.__screen_type = screen_type

    def display(self):
        return f'{self.__screen_size}, {self.__screen_type}'


class Computer(Equipment):

    def __init__(self, screen_size, screen_type, keybord_type, memory_capacity):
        super().__init__(screen_size, screen_type)
        self.__keybord_type = keybord_type
        self.__memory_capacity = memory_capacity

    @property
    def keyboard_type(self):
        return self.__keybord_type

    @property
    def memory_capacity(self):
        return self.__memory_capacity

    @keyboard_type.setter
    def keyboard_type(self, keyboard_type):
        self.__keybord_type = keyboard_type

    @memory_capacity.setter
    def memory_capacity(self, memory_capacity):
        self.__keybord_type = memory_capacity

    def display(self):
        return f'{super().display()}, {self.__keybord_type}, {self.__memory_capacity}'


class TestEquipment:

    @staticmethod
    def main():
        equipment1 = Equipment(15.6, 'Led')
        cpu = Computer(24, 'Led', 'ABNT2', 8)
        return equipment1, cpu


equipment_a, equipment_b = TestEquipment.main()
print(equipment_a.display())
print(equipment_b.display())
