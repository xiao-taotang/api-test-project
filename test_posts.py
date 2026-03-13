import requests

def test_get_posts_list(base_url):
    response = requests.get(f"{base_url}/posts")
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0

def test_get_post_comments(base_url):
    response = requests.get(f"{base_url}/posts/1/comments")
    data = response.json()
    assert response.status_code == 200
    assert len(data) > 0
    assert "email" in data[0]

def test_create_post(base_url):
    new_post = {"title":"测试内容","body":"这是内容","userId":1}
    response = requests.post(f"{base_url}/posts", json=new_post)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == "测试内容"

import pytest

@pytest.mark.parametrize("post_id", [1, 2, 3])

def test_get_multiple_posts(post_id, base_url):
    response = requests.get(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id