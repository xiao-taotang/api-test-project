import pytest
import requests

# 第一步：把测试数据抽离出来，存放在一个列表里
# 每一项包含了：请求体、预期状态码、预期标题
test_data = [
    ({"title": "测试内容1", "body": "这是内容1", "userId": 1}, 201, "测试内容1"),
    ({"title": "测试内容2", "body": "这是内容2", "userId": 2}, 201, "测试内容2"),
    ({"title": "特殊符号#￥%", "body": "边界测试", "userId": 3}, 201, "特殊符号#￥%")
]


# 第二步：用 parametrize 装饰器把数据传递给下方的测试函数
@pytest.mark.parametrize("payload, expected_status, expected_title", test_data)

def test_create_post(payload, expected_status, expected_title,base_url):
    # 第三步：原本写死的值，全部替换成传入的参数变量
    response = requests.post(f"{base_url}/posts", json=payload)
    data = response.json()

    assert response.status_code == expected_status
    assert data.get("title") == expected_title

