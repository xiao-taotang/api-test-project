import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts_list():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0

def test_get_post_comments():
    response = requests.get(f"{BASE_URL}/posts/1/comments")
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0
    assert "email" in data[0]

def test_create_post():
    new_post = {"title":"测试内容","body":"这是内容","userId":1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == "测试内容"

import pytest

@pytest.mark.parametrize("post_id", [1, 2, 3])

def test_get_multiple_posts(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id