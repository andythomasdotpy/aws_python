import psycopg2
import os


def get_all_info(database,user, password, host, port):
    """ query data from the vendors table """
    query = """ SELECT * 
                FROM employee
            """

    conn = None
    try:
        conn = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

        cur = conn.cursor()
        cur.execute(query)
        print("The number of employees: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()


get_all_info(
    database="mydb",
    user="postgres",
    password=os.environ["pass.env"],
    host=os.environ["host.env"],
    port='5432'
)