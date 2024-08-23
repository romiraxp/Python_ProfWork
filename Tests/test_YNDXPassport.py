import time
import pytest
import requests
import configparser
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By

URL = 'https://passport.yandex.ru/auth/'

class TestYandexAutomate:

    def setup_method(self):
        self.path = EdgeChromiumDriverManager().install()  # вернет путь куда установится
        self.browser_service = Service(executable_path=self.path)
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.login = config.get('Settings', 'LOGIN')
        self.password = config.get('Settings', 'PASSWORD')

        # driver.find_element(By.XPATH,'//*[@id="passp-field-login"]').send_keys(login)
        # driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()
        # driver.find_element(By.XPATH,'//*[@id="passp-field-passwd"]').send_keys(password)
        # driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()
        # login_field = driver.find_element(By.XPATH,'//*[@id="passp-field-login"]').send_keys(login)
        # password_field = driver.find_element(By.XPATH,'')
        # return response.status_code
    @pytest.mark.parametrize(
        'auth, status',
        (
            [('ваш_имейл@yandex.ru', 'пароль'), 200],
            [('illarion@yandex.ru', 'test'), 200]
        )

    )

    def test_navigate_to_page(self,auth,status):
        driver = Edge(service=self.browser_service)
        driver.get(URL)
        driver.find_element(By.XPATH,'//*[@id="passp-field-login"]').send_keys(auth[0])
        driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="passp-field-passwd"]').send_keys(auth[1])
        driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()
        url = driver.current_url
        response = requests.get(url,auth=auth)
        assert status == response.status_code

# if __name__ == '__main__':
#     yndx_login = TestYandexAutomate()
#     # yndx_login.login_to_YNDX(LOGIN,PASSWORD)
#     print(yndx_login.test_(LOGIN,PASSWORD))
    # // *[ @ id = "passp-field-login"] - login
    # //*[@id="passp:sign-in"] кнопка войти
    # // *[ @ id = "passp-field-passwd"] пароль
    # // *[ @ id = "passp:sign-in"] кнопка продолжить
    # //*[@id="passp-field-confirmation-code"] код подтверждения
    # // *[ @ id = "root"] / div / div[2] / div[2] / div / div / div[2] / div[3] / div / div / div[1] / div[
    #     1] / form / div / div[3] / div / button
    # // *[ @ id = "root"] / div / div[2] / div[2] / div / div / div[2] / div[3] / div / div / div[1] / div[
    #     1] / form / div / div[3] / div / button