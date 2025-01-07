import requests

base_url = "https://yougile.com/api-v2"
headers = {
    'Authorization' = 'Bearer r5E7QPvxBg1AJ+uzBA-MJyyKKQn-Ll-LHwDzHnYrH4TR-fLLLQjUR4KBVh-Li2NW'
}
def get_projects_list(params_to_add = None):
    resp = requests.get(base_url + '/projects', params_to_add)
    return resp.json()


def get_token(user = 'Anastasiastasia82@gmail.com', password = 'Ycheba2024*', companyId = 'a00ef800-2610-4b8e-bbe8-00d7b4a4300f'):
    creds = {
        'username': user,
        'password': password,
        'companyId': companyId
    }
    # авторизация
    resp = requests.post(base_url + '/auth/keys', json=creds)
    return resp.json()["key"]

def test_projects(): #Получение списка всех компаний
    # Получить список всех компаний
    resp = requests.get(base_url +'/projects')
    body = resp.json()
    assert resp.status_code == 200
    assert len(body) > 0