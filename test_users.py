import requests
from payloads import *

users_link = "https://reqres.in/api/users"
page2 = {'page': 2}
delayed = {'delay': 3}
user2 = "https://reqres.in/api/users/2"

def test_get_users_list():
    resp = requests.get(users_link, params = page2)
    assert resp.status_code == 200

#def test_get_single_user():
#def test_create_user():
#def test_update_user():
#def test_delete_user():

def test_delayed_response():
    resp = requests.get(users_link, params=delayed, timeout=3.5)
    assert resp.status_code == 200