# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\parsing_inf_from_social_networks\vk_parser\widget_groups_getMembers.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Groups_GetMembers(object):
    def setupUi(self, MainWindow_Groups_GetMembers):
        MainWindow_Groups_GetMembers.setObjectName("MainWindow_Groups_GetMembers")
        MainWindow_Groups_GetMembers.resize(301, 160)
        self.centralwidget = QtWidgets.QWidget(MainWindow_Groups_GetMembers)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_groups_getMembers = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_groups_getMembers.setGeometry(QtCore.QRect(10, 10, 281, 141))
        self.groupBox_groups_getMembers.setObjectName("groupBox_groups_getMembers")
        self.lineEdit_groups_getMembers_id = QtWidgets.QLineEdit(self.groupBox_groups_getMembers)
        self.lineEdit_groups_getMembers_id.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.lineEdit_groups_getMembers_id.setText("")
        self.lineEdit_groups_getMembers_id.setObjectName("lineEdit_groups_getMembers_id")
        self.label_16 = QtWidgets.QLabel(self.groupBox_groups_getMembers)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_16.setObjectName("label_16")
        self.pushButton_groups_getMembers_save = QtWidgets.QPushButton(self.groupBox_groups_getMembers)
        self.pushButton_groups_getMembers_save.setGeometry(QtCore.QRect(230, 110, 41, 23))
        self.pushButton_groups_getMembers_save.setObjectName("pushButton_groups_getMembers_save")
        self.lineEdit_groups_getMembers_status = QtWidgets.QLineEdit(self.groupBox_groups_getMembers)
        self.lineEdit_groups_getMembers_status.setEnabled(False)
        self.lineEdit_groups_getMembers_status.setGeometry(QtCore.QRect(160, 70, 111, 21))
        self.lineEdit_groups_getMembers_status.setObjectName("lineEdit_groups_getMembers_status")
        self.lineEdit_groups_getMembers_file_name = QtWidgets.QLineEdit(self.groupBox_groups_getMembers)
        self.lineEdit_groups_getMembers_file_name.setGeometry(QtCore.QRect(10, 110, 211, 21))
        self.lineEdit_groups_getMembers_file_name.setText("")
        self.lineEdit_groups_getMembers_file_name.setObjectName("lineEdit_groups_getMembers_file_name")
        self.pushButton_groups_getMembers_load = QtWidgets.QPushButton(self.groupBox_groups_getMembers)
        self.pushButton_groups_getMembers_load.setGeometry(QtCore.QRect(10, 70, 71, 23))
        self.pushButton_groups_getMembers_load.setObjectName("pushButton_groups_getMembers_load")
        self.pushButton_groups_getMembers_clear = QtWidgets.QPushButton(self.groupBox_groups_getMembers)
        self.pushButton_groups_getMembers_clear.setGeometry(QtCore.QRect(80, 70, 71, 23))
        self.pushButton_groups_getMembers_clear.setObjectName("pushButton_groups_getMembers_clear")
        MainWindow_Groups_GetMembers.setCentralWidget(self.centralwidget)
        self.action_6 = QtWidgets.QAction(MainWindow_Groups_GetMembers)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow_Groups_GetMembers)
        self.action_7.setObjectName("action_7")

        self.retranslateUi(MainWindow_Groups_GetMembers)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Groups_GetMembers)

    def retranslateUi(self, MainWindow_Groups_GetMembers):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Groups_GetMembers.setWindowTitle(_translate("MainWindow_Groups_GetMembers", "MainWindow"))
        self.groupBox_groups_getMembers.setTitle(_translate("MainWindow_Groups_GetMembers", "Поиск членов сообщества"))
        self.label_16.setText(_translate("MainWindow_Groups_GetMembers", "ID группы"))
        self.pushButton_groups_getMembers_save.setText(_translate("MainWindow_Groups_GetMembers", "Save"))
        self.lineEdit_groups_getMembers_status.setText(_translate("MainWindow_Groups_GetMembers", "Данных нет"))
        self.pushButton_groups_getMembers_load.setText(_translate("MainWindow_Groups_GetMembers", "Загрузка"))
        self.pushButton_groups_getMembers_clear.setText(_translate("MainWindow_Groups_GetMembers", "Очистка"))
        self.action_6.setText(_translate("MainWindow_Groups_GetMembers", "Создать новую базу"))
        self.action_7.setText(_translate("MainWindow_Groups_GetMembers", "Загрузить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Groups_GetMembers = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Groups_GetMembers()
    ui.setupUi(MainWindow_Groups_GetMembers)
    MainWindow_Groups_GetMembers.show()
    sys.exit(app.exec_())
