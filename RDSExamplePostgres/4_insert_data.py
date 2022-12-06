import os
import psycopg2


def insert_data(database,user, password, host, port):
    sql = """   INSERT INTO employee (id, name, email) 
                VALUES(4, 'dan', 'dan@gmail.com') RETURNING id;"""

    conn = psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host,
        port=port
    )

    cur = conn.cursor()

    cur.execute(sql)

    id = cur.fetchone()[0]

    conn.commit()

    cur.close()

    print(f"Database insert complete. Vendor ID ={id}")



insert_data(
    database="mydb",
    user="postgres",
    password=os.environ["pass.env"],
    host=os.environ["host.env"],
    port='5432'
)