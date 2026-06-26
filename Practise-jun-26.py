# challenge 1
import re

text = "My emails are abdullah@gmail.com and admin@comsats.edu.pk, please reply soon."

pattern = r"[a-z]+@[\w.]+"
mail = re.findall(pattern,text)
print(mail)

# challenge 2 

class Box:
    def __init__(self, weight):
        self.weight = weight
    def __add__(self, other):
        return int(self.weight + other.weight)
    

box1 = Box(10.5)
box2 = Box(20.3)

total_weight = box1 + box2
print(f"Total Weight: {total_weight}")
