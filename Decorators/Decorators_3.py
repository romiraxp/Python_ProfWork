'''
Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор, который записывает в файл дату
и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение.
Путь к файлу должен передаваться в аргументах декоратора.
Функция test_2 в коде ниже также должна отработать без ошибок.
'''
import datetime
from functools import wraps

def my_logger(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):
        start = datetime.datetime.now(datetime.UTC)
        result = old_function(*args, **kwargs)
        to_write = (f'Дата и время вызова функции {old_function.__name__}: {start}, '
                    f'аргументы: {args},{kwargs}, '
                    f'результат: {result}\n')
        with open('my_log.log', 'a', encoding='UTF-8') as f:
            f.write(to_write)
        return result

    return new_function