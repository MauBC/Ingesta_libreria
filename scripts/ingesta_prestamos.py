import pandas as pd
import boto3
from pymongo import MongoClient

client = MongoClient("mongodb://172.31.30.170:4003/")
db = client["loan"]
collection = db["loan"]

data = list(collection.find())
df = pd.json_normalize(data)
client.close()

csv_file = "prestamos_mongo.csv"
df.to_csv(csv_file, index=False)

s3 = boto3.client("s3")
s3.upload_file(csv_file, "libreriadata", csv_file)
