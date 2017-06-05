import json

with open("c:/GitH/config.json") as f:
    try:
        res = json.load(f)
    except ValueError as ex:
        print(ex)
        res ={}

print(res)