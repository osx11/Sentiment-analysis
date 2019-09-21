# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'information.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Information(object):
    def setupUi(self, Information):
        Information.setObjectName("Information")
        Information.setFixedSize(842, 731)
        self.verticalLayout = QtWidgets.QVBoxLayout(Information)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Information)
        self.label.setStyleSheet("font: 25pt \"Fregat\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Information)
        self.label_2.setStyleSheet("font: 17pt \"Fregat\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Information)
        self.label_3.setStyleSheet("font: 17pt \"Fregat\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Information)
        self.label_4.setStyleSheet("font: 17pt \"Fregat\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(Information)
        self.label_5.setStyleSheet("font: 17pt \"Fregat\";")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(Information)
        self.label_6.setStyleSheet("font: 17pt \"Fregat\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.source_code_link = QtWidgets.QLabel(Information)
        self.source_code_link.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.source_code_link.setMouseTracking(True)
        self.source_code_link.setStyleSheet("font: 17pt \"Fregat\";")
        self.source_code_link.setTextFormat(QtCore.Qt.RichText)
        self.source_code_link.setObjectName("source_code_link")
        self.verticalLayout.addWidget(self.source_code_link)

        self.retranslateUi(Information)
        QtCore.QMetaObject.connectSlotsByName(Information)

    def retranslateUi(self, Information):
        _translate = QtCore.QCoreApplication.translate
        Information.setWindowTitle(_translate("Information", "Информация о программе"))
        self.label.setText(_translate("Information", "Информация о программе"))
        self.label_2.setText(_translate("Information", "Язык программирования: Python"))
        self.label_3.setText(_translate("Information", "Библиотека нейронной сети: Keras (TensorFlow)"))
        self.label_4.setText(_translate("Information", "Время тренировки: 7 минут"))
        self.label_5.setText(_translate("Information", "Количество полных эпох обучения: 2"))
        self.label_6.setText(_translate("Information", "Точность на тестовой выборке: 74%"))
        self.source_code_link.setText(_translate("Information", "<html><head/><body><p>Исходник: <a href=\"https://github.com/osx11/Sentiment-analysis\"><span style=\" color:#4566f0;\">https://github.com/osx11/Sentiment-analysis</span></a></p></body></html>"))
