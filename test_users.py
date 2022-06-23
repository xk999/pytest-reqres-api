import requests
from payloads import *

users_link = "https://reqres.in/api/users"
page2 = {'page': 2}
delayed = {'delay': 3}
user2 = "https://reqres.in/api/users/2"


def test_get_users_list():
    resp = requests.get(users_link, params = page2)
    assert resp.status_code == 200, f"Error: got status code {resp.status_code} instead of 200"

def test_get_single_user():
    resp = requests.get(user2)
    assert resp.status_code == 200, f"Error: got status code {resp.status_code} instead of 200"

def test_create_user():
    resp = requests.post(users_link, data=valid_user)
    assert resp.status_code == 201, f"Error: got status code {resp.status_code} instead of 201"

def test_update_user():
    resp = requests.patch(user2, data=update_user)
    assert resp.status_code == 200, f"Error: got status code {resp.status_code} instead of 200"

def test_delete_user():
    resp = requests.delete(user2)
    assert resp.status_code == 204, f"Error: got status code {resp.status_code} instead of 205"

def test_delayed_response():
    resp = requests.get(users_link, params=delayed, timeout=3.5)
    assert resp.status_code == 200, f"Error: got status code {resp.status_code} instead of 200"