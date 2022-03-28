class Clients():
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    def bal(self):
        print(f'Клиент {self.name} {self.surname}. Баланс: {self.balance} руб.')


cl1 = Clients("Иван", "Петров", 50)
cl1.bal()
