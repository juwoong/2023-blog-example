from flask import Flask, render_template
from mysql.connector import pooling

import typing as t

app = Flask(__name__)

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

def get_posts() -> t.List[dict]:
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

        return results
    
    return []

@app.route('/')
def index():
    posts = get_posts()

    return render_template('index.html', items=posts)


if __name__ == "__main__":
    app.run(debug=True)

