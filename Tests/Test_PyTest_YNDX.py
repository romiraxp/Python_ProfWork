import requests
import pytest
import configparser

class TestPyYNDX:
    def setup_method(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        yandex_polygon_token = config.get('Settings', 'yandex_polygon_token')
        self.ya_headers = {'Authorization': yandex_polygon_token}
        self.folder = "PyTestFolder"
        self.YANDEX_DRIVE_URL = 'https://cloud-api.yandex.net/v1/disk'
        self.yandex_params = {'path': self.folder}

    @pytest.mark.parametrize(
        'status',
        (
            201,
            409
        )
    )

    def test_yndx_folder_creation(self, status):
        yandex_response = requests.put(f'{self.YANDEX_DRIVE_URL}/resources',
                                    params=self.yandex_params,
                                    headers=self.ya_headers)
        assert yandex_response.status_code == status

    @pytest.mark.parametrize(
        'status',
        (
            204,
            404
        )
    )

    def test_yndx_folder_removal(self, status):
        yandex_response_del = requests.delete(f'{self.YANDEX_DRIVE_URL}/resources',
                                              params=self.yandex_params,
                                              headers=self.ya_headers)
        assert yandex_response_del.status_code == status
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