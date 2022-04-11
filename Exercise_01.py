class People:

    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_method(self, data):
        if data.lower() == 'name':
            return self.__name
        elif data.lower() == 'age':
            return self.__age
        elif data.lower() == 'height':
            return self.__height
        else:
            return print('Invalid parameter.')

    def set_method(self, data, new_value):
        if data.lower() == 'name':
            self.__name = str(new_value)
            return self.__name
        elif data.lower() == 'age':
            self.__age = new_value
            return self.__age
        elif data.lower() == 'height':
            self.__height = new_value
            return self.__height
        else:
            return print('Invalid parameter.')


people = People('Gabriella', 27, 1.59)

print(people.get_method('name'))
people.set_method('name', 'Gabi')
print(people.get_method('name'))
