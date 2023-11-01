# Python program to read
# json file

import json

# Opening JSON file
#f = open('worlddata.json')
f = open('worldflags.json')

# returns JSON object as 
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for country in data["countries"]:
	print(country)
	

# Closing file
f.close()



