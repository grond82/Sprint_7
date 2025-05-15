from methods.courier_methods import CourierMethods
from data import Data
import pytest
import allure

class TestCourier:

    @allure.title('Создание курьера')
    def test_create_courier_full(self, create_delete_courier):
        courier_methods = CourierMethods()
        status_code, text = courier_methods.create_courier(create_delete_courier)
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
        assert text.get('message') == Data.MESSAGE_CREATE_COURIER_NOT_FULL

    @allure.title('Создание курьера с уже существующим логином')
    def test_create_same_courier(self, create_delete_courier):
        courier_methods = CourierMethods()
        courier_methods.create_courier(create_delete_courier)
        status_code, text = courier_methods.create_courier(create_delete_courier)
        assert status_code == 409
        assert text.get('message') == Data.MESSAGE_CREATE_SAME_COURIER

    @allure.title('Удаление курьера')
    def test_delete_courier(self):
        courier_methods = CourierMethods()
        courier_methods.create_courier(Data.CREATE_COURIER_DELETE)
        status_code, text = courier_methods.delete_courier(Data.CREATE_COURIER_DELETE)
        assert status_code == 200