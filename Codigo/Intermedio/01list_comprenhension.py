# creating lists using list comprenhension

my_list = [i + 1 for i in range(8)]
print(my_list)

# multipliying every value * 2
my_list = [i * 2 for i in range(8)]
print(my_list)

# multipliying iterator value
my_list = [i * i for i in range(8)]
print(my_list)

# sum to each i value.
def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(8)]
print(my_list)