from pymongo import MongoClient
import os
import random
import cv2
from PIL import Image
import numpy as np
client = MongoClient('mongodb://localhost:27017/')

period = ["September-October", "June-July", "October-November"]
area = ["The North", "North Central", "Central", "Southern", "South Central"]

def randomNumber():
    return round(random.uniform(5.0, 9.0), 1)
def randomColor():
    return round(random.uniform(0.52, 1), 2)

db = client["pineapple"]
collection = db["data"]

img_folder = "./image"

for i in range(1, 1471):
    for filename in os.listdir(img_folder):

        img = cv2.imread(os.path.join(img_folder, filename))
        height, width, channels = img.shape

        brightness = round(cv2.mean(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))[0], 2)
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        luminance = round(hsv_img[..., 2].mean(),2)


        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        color = cv2.mean(rgb_img)
        dominant_color = round(cv2.mean(color)[0:3][0], 2)
        
        image_document = {"path": "/image/" + filename, "width": width, "heigth": height, "color": dominant_color, "period": period[random.randint(0, 2)], "area": "Da Nang - Quang Nam", "brightness": brightness, "luminance": luminance}
        collection.insert_one(image_document)