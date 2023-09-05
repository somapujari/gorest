import string

import pytest as pytest
import requests
import random
import json
base_url = 'https://gorest.co.in/'
auth_token = 'Bearer 6c9316180dc780552f174994a88a7661e0d19117bb231f41e65dd366c6b7bdfe'
headers = {'authorization': auth_token}


def email_genrerate(size=8, char=string.ascii_lowercase+string.digits):
    return "".join(random.choices(char, k=size))


def test_get_requests():
    url = base_url + '/public/v2/users'

    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.status_code)
    assert response.status_code == 200
    json_data = response.json()
    json_string = json.dumps(json_data, indent=4)
    print(json_string)
    print('++++++++++++++++get_request compleated =======================')


def test_post_request():
    email = email_genrerate() + '@gmail.com'
    data = {

        "name": "vish  Gandhi",
        "email": email,
        "gender":  "male",
        "status": "active"
    }
    url = base_url + '/public/v2/users'
    headesrs = {'Autoorization': auth_token}
    res = requests.post(url, headers=headers, json=data)
    print(res.status_code)
    json_data = res.json()
    json_string = json.dumps(json_data)
    print(json_string)
    # assert json_data["name"] == "vish Gandhi"
    id = json_data["id"]
    print("++++++++++++++POST REQUESTS COMPLETED===============")
    return id

@pytest.mark.skip
def test_put_request(id):
    email = email_genrerate() + '@gmail.com'
    data = {
        "name": "sweat",
        "email":  email_genrerate()+ '@gmail.com',
        "gender": "male",
        "status": "active"
    }
    url = base_url+ f'/public/v2/users/{id}'
    headers = {'Authorization': auth_token}
    res = requests.put(url, headers=headers, json=data)
    print(res.status_code)
    json_data = res.json()
    json_string = json.dumps(json_data)
    print(json_string)
    assert json_data["name"] == "sweat"
    print("++++++++++++++PUT REQUESTS COMPLETED===============")

@pytest.mark.skip
def test_delete_requests(id):
    url = base_url + f'/public/v2/users{id}'
    res = requests.delete(url, headers=headers)
    print(res.status_code)
    assert res.status_code == 204
    print("+++++++++++++delete REQUESTS COMPLETED===============")


test_get_requests()
id = test_post_request()
# test_put_request(id)
# test_delete_requests(id)



