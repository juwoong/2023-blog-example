from mysql.connector import pooling

db_config = {
    'host': '127.0.0.1',
    'user': 'soy',
    'database': 'soy',
    'password': '1234',
}

pool = pooling.MySQLConnectionPool(
    pool_name = "test",
    pool_size = 10,
    **db_config,
)

conn = pool.get_connection()

if conn.is_connected():
    c = conn.cursor()
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
        print(f"id: {row[0]}")
        print(f"title: {row[1]}")
        print(f"content: {row[2]}")
        print(f"created_at: {row[3]}")
        print(f"updated_at: {row[4]}\n")
