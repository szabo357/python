# Diccionarios.
# Los diccionarios son utilizados para almacenar valores en pares llave:valor.
# Un diccionario es una coleccion que esta ordenada, es actualizable y no admite duplicados.

# Formas de declarar un diccionario
my_dict = dict()
my_other_dict = {}

# Imprime el tipo de dato de las variables my_dict y my_other_dict.
print(type(my_dict))
print(type(my_other_dict))

my_dict = {'sport1':'soccer','sport2':'basketball','sport3':'volleyball','sport4':'cycling'}

my_other_dict ={ 'Nombre'  : 'Jorge',
                 'Apellido': 'Guerra',
                 'Deporte': 'Natacion'
}

# Imprime el contenido de los diccionarios.
print(my_dict)
print(my_other_dict)

# Imprime la cantidad de elementos llave-valor en el diccionario.
print(len(my_dict))

# Imprime el valor de la llave sport1
#print(my_other_dict[1]) # Key Error 1
print(my_other_dict["Nombre"])
print(my_dict.values())
print('soccer' in my_dict.values())
print(my_dict.get('first_name')) # la funcion get devuelve None si el indice no existe en el dict.
print(my_dict.get('sport1'))

# Inserción
my_dict["Calle"] = "Calle 14"
print(my_dict)

# Actualización
my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación
del my_dict["Calle"]
print(my_dict)

# Otras operaciones
print("#####################")
print(my_dict.items())  # .items() Cambia el diccionario a una lista de tuplas
print(my_dict.keys())   # .keys() devuelve una lista con todas las llaves del diccionario.
print(my_dict.values()) # .values() devuelve una lista con todos los valores del diccionario.

my_list =  ["Nombre", "Apellido", "Piso"]
my_values= ["Juan","Castro",2]
my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))

my_new_dict.update({"sport1":"ping pong"})
my_new_dict.update({"sport2":"tenis"})
my_new_dict.update({"sport3":"soccer"})
my_new_dict.update({"sport4":"baseball"})
my_new_dict.update({"Nombre":"Juan"})
print((my_new_dict))

# looping a dictionary ( return key names )
for x in my_new_dict:
  print(x)

#looping dictionaries values one by one (return values)
for x in my_new_dict:
  print(my_new_dict[x])

#looping dictionaries values ( return values)
for x in my_new_dict.values():
  print(x)

#looping dictionaries keys ( return keys)
for x in my_new_dict.keys():
  print(x)

# looping key-values of dictionary (return key-values)
for x,y in my_new_dict.items():
  print(x,y)

# make a copy of a dictionary
new_dict = my_new_dict.copy()
print( new_dict)
# del my_new_dict  deletes dictionary.

# Nested dictionaries.
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

# Accessing Nested dictionary
print(myfamily["child2"]["name"])
print(myfamily["child2"]["year"])

# dictionaries methods list
myfamily.clear()         #Removes all the elements from the dictionary
myfamily.copy()          #Returns a copy of the dictionary
myfamily.fromkeys()      #Returns a dictionary with the specified keys and value
myfamily.get()           #Returns the value of the specified key
myfamily.items()         #Returns a list containing a tuple for each key value pair
myfamily.keys()          #Returns a list containing the dictionary's keys
myfamily.pop()           #Removes the element with the specified key
myfamily.popitem()       #Removes the last inserted key-value pair
myfamily.setdefault()    #Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
myfamily.update()        #Updates the dictionary with the specified key-value pairs
myfamily.values()        #Returns a list of all the values in the dictionary
