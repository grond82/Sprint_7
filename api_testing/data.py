class Data:
    LOGIN_DATA_FULL = {'login': 'timvas','password': '1234'}
    LOGIN_DATA_NOT_LOGIN = {'login': '','password': '1234'}
    LOGIN_DATA_NOT_PASSWORD = {'login': 'timvas','password': ''}
    LOGIN_DATA_WRONG_LOGIN = {'login': 'rt', 'password': '1234'}
    LOGIN_DATA_WRONG_PASSWORD = {'login': 'timvas', 'password': 'g'}
    CREATE_COURIER_FULL = {'login': 'timvas','password': '1234', 'firstName': 'timofei'}
    CREATE_COURIER_DELETE = {'login': 'timvas1', 'password': '1234', 'firstName': 'timofei1'}
    CREATE_COURIER_NOT_LOGIN = {'login': '', 'password': '1234', 'firstName': 'timofei'}
    CREATE_COURIER_NOT_PASSWORD = {'login': 'timvas', 'password': '', 'firstName': 'timofei'}
    CREATE_COURIER_NOT_FIRSTNAME = {'login': 'timvas', 'password': '1234', 'firstName': ''}
    ORDER_DATA_1 = {
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'address': 'Piter, Nevskiy prospect',
        'metroStation': '4',
        'phone': '+79211234556',
        'rentTime': '3',
        'delivery-date': '2025-06-06',
        'comment': 'Wait',
        'color': ['BLACK', 'GREY']
    }
    ORDER_DATA_2 = {
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'address': 'Piter, Nevskiy prospect',
        'metroStation': '4',
        'phone': '+79211234556',
        'rentTime': '3',
        'delivery-date': '2025-06-06',
        'comment': 'Wait',
        'color': ['BLACK']
    }
    ORDER_DATA_3 = {
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'address': 'Piter, Nevskiy prospect',
        'metroStation': '4',
        'phone': '+79211234556',
        'rentTime': '3',
        'delivery-date': '2025-06-06',
        'comment': 'Wait',
        'color': ['GREY']
    }
    ORDER_DATA_4 = {
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'address': 'Piter, Nevskiy prospect',
        'metroStation': '4',
        'phone': '+79211234556',
        'rentTime': '3',
        'delivery-date': '2025-06-06',
        'comment': 'Wait',
        'color': []
    }