# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(299, 378)
        MainWindow.setBaseSize(QtCore.QSize(300, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_off = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_off.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_off.setFont(font)
        self.pushButton_off.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.pushButton_off.setObjectName("pushButton_off")
        self.horizontalLayout_7.addWidget(self.pushButton_off)
        self.pushButton_AC = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_AC.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_AC.setFont(font)
        self.pushButton_AC.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.pushButton_AC.setObjectName("pushButton_AC")
        self.horizontalLayout_7.addWidget(self.pushButton_AC)
        self.pushButton_perc = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_perc.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_perc.setFont(font)
        self.pushButton_perc.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.pushButton_perc.setObjectName("pushButton_perc")
        self.horizontalLayout_7.addWidget(self.pushButton_perc)
        self.pushButton_split = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_split.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_split.setFont(font)
        self.pushButton_split.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.pushButton_split.setObjectName("pushButton_split")
        self.horizontalLayout_7.addWidget(self.pushButton_split)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_6.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_6.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_6.addWidget(self.pushButton_9)
        self.pushButton_multiple = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiple.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_multiple.setFont(font)
        self.pushButton_multiple.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.pushButton_multiple.setObjectName("pushButton_multiple")
        self.horizontalLayout_6.addWidget(self.pushButton_multiple)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_minus.setFont(font)
        self.pushButton_minus.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.horizontalLayout_5.addWidget(self.pushButton_minus)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_4.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_plus.setFont(font)
        self.pushButton_plus.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.horizontalLayout_4.addWidget(self.pushButton_plus)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_0")
        self.horizontalLayout_3.addWidget(self.pushButton_0)
        self.pushButton_point = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_point.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_point.setFont(font)
        self.pushButton_point.setObjectName("pushButton_point")
        self.horizontalLayout_3.addWidget(self.pushButton_point)
        self.pushButton_LOG = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_LOG.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_LOG.setFont(font)
        self.pushButton_LOG.setStyleSheet("background-color: rgb(121, 121, 121);")
        self.pushButton_LOG.setObjectName("pushButton_LOG")
        self.horizontalLayout_3.addWidget(self.pushButton_LOG)
        self.pushButton_final = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_final.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_final.setFont(font)
        self.pushButton_final.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.pushButton_final.setObjectName("pushButton_final")
        self.horizontalLayout_3.addWidget(self.pushButton_final)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_off.setText(_translate("MainWindow", "OFF"))
        self.pushButton_AC.setText(_translate("MainWindow", "AC"))
        self.pushButton_perc.setText(_translate("MainWindow", "%"))
        self.pushButton_split.setText(_translate("MainWindow", "/"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_multiple.setText(_translate("MainWindow", "*"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_point.setText(_translate("MainWindow", "."))
        self.pushButton_LOG.setText(_translate("MainWindow", "LOG"))
        self.pushButton_final.setText(_translate("MainWindow", "="))
