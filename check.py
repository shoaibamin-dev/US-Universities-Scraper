import json
# Opening JSON file
f = open('links.json')
 
# returns JSON object as
# a dictionary
links = json.load(f)


print(len(links), "length")
