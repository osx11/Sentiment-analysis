from sys import argv

from neural_network import NeuralNetwork
from exceptions.InvalidStartParameter import InvalidStartParameter
from settings import NEGATIVE_PERCENT, POSITIVE_PERCENT

if __name__ == '__main__':
    if len(argv) > 1:
        start_argument = argv[1]

        nn = NeuralNetwork(load_existing_data=True)

        if start_argument == 'train':
            nn = NeuralNetwork()
            nn.train_model()

        elif start_argument == 'test':
            nn.test_accuracy()

        elif start_argument == 'predict':
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


# def train():
    # model_ = keras.models.Sequential()
    #
    # model_.add(keras.layers.Embedding(input_dim=st.NUM_WORDS, output_dim=st.EMBEDDING_SIZE, input_length=st.PADDING_LENGTH))
    # model_.add(keras.layers.LSTM(units=16, return_sequences=True))
    # model_.add(keras.layers.LSTM(units=8))
    # model_.add(keras.layers.Dropout(0.5))
    # model_.add(keras.layers.Dense(units=1))
    # model_.add(keras.layers.Activation('sigmoid'))
    #
    # optimizer = keras.optimizers.Adam(lr=st.LEARNING_RATE)
    #
    # model_.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    # print(model_.summary())
    # print('start training')
    # sleep(2)
    #
    # try:
    #     model_.fit(x_train_pad, y_train, validation_split=0.05, epochs=st.EPOCHS, batch_size=st.BATCH_SIZE)
    # except (KeyboardInterrupt, SystemExit):
    #     print('Detected keyboard interrupt. Saving model and exiting.')
    # finally:
    #     model_.save('model.h5')
    #     del model_
    #     print('Thank you and goodbye!')
    #     exit(0)


# def load_model():
#     return keras.models.load_model('model.h5')


# def test():
#     model_ = load_model()
#     result = model_.evaluate(x_test_pad, y_test)
#     print('Accuracy: {0:.2%}'.format(result[1]))


# def predict(model_, seq_, tokenizer_):
#     # for word in seq_.split(' '):
#     #     if word not in list(tokenizer_.word_index.keys()):
#     #         print('неизвестное слово: ' + word)
#
#     for word in seq_.split(' '):
#         if get_stem(word) not in list(tokenizer_.vocab.keys()):
#             print('неизвестное слово: ' + word)
#
#     tokens = tokenizer_.texts_to_sequences([seq_])
#     pad_tokens_ = pad_tokens(tokens, st.PADDING_LENGTH)
#     prediction_ = model_.predict(pad_tokens_)
#     return prediction_
#
#
# if __name__ == '__main__':
#     keras.backend.clear_session()
#
#     print('Инициализация. Подождите.')
#
#     # подгружаем базу с постами
#
#     # TODO: привести в годный вид. типа сохранять, если мы тренируем модель, и подружать, если учим/тестим.
#
#     if argv[1] == 'train':
#         (x_train, x_test), (y_train, y_test) = load_data()
#
#         tokenizer = Tokenizer()
#         tokenizer.create_vocab(x_train + x_test)
#
#         with open('tokenizer_object.pkl', 'wb') as f:
#             dump(tokenizer, f, HIGHEST_PROTOCOL)
#
#         x_train_tokens = tokenizer.texts_to_sequences(x_train)
#         with open('tokenized_x_train.pkl', 'wb') as f:
#             dump(x_train_tokens, f, HIGHEST_PROTOCOL)
#
#         x_test_tokens = tokenizer.texts_to_sequences(x_test)
#         with open('tokenized_x_test.pkl', 'wb') as f:
#             dump(x_test_tokens, f, HIGHEST_PROTOCOL)
#
#         with open('y_train.pkl', 'wb') as f:
#             dump(y_train, f, HIGHEST_PROTOCOL)
#
#         with open('y_test.pkl', 'wb') as f:
#             dump(y_test, f, HIGHEST_PROTOCOL)
#     else:
#         with open('tokenizer_object.pkl', 'rb') as f:
#             tokenizer = load(f)
#
#         with open('tokenized_x_train.pkl', 'rb') as f:
#             x_train_tokens = load(f)
#
#         with open('tokenized_x_test.pkl', 'rb') as f:
#             x_test_tokens = load(f)
#
#         with open('y_train.pkl', 'rb') as f:
#             y_train = load(f)
#
#         with open('y_test.pkl', 'rb') as f:
#             y_test = load(f)
#
#     # превращаем слова в токены в порядке их частоты использования в постах
#     # tokenizer = keras.preprocessing.text.Tokenizer(num_words=NUM_WORDS)
#     #
#     # tokenizer.fit_on_texts(x_train + x_test)
#
#     if argv[1] == 'pred':
#         model = load_model()
#
#         print('Инициализация завершена. Введите сообщение.')
#
#         try:
#             while True:
#                 seq = input('> ')
#                 prediction = predict(model, seq, tokenizer)[0][0]
#                 if 0.35 <= prediction < 0.65:
#                     print(f'Нейтральный [{prediction:.3}]')
#                 elif prediction >= 0.65:
#                     print(f'Позитивный [{prediction:.3}]')
#                 else:
#                     print(f'Негативный [{prediction:.3}]')
#         except (KeyboardInterrupt, SystemExit):
#             print('Thank you and goodbye!')
#         finally:
#             exit(0)
#
#     # x_train_tokens = tokenizer.texts_to_sequences(x_train)
#     # x_test_tokens = tokenizer.texts_to_sequences(x_test)
#
#     # num_tokens - массив с числом токенов в каждом посте
#     # num_tokens = np.array([len(tokens) for tokens in x_train_tokens + x_test_tokens])
#
#     # нам надо, чтобы все посты были одинакого размера. для этого используются паддинги (обрезание больших постов
#     # и увеличение маленьких). в больших текстах невыгодно все приводить к самому большому размеру,
#     # но в наших постах размер самого большого - 29 слов (np.max(num_tokens)),
#     # поэтому можно все привести к этому размеру (PADDING_LENGTH).
#     # однако чтобы было понятнее, ниже оставлю формулу для нахождения значения, до которого будем обрезать/увеличивать
#     # посты
#     #
#     # находим среднее количество токенов во всех постах
#     # average = np.mean(num_tokens)  # ~8
#     #
#     # np.std - стандартное отклонение (насколько обычно значения отличаются от среднего)
#     # std = np.std(num_tokens)  # ~4
#     #
#     # сколько мы будем использовать максимум токенов в посте (для паддингов)
#     # среднее + 2*станд. отклон.
#     #
#     # это покроет ~99% всех постов: np.sum(num_tokens < np.max(num_tokens)) / len(num_tokens)
#     # max_tokens = int(average + 2 * std)  # 17
#
#     # теперь все посты будут одинакового размера
#     x_train_pad = pad_tokens(x_train_tokens, st.PADDING_LENGTH)
#     x_test_pad = pad_tokens(x_test_tokens, st.PADDING_LENGTH)
#
#     if argv[1] == 'train':
#         train()
#     elif argv[1] == 'test':
#         test()
