import pandas as pd
import boto3
import psycopg2

conn = psycopg2.connect(
    host="172.31.30.170",
    port=4001,
    database="library_db",
    user="postgres",
    password="root"
)

df1 = pd.read_sql("SELECT * FROM authors", conn)
df2 = pd.read_sql("SELECT * FROM books", conn)
conn.close()

csv_file = "autores_postgres.csv"
csv2_file = "libros_postgres.csv"

df1.to_csv(csv_file, index=False)
df2.to_csv(csv2_file, index=False)


s3 = boto3.client("s3")
s3.upload_file(csv_file, "libreriadata", csv_file)
s3.upload_file(csv2_file, "libreriadata", csv2_file)
