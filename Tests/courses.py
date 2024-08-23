# Наводим порядок: упорядочиваем курсы по продолжительности
import re
# from unittest import TestCase
from inputs import courses, mentors, durations
def create_courses_list(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
	    course_dict = {"title":course, "mentors":mentor, "duration":duration}
	    courses_list.append(course_dict)
    return courses_list

# С этого момента начинается выполнение задания 2
# На входе у вас есть только список курсов courses_list. Об исходных данных, на базе которых он был сделан, вы ничего не знаете

# Отсортируйте курсы по длительности (ключ duration), но при этом сохраните порядковый номер каждого курса из courses_list
# Самое простое — создать новый словарь durations_dict с ключом — duration и значением — исходным номером курса в courses_list
# Но у нас могут быть курсы с одинаковой длительностью, поэтому значение словаря — это список индексов, а не одно значение
def get_duration(courses_list):
    durations_dict = {}
# Допишите код цикла так, чтобы в нём вы получали id курса. Подсказка: помните о функции enumerate
    for id, title in enumerate(courses_list):
        key = courses_list[id]['duration']
        durations_dict.setdefault(key,[])
        durations_dict[key].append(id)
    durations_dict = dict(sorted(durations_dict.items()))
    return durations_dict
    # Получите значение из ключа duration
	# Допишите код ниже, который добавляет в словарь durations_dict по ключу key значения — id

# Отсортируем словарь по ключам. Этот код уже готов, ничего менять не нужно
# Здесь мы получаем пары ключ-значение в виде кортежа, и функция sorted выполняет сортировку по первым значениям кортежа — ключам

# Выведите курсы, отсортированные по длительности
# Допишите код цикла так, чтобы в нём вы получали из durations_dict ключи и значения
def get_result(durations_dict):
    res = ""
    for keys, key_value in durations_dict.items():
	# Допишите код, который проходит по всему списку значений и выводит на экран текст вида «название курса — длительность»
        for v in key_value:
            res = res + f'{courses_list[v]["title"]} - {keys} месяцев\n'
    return res

if __name__ == '__main__':
    # TestCase.test_main()
    courses_list = create_courses_list(courses, mentors, durations)
    duration = get_duration(courses_list)
    res = get_result(duration)
    print(res)
