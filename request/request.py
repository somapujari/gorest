import string

import requests
import random
import json
auth_token = 'Bearer 6c9316180dc780552f174994a88a7661e0d19117bb231f41e65dd366c6b7bdfe'
base_url = 'https://gorest.co.in'
headers = {'Authorization': auth_token}


def email_generate(size=8, char=string.ascii_lowercase+string.digits):
    return ''.join(random.choices(char, k=size))


def get_request():
    url = base_url + '/public/v2/users'
    header = {'Authorization': auth_token}
    response = requests.get(url, headers=header)
    json_data = response.json()
    string = json.dumps(json_data, indent=4)
    print(string)
    assert response.status_code == 200
    print('===================get_reequest compleated ==================')


def post_request():
    url = base_url + '/public/v2/users'
    header = {'Authorization': auth_token}
    email = email_generate()+'@gmail.com'
    data = {
        "name": "vilas Gandhi",
        "email": email_generate()+'@gmail.com',
        "gender": "female",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=header)

    json_data = response.json()
    string = json.dumps(json_data, indent=4)
    print(string)
    print(response.status_code)
    assert response.status_code == 201
    assert json_data["name"] == "vilas Gandhi"
    user_id = json_data["id"]
    print(user_id)
    print('===================post_reequest compleated ==================')

    return user_id


def put_request(user_id):
    data = {
        "name": "vi bird",
        "email": email_generate()+'@gmail.com',
        "gender": "male",
        "status": "active"
    }
    url = base_url+f'/public/v2/users/{user_id}'
    response = requests.put(url, headers=headers, json=data)
    print(response.status_code)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print(json_str)
    # assert json_data["name"] == "vilas birajdar"
    assert response.status_code == 200
    print('===================put_reequest compleated ==================')


def delete_request(user_id):
    url = base_url+f'/public/v2/users/{user_id}'
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print(response.status_code)
    print('===================delete_reequest compleated ==================')


get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)


