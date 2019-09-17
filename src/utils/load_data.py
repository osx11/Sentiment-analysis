from pandas import read_csv

from settings import DATA_FOLDER


def load_data():
    """
    загружает негативный и позитивные твиты из файлов, разделяет их на "вопросы" и "ответы",
    а также на тренировочный и тестовый массивы

    :return: массив "вопросов" для тренировки, массив "вопросов" для тестов, массив "ответов" для тренировки,
    массив "ответов" для тестов
    :type: tuple
    """

    negative = read_csv(f'{DATA_FOLDER}/datasets/negative.csv', header=None, delimiter=';')
    positive = read_csv(f'{DATA_FOLDER}/datasets/positive.csv', header=None, delimiter=';')

    # сложить негативы и позитивы и рандомизировать их
    both = negative.append(positive).sample(frac=1)

    # x - пост (вопрос)
    # y - его тональность (ответ)
    x = [i for i in both[3]]
    y = [i for i in both[4]]

    assert len(x) == len(y)

    # для тренировки будут использоваться все посты, кроме последних 20к
    # последние 20к постов будут использоваться для теста
    x_train = x[:len(x)-20000]
    x_test = x[len(x)-20000:]

    y_train = y[:len(y)-20000]
    y_test = y[len(y)-20000:]

    # отдать массивы для тренировки и для тестов с ответами
    return (x_train, x_test), (y_train, y_test)
