#Challenge 1:
import json

data = {"id": 1, "name": "Muhammad Abdullah", "role": "Intern", "is_active": True}

data_json = json.dumps(data)
print(data_json)

#challenge 2 

prices = [100, 250, 'N/A', 45, 800, 'Error', 120]

values = [x for x in prices if isinstance(x, int) and not isinstance(x,bool)]
print(values)

