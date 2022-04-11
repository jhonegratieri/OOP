
class Person:

    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height
    
    def set_name(self, value):
        self.__name = str(value)
        return self.__name

    def set_age(self, value):
        self.__age = value
        return self.__age

    def set_height(self, value):
        self.__height = value
        return self.__height


person = Person('Gabriella', 27, 1.59)

print(person.get_name())
person.set_name('Gabsteka')
print(person.get_name())
