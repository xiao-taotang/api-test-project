# API自动化测试项目

基于 pytest 和 requests 对 REST API 进行接口自动化测试，结合 sqlite3 模拟底层数据库断言，测试对象为 JSONPlaceholder 模拟接口。

## 技术栈
- Python 3.13
- pytest
- requests
- sqlite3
- pytest-html

## 核心亮点
- 接口与数据库双向断言：跳出单调的状态码验证，通过 sqlite3 模拟真实业务的数据落库过程。使用 SQL 语句提取底层真实存储数据，完成接口响应与数据库持久化的全链路闭环验证。
- 数据驱动架构：利用 pytest 参数化功能，实现测试数据与核心代码的彻底分离。大幅降低代码冗余，提升测试框架的扩展能力与后期维护效率。
- 可视化测试报告：集成 pytest-html 插件，实现测试执行结果的自动化捕获与标准化交付。

## 测试用例

| 用例                           | 测试内容 | 类型 |
|------------------------------|----------|------|
| test_get_user_info           | 获取用户信息，验证id、name和email字段 | 正向 |
| test_get_posts_list          | 获取文章列表，验证返回数据不为空 | 正向 |
| test_get_comments            | 获取文章评论，验证email字段存在 | 正向 |
| test_get_users_list          | 获取用户列表，验证嵌套字段company和address | 正向 |
| test_get_user_not_found      | 获取不存在的用户id为9999，验证返回404及空数据 | 异常 |
| test_create_post             | POST创建文章，验证返回状态码201及字段 | 正向 |
| test_create_user             | POST创建用户，验证返回数据正确 | 正向 |
| test_get_multiple_posts      | 参数化测试，用不同id分别获取文章 | 参数化 |
| test_create_post_data_driven | POST创建文章，覆盖正常内容、多用户、特殊符号边界值共3组数据 | 数据驱动 |
| test_db                      | 结合SQL语句，验证接口请求后底层数据库的数据落库准确性 | 数据库断言 |

## 运行方式
pip install requests pytest pytest-html 

pytest test_blog.py -v --html=report.html

## 测试报告
运行后生成report.html，用浏览器打开查看。