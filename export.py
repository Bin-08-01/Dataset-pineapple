import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["pineapple"]
collection = db["data"]

data = pd.DataFrame(list(collection.find()))

data.to_csv("du_lieu.csv", index=False, encoding="utf-8", index_label=True)