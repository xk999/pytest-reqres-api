import pytest
import requests
from payloads import *

login_link = "https://reqres.in/api/login"

#check POST response for valid data
def test_login():
    resp = requests.post(login_link, data = valid_login)
    assert resp.status_code == 200, f"Error: got status code {resp.status_code} instead of 200"

#check POST response for invalid data
@pytest.mark.parametrize("test_data", invalid_login)
def test_invalid_login(test_data):
    assert requests.post(login_link, test_data).status_code in range(400,499), f"This invalid data was processed as valid: {test_data}"