import keras
import numpy as np
from time import sleep
from sys import argv

from load_data import load_data

NUM_WORDS = 30000
PAD = 'pre'  # вставляем паддинги в начало поста
PADDING_LENGTH = 50  # до какого размера будем обрезать/увеличивать посты
EMBEDDING_SIZE = 150
LEARNING_RATE = 0.001
EPOCHS = 15
BATCH_SIZE = 128


def pad_tokens(tokens, max_tok):
    return keras.preprocessing.sequence.pad_sequences(tokens, maxlen=max_tok, padding=PAD, truncating=PAD)


def train():
    model_ = keras.models.Sequential()

    model_.add(keras.layers.Embedding(input_dim=NUM_WORDS, output_dim=EMBEDDING_SIZE, input_length=PADDING_LENGTH))
    model_.add(keras.layers.GRU(units=32, return_sequences=True))
    model_.add(keras.layers.GRU(units=16, return_sequences=True))
    model_.add(keras.layers.GRU(units=8))
    model_.add(keras.layers.Dense(units=1, activation='sigmoid'))

    optimizer = keras.optimizers.Adam(lr=LEARNING_RATE)

    model_.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    print(model_.summary())
    print('start training')
    sleep(2)

    try:
        model_.fit(x_train_pad, y_train, validation_split=0.05, epochs=EPOCHS, batch_size=BATCH_SIZE)
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        model_.save('model.h5')
        del model_


def load_model():
    return keras.models.load_model('model.h5')


def test():
    model_ = load_model()
    result = model_.evaluate(x_test_pad, y_test)
    print('Accuracy: {0:.2%}'.format(result[1]))


def predict(model_, seq_, tokenizer_):
    for word in seq_.split(' '):
        if word not in list(tokenizer_.word_index.keys()):
            print('неизвестное слово: ' + word)

    tokens = tokenizer_.texts_to_sequences(np.array([seq_]))
    pad_tokens_ = pad_tokens(tokens, PADDING_LENGTH)
    prediction_ = model_.predict(pad_tokens_)
    return prediction_


if __name__ == '__main__':
    keras.backend.clear_session()

    print('Инициализация. Подождите.')

    # подгружаем базу с постами
    (x_train, x_test), (y_train, y_test) = load_data()

    # превращаем слова в токены в порядке их частоты использования в постах
    tokenizer = keras.preprocessing.text.Tokenizer(num_words=NUM_WORDS)
    tokenizer.fit_on_texts(np.append(x_train, x_test))

    if argv[1] == 'pred':
        model = load_model()

        print('Инициализация завершена. Введите сообщение.')

        while True:
            seq = input('> ')
            prediction = predict(model, seq, tokenizer)
            if prediction >= 0.5:
                print('Позитивный [%s]' % prediction)
            else:
                print('Негативный [%s]' % prediction)

    x_train_tokens = tokenizer.texts_to_sequences(x_train)
    x_test_tokens = tokenizer.texts_to_sequences(x_test)

    # num_tokens - массив с числом токенов в каждом посте
    num_tokens = np.array([len(tokens) for tokens in x_train_tokens + x_test_tokens])

    # нам надо, чтобы все посты были одинакого размера. для этого используются паддинги (обрезание больших постов
    # и увеличение маленьких). в больших текстах невыгодно все приводить к самому большому размеру,
    # но в наших постах размер самого большого - 29 слов (np.max(num_tokens)),
    # поэтому можно все привести к этому размеру (PADDING_LENGTH).
    # однако чтобы было понятнее, ниже оставлю формулу для нахождения значения, до которого будем обрезать/увеличивать
    # посты
    #
    # находим среднее количество токенов во всех постах
    # average = np.mean(num_tokens)  # ~8
    #
    # np.std - стандартное отклонение (насколько обычно значения отличаются от среднего)
    # std = np.std(num_tokens)  # ~4
    #
    # сколько мы будем использовать максимум токенов в посте (для паддингов)
    # среднее + 2*станд. отклон.
    #
    # это покроет ~99% всех постов: np.sum(num_tokens < np.max(num_tokens)) / len(num_tokens)
    # max_tokens = int(average + 2 * std)  # 17

    # теперь все посты будут одинакового размера
    x_train_pad = pad_tokens(x_train_tokens, PADDING_LENGTH)
    x_test_pad = pad_tokens(x_test_tokens, PADDING_LENGTH)

    if argv[1] == 'train':
        train()
    elif argv[1] == 'test':
        test()
