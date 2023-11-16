# Python program to update "worlddata.json" file.
# links to flags in "worlddata.json" file doesn't work
# "worldflags.json"file contains links to flags that works.

#Lessons Learned :
#
#0- f = open("wrlddata.json",encoding="utf8")
#	without passing the encoding to the open function. python returned
#	UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 
# 	in position 44223: character maps to <undefined>
#
#1- json.load() returns JSON object as a dictionary
#
#2- json.dump(data,f,indent=4,ensure_ascii=False)
#2-1-If ensure_ascii is true (the default), the output is guaranteed to have 
#   all incoming non-ASCII characters escaped. 
#   If ensure_ascii is false, these characters will be output as-is.
#2-2-indent = 4. adds 4 spaces of indentation to output json file.
# 	making it easier to read.
#
#3- An 'r' before a string tells the Python interpreter to treat backslashes 
# 	as a literal (raw) character. Normally, Python uses backslashes as
#  	escape characters.

import json
import os

#JSON file names stored as constants.
WORLDDATA_JSON_FILE = "worlddata.json"
WORLDFLAGS_JSON_FILE = "worldflags.json"

def open_json_file(filename:str):
	with open(filename,encoding="utf8") as f:
		return json.load(f)

def update_json_file(filename:str,data:dict):
	with open(filename,"w",encoding="utf8") as f:
		json.dump(data,f,indent=4,ensure_ascii=False)

saved_cwd = os.getcwd() #Save the current working directory..
#print("Current Working Directory is: " + saved_cwd)
os.chdir(r"C:\Users\jmsa3\Documents\Curso Python\python\Codigo\jsonfiles")
#print("Current Working Directory is: " + os.getcwd())
#file_list = os.listdir(os.getcwd())
#print(file_list)

world = open_json_file(WORLDDATA_JSON_FILE)
flags = open_json_file(WORLDFLAGS_JSON_FILE)

print(type(world["countries"]), len(world["countries"]))
print(type(flags["countries"]), len(flags["countries"]))

temp1 = world["countries"]
temp2 = flags["countries"]
s1,s2 = set() , set()

# Iterating through the json lists objects and adding the countries
# names to s1,s2 sets.
for country in temp2:s1.add(country["country"])
for country in temp1:s2.add(country["name"])

# get countries sets differences and then 
# convert it to a list and sort it in alphabetical order.
diff = list(s1.difference(s2))
diff.sort()
print(diff, f"Sets diffence length: {len(diff)}")

# Iterates temp1 and temp2 dictionaries lists to update
# temp1 flag hyperlink with the flag hyperlink contained in temp2.
for cntry in temp2:
	for country in temp1:
		if cntry["country"] == country["name"]:
			country["flag"] = cntry["flag"]
			continue

countries_data = {"countries":temp1} #creates dicitiony to update JSON file.
update_json_file(WORLDDATA_JSON_FILE,countries_data)
os.chdir(saved_cwd) # change current working directory to the original one.
