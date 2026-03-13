import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_info():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert data["email"] == "Sincere@april.biz"

def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    assert response.status_code == 200
    assert data[2]["id"] == 3
    assert "company" in data[3]
    assert "street" in data[2]["address"]

def test_get_user_not_found():
    response = requests.get(f"{BASE_URL}/users/9999")
    data = response.json()
    assert response.status_code == 404
    assert data == {}

def test_create_user():
    new_post = {"name":"dulcie","body":"she love caden","userId":3}
    response = requests.post(f"{BASE_URL}/users", json=new_post)
    data = response.json()
    assert response.status_code == 201
    assert data["name"] == "dulcie"
    assert data["body"] == "she love caden"