import psycopg2

try:
    conn = psycopg2.connect(
        database="mydb",
        user="postgres",
        password="password",
        host="database-2.cxqdcmpuok8u.us-east-1.rds.amazonaws.com",
        port=5432
    )
    print("Database connected")

except:
    print("Failed to connect")