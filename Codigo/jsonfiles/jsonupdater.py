# Python program to read
# json file
# \u to search unicode characters encoded/decoded by the json library.

import json
import os

def write_json(data,filename):
	with open(filename,"w",encoding="utf8") as f:
	#with open(filename,"w") as f:	
		#json.dump(data,f,indent=4)
		json.dump(data,f,indent=4,ensure_ascii=False)
	

saved_path = os.getcwd()
#print("Current Working Directory is: " + saved_path)
#An 'r' before a string tells the Python interpreter to treat backslashes 
# as a literal (raw) character. Normally, Python uses backslashes as
#  escape characters.
os.chdir(r"C:\Users\jmsa3\Documents\Curso Python\python\Codigo\jsonfiles")
#print("Current Working Directory is: " + os.getcwd())

#file_list = os.listdir(os.getcwd())
#print(file_list)
#file_list = os.listdir(r"C:\Users\jmsa3\Documents\Curso Python\python\Codigo\jsonfiles")


# Opening JSON file

f = open("worlddata.json",encoding="utf8")
#f = open("wrlddata.json",encoding="utf8")
# without passing the encoding to the open function. python returned
#UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 
# in position 44223: character maps to <undefined>

f2 = open("worldflags.json",encoding="utf8")

# returns JSON object as a dictionary
world = json.load(f) # dictionary
wrld = json.load(f2) # dictionary
#print(data)
print(type(world["countries"]), len(world["countries"]))
print(type(wrld["countries"]), len(wrld["countries"]))
temp1 = world["countries"]
temp2 = wrld["countries"]

# Iterating through the json list


# difference between the two dictionaries.
s1 = set()
s2 = set()

for country in temp2:
    s1.add(country["country"])
    
for country in temp1:
    s2.add(country["name"])

# get countries sets differences and then 
# convert it to a list and sort it in alphabetical order.
diff = list(s1.difference(s2))
diff.sort()

print(diff)
print(len(diff))

for cntry in temp2:
	for country in temp1:
		if cntry["country"] == country["name"]:
			country["flag"] = cntry["flag"]
			continue
		
#print(temp1)		

# Closing file
f.close()
f2.close()

new_data = {"countries":temp1}

write_json(new_data,"worlddata.json")

os.chdir(saved_path)
#print("Current Working Directory is " + saved_path)
