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
