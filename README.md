# API自动化测试项目

基于pytest+requests对REST API进行接口自动化测试，测试对象为JSONPlaceholder模拟接口。

## 技术栈
- Python 3.13
- pytest
- requests
- pytest-html（测试报告）

## 测试用例

| 用例 | 测试内容 | 类型 |
|------|----------|------|
| test_get_post1 | 获取用户信息，验证id/name/email字段 | 正向 |
| test_get_post2 | 获取文章列表，验证返回数据不为空 | 正向 |
| test_get_comments | 获取文章评论，验证email字段存在 | 正向 |
| test_get_posts_list | 获取用户列表，验证嵌套字段company/address | 正向 |
| test_create_post | POST创建文章，验证返回状态码201及字段 | 正向 |
| test_create_post2 | POST创建用户，验证返回数据正确 | 正向 |
| test_get_multiple_posts | 参数化测试，用id=1/2/3分别获取文章 | 参数化 |

## 运行方式
```
pip install requests pytest pytest-html
pytest test_blog.py -v --html=report.html
```

## 测试报告
运行后生成report.html，用浏览器打开查看。