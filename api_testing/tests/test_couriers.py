from methods.courier_methods import CourierMethods
from data import Data
from helpers import Helpers
import pytest
import allure

class TestCourier:

    @allure.title('Создание курьера')
    def test_create_courier_full(self):
        courier_methods = CourierMethods()
        helpers_methods = Helpers()
        payload = helpers_methods.generate_courier_param()
        status_code, text = courier_methods.create_courier(payload)
        assert status_code == 201
        assert text.get('ok') == True

    @allure.title('Создание курьера без логина и пароля')
    @pytest.mark.parametrize(
        'create_data',
        [
            (Data.CREATE_COURIER_NOT_LOGIN),
            (Data.CREATE_COURIER_NOT_PASSWORD)
        ]
    )
    def test_create_courier_not_full(self,create_data):
        courier_methods = CourierMethods()
        status_code, text = courier_methods.create_courier(create_data)
        assert status_code == 400
        assert text.get('message') == "Недостаточно данных для создания учетной записи"

    @allure.title('Создание курьера с уже существующим логином')
    def test_create_same_courier(self):
        courier_methods = CourierMethods()
        status_code, text = courier_methods.create_courier(Data.CREATE_COURIER_FULL)
        assert status_code == 409
        assert text.get('message') == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Логин курьера')
    def test_login_courier(self):
        courier_methods = CourierMethods()
        status_code, text = courier_methods.login_courier(Data.LOGIN_DATA_FULL)
        assert status_code == 200
        assert list(text.keys())[0] == 'id'

    @allure.title('Логин курьера без логина и пароля')
    @pytest.mark.parametrize(
        'login_data',
        [
            (Data.LOGIN_DATA_NOT_LOGIN),
            (Data.LOGIN_DATA_NOT_PASSWORD)
        ]
    )
    def test_login_not_full(self, login_data):
        courier_methods = CourierMethods()
        status_code, text = courier_methods.login_courier(login_data)
        assert status_code == 400
        assert text.get('message') == 'Недостаточно данных для входа'

    @allure.title('Логин курьера с неправильным логином и паролем')
    @pytest.mark.parametrize(
        'login_data',
        [
            (Data.LOGIN_DATA_WRONG_LOGIN),
            (Data.LOGIN_DATA_WRONG_PASSWORD)
        ]
    )
    def test_login_password_wrong(self, login_data):
        courier_methods = CourierMethods()
        status_code, text = courier_methods.login_courier(login_data)
        assert status_code == 404
        assert text.get('message') == 'Учетная запись не найдена'

    @allure.title('Удаление курьера')
    def test_delete_courier(self):
        courier_methods = CourierMethods()
        courier_methods.create_courier(Data.CREATE_COURIER_DELETE)
        status_code, text = courier_methods.delete_courier(Data.CREATE_COURIER_DELETE)
        assert status_code == 200