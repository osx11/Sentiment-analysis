import webbrowser

from PyQt5 import QtWidgets

from gui.main_window import *
from gui.information import *
from neural_network import NeuralNetwork


def open_source_code_link(*args):
    webbrowser.open('https://github.com/osx11/Sentiment-analysis')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_SentimentAnalysis()
        self.ui.setupUi(self)

        self.neural_network = NeuralNetwork(load_existing_data=True)
        self.information_window = InformationWindow()

        self.ui.predict_button.clicked.connect(self.predict)
        self.ui.information_button.mousePressEvent = self.show_information
        self.ui.source_code_link.mousePressEvent = open_source_code_link

    def predict(self):
        input_text = self.ui.text_input.text()

        prediction = self.neural_network.predict(input_text)

        self.ui.prediction_result.setText(prediction[0])
        self.ui.prediction_percent.setText(prediction[1])

    def show_information(self, *args):
        self.information_window.show()


class InformationWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Information()
        self.ui.setupUi(self)

        self.ui.source_code_link.mousePressEvent = open_source_code_link

