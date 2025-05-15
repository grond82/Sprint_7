from data import Data
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods
import pytest
import allure

class TestOrders:

    @allure.title('Создание заказа')
    @pytest.mark.parametrize(
        'order_data',
        [
            Data.ORDER_DATA_1,
            Data.ORDER_DATA_2,
            Data.ORDER_DATA_3,
            Data.ORDER_DATA_4
        ]
    )
    def test_create_order(self, order_data):
        order_methods = OrderMethods()
        status_code, text = order_methods.create_order(order_data)
        assert status_code == 201
        assert list(text.keys())[0] == 'track'

    @allure.title('Принятие заказа')
    def test_accept_order(self):
        courier_methods = CourierMethods()
        order_methods = OrderMethods()
        courier_id = courier_methods.get_courier_id()
        track_id = order_methods.get_track_id()
        order_id = order_methods.get_order_id(track_id)
        status_code, text = order_methods.accept_order(order_id,courier_id)
        assert status_code == 200
        assert text.get('ok') == True

    @allure.title('Получение списка заказов курьера')
    def test_get_orders_by_courier(self):
        courier_methods = CourierMethods()
        order_methods = OrderMethods()
        _, text_courier = courier_methods.login_courier(Data.LOGIN_DATA_FULL)
        courier_id = list(text_courier.values())[0]
        status_code, text = order_methods.get_orders_by_courier(courier_id)
        assert status_code == 200
