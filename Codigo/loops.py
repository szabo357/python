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
# print half triangle
my_str ="#"
for _ in range(7):
    print(my_str)
    my_str+="#"
else:
    print("Triangle has been printed!")