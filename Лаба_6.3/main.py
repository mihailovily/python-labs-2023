import sys
from PyQt5 import QtWidgets
import calc
import os


class ExampleApp(QtWidgets.QMainWindow, calc.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.currentResult = 0
        self.currentAction = '+'
        self.currentEntered = ''
        self.pushButton_0.clicked.connect(self.action)
        self.pushButton_1.clicked.connect(self.action)
        self.pushButton_2.clicked.connect(self.action)
        self.pushButton_3.clicked.connect(self.action)
        self.pushButton_4.clicked.connect(self.action)
        self.pushButton_5.clicked.connect(self.action)
        self.pushButton_6.clicked.connect(self.action)
        self.pushButton_7.clicked.connect(self.action)
        self.pushButton_8.clicked.connect(self.action)
        self.pushButton_9.clicked.connect(self.action)
        self.pushButton_00.clicked.connect(self.action)
        self.pushButton_AC.clicked.connect(self.clear)
        self.pushButton_perc.clicked.connect(self.action)
        self.pushButton_off.clicked.connect(self.off)
        self.pushButton_split.clicked.connect(self.action)
        self.pushButton_multiple.clicked.connect(self.action)
        self.pushButton_minus.clicked.connect(self.action)
        self.pushButton_plus.clicked.connect(self.action)
        self.pushButton_final.clicked.connect(self.action)
        self.pushButton_point.clicked.connect(self.action)

    def action(self):
        text = self.sender().text()
        self.label.setText(self.label.text() + text)
        if is_number(text) or text == '.':
            self.currentEntered += text
        else:
            if self.currentAction == '%':
                self.currentResult %= float(self.currentEntered)
            elif self.currentAction == '/':
                self.currentResult /= float(self.currentEntered)
            elif self.currentAction == '*':
                self.currentResult *= float(self.currentEntered)
            elif self.currentAction == '-':
                self.currentResult -= float(self.currentEntered)
            elif self.currentAction == '+':
                self.currentResult += float(self.currentEntered)
            elif self.currentAction == '=':
                pass
            elif self.currentAction == 'after=':
                self.currentResult = float(self.currentEntered)
            else:
                print('error', text, self.currentAction)
            self.currentAction = text
            self.currentEntered = ''
        if self.currentAction == '=':
                if int(self.currentResult) == self.currentResult:
                    self.label.setText(str(int(self.currentResult)))
                    self.currentEntered = str(int(self.currentResult))
                else:
                    self.label.setText(str(self.currentResult))
                    self.currentEntered = str(self.currentResult)
                self.currentAction = 'after='
                
        print(self.currentEntered, self.currentResult)
    
    def action_del(self):
        self.currentResult = self.currentEntered[:-1]
    
    def off(self):
        sys.exit()
    
    def clear(self):
        self.label.setText("")
        self.currentResult = 0
        self.currentAction = '+'
        self.currentEntered = ''
    
    def result(self):
        if self.currentResult == int(self.currentResult):
            pass

def is_number(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
