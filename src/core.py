from sys import argv, exit

from PyQt5 import QtWidgets

from neural_network import NeuralNetwork
from exceptions.InvalidStartParameter import InvalidStartParameter
from gui.gui import MainWindow


if __name__ == '__main__':
    if len(argv) > 1:
        start_argument = argv[1]

        if start_argument == 'train':
            nn = NeuralNetwork()
            nn.train_model()

        elif start_argument == 'test':
            nn = NeuralNetwork(load_existing_data=True)
            # nn.test_accuracy()
            nn.test_accuracy_custom()

        elif start_argument == 'predict':
            nn = NeuralNetwork(load_existing_data=True)
            print('Ввод текстов активен (CTRL + C для выхода)')

            try:
                while True:
                    text = input('> ')
                    prediction = nn.predict(text)
                    print(f'{prediction[0]} [{prediction[1]}]')
            except (KeyboardInterrupt, SystemExit):
                print('До свидания!')

        else:
            raise InvalidStartParameter

        exit(0)

    app = QtWidgets.QApplication(argv)
    main_window = MainWindow()
    main_window.show()

    exit(app.exec_())
