import json
from const import KEY_WORD_1, KEY_WORD_2, KEY_WORD_3
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

def wait_element(browser, delay_seconds=1, by = By.CLASS_NAME, value = None):
    return WebDriverWait(browser, delay_seconds).until(presence_of_element_located((by, value)))

def parse_data(tags):

    # тег в котором содержится информация по зарплате
    #<span class="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh">
    # пробегаемся по странице с вакансиями
    for vacancy in tags:
        a_tag = wait_element(vacancy, 1, By.TAG_NAME, 'a')
        vacancy_url = a_tag.get_attribute('href') # ссылка на вакансию
        title = vacancy.find_element(By.XPATH, '//span[@class="vacancy-name--c1Lay3KouCl7XasYakLk serp-item__title-link"]').text.strip() # вакансия

        # в "wide-container--lnYNwDTY2HXOzvtbTaHf" основная информация о зарплате, опыте работы и т.п.
        vacancy_salary = vacancy.find_element(By.XPATH, '//div[@class="wide-container--lnYNwDTY2HXOzvtbTaHf"]')

        # в блоке "wide-container--lnYNwDTY2HXOzvtbTaHf" ищем информацию о зарплате, которая лежит
        # в "fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh"
        # но ее может и не быть и в таком случае мы пишем "не указано"
        salary_val = vacancy_salary.find_element(By.XPATH, '//span[@class="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh"]')
        if salary_val:
            salary = salary_val.text.strip()
        else:
            salary = "не указано"

        # в этом блоке находится информация о компании и городе, предоставляющих вакансию
        tag_infocompany_city = vacancy.find_element(By.XPATH,'//div[@class="info-section--N695JG77kqwzxWAnSePt"]')

        # компания, предоставляющая вакансию
        vacancy_company = tag_infocompany_city.find_element(By.XPATH, '//span[@class="separate-line-on-xs--mtby5gO4J0ixtqzW38wh"]').text.strip()

        # город, в котором находится вакансия
        vacancy_city = tag_infocompany_city.find_element(By.XPATH, '//span[@data-qa="vacancy-serp__vacancy-address"]').text.strip()
        # т.к. для Django и Flask мало на странице - добавил Developer
        if KEY_WORD_1.upper() in title.upper() or KEY_WORD_2.upper() in title.upper() or KEY_WORD_3.upper() in title.upper():
            parsed_data.append({
                "link": vacancy_url,
                "title": title,
                "salary": salary,
                "company": vacancy_company,
                "city": vacancy_city
            })
    with open("parsed_data_sel.json", 'w+', encoding="UTF-8") as f:
        json.dump(parsed_data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    parsed_data = []
    path = EdgeChromiumDriverManager().install()  # вернет путь куда установится
    browser_service = Service(executable_path=path)
    driver = Edge(service=browser_service)
    driver.get("https://spb.hh.ru/search/vacancy?text=python&area=1&area=2&search_period=1")
    div_vacancy_page_info = driver.find_element(By.ID, 'a11y-main-content')
    tags = div_vacancy_page_info.find_elements(By.XPATH, '//div[@data-sentry-element ="Element"]')
    parse_data(tags)

    print("Выполение программы завершено")