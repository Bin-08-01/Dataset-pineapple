import pymongo
import csv

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pineapple"]
collection = db["data"]

cursor = collection.find()
data = list(cursor)

with open('data.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    header = ['_id', 'path', 'width', 'heigth', 'color', 'period', 'area', 'brightness', 'luminance']
    writer.writerow(header)
    
    for item in data:
        row = [str(item['_id']), item['path'], item['width'], item['heigth'],item['color'],item['period'],item['area'],item['brightness'],item['luminance']]
        writer.writerow(row)