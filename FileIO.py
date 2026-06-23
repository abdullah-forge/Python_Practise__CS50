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
    #grayscale_image = im.convert("L")
    grayscale_image = size_image.convert("L")
    grayscale_image.save("ml_ready.jpg")

# Generating employee ID CARD

from PIL import Image
import sys
import csv

keyword = 1
analytics = []
match = []

with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        analytics.append({"Name" : row["Name"], "Rank" : row["Rank"]})
        #if int(keyword) in row:
         #   match.append(row)


for analytic in sorted(analytics , key = lambda analytic:int(analytic["Rank"]), reverse= False):
    print(f"{analytic['Name']} Rank is {analytic['Rank']}")
    if int(analytic['Rank']) == 1:
        id_card = Image.new(mode="RGB" , size=(300,500), color = "blue")
        filename = f"employee_id_{analytic['Name']}.png"
        id_card.save(filename)
        print(f"--> Generated ID Card Image: {filename}")
        match.append(f"ID issued to {analytic['Name']}\n")

        
with open ("id_issued_logs.txt", "a") as file:
    file.writelines(match)

