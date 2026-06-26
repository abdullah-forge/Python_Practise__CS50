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

# challenge 3

def calculate_bill(*args, **kwargs):
    total = sum(args)
    discount = kwargs.get('discount', 0)
    bill = total - discount
    return bill
    


bill1 = calculate_bill(100, 250, 50)
print(f"Bill 1: {bill1}")
bill2 = calculate_bill(100, 250, 50, discount=20)
print(f"Bill 2: {bill2}")

# challenge 4

def square_gen(limit):
    for n in range(1, limit + 1):
        yield n * n

x = int(input("Enter any number: "))

for index, square in enumerate(square_gen(x)):
    print(f"Index {index+1}: Square {square}")
