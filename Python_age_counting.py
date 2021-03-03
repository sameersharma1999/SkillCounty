import requests
import ast

string_dict = requests.get('https://coderbyte.com/api/challenges/json/age-counting').text
data = ast.literal_eval(string_dict)['data'].split(',')

count = 0

for index in range(1, len(data), 2):
	if int(data[index].strip()[4:]) >= 50:
		count +=1

print(count)