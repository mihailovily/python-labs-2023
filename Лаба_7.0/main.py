import sys
from PyQt5 import QtWidgets
import bank


class BankAccount:
    def __init__(self):
        self.cash = 0

    def deposit(self, money):
        if money > 0:
            self.cash += money
            return "Текущий баланс: " + str(self.cash)
        else:
            return "Попытка взлома зафиксирована"

    def withdraw(self, money):
        if (self.cash - money) > 0:
            self.cash -= money
            out = "Текущий баланс: " + str(self.cash)
        else:
            out = "Недостаточно средств"
        return out


class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()

    def withdraw(self, money):
        if (self.cash - money) > 0:
            self.cash -= money + (money * 0.01)
            out = (
                "Комиссия: " + str(money * 0.01) + "\nТекущий баланс: " + str(self.cash)
            )
        else:
            out = "Недостаточно средств"
        return out


class CurrentAccount(BankAccount):
    def __init__(self):
        super().__init__()

    def deposit(self, money):
        if money > 0:
            self.cash += money * 0.99
            return (
                "Комиссия: " + str(money * 0.01) + "\nТекущий баланс: " + str(self.cash)
            )
        else:
            return "Попытка взлома зафиксирована"


class ExampleApp(QtWidgets.QMainWindow, bank.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bank = BankAccount()
        self.savings = SavingsAccount()
        self.current = CurrentAccount()
        self.selectAcc.addItems(
            ["Банковский счет", "Сберегательный счет", "Текущий счет"]
        )
        self.selectAcc.activated.connect(self.activated)
        self.pushWith.clicked.connect(self.withdrawal)
        self.pushDep.clicked.connect(self.deposit)
        self.__bank_acc_selected()

    def activated(self, index):
        print("Activated index:", index)
        if index == 0:
            self.__bank_acc_selected()
        elif index == 1:
            self.__savings_acc_selected()
        elif index == 2:
            self.__current_acc_selected()

    def __bank_acc_selected(self):
        self.label.setText("Текущий баланс: " + str(self.bank.cash))

    def __savings_acc_selected(self):
        self.label.setText("Текущий баланс: " + str(self.savings.cash))

    def __current_acc_selected(self):
        self.label.setText("Текущий баланс: " + str(self.current.cash))

    def withdrawal(self):
        curIndex = self.selectAcc.currentIndex()
        if curIndex == 0:
            message = self.bank.withdraw(self.spinWith.value())
        elif curIndex == 1:
            message = self.savings.withdraw(self.spinWith.value())
        elif curIndex == 2:
            message = self.current.withdraw(self.spinWith.value())
        else:
            message = 'error'
        self.label.setText(message)

    def deposit(self):
        curIndex = self.selectAcc.currentIndex()
        if curIndex == 0:
            message = self.bank.deposit(self.spinDep.value())
        if curIndex == 1:
            message = self.savings.deposit(self.spinDep.value())
        if curIndex == 2:
            message = self.current.deposit(self.spinDep.value())
        self.label.setText(message)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


main()
