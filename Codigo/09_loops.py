# Python has two types of loops
# while loops
# for loops

# we use a while loop to execute a block of code
# repeatedly intil a given condition is satisfied

# Example 1
contador=0
while contador < 5:
    print(contador)
    contador+=1
print("First while execution has finished")


# Example 2 break
# break is used to exit the while loop even though
# the while condition is true.
contador = 0
while contador < 10:
    print(contador)
    contador+=1
    if contador == 3:
        break


# Example 3 continue
#With the continue statement we can skip the current iteration, and continue with the next
contador = 0
while contador < 10:
    print(contador)
    contador+=1
    if contador == 4:
        contador+=1
        continue

# Example 4 else
# You can add an opcional else al the end of the while loop
contador = 0
while contador < 10:
    print(contador)
    contador+=1
else: 
    print(f"contador es igual a {contador}")



# for Loop
# In Python the for loop is used for iterating
# over a sequence : list,tuple,set,dictionary, or a string.

# for loop with list
my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

# for loop with Strings.
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# for loop with tuple
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# for loop with sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)

# for with dictionaries
my_dict = {"name": "Jose", "lastname": "Avila", "age": 35, "language": "Python"}

for element in my_dict:
    print(element)
    if element == "age":
        break
else:
    print("for loop for dictionaries has finished.")


# print half triangle
my_str ="#"
for _ in range(7):
    print(my_str)
    my_str+="#"
else:
    print("Triangle has been printed!")

# Nested for loops cube example

for _ in range(10):
    my_str=""
    for _ in range(10):
        my_str+="#"
    print(my_str )