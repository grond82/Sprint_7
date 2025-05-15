from url import TestUrl
import requests
import allure

class LoginMethods:

    @allure.step('Логин курьера')
    def login_courier(self, login_data):
        response = requests.post(TestUrl.LOGIN_URL, json=login_data)
        return response.status_code, response.json()

    @allure.step('Получение Id курьера')
    def get_courier_id(self, login_data):
        _, text_courier = self.login_courier(login_data)
        courier_id = list(text_courier.values())[0]
        return courier_id