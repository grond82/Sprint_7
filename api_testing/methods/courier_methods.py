from url import TestUrl
import requests
import allure
from methods.login_methods import LoginMethods

class CourierMethods:

    @allure.step('Создание курьера')
    def create_courier(self, create_data):
        response = requests.post(TestUrl.COURIER_URL, data=create_data)
        return  response.status_code, response.json()

    @allure.step('Удаление курьера')
    def delete_courier(self,login_data):
        login_methods = LoginMethods()
        courier_id = login_methods.get_courier_id(login_data)
        response = requests.delete(f'{TestUrl.COURIER_URL}/{courier_id}')
        return response.status_code, response.text