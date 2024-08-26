class MyStack:
    def __init__(self):
        self.mystack = []
    # is_empty — проверка стека на пустоту. Метод возвращает True или False;
    def is_empty(self,stack):
        length = len(self.mystack)
        if length == 0:
            bool_val = True
        else:
            bool_val = False
        return bool_val
    # push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
    def push(self, item):
        self.mystack.append(item)
        return self.mystack
    # pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
    def pop(self):
        length = len(self.mystack)
        if length == 0:
            return "Нет элементов для удаления"
        else:
            return self.mystack.pop()
    # peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
    def peek(self, stack):
        el = len(self.mystack) - 1
        return self.mystack[el]
    # size — возвращает количество элементов в стеке.
    def size(self,stack):
        length = len(self.mystack)
        return length

def balance(sample):
    to_compare = '()[]{}'
    for letter in sample:
        if letter in to_compare:
            res = ''.join(my_stack.push(letter))
    length = len(res)
    while length:
        total_res = res
        res = res.replace('{}', '')
        res = res.replace('[]', '')
        res = res.replace('()', '')
        length = len(res)
        if total_res == res:
            break
        if length == 0:
            res_text = 'Сбалансированно'
        else:
            res_text = 'Несбалансированно'
    return res_text

if __name__ == '__main__':
    my_stack = MyStack()
    sample = '(((([{}]))))'
    print(f'Фраза "{sample}": {balance(sample)}')
    sample = '[[{())}]'
    print(f'Фраза "{sample}": {balance(sample)}')