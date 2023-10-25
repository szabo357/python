# This file is to learn about conditionals

# The if statement is used to test if certain condition is true. if true, then a block of code
# is executed.
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number


age = 25
# The elif keyword is Python's way of saying 
# "if the previous conditions were not true, then try this condition".
if (age >= 10 and age <= 20) :
    #block1
    print("Age is between 10 an 20 years")
elif (age >= 20 and age <= 30):
    #block2
    print("Age is between 10 an 20 years")



#The else keyword catches anything which isn't caught by the preceding conditions.
if (age >= 10 and age <= 20) :
    #block1
    print("Age is between 10 an 20 years")
elif (age >= 20 and age <= 30):
    #block2
    print("Age is between 10 an 20 years")
else:
    #block3
    print("Age is  30 or greater")



