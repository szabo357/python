# created functions file to create
# custom functions.

# function definition
def half_triangle(num:int):
    my_str ="#"
    for _ in range(num):
        print(my_str)
        my_str+="#"

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    
    return total

# calling the functions
half_triangle(10)
print(area_of_circle(10))
print(area_of_circle(5))
print(sum_of_numbers(5))
#print(sum_of_numbers(10))
#print(sum_of_numbers(100))
#print(sum_of_numbers(1000))