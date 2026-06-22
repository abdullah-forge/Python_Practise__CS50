#Day3 the topic covered are random, import, from, packages, statistics, sys, sys.argv, slices, json, request
import random
import sys

if len(sys.argv) < 2:
    sys.exit("Error please provide the name")

sel = random.choice(sys.argv[1:])
print("Winner, name is ", sel)

#for arg in sys.argv[1:]:
#    print("hello, my name is ", arg)

#Practice challenge 2

import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}")
#requests.get("https://jsonplaceholder.typicode.com/users/" + sys.argv[1])
print(json.dumps(response.json(), indent=4))

o = response.json()
e_name = o["name"]
e_city = o["address"]["city"]

print(f"Name : {e_name}, City : {e_city}")
