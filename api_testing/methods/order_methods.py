from url import TestUrl
import requests
from data import Data
import allure

class OrderMethods:

    @allure.step('Создание заказа')
    def create_order(self, order_data):
        response = requests.post(TestUrl.ORDERS_URL, json = order_data)
        return response.status_code, response.json()

    @allure.step('Принятие заказа')
    def accept_order(self, track_id, courier_id):
        payload = {'courierId': courier_id}
        response = requests.put(f'{TestUrl.ACCEPT_ORDER_URL}/{track_id}', params=payload)
        return response.status_code, response.json()

    @allure.step('Получение Id заказа')
    def get_order_id(self, track_id):
        payload = {'t': track_id}
        response = requests.get(TestUrl.TRACK_ID_URL, params=payload)
        order = list(response.json().values())[0]
        order_id = order.get('id')
        return order_id

    @allure.step('Получение списка заказов курьера')
    def get_orders_by_courier(self, courier_id):
        payload = {'courierId': courier_id}
        response = requests.get(TestUrl.ORDERS_URL, params=payload)
        return response.status_code, response.text

    @allure.step('Получение trackID заказа')
    def get_track_id(self):
        order_methods = OrderMethods()
        _, text_track = order_methods.create_order(Data.ORDER_DATA_1)
        track_id = list(text_track.values())[0]
        return track_id