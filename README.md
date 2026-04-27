# 自动化测试项目

基于 pytest 框架，覆盖接口自动化测试与 UI 自动化测试，结合 sqlite3 模拟数据库断言，实现多层级的自动化测试方案。

## 技术栈
- Python 3.13
- pytest + pytest-html
- requests（接口测试）
- Selenium WebDriver（UI自动化）
- sqlite3（数据库断言）

## 项目结构
api-test-project/
├── conftest.py        # 公共配置与fixture
├── test_users.py      # 用户接口测试（GET/POST/异常场景）
├── test_posts.py      # 文章接口测试（GET/POST/PUT/DELETE/参数化/数据驱动）
├── test_db.py         # 数据库断言测试
├── test_ui.py         # UI自动化测试（Selenium）
├── report.html        # 测试报告
└── README.md

## 接口自动化测试

使用 requests 对 JSONPlaceholder 模拟接口进行全方法覆盖测试。

| 用例 | 测试内容 | 类型 |
|------|----------|------|
| test_get_user_info | 获取用户信息，验证id、name、email字段 | 正向 |
| test_get_posts_list | 获取文章列表，验证返回数据不为空 | 正向 |
| test_get_comments | 获取文章评论，验证email字段存在 | 正向 |
| test_get_users_list | 获取用户列表，验证嵌套字段company和address | 正向 |
| test_get_user_not_found | 获取不存在的用户，验证返回404及空数据 | 异常 |
| test_create_post | POST创建文章，验证返回201及字段 | 正向 |
| test_create_user | POST创建用户，验证返回数据正确 | 正向 |
| test_update_post | PUT修改文章，验证返回数据与修改内容一致 | 正向 |
| test_delete_post | DELETE删除文章，验证返回200 | 正向 |
| test_get_multiple_posts | 参数化测试，用不同id分别获取文章 | 参数化 |
| test_create_post_data_driven | 数据驱动POST，覆盖正常内容、多用户、特殊符号 | 数据驱动 |
| test_database_assertion | 接口请求后验证数据库落库准确性 | 数据库断言 |

## UI自动化测试

使用 Selenium WebDriver 对 Web 页面进行 UI 交互测试。

| 用例 | 测试内容 | 定位方式 |
|------|----------|----------|
| test_text_input | 文本框输入验证 | By.NAME |
| test_select_dropdown | 下拉框选择验证 | By.ID + Select |
| test_checkbox | 复选框勾选验证 | By.CSS_SELECTOR |
| test_radio_button | 单选按钮选中验证 | By.CSS_SELECTOR |
| test_link_jump | 点击链接跳转后操作验证 | By.XPATH + By.CSS_SELECTOR |

## 核心亮点
- 接口全方法覆盖：GET、POST、PUT、DELETE 四种请求方式完整测试
- 接口与数据库双向断言：通过 sqlite3 模拟数据落库，完成接口响应与数据库持久化的全链路验证
- 数据驱动架构：利用 pytest 参数化实现测试数据与代码分离
- UI自动化覆盖：涵盖文本输入、下拉框、复选框、单选按钮、页面跳转等常见交互场景
- 多种定位策略：综合运用 ID、Name、CSS Selector、XPath 等元素定位方式
- 可视化测试报告：集成 pytest-html 生成标准化测试报告

## 运行方式
```bash
pip install requests pytest pytest-html selenium

# 运行全部测试
pytest -v --html=report.html

# 仅运行接口测试
pytest test_posts.py test_users.py test_db.py -v

# 仅运行UI测试
pytest test_ui.py -v
```
##  测试报告
运行后生成 report.html，用浏览器打开查看。
