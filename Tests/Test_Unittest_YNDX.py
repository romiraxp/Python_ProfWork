import requests
import configparser
from unittest import TestCase

class TestYNDX(TestCase):
    def setUp(self):
        self.folder = "UnitTestFolder"
        self.YANDEX_DRIVE_URL = 'https://cloud-api.yandex.net/v1/disk'
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.yandex_polygon_token = config.get('Settings', 'yandex_polygon_token')
        self.ya_headers = {'Authorization': self.yandex_polygon_token}
        self.yandex_params = {'path': self.folder}
        self.yandex_response = requests.put(f'{self.YANDEX_DRIVE_URL}/resources',
                                        params=self.yandex_params,
                                        headers=self.ya_headers)
        self.yandex_response_del = requests.delete(f'{self.YANDEX_DRIVE_URL}/resources',
                                        params=self.yandex_params,
                                        headers=self.ya_headers)

    def test_folder_creation(self):
        self.assertEqual(201,self.yandex_response.status_code)

    def test_folder_exists(self):
        self.assertEqual(409,self.yandex_response.status_code,"Папка не существует")

    def test_folder_delete(self):
        self.assertEqual(204,self.yandex_response_del.status_code)

    def test_folder_to_delete(self):
        self.assertEqual(404,self.yandex_response_del.status_code)

class YNDX:

    YANDEX_DRIVE_URL = 'https://cloud-api.yandex.net/v1/disk'

    def __init__(self, ya_access_token):
        self.ya_token = ya_access_token
        self.ya_headers = {'Authorization': self.ya_token}

    # метод создания папки на Яндекс диск для хранения фото
    def create_yandex_folder(self, folder):
        yandex_params = {'path': folder}
        yandex_response = requests.put(f'{self.YANDEX_DRIVE_URL}/resources',
                                       params=yandex_params,
                                       headers=self.ya_headers)
        return yandex_response.status_code

if __name__ == '__main__':
    folder_to_create = 'UnitTestFolder' #переменная для создания папки с фото из профайла
    yndx = YNDX(yandex_polygon_token)

    print(yndx.test_folder_creation(folder_to_create))
    # print(yndx.get_info_yandex_folder(folder_to_create).)