### Listas ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Miklos", "Szabo"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
#print(my_other_list[4])  #IndexError
#print(my_other_list[-5]) #IndexError

print(my_other_list.index("Miklos"))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("Miklos")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas
print(my_new_list[1:3])

# Cambio de tipo
my_list = "Hola Python"
print(my_list)
print(type(my_list))


# creacion de listas
print([1,2,3,4])
print(["A","B","C"])
print(["spam",2.4,1,["A","B"]])
# Las listas son mutables. es decir podemos actualizar los valores dentro de ellas.
lista =[1,2,3,4]
lista[1]=5   # asi como las cadenas los indices de las listas comienzan desde cero.
print(lista)
#El operador "in" funciona también en listas.
quesos = ['Cheddar', 'Edam', 'Gouda']
print('Edam' in quesos)
print('Brie' in quesos)

#recorriendo listas.
# Para leer el contenido de una lista.
for queso in quesos:
    print(queso)

# Para actualizar el contenido de una lista
for i in range(len(lista)):
    lista[i] = lista[i]*2
print(lista)

#Ejercicios 

def recortar(l):
    del l[0]
    del l[len(l)-1]
    return None

def medio(l):
    my_list = []
    my_list.extend(l)
    del my_list[0]
    del my_list[len(my_list) - 1]
    return my_list

fruits = ["Apple","Banana", "Carrot"]
recortar(fruits)
print(fruits)

fruits = ["Apple","Banana", "Carrot","Grape","Orange","Watermelon"]
n_list = medio(fruits)
print(n_list)

numeros = [42, 123]
print(numeros)
numeros[1]= 5
print(numeros)
