import emoji # импорт модуля emoji
from datetime import datetime # из модуля datetime импортируем метод datetime
from application.salary import calculate_salary # из пакета application.salary импортируем фунцию calculate_salary
from application.db.people import get_employees # из пакета application.db.people импортируем фунцию get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(emoji.emojize('\U0001F40D is :thumbs_up:'))
    print(f'Сегодня {datetime.date(datetime.today())} время {datetime.timetz(datetime.today())}')