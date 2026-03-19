import requests

def test_get_user_info(base_url):
    response = requests.get(f"{base_url}/users/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert data["email"] == "Sincere@april.biz"

def test_get_users_list(base_url):
    response = requests.get(f"{base_url}/users")
    data = response.json()
    assert response.status_code == 200
    assert data[2]["id"] == 3
    assert "company" in data[3]
    assert "street" in data[2]["address"]

def test_get_comments(base_url):
    response = requests.get(f"{base_url}/posts/1/comments")
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0
    assert "email" in data[0]

def test_get_user_not_found(base_url):
    response = requests.get(f"{base_url}/users/9999")
    data = response.json()
    assert response.status_code == 404
    assert data == {}

def test_create_user(base_url):
    new_post = {"name":"dulcie","body":"she love caden","userId":3}
    response = requests.post(f"{base_url}/users", json=new_post)
    data = response.json()
    assert response.status_code == 201
    assert data["name"] == "dulcie"
    assert data["body"] == "she love caden"