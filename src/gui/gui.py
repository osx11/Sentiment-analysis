import webbrowser

from PyQt5 import QtWidgets

from gui.main_window import *
from gui.information import *
from neural_network import NeuralNetwork
from utils.database_manager import DataBaseManager
from settings import DATABASE_NAME


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
        self.ui.select_file.clicked.connect(self.analyze_selected_file)
        self.ui.information_button.clicked.connect(self.show_information)
        self.ui.source_code_link.clicked.connect(open_source_code_link)

        self.db_manager = DataBaseManager(DATABASE_NAME)

    def predict(self):
        input_text = self.ui.text_input.text()

        prediction = self.neural_network.predict(input_text)

        self.ui.prediction_result.setText(prediction[0])
        self.ui.prediction_percent.setText(prediction[1])

        self.db_manager.append_result([input_text, prediction[0]])

    def show_information(self, *args):
        self.information_window.show()

    def analyze_selected_file(self):
        input_filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбрать файл для анализа')[0]

        output_filename = input_filename.split('/')[-1].split('.')[0] + '_result.xlsx'
        output_database = DataBaseManager(output_filename, save_atexit_only=False)

        with open(input_filename, 'rb') as f:
            for l in f:
                input_text = l.decode('utf-8')
                prediction = self.neural_network.predict(input_text)
                output_database.append_result([input_text, prediction[0]])

        output_database.save()

        self.ui.prediction_result.setText('Анализ завершен. Результаты сохранены в')
        self.ui.prediction_percent.setText(output_filename)


class InformationWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Information()
        self.ui.setupUi(self)

        self.ui.source_code_link.mousePressEvent = open_source_code_link

