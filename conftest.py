import pytest

# 中文编码修复
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

# 公共配置
@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"