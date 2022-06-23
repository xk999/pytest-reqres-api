import requests
from jsonschema import validate
from payloads import *

register_link =  "https://reqres.in/api/register"
login_link = "https://reqres.in/api/login"
users_link = "https://reqres.in/api/users"
user2_link = "https://reqres.in/api/users/2"

def test_register():
    resp = requests.post(register_link, data=valid_reg)
    validate(instance=resp.json(), schema=reg_schema)

def test_login():
    resp = requests.post(login_link, data=valid_login)
    validate(instance=resp.json(), schema=login_schema)    

def test_get_users_list():
    resp = requests.get(users_link)
    validate(instance=resp.json(), schema=get_users_schema)  

def test_get_single_user(): 
    resp = requests.get(user2_link)
    validate(instance=resp.json(), schema=single_user_schema) 

def test_create_user():
    resp = requests.post(users_link, data=valid_user)
    validate(instance=resp.json(), schema=create_user_schema)

def test_update_user():
    resp = requests.patch(user2_link, data=update_user)
    validate(instance=resp.json(), schema=update_user_schema)
    
