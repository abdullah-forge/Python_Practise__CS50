# challenge 1
import re

text = "My emails are abdullah@gmail.com and admin@comsats.edu.pk, please reply soon."

pattern = r"[a-z]+@[\w.]+"
mail = re.findall(pattern,text)
print(mail)
