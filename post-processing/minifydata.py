#only keep top 30 modules by bid points
import json

json_data = open('abp1415.json') #sorted list in descending order
data = json.load(json_data)

while (len(data) > 30):
	data.pop()

with open('abp1415-min.json', 'w') as outfile:
    json.dump(data, outfile);

json_data.close()
