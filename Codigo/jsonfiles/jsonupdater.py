# Python program to read
# json file

import json
import os


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

#f = open("worlddata.json",encoding="utf8")
f = open("wrlddata.json",encoding="utf8")
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

# Iterating through the json list
#nwrld = dict()

# difference between the two dictionaries.
s1 = set()
s2 = set()
diff = set()
for country in wrld["countries"]:
    s1.add(country["country"])
    
for country in world["countries"]:
    s2.add(country["name"])

diff = s1.difference(s2)
print(diff)
print(len(diff))

# for cntry in wrld["countries"]:
# 	for country in world["countries"]:
# 		if cntry["country"] not in country["name"]:
# 			print(cntry["country"])
# 			break
		
# Closing file
f.close()
f2.close()

os.chdir(saved_path)
#print("Current Working Directory is " + saved_path)
