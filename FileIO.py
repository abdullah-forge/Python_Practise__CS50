# Day4 topic covered are, file i/o ,txt, lis, csv, pillow, read, open , sorted , with, lambda 

keyword = "ERROR"
match = []
with open ("serverlog.txt") as file:
    for line in file:
        status,desp = line.rstrip().split(":")
        print(f"{status} : {desp}")
        if keyword in line:
            match.append(line)


with open ("criticalError.txt" , "a") as file:
    file.writelines(match)
    
# csv file 

import csv 
analytics = []

with open ("sensor.csv" , "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        analytics.append({"Sensor_ID" : row["Sensor_ID"], "Temperature" : row["Temperature"]})

for analytic in sorted(analytics, key = lambda analytic:int(analytic["Temperature"]), reverse=True):
    print(f"{analytic['Sensor_ID']} temperature is {analytic['Temperature']}")

# Pillow Library 

import sys
from PIL import Image

image = []
size = 400,400

with Image.open("test_image.jpeg") as im:
    size_image = im.resize(size)
    grayscale_image = im.convert("L")
    grayscale_image.save("ml_ready.jpg")

