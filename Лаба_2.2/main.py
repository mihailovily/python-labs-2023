import sys

class Account(object):
 
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return "Баланс пополнен"
        return "Пополнение не бывает отрицательным"
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return "Успешно выведено"
        return "Недостаточно средств на счете"
    def check_balance(self):
        return self.balance
    

bank_acc = Account(0)

print('Вам создан банковский счет. Текущий баланс = 0')
while True:
    print('Что будете делать?\n\n1 - пополнить баланс\n2 - вывести деньги со счета\n3 - проверить остаток средств\n0 - завершение работы')
    selected = int(input())
    if selected == 1:
        print(bank_acc.deposit(int(input('Введите сумму пополнения\n'))))
    elif selected == 2:
        print(bank_acc.withdraw(int(input('Введите сумму вывода\n'))))
    elif selected == 3:
        print(bank_acc.check_balance())
    elif selected == 0:
        sys.exit()
    else:
        print('я тебя совсем не понял')