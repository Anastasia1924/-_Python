import requests

base_url = "https://yougile.com/api-v2"
headers = {
    'Authorization' : 'Bearer r5E7QPvxBg1AJ+uzBA-MJyyKKQn-Ll-LHwDzHnYrH4TR-fLLLQjUR4KBVh-Li2NW'
}

def test_get_projects(): #Получение списка всех компаний
    # Получить список всех компаний
    resp = requests.get(base_url + '/projects', headers=headers)
    body = resp.json()
    assert resp.status_code == 200
    assert len(body) > 0

def test_get_projects_negative(): #Получение списка всех компаний
    # Получить список всех компаний
    resp = requests.get(base_url + '/projects')
    body = resp.json()
    assert resp.status_code == 401

def test_create_projects(): #Получение списка всех компаний
    # Получить список всех компаний
    body = {
  "title": "Проект к дз 4"
}
    resp = requests.post(base_url + '/projects', json=body, headers=headers)
    body = resp.json()
    assert resp.status_code == 201

def test_create_projects_negative(): #Получение списка всех компаний
    # Получить список всех компаний
    body = {
  "title": "Проект к дз 4"
}
    resp = requests.post(base_url + '/projects', headers=headers)
    body = resp.json()
    assert resp.status_code == 400

def test_get_id(): #Получение списка всех компаний
    # Получить список всех компаний
    body = {
  "title": "Проект к дз 4"
}
    resp = requests.post(base_url + '/projects', json=body, headers=headers)
    body = resp.json()
    resp2 = requests.get(base_url + '/projects/'+ body['id'], headers=headers)
    assert resp2.status_code == 200

def test_get_id_negative(): #Получение списка всех компаний
    # Получить список всех компаний
    body = {
  "title": "Проект к дз 4"
}
    resp = requests.post(base_url + '/projects', json=body, headers=headers)
    body = resp.json()
    resp2 = requests.get(base_url + '/projects'+ body['id'], headers=headers)
    assert resp2.status_code == 404


def test_change_title(): #Получение списка всех компаний
    # Получить список всех компаний
    body = {
  "title": "Проект к дз 4"
}
    resp = requests.post(base_url + '/projects', json=body, headers=headers)
    body = resp.json()
    change_body = {
        "title": "Проект к дз 5"
    }
    resp2 = requests.put(base_url + '/projects/'+ body['id'], json=change_body, headers=headers)
    assert resp2.status_code == 200

def test_change_title_negative(): #Получение списка всех компаний
    # Получить список всех компаний
    body = {
  "title": "Проект к дз 4"
}
    resp = requests.post(base_url + '/projects', json=body, headers=headers)
    body = resp.json()
    change_body = {
        "title": "Проект к дз 5"
    }
    resp2 = requests.put(base_url + '/projects/'+ body['id'], json=body, headers=headers)
    assert resp2.status_code == 400

