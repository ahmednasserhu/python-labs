import json
from math import sqrt

numbers = [4, 9, 16, 25, 36]

sqrt_of_numbers = list(map(lambda x: sqrt(x), numbers))

result_dict = {num: sqrt_num for num, sqrt_num in zip(numbers, sqrt_of_numbers)}

json_file_path = "result.json"

try:
    with open(json_file_path, 'w') as json_file:
        json.dump(result_dict, json_file, indent=2)
    print(f"Results written to {json_file_path}")
except IOError:
    print("Error writing to JSON file.")
