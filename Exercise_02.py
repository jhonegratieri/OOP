
class Register:
    list = []

    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
        Register.list.append(dict(zip(['Name', 'Age', 'Height'], [self.__name, self.__age, self.__height])))

    def remove(self):
        for index, dicionaries in enumerate(Register.list):
            if dicionaries['Name'] == self.__name:
                Register.list.pop(index)
                break

    def search(self):
        for index, dicionaries in enumerate(Register.list):
            if dicionaries['Name'] == self.__name:
                print(f'{self.__name} is at position {index} on the list. ')

    @staticmethod
    def print_list():
        print(Register.list)

    @staticmethod
    def personal_data(index):
        print(Register.list[index])


gabi = Register('Gabi', 27, 190)
jhone = Register('jhone', 30, 190)
abc = Register('teste', 34, 123)

gabi.personal_data(2)
abc.print_list()
abc.remove()
jhone.print_list()
gabi.search()
