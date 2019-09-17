class InvalidStartParameter(Exception):
    def __init__(self):
        super(InvalidStartParameter, self).__init__('\nУказан неверный параметр для запуска. Доступные параметры:\n'
                                                    'train - тренировка сети\n'
                                                    'test - оценка точности на тестовой выборке\n'
                                                    'predict - проверка точности предсказания')
