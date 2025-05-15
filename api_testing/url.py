class TestUrl:

    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
    COURIER_URL = BASE_URL + '/courier'
    LOGIN_URL = COURIER_URL + '/login'
    ORDERS_URL = BASE_URL + '/orders'
    ACCEPT_ORDER_URL = ORDERS_URL + '/accept'
    TRACK_ID_URL = ORDERS_URL + '/track'