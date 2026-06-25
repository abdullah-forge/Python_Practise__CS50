#Challenge 1:
import json

data = {"id": 1, "name": "Muhammad Abdullah", "role": "Intern", "is_active": True}

data_json = json.dumps(data)
print(data_json)

#challenge 2 

prices = [100, 250, 'N/A', 45, 800, 'Error', 120]

values = [x for x in prices if isinstance(x, int) and not isinstance(x,bool)]
print(values)

#challenge 3
class Student:
    def __init__(self,name, registration_id):
        self.name = name
        self.registration_id = registration_id
    def print_student(self):
        return f"name {self.name} : reistration id {self.registration_id}"


def main():
    name = "Abdullah"
    registration_id = "fa23-bce-049"
    print(student_detail(name, registration_id))

def student_detail(name, registration_id):
    student = Student(name , registration_id)
    return student.print_student()
    
if __name__ == "__main__":
    main()


#challenge 4
def main():
    price = input("Enter the Price: ")
    discount = input("Enter the discount: ")
    calculate_discount(price, discount)

def calculate_discount(price, discount):
    try:
        price = int(price)
        discount = int(discount)
    except ValueError:
        print("Invalid input: Numbers only.")
    else:
        final_price = price - discount
        print(f"Final Price is {final_price}")

if __name__ == "__main__":
    main()
#challenge 5
def my_decorators(func):
    def wrapper():
      print("API Endpoint Called!.")
      func()
    return wrapper


@my_decorators
def say_hello():
   print("Hello!")

if __name__ == "__main__":
   say_hello()

# challenge 6
temps_c = [0, 25, 30, 40, 100]

f_list = list(map(lambda c: (c * 9/5) + 32, temps_c))

print(f_list)

#challenge 7

t_word = "ERROR"
count = 0

with open ("server_logs.txt", "r") as file:
    for line in file:
        #words = line.split()
        #for word in line:
        if t_word in line:
            count +=1

print("Total Error count in file is : ", count)


