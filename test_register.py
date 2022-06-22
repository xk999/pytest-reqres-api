from email.policy import strict
import pytest
import requests
from payloads import *

register_link =  "https://reqres.in/api/register"

#check POST response for valid data
def test_reg():
    resp = requests.post(register_link, data=valid_reg)
    assert resp.status_code == 200, f"Error: got status code {resp.status_code} instead of 200"

#check POST response for invalid data
@pytest.mark.parametrize("test_data", invalid_reg)
def test_invalid_reg(test_data):
    if test_data == invalid_reg[2]:
        pytest.xfail("Expected bug")
    assert requests.post(register_link, test_data).status_code in range(400,499), f"This invalid data was processed as valid: {test_data}"



