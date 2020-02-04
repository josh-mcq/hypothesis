#!/usr/local/bin/python3
import json


with open('guesses.json', 'r') as file:
    json_object = json.load(file)

json_formatted = json.dumps(json_object, indent=2)
print(json_formatted)
