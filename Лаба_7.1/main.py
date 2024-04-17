import time
import sys
import gibdd
from PyQt5 import QtWidgets


class Vehicle:
    def __init__(self, manufacturer, model, release_date):
        self.manufacturer = manufacturer
        self.model = model
        self.release_date = release_date
        self.mileage = 0
        self.tires = []
        self.gas_tank_max = 0
        self.gas_tank = 0

    def ride(self, distance):
        return "wr-wr-wr " * distance

    def tire_service(self):
        for i in range(len(self.tires)):
            self.tires[i] = 5
        return True

    def gas_station(self):
        self.gas_tank = self.gas_tank_max
        return True

    def display_info(self):
        info = [
            "Производитель: " + str(self.manufacturer),
            "Модель: " + str(self.model),
            "Год выпуска: " + str(self.release_date),
            "Пробег: " + str(self.mileage),
            "Состояние шин: " + str(self.tires),
            "Вместимость бака: " + str(self.gas_tank_max),
            "Остаток топлива: : " + str(self.gas_tank),
        ]
        return info


class Motocycle(Vehicle):
    def __init__(self, manufacturer, model, release_date):
        super().__init__(manufacturer, model, release_date)
        self.tires = [5, 5]
        self.gas_tank = 10
        self.gas_tank_max = 10

    def display_info(self):
        info = super().display_info()
        info_to_return = ""
        for i in info:
            info_to_return += i + "\n"
        return info_to_return

    def ride(self, distance):
        if sum(self.tires) >= 3 and self.tires[1] > 1:
            if distance / 30 <= self.gas_tank:
                self.gas_tank -= distance / 30
                self.gas_tank = round(self.gas_tank, 4)
                self.tires[1] -= distance * 0.0011
                self.tires[0] -= distance * 0.0009
                for i in range(len(self.tires)):
                    self.tires[i] = round(self.tires[i], 4)
                self.mileage += distance
                return "OK"
            else:
                return "Пора на заправку"
        else:
            return "Пора на шиномонтаж"


class Car(Vehicle):
    def __init__(self, manufacturer, model, release_date, privod):
        super().__init__(manufacturer, model, release_date)
        self.tires = [5, 5, 5, 5]
        self.gas_tank = 50
        self.privod = privod  # 1 - перед, 2 - зад
        self.gas_tank_max = 50

    def display_info(self):
        info = super().display_info()
        if self.privod == 1:
            privod = "Передний"
        else:
            privod = "Задний"
        info.append("Привод: " + privod)
        info_to_return = ""
        for i in info:
            info_to_return += i + "\n"
        return info_to_return

    def ride(self, distance):
        if sum(self.tires) >= 2 and self.tires[1] > 0.5:
            if distance / 15 <= self.gas_tank:
                self.gas_tank -= distance / 15
                self.gas_tank = round(self.gas_tank, 4)
                if self.privod == 2:
                    self.tires[2] -= distance * 0.0016
                    self.tires[3] -= distance * 0.0016
                    self.tires[0] -= distance * 0.0013
                    self.tires[1] -= distance * 0.0013
                else:
                    self.tires[0] -= distance * 0.0016
                    self.tires[1] -= distance * 0.0016
                    self.tires[2] -= distance * 0.0013
                    self.tires[3] -= distance * 0.0013
                for i in range(len(self.tires)):
                    self.tires[i] = round(self.tires[i], 4)
                self.mileage += distance
                return "OK"
            else:
                return "Пора на заправку"
        else:
            return "Пора на шиномонтаж"


class Truck(Vehicle):
    def __init__(self, manufacturer, model, release_date, lifting):
        super().__init__(manufacturer, model, release_date)
        self.tires = [5, 5, 5, 5, 5, 5]
        self.gas_tank = 300
        self.lifting = lifting
        self.gas_tank_max = 300

    def display_info(self):
        info = super().display_info()
        info.append("Грузоподъемность (тонн): " + str(self.lifting))
        info_to_return = ""
        for i in info:
            info_to_return += i + "\n"
        return info_to_return

    def ride(self, distance):
        if sum(self.tires) >= 3 and self.tires[1] > 1.5:
            if distance / 5 <= self.gas_tank:
                self.gas_tank -= distance / 5
                self.gas_tank = round(self.gas_tank, 4)
                for i in range(len(self.tires)):
                    self.tires[i] -= round(distance * 0.005, 4)
                    self.tires[i] = round(self.tires[i], 4)
                self.mileage += distance
                return "OK"
            else:
                return "Пора на заправку"
        else:
            return "Пора на шиномонтаж"


class ExampleApp(QtWidgets.QMainWindow, gibdd.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.moto = Motocycle("Kawasaki", "Ninja 650", 2014)
        self.car = Car("Nissan", "Silvia S15", 2002, 2)
        self.truck = Truck("IVECO", "Trakker", 2018, 25)
        self.selectVehicle.addItems(["Мотоцикл", "Автмобиль", "Грузовой транспорт"])
        self.selectVehicle.activated.connect(self.activated)
        self.pushGas.clicked.connect(self.gas_station)
        self.pushTier.clicked.connect(self.tier_station)
        self.pushRide.clicked.connect(self.try_to_ride)
        self.__moto_selected()

    def activated(self, index):
        if index == 0:
            self.__moto_selected()
        elif index == 1:
            self.__car_selected()
        elif index == 2:
            self.__truck_selected()

    def __moto_selected(self):
        self.label.setText(self.moto.display_info())

    def __car_selected(self):
        self.label.setText(self.car.display_info())

    def __truck_selected(self):
        self.label.setText(self.truck.display_info())

    def gas_station(self):
        index = self.selectVehicle.currentIndex()
        if index == 0:
            self.moto.gas_station()
            self.__moto_selected()
        elif index == 1:
            self.car.gas_station()
            self.__car_selected()
        elif index == 2:
            self.truck.gas_station()
            self.__truck_selected()

    def tier_station(self):
        index = self.selectVehicle.currentIndex()
        if index == 0:
            self.moto.tire_service()
            self.__moto_selected()
        elif index == 1:
            self.car.tire_service()
            self.__car_selected()
        elif index == 2:
            self.truck.tire_service()
            self.__truck_selected()

    def try_to_ride(self):
        now_selected = self.selectVehicle.currentIndex()
        if now_selected == 0:
            trying = self.moto.ride(self.spinRide.value())
            if trying == "OK":
                self.__moto_selected()
            else:
                error_dialog.showMessage(trying)
        elif now_selected == 1:
            trying = self.car.ride(self.spinRide.value())
            if trying == "OK":
                self.__car_selected()
            else:
                error_dialog.showMessage(trying)
        elif now_selected == 2:
            trying = self.truck.ride(self.spinRide.value())
            if trying == "OK":
                self.__truck_selected()
            else:
                error_dialog.showMessage(trying)


app = QtWidgets.QApplication(sys.argv)
window = ExampleApp()
window.show()
error_dialog = QtWidgets.QErrorMessage()
app.exec_()
