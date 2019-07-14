from pandas import read_csv
from numpy import array_split


def load_data():
    negative = read_csv('negative.csv', header=None, delimiter=';')
    positive = read_csv('positive.csv', header=None, delimiter=';')

    # сложим негативы и позитивы и рандомизируем их
    both = negative.append(positive).sample(frac=1)

    # x - пост
    # y - ответ
    x = [i for i in both[3]]
    y = [i for i in both[4]]

    # заменим -1 на 0 для негативных ответов
    for i in range(len(y)):
        y[i] = 0 if y[i] == -1 else 1

    # отдаем массивы для тренировки и для тестов с ответами
    return array_split(x, 2), array_split(y, 2)
