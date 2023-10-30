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

# Example 2
# break is used to exit the while loop even though
# the while condition is true.
contador = 0
while contador < 10:
    print(contador)
    contador+=1
    if contador == 3:
        break

