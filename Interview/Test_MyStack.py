'''
Нужно реализовать класс Stack со следующими методами:
is_empty — проверка стека на пустоту. Метод возвращает True или False;
push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
size — возвращает количество элементов в стеке.
'''
import pytest
import classMyStack

class TestMyStack:
    def setup_method(self):
        self.my_stack = classMyStack.MyStack()

    @pytest.mark.parametrize(
        'sample',
        (
            '(((([{}]))))',
            '[([])((([[[]]])))]',
            '{()}',
            '{{[()]}}',
            'as[gh]h]fg9({)jk{f[gf]g}',
            '}{}',
            '{{[(])]}}',
            '[[{())}]'
        )
    )

    def test_balance(self, sample):
        to_compare = '()[]{}'
        for letter in sample:
            if letter in to_compare:
                res = ''.join(self.my_stack.push(letter))
        length = len(res)
        while length:
            total_res = res
            res = res.replace('{}', '')
            res = res.replace('[]', '')
            res = res.replace('()', '')
            length = len(res)
            if total_res == res:
                break
        assert length == 0, "Несбалансированно"

if __name__ == '__main__':
    my_stack = classMyStack.MyStack()
