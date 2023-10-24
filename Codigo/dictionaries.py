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
print(my_dict['sport1'])

print(my_dict.values())

print('soccer' in my_dict.values())