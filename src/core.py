from sys import argv

from neural_network import NeuralNetwork
from exceptions.InvalidStartParameter import InvalidStartParameter
from settings import NEGATIVE_PERCENT, POSITIVE_PERCENT

if __name__ == '__main__':
    if len(argv) > 1:
        start_argument = argv[1]

        if start_argument == 'train':
            nn = NeuralNetwork()
            nn.train_model()

        elif start_argument == 'test':
            nn = NeuralNetwork(load_existing_data=True)
            nn.test_accuracy()

        elif start_argument == 'predict':
            nn = NeuralNetwork(load_existing_data=True)
            print('Ввод текстов активен (CTRL + C для выхода)')

            try:
                while True:
                    text = input('> ')
                    prediction = nn.predict(text)
                    if NEGATIVE_PERCENT <= prediction < POSITIVE_PERCENT:
                        print(f'Нейтральный [{prediction:.3}]')
                    elif prediction >= POSITIVE_PERCENT:
                        print(f'Позитивный [{prediction:.3}]')
                    else:
                        print(f'Негативный [{prediction:.3}]')
            except (KeyboardInterrupt, SystemExit):
                print('Thank you and goodbye!')

        else:
            raise InvalidStartParameter

        exit(0)
