import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_post1():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert data["email"] == "Sincere@april.biz"

def test_get_post2():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0

def test_get_comments():
    response = requests.get(f"{BASE_URL}/posts/1/comments")
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0
    assert "email" in data[0]


def test_get_posts_list():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    assert response.status_code == 200
    assert data[2]["id"] == 3
    assert "company" in data[3]
    assert "street" in data[2]["address"]

def test_create_post():
    new_post = {"title":"测试内容","body":"这是内容","userId":1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == "测试内容"

def test_create_post2():
    new_post = {"name":"dulcie","body":"she love caden","userId":3}
    response = requests.post(f"{BASE_URL}/users", json=new_post)
    data = response.json()
    assert response.status_code == 201
    assert data["name"] == "dulcie"
    assert data["body"] == "she love caden"