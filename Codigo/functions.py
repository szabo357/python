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

# Arbitrary number of Arguments
# puede evaluar varios numeros a la vez
# si se pasan como argumento de manera independiente.
# si en cambio se pasa una lista devuelve el error
def sum_all(*args):
    total = 0
    for num in args:
        total+=num
    return total

def sum_all_listvalues(*args):
    sum = 0
    for list in args:
       for number in list:
        sum+=number
    return sum


# calling the functions
half_triangle(10)
print(area_of_circle(10))
print(area_of_circle(5))
print(sum_of_numbers(5))
print(is_prime(7))
print(squarenum(sum_two_values(1,2)))
print(sum_all(1,2,3,4,5,6))
print(sum_all_listvalues([1,2,3,4,5,6],[20,30,50],[50,100,150]))