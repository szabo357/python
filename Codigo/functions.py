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

def is_prime(num)->bool:
    if num == 1:
        return False
    elif num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            return True
    else:
        return False

def sum_two_values(firstval,secondval):
    return firstval+secondval

def squarenum(num):
    return num**2


# calling the functions
half_triangle(10)
print(area_of_circle(10))
print(area_of_circle(5))
print(sum_of_numbers(5))
print(is_prime(7))
print(squarenum(sum_two_values(1,2)))
