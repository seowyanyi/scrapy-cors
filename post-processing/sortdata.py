import json
from pprint import pprint

json_data = open('abp0809raw.json')
data = json.load(json_data)


#convert list to string
for item in data:
    avgpts = item["AveragePoints"][0]
    title = item["ModuleTitle"][0]
    code = item["ModuleCode"][0]
    acct = item["StudentAcctType"][0]
    item["AveragePoints"] = avgpts
    item["ModuleTitle"] = title
    item["ModuleCode"] = code
    item["StudentAcctType"] = acct


results = sorted(data, key = lambda item : int(item["AveragePoints"]), reverse = True)


with open('abp0809.json', 'w') as outfile:
    json.dump(results, outfile);

json_data.close()

