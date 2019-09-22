from keras.models import Sequential, load_model
from keras.layers import Embedding, LSTM, Dropout, Dense, Activation
from keras.optimizers import Adam
from keras.preprocessing.sequence import pad_sequences
from time import sleep

import settings as st
from utils.common_utils import load_object, dump_object
from utils.tokenizer import get_stem, Tokenizer
from utils.load_data import load_data


def pad_tokens(tokens):
    return pad_sequences(tokens, maxlen=st.PADDING_LENGTH, padding=st.PAD, truncating=st.PAD)


class NeuralNetwork:
    def __init__(self, load_existing_data=False):
        """
        модель имеет всего 4 слоев:
        1x Embedding. Векторное представления слов
        2x LSTM. На первом 16 нейронов, на втором - 8. Слой долгой краткосрочной памяти
        1x Dense. Обычный перцептрон с сигмоидальной функцией активации

        :param load_existing_data: загрузить существующие данные. По умолчанию создаются и
        сохраняются новая модель и все данные
        :type load_existing_data: bool
        """

        if load_existing_data:
            self.model = load_model(f'{st.DATA_FOLDER}/{st.MODEL_NAME}')

            self.tokenizer = load_object(f'{st.DATA_FOLDER}/tokenizer_object.pkl')
            self.x_train_tokens = load_object(f'{st.DATA_FOLDER}/tokenized_x_train.pkl')
            self.x_test_tokens = load_object(f'{st.DATA_FOLDER}/tokenized_x_test.pkl')
            self.y_train = load_object(f'{st.DATA_FOLDER}/y_train.pkl')
            self.y_test = load_object(f'{st.DATA_FOLDER}/y_test.pkl')
        else:
            # использовать последовательное описание модели
            self.model = Sequential()

            self.model.add(Embedding(input_dim=st.NUM_WORDS, output_dim=st.EMBEDDING_SIZE, input_length=st.PADDING_LENGTH))
            self.model.add(LSTM(16, return_sequences=True))
            self.model.add(LSTM(8))
            self.model.add(Dense(1, activation='sigmoid'))

            optimizer = Adam(lr=st.LEARNING_RATE)

            self.model.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

            # подгрузка датасетов
            (self.x_train, self.x_test), (self.y_train, self.y_test) = load_data()

            # создание словаря
            self.tokenizer = Tokenizer()
            self.tokenizer.create_vocab(self.x_train + self.x_test)

            # перевод текстов датасета в токены
            self.x_train_tokens = self.tokenizer.texts_to_sequences(self.x_train)
            self.x_test_tokens = self.tokenizer.texts_to_sequences(self.x_test)

            # сохранение созданных объектов
            dump_object(self.tokenizer, f'{st.DATA_FOLDER}/tokenizer_object.pkl')
            dump_object(self.x_train_tokens, f'{st.DATA_FOLDER}/tokenized_x_train.pkl')
            dump_object(self.x_test_tokens, f'{st.DATA_FOLDER}/tokenized_x_test.pkl')
            dump_object(self.y_train, f'{st.DATA_FOLDER}/y_train.pkl')
            dump_object(self.y_test, f'{st.DATA_FOLDER}/y_test.pkl')

    def test_accuracy(self):
        """
        показывает точность предсказания на тестовой выборке для текущей модели
        :return:
        """

        x_test_pad = pad_tokens(self.x_test_tokens)
        result = self.model.evaluate(x_test_pad, self.y_test)
        print(f'Accuracy: {result[1]:.2%}')

    def train_model(self):
        """
        тренировка модели

        :except KeyboardInterrupt, SystemExit: по нажатию CTRL + C тренировка прекращается и текущее состояние модели
        сохраняется в файл, указанный в settings.py

        :return:
        """

        x_train_pad = pad_tokens(self.x_train_tokens)

        print(self.model.summary())
        sleep(2)

        try:
            self.model.fit(x_train_pad, self.y_train, validation_split=0.05, epochs=st.EPOCHS, batch_size=st.BATCH_SIZE)
        except (KeyboardInterrupt, SystemExit):
            print('Detected keyboard interrupt. Saving model and exiting.')
        finally:
            self.model.save(f'{st.DATA_FOLDER}/{st.MODEL_NAME}')
            print('Thank you and goodbye!')

    def predict(self, text):
        """
        предсказывает вероятность положительного эмоционального окраса (1 - положительный, 0 - отрицательный)
        если в словаре нет стеммы какого-то слова из текста, пользователь будет уведомлен об этом

        :param text: текст, тональность которого нужно определить
        :type text: str

        :return prediction: кортеж с двумя элементами: окончательная оценка (положительный, нейтральный, отрицательный)
        и вероятность в процентах
        :type: tuple
        """

        for word in text.split(' '):
            if get_stem(word) not in list(self.tokenizer.vocab.keys()):
                print('Неизвестное слово: ' + word)

        tokens = self.tokenizer.texts_to_sequences([text])
        x_pad = pad_tokens(tokens)
        prediction = self.model.predict(x_pad)[0][0]

        if st.NEGATIVE_PERCENT <= prediction < st. POSITIVE_PERCENT:
            result = 'Нейтральный'
        elif prediction >= st.POSITIVE_PERCENT:
            result = 'Позитивный'
        else:
            result = 'Негативный'

        return result, f'{prediction*100:.4}%'
