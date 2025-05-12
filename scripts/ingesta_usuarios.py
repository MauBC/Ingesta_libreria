import pandas as pd
import boto3
import pymysql

conn = pymysql.connect(
    host="172.31.30.170",
    port=4002,
    user="root",
    password="admin",
    database="clientes_db"
)

df = pd.read_sql("SELECT * FROM usuarios", conn)
conn.close()

csv_file = "usuarios_mysql.csv"
df.to_csv(csv_file, index=False)

s3 = boto3.client("s3")
s3.upload_file(csv_file, "libreriadata", csv_file)
