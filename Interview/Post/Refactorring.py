'''
Мы устроились на новую работу. Бывший сотрудник начал разрабатывать модуль для работы с почтой, но не успел доделать его. Код рабочий. Нужно только провести рефакторинг кода.
Создать класс для работы с почтой;
Создать методы для отправки и получения писем;
Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
Переменные должны быть названы по стандарту PEP8;
Весь остальной код должен соответствовать стандарту PEP8;
Класс должен инициализироваться в конструкции.
'''

import re
import classPost
from Post.inputs import recipients
'''
функция "email_check" проверки имейл (простенькая), 
которая проверяет введенный имейл на соответствие паттерну
'''
def email_check(login_email):
    pattern = r'([A-Za-z._0-9-]*)(@)([A-Za-z._0-9-]*)\.(com|ru)'
    if re.match(pattern, login_email):
        res_check = 'Yes'
    else:
        res_check = 'No'
    return res_check

if __name__ == '__main__':
    # запрашиваем ввести логин
    login_email = input('Введите логин в виде адреса электронной почты:\n')
    res = email_check(login_email) # результат проверки email помещаем в переменную res
    # если проверка прошла успешно, создаем письмо
    if res == 'Yes':
        # для получения пароля я использовал эту ссылку
        # https://myaccount.google.com/apppasswords?rapt=AEjHL4NJSclEOglUiSHjHrWNXgaIUEMF11m7VIiCflIMPjtRVklow9lIXWj5T3K1i4re3viTonG5S3w98IpMEuzfQePXPrDQTWZXyQNeEB-lkZBDi6P-jMM
        password = input('Введите пароль:')
        # создаем экземпляр класса Post
        a_message = classPost.Post(login_email, password)
        # просим ввести тему письма например,
        # "This is a my first Python scripts's message"
        subject = input('Введите тему письма:\n')
        # просим ввести текст письма, например 
        # 'Hi, dear friend!\nThis is my test message through the python script refactorr ing'
        message = input('Напишите письмо:\n')
        # вызываем метод отправки сообщения в который передаем 
        # адресатов - recipients, тему - subject, сообщение - message
        a_message.send_email(recipients, subject, message)
        
        header = None
        # печатаем результат вызова метода последнего полученного сообщения
        print(a_message.receive_email(header)) 
    else:
        print("Проверьте имейл")
