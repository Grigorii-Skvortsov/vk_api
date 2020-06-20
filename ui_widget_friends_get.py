# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\GitHub\parsing_inf_from_social_networks\vk_parser\widget_friends_get.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Friends_Get(object):
    def setupUi(self, MainWindow_Friends_Get):
        MainWindow_Friends_Get.setObjectName("MainWindow_Friends_Get")
        MainWindow_Friends_Get.resize(301, 157)
        self.centralwidget = QtWidgets.QWidget(MainWindow_Friends_Get)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_friends_get = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_friends_get.setGeometry(QtCore.QRect(10, 10, 281, 141))
        self.groupBox_friends_get.setObjectName("groupBox_friends_get")
        self.lineEdit_friends_get_id = QtWidgets.QLineEdit(self.groupBox_friends_get)
        self.lineEdit_friends_get_id.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.lineEdit_friends_get_id.setText("")
        self.lineEdit_friends_get_id.setObjectName("lineEdit_friends_get_id")
        self.label_16 = QtWidgets.QLabel(self.groupBox_friends_get)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_friends_get_status = QtWidgets.QLineEdit(self.groupBox_friends_get)
        self.lineEdit_friends_get_status.setEnabled(False)
        self.lineEdit_friends_get_status.setGeometry(QtCore.QRect(160, 70, 111, 21))
        self.lineEdit_friends_get_status.setObjectName("lineEdit_friends_get_status")
        self.lineEdit_friends_get_file_name = QtWidgets.QLineEdit(self.groupBox_friends_get)
        self.lineEdit_friends_get_file_name.setGeometry(QtCore.QRect(10, 110, 211, 21))
        self.lineEdit_friends_get_file_name.setText("")
        self.lineEdit_friends_get_file_name.setObjectName("lineEdit_friends_get_file_name")
        self.pushButton_friends_get_save = QtWidgets.QPushButton(self.groupBox_friends_get)
        self.pushButton_friends_get_save.setGeometry(QtCore.QRect(230, 110, 41, 21))
        self.pushButton_friends_get_save.setObjectName("pushButton_friends_get_save")
        self.pushButton_friends_get_load = QtWidgets.QPushButton(self.groupBox_friends_get)
        self.pushButton_friends_get_load.setGeometry(QtCore.QRect(10, 70, 71, 23))
        self.pushButton_friends_get_load.setObjectName("pushButton_friends_get_load")
        self.pushButton_friends_get_clear = QtWidgets.QPushButton(self.groupBox_friends_get)
        self.pushButton_friends_get_clear.setGeometry(QtCore.QRect(80, 70, 71, 23))
        self.pushButton_friends_get_clear.setObjectName("pushButton_friends_get_clear")
        MainWindow_Friends_Get.setCentralWidget(self.centralwidget)
        self.action_6 = QtWidgets.QAction(MainWindow_Friends_Get)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow_Friends_Get)
        self.action_7.setObjectName("action_7")

        self.retranslateUi(MainWindow_Friends_Get)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Friends_Get)

    def retranslateUi(self, MainWindow_Friends_Get):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Friends_Get.setWindowTitle(_translate("MainWindow_Friends_Get", "MainWindow"))
        self.groupBox_friends_get.setTitle(_translate("MainWindow_Friends_Get", "Поиск друзей пользователя"))
        self.label_16.setText(_translate("MainWindow_Friends_Get", "ID пользователя"))
        self.lineEdit_friends_get_status.setText(_translate("MainWindow_Friends_Get", "Данных нет"))
        self.pushButton_friends_get_save.setText(_translate("MainWindow_Friends_Get", "Save"))
        self.pushButton_friends_get_load.setText(_translate("MainWindow_Friends_Get", "Загрузка"))
        self.pushButton_friends_get_clear.setText(_translate("MainWindow_Friends_Get", "Очистка"))
        self.action_6.setText(_translate("MainWindow_Friends_Get", "Создать новую базу"))
        self.action_7.setText(_translate("MainWindow_Friends_Get", "Загрузить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_Friends_Get = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Friends_Get()
    ui.setupUi(MainWindow_Friends_Get)
    MainWindow_Friends_Get.show()
    sys.exit(app.exec_())
