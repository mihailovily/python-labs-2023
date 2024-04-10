import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import calc
import os

class ExampleApp(QtWidgets.QMainWindow, calc.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_0.clicked.connect(self.action_0)
        self.pushButton_1.clicked.connect(self.action_1)

                
    def action_0(self):
        self.label.setText(self.label.text() + "0")
        
    def action_1(self):
        self.label.setText(self.label.text() + "1")
    

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()