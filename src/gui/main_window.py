# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from . import mountains_rc


class Ui_SentimentAnalysis(object):
    def setupUi(self, SentimentAnalysis):
        SentimentAnalysis.setObjectName("SentimentAnalysis")
        SentimentAnalysis.setFixedSize(1500, 791)
        font = QtGui.QFont()
        font.setFamily("Fregat")
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        SentimentAnalysis.setFont(font)
        SentimentAnalysis.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        SentimentAnalysis.setAutoFillBackground(False)
        SentimentAnalysis.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.829818, x2:1, y2:0.307, stop:0 rgba(230, 0, 230, 255), stop:1 rgba(138, 2, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(SentimentAnalysis)
        self.centralwidget.setObjectName("centralwidget")
        self.mountain = QtWidgets.QLabel(self.centralwidget)
        self.mountain.setGeometry(QtCore.QRect(0, 270, 1651, 601))
        self.mountain.setStyleSheet("background: transparent;\n"
"")
        self.mountain.setObjectName("mountain")
        self.copyright = QtWidgets.QLabel(self.centralwidget)
        self.copyright.setGeometry(QtCore.QRect(1140, 750, 351, 31))
        self.copyright.setStyleSheet("background: transparent;\n"
"font: 13pt \"Fregat\";\n"
"color: #ffffff;")
        self.copyright.setObjectName("copyright")
        self.main = QtWidgets.QWidget(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(10, 26, 1481, 441))
        self.main.setStyleSheet("background: transparent;\n"
"")
        self.main.setObjectName("main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title = QtWidgets.QLabel(self.main)
        font = QtGui.QFont()
        font.setFamily("Fregat")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("color: #ffffff;\n"
"font: 36pt \"Fregat\";\n"
"font-family: \'Fregat\';\n"
"font-weight: normal;\n"
"background-color: transparent;\n"
"margin-bottom: 27px;")
        self.title.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.title.setObjectName("title")
        self.verticalLayout_3.addWidget(self.title)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text_input = QtWidgets.QPlainTextEdit(self.main)
        self.text_input.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.text_input.setAcceptDrops(True)
        self.text_input.setStyleSheet("background-color: #ecdbf7;\n"
"height: 10px;\n"
"border-radius: 3px;\n"
"color: #a7a7a7;\n"
"font: 32px \"Fregat\";\n"
"min-height: 45px;\n"
"max-height: 45px;\n"
"max-width: 1300px;\n"
"margin-left: 93px;\n"
"margin-bottom: 30px;")
        self.text_input.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.text_input.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.text_input.setObjectName("text_input")
        self.verticalLayout_2.addWidget(self.text_input)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.predict_button = QtWidgets.QPushButton(self.main)
        self.predict_button.setEnabled(True)
        self.predict_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.predict_button.setStyleSheet("background-color: #4d1a81;\n"
"color: #ffffff;\n"
"font: 19pt \"Fregat\";\n"
"border-radius: 6px;\n"
"max-width: 250px;\n"
"min-height: 45px;\n"
"/*margin-left: 618px;*/\n"
"padding: 5px 14px 5px 14px;")
        self.predict_button.setObjectName("predict_button")
        self.horizontalLayout.addWidget(self.predict_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.prediction_result = QtWidgets.QLabel(self.main)
        self.prediction_result.setStyleSheet("background-color: transparent;\n"
"color: #fff;\n"
"font: 42pt \"Fregat\";\n"
"margin-top: 10px;\n"
"text-transform: uppercase;\n"
"")
        self.prediction_result.setText("")
        self.prediction_result.setAlignment(QtCore.Qt.AlignCenter)
        self.prediction_result.setObjectName("prediction_result")
        self.verticalLayout.addWidget(self.prediction_result)
        self.prediction_percent = QtWidgets.QLabel(self.main)
        self.prediction_percent.setStyleSheet("background-color: transparent;\n"
"color: #fff;\n"
"font: 26pt \"Fregat\";")
        self.prediction_percent.setText("")
        self.prediction_percent.setAlignment(QtCore.Qt.AlignCenter)
        self.prediction_percent.setObjectName("prediction_percent")
        self.verticalLayout.addWidget(self.prediction_percent)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.information_button = QtWidgets.QLabel(self.centralwidget)
        self.information_button.setGeometry(QtCore.QRect(10, 750, 161, 31))
        self.information_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.information_button.setStyleSheet("background: transparent;\n"
"font: 13pt \"Fregat\";\n"
"color: #ffffff;")
        self.information_button.setObjectName("information_button")
        self.source_code_link = QtWidgets.QLabel(self.centralwidget)
        self.source_code_link.setGeometry(QtCore.QRect(180, 750, 191, 31))
        self.source_code_link.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.source_code_link.setFocusPolicy(QtCore.Qt.NoFocus)
        self.source_code_link.setStyleSheet("background: transparent;\n"
"font: 13pt \"Fregat\";\n"
"color: #ffffff;\n"
"")
        self.source_code_link.setObjectName("source_code_link")
        SentimentAnalysis.setCentralWidget(self.centralwidget)

        self.retranslateUi(SentimentAnalysis)
        QtCore.QMetaObject.connectSlotsByName(SentimentAnalysis)

    def retranslateUi(self, SentimentAnalysis):
        _translate = QtCore.QCoreApplication.translate
        SentimentAnalysis.setWindowTitle(_translate("SentimentAnalysis", "Sentiment Analysis"))
        self.mountain.setText(_translate("SentimentAnalysis", "<html><head/><body><p><img src=\":/mountain/mountain.png\"/></p></body></html>"))
        self.copyright.setText(_translate("SentimentAnalysis", "Copyright © 2020 Grigory Gilev"))
        self.title.setText(_translate("SentimentAnalysis", "S E N T I M E N T  A N A L Y S I S"))
        self.text_input.setPlaceholderText(_translate("SentimentAnalysis", "Введите здесь что-нибудь для определения эмоционального окраса"))
        self.predict_button.setText(_translate("SentimentAnalysis", "Предсказать"))
        self.information_button.setText(_translate("SentimentAnalysis", "О программе"))
        self.source_code_link.setText(_translate("SentimentAnalysis", "Исходный код"))
