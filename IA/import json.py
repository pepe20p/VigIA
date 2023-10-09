import json

with open('IA/events.json') as file:

    json = json.load(file)

for i in json:
    print(i['frame'])
