#Phone Number validator

import re
numbers = ["0300-1234567", "+92-345-9876543", 
           "00923111234567", "0333 1234567", 
           "042-99201145"]

print("Valid Numbers")
for number in numbers:
    if re.search(r"^(0|\+92-)3\d{2}-\d{7}$", number):
        print(number)
    
    else:
        print("Invalid Number")
        print(number)

