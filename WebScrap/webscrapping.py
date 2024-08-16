import json
import requests
from bs4 import BeautifulSoup
from const import KEY_WORD_1, KEY_WORD_2, KEY_WORD_3, HEADERS

def parse_data(tags):
    # тег в котором содержится информация по зарплате
    #<span class="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh">
    parsed_data = []
    # пробегаемся по странице с вакансиями
    for vacancy in tags:
        a_tag = vacancy.find("a")
        vacancy_url = a_tag['href'] # ссылка на вакансию
        vacancy_title = vacancy.find(attrs={"data-qa": "serp-item__title"}) # вакансия
        title = vacancy_title.text.strip()
        # в "wide-container--lnYNwDTY2HXOzvtbTaHf" основная информация о зарплате, опыте работы и т.п.
        vacancy_salary = vacancy.find("div", class_="wide-container--lnYNwDTY2HXOzvtbTaHf")
        # в блоке "wide-container--lnYNwDTY2HXOzvtbTaHf" ищем информацию о зарплате, которая лежит
        # в "fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh"
        # но ее может и не быть и в таком случае мы пишем "не указано"
        salary_val = vacancy_salary.find("span", class_="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh")
        if salary_val:
            salary = salary_val.text.strip()
            # salary = salary.replace(u'\xa0', ' ')
            # salary = salary_val.text.replace("\u202f",' ').strip()
            # salary = salary.replace(u'\xa0', ' ')
        else:
            salary = "не указано"
        # salary = vacancy_salary.text.replace("\u202f",' ').strip()
        # salary = salary.replace(u'\xa0',' ')

        # в этом блоке находится информация о компании и городе, предоставляющих вакансию
        tag_infocompany_city = vacancy.find("div", class_="info-section--N695JG77kqwzxWAnSePt")
        # компания, предоставляющая вакансию
        vacancy_company = tag_infocompany_city.find("span", class_ ="separate-line-on-xs--mtby5gO4J0ixtqzW38wh")
        # город, в котором находится вакансия
        vacancy_city = tag_infocompany_city.find("div", class_="wide-container--lnYNwDTY2HXOzvtbTaHf")
        # т.к. для Django и Flask мало на странице - добавил Developer
        if KEY_WORD_1.upper() in title.upper() or KEY_WORD_2.upper() in title.upper() or KEY_WORD_3.upper() in title.upper():
            parsed_data.append({
                "link": vacancy_url,
                "title": title,
                "salary": salary,
                "company": vacancy_company.text.strip(),
                "city": vacancy_city.text.strip()

                # "company": vacancy_company.text.replace(u'\xa0', ' ').strip(),
                # "city": vacancy_city.text.replace(u'\xa0', ' ').strip()
            })
    with open("parsed_data.json", 'w+', encoding="UTF-8") as f:
        json.dump(parsed_data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    url = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&search_period=1" # ссылка для подключения и дальнейшего парсинга
    main_html = requests.get(url,
                         headers=HEADERS.generate()
                         ).text # получаем содержимое страницы в виде текста
    main_soup = BeautifulSoup(main_html, features="lxml") # разбор страницы библиотекой BS4

    # тег в котором содержатся все вакансии на странице
    div_vacancy_page_info = main_soup.find('div', id='a11y-main-content')
    tags = div_vacancy_page_info.find_all('div', attrs={'data-sentry-element': 'Element'})

    parse_data(tags)
    print("Выполение программы завершено")

