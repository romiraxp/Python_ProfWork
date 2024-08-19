'''
Доработать класс FlatIterator в коде ниже. Должен получиться итератор, который принимает список списков и возвращает
их плоское представление, т. е. последовательность, состоящую из вложенных элементов.
Функция test в коде ниже также должна отработать без ошибок.
'''
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.element = 0 # начальный элемент основного списика
        # делаем начальный элемент вложенного списка как -1, потому как затем будем итерироваться
        # и увеличивать на 1 индекс элемента списка
        self.inside_element = -1 
        return self

    def __next__(self):
        # пока индекс внутреннего элемента списка не равен длине этого элемента
        if self.inside_element >= len(self.list_of_list[self.element])-1:
            self.element += 1
            self.inside_element = 0
        else:
            self.inside_element += 1

        if self.element >= len(self.list_of_list):
            raise StopIteration  # выход из цикла
        return self.list_of_list[self.element][self.inside_element] # то, что возвращается в next подставится в item и должно быть определено условие выхода из цикла

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()