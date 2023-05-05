import pymysql.cursors 
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='soy',
    password='1234',
    database='soy',
    cursorclass=pymysql.cursors.DictCursor,
)

with conn.cursor() as c:
    insert_sql = """
    INSERT INTO `post`(`title`, `content`) VALUES ("test1", "test2");
    """
    c.execute(insert_sql)
    conn.commit()  # 이게 없다면? => 데이터베이스의 메모리

    select_sql = """SELECT * FROM `post`;"""

    c.execute(select_sql)
    results = c.fetchall()

    for row in results:
        print("====== Post ======")
        print(f"id: {row['id']}")
        print(f"title: {row['title']}")
        print(f"content: {row['content']}")
        print(f"created_at: {row['created_at']}")
        print(f"updated_at: {row['updated_at']}\n")

