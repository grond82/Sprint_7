from url import TestUrl
import requests
from data import Data
import allure

class CourierMethods:

    @allure.step('Создание курьера')
    def create_courier(self, create_data):
        response = requests.post(TestUrl.COURIER_URL, data=create_data)
        return  response.status_code, response.json()

    @allure.step('Логин курьера')
    def login_courier(self, login_data):
        response = requests.post(TestUrl.LOGIN_URL, json=login_data)
        return response.status_code, response.json()

    @allure.step('Удаление курьера')
    def delete_courier(self,login_data):
        courier_id = self.get_courier_id()
        response = requests.delete(f'{TestUrl.COURIER_URL}/{courier_id}')
        return response.status_code, response.text

    @allure.step('Получение Id курьера')
    def get_courier_id(self):
        _, text_courier = CourierMethods.login_courier(self,Data.LOGIN_DATA_FULL)
        courier_id = list(text_courier.values())[0]
        return courier_id