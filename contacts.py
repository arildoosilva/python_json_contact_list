import json
from pprint import pprint

class Person:
 def __init__(self, name, num):
  self.name = name
  self.num = num
 def addPerson(self):
  data = { 'name':self.name, 'num':self.num }
  json_file=open('data.json')
  json_data = json.load(json_file)
  json_data.append(data)
  json_file.close()
  with open('data.json', mode='w', encoding='utf-8') as json_file:
   json.dump(json_data, json_file)
   print('Saved')

 def getContactsPPrint():
  json_data=open('data.json')
  data = json.load(json_data)
  for line in range(0, len(data)):
   print(' - '.join([data[line]['name'], data[line]['num']]))
  json_data.close()

 def getContactsJSON():
  data = json.loads(open("data.json").read())
  print(json.dumps(data, indent=4, sort_keys=True))

 def search(string_to_match):
  json_data=open('data.json')
  data = json.load(json_data)
  for line in range(0, len(data)):
   if (string_to_match in data[line]['name']):
    print(' - '.join([data[line]['name'], data[line]['num']]))
  json_data.close()