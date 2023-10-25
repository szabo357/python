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



