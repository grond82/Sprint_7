import pytest
from methods.login_methods import LoginMethods
from helpers import Helpers
import requests
from url import TestUrl


@pytest.fixture()
def create_delete_courier():
    helpers_methods = Helpers()
    payload = helpers_methods.generate_courier_param()
    yield payload
    login_methods = LoginMethods()
    courier_id = login_methods.get_courier_id(payload)
    requests.delete(f'{TestUrl.COURIER_URL}/{courier_id}')