#Generates a unique list of modules from the given data

import json

json_data1415 = open('abp1415.json')
data1415 = json.load(json_data1415)

json_data1314 = open('abp1314.json')
data1314 = json.load(json_data1314)

json_data1213 = open('abp1213.json')
data1213 = json.load(json_data1213)

overalldata = data1314 + data1415 + data1213

class Module(object):
    def __init__(self, ModuleCode, **data):
        self.ModuleCode = ModuleCode
        self.data = data

    def __eq__(self, other):
        return self.ModuleCode == other.ModuleCode

    def __hash__(self):
        return hash(('ModuleCode', self.ModuleCode))

unique = set()
masterList = []

counter = 0
for item in overalldata:
    cur = Module(**item)
    if cur not in unique:
        unique.add(cur)
        masterList.append({"ModuleCode": item["ModuleCode"], 
            "ModuleTitle": item["ModuleTitle"]})
        counter += 1
        print "added " + item["ModuleCode"] + " " + item["ModuleTitle"]

print "total modules: " + str(counter)

with open('ModulesMasterList.json', 'w') as outfile:
    json.dump(masterList, outfile);

json_data1415.close()
json_data1314.close()
json_data1213.close()