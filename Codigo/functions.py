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

# calling the function
half_triangle(10)
print(area_of_circle(10))