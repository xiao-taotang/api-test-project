import sqlite3


def test_database_assertion():
    # 第一步：连接本地数据库。如果没有这个文件它会自动在你的项目左侧生成一个
    connection = sqlite3.connect("test_project.db")
    cursor = connection.cursor()

    # 第二步：建表。我们在数据库里建一个叫 posts 的表格用来存文章
    cursor.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, body TEXT, userId INTEGER)")

    # 第三步：模拟后台真实落库逻辑。假设接口调用成功后，服务器把这条数据存进了数据库
    cursor.execute("INSERT INTO posts (title, body, userId) VALUES ('测试内容', '这是内容', 1)")
    connection.commit()

    # 第四步：核心断言步骤。作为测试人员，我们用 SQL 语句去数据库里查出刚才存的数据
    cursor.execute("SELECT title FROM posts WHERE userId = 1")

    # 提取查询到的第一条结果
    result = cursor.fetchone()

    # 第五步：将数据库里查出来的真实标题与我们的预期结果进行严格对比
    # result 提取出来是一个组合，它的第一个元素就是标题，所以我们用索引 0 去取值
    assert result[0] == "测试内容"

    # 最后清理测试残留数据并关闭连接，保持测试环境的干净无污染
    cursor.execute("DROP TABLE posts")
    connection.commit()
    connection.close()