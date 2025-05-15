from methods.login_methods import LoginMethods
from methods.courier_methods import CourierMethods
from data import Data
import pytest
import allure

class TestLogin:

    @allure.title('Логин курьера')
    def test_login_courier(self, create_delete_courier):
        login_methods = LoginMethods()
        courier_methods = CourierMethods()
        courier_methods.create_courier(create_delete_courier)
        status_code, text = login_methods.login_courier(create_delete_courier)
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
        login_methods = LoginMethods()
        status_code, text = login_methods.login_courier(login_data)
        assert status_code == 400
        assert text.get('message') == Data.MESSAGE_LOGIN_NOT_FULL

    @allure.title('Логин курьера с неправильным логином и паролем')
    @pytest.mark.parametrize(
        'login_data',
        [
            (Data.LOGIN_DATA_WRONG_LOGIN),
            (Data.LOGIN_DATA_WRONG_PASSWORD)
        ]
    )
    def test_login_password_wrong(self, login_data):
        login_methods = LoginMethods()
        status_code, text = login_methods.login_courier(login_data)
        assert status_code == 404
        assert text.get('message') == Data.MESSAGE_LOGIN_PASSWORD_WRONG