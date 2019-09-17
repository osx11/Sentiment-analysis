import re
from collections import Counter

import snowballstemmer

from settings import NUM_WORDS


# все, что не является русскими буквами, будет удаляться из текста
char_filter = re.compile('[^А-я ]')

stemmer = snowballstemmer.RussianStemmer()

# чтобы каждый раз не получать стемму слова алгоритмом, можно записывать их в словарь и потом брать оттуда
stem_cache = dict()


def get_stem(word):
    """
    возвращает стемму слова

    поскольку в русском языке огромное количество различных форм слов, правильнее будет использовать их стеммы (основы)
    для заполнения словаря. Используя такой подход, мне удалось повысить точность на тестовой выборке
    на 9% (с 65 до 74), что на самом деле, не смотря на низкую цифру, является большим приростом.

    примеры:

    >>> from utils.tokenizer import get_stem
    >>> get_stem('проектный')
    ... 'проекнт'
    >>> get_stem('использующий')
    ... 'использ'
    >>> get_stem('целочисленный')
    ... 'целочислен'


    :param word: слово, стемму которого нужно получить
    :type word: str

    :return: стемма полученного слова
    :type: str
    """

    stem = stem_cache.get(word, None)

    if stem:
        return stem

    word = char_filter.sub('', word).lower()
    stem = stemmer.stemWord(word)
    stem_cache[word] = stem

    return stem


class Tokenizer:
    def __init__(self):
        self.vocab = dict()
        self.word_list = Counter()

    def create_vocab(self, texts):
        """
        создает словарь по предоставленным текстам

        :param texts: лист текстов
        :type texts: list

        :return:
        """

        for text in texts:
            for word in text.split(' '):
                stem = get_stem(word)
                self.word_list[stem] += 1

        # создать словарь слов, отсортированный по количеству использований этих слов

        vocab = sorted(self.word_list, key=self.word_list.get, reverse=True)[:NUM_WORDS]
        vocab.pop(vocab.index(''))

        self.vocab = {vocab[i]: i+1 for i in range(len(vocab))}

    def get_token_id(self, token):
        """
        возвращает индекс токена (слова) в словаре

        :param token: токен, индекс которого нужно получить
        :type token: str

        :return: если токен существует в словаре, вернет его индекс, иначе None
        :type: int or None
        """

        # return self.vocab.index(token) if token in self.vocab else 0
        return self.vocab.get(token, None)

    def texts_to_sequences(self, texts):
        """
        конвертирует тексты в последовательности индексов токенов в словаре (в векторы)

        примеры:

        >>> from pickle import load
        >>> file = open('tokenizer_object.pkl', 'rb')
        >>> tokenizer = load(file)
        >>> file.close()
        >>> tokenizer.texts_to_sequences(['Системы искусственного интеллекта'])
        ... [[1746, 4071, 7531]]
        >>> tokenizer.texts_to_sequences(['"640 Кб должно хватить для любых задач"'])
        ... [[8075, 319, 515, 64, 130, 1443]]

        :param texts: тексты, которые нужно конвертировать в индексы
        :type texts: list

        :return: те же тексты, но уже записанные не словами, а индексами
        :type: list
        """

        sequences = list()

        for text in texts:
            vector = list()

            for word in text.split(' '):
                stem = get_stem(word)
                token_id = self.get_token_id(stem)

                if token_id:
                    vector.append(token_id)

            sequences.append(vector)

        return sequences
