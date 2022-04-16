
class Account:

    def __init__(self, name, account_number, balance=0):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    def change_name(self, new_name):
        self.__name = new_name

    def deposit(self, value):
        self.__balance += value

    def bank_draft(self, value):
        if value <= self.__balance:
            self.__balance -= value
        else:
            print('Insufficient funds.')


person = Account('Jorge', 1234)
person.deposit(1000)
print(vars(person))
person.change_name('oi')
print(vars(person))
person.bank_draft(1100)
person.bank_draft(100)
print(vars(person))
