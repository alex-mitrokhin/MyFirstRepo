import requests

base_url = 'http://10.100.24.147:81/eldoca/app'

auth_body = {
    'login': 'ADMIN',
    'password': 'admin'
}

resp = requests.post(base_url + '/auth/login', json = auth_body)
resp_body = resp.json()
token = resp_body['accessToken']
print(token)


headers = {
     'Authorization': 'Bearer ' + token,
     'Cookie': 'refreshToken=FycxgaSUgHnBlzMqYn/qsBEm5YBcmX52/eYbm+daUHMkFWLfp7J9PhBERSBxlstB8WLIgM+GS1vVK8nrgHaxGmmstKV+I1rBqbkpItg3yD3WSeDzzKfe9uFN8uyyTzLqS8lsI7r8f0EDvfhBM1ZUcZ4C+6UMWrpnNiJQlnTeTvwOCD4HsZfwcHR4yyKoVAJjWuONs55/jgfK0yMyVmpJOi0zIxfV1Y587AlvwfttCjk='
}

body = {
    'id': "988",
    'identifier': "АТРИБУТ 988",
    'value': "988",
    'dataType': 11
}

def test_response_1():
    response_1 = requests.get(base_url + '/documents/1/attributes/count', headers=headers)
    response_1_body = response_1.json()
    assert response_1_body['count'] == 22
    assert response_1.status_code == 200

def test_response_2():
    response_2 = requests.get(base_url + '/documents/1/attributes', headers=headers)
    assert response_2.status_code == 200

def test_response_3():
    response_3 = requests.get(base_url + '/documents/1/attributes/readOnly', headers=headers)
    assert response_3.status_code == 200

def test_response_4():
    response_4 = requests.get(base_url + '/documents/1/attributes/available', headers=headers)
    assert response_4.status_code == 200

def test_response_5():
    response_5 = requests.post(base_url + '/documents/1/attributes', headers=headers, json=body)
    assert response_5.status_code == 200
