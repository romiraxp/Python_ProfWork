'''
Доработать функцию flat_generator. Должен получиться генератор, который принимает список списков и возвращает
их плоское представление. Функция test в коде ниже также должна отработать без ошибок.
'''
import types

def flat_generator(list_of_lists):
    element = 0 # индекс элемента основного списка
    counter_outside = 1 # счетчик элементов основного списка
    while counter_outside <= len(list_of_lists):
        inside_element = 0 # индекс элемента вложенного списка
        counter_inside = 1 # счетчик элементов вложенного списка
        while counter_inside <= len(list_of_lists[element]):
            yield list_of_lists[element][inside_element] # возвращаем полученный элемент
            # увеличиваем счетчие и индекс элемента внутреннего списка
            inside_element += 1
            counter_inside += 1
        # увеличиваем счетчие и индекс элемента внешнего списка
        element += 1
        counter_outside += 1

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_2()