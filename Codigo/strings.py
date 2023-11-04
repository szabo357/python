### Strings ###

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Miklos", "Szabo", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo

# Funciones de Strings
prueba = "Hola"

print(prueba.count("a"))
print(prueba.isalnum())
print(prueba.isalpha())
print(prueba.isascii())
print(prueba.isdecimal())
print(prueba.isdigit())
print(prueba.isidentifier())
print(prueba.islower())
print(prueba.isnumeric())
print(prueba.isprintable())
print(prueba.isspace())
print(prueba.istitle())
print(prueba.isupper())


#Ejercicios con strings

fruta = "Banana"

print("Recorrido cadena izquierda a derecha con while.")
indice = 0
while indice < len(fruta):
    letra = fruta[indice]
    print(letra)
    indice = indice + 1

print("Recorrido cadena derecha a izquierda con while.")
indice = len(fruta)
while indice > 0:
    print(fruta[indice-1])
    indice-=1

print("Recorrido cadena izquierda a derecha con for.")
for caracter in fruta:
    print(caracter)

print("Recorrido cadena derecha a izquierda con for.")
for caracter in fruta[::-1]:
    print(caracter)

# Rebanando cadenas ( slicing strings)
print(fruta[:3])
print(fruta[3:])
print(fruta[3:3])
print(fruta[:])
print(fruta[::])
print(fruta[::-1])    

# Contador de letras
palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)


#Ejercicio cuenta letras
def cuenta(cadena,letra):
    contador = 0
    for letr in cadena:
        if letr == letra:
            contador = contador + 1
    return contador

print(cuenta("Esta es una cadena que contiene varias letras as.","a"))

# Operador in. 
# Es un operador booleano. retorna True si la primera cadena 
# aparece como una subcadena de la segunda cadena.
print('a' in 'banana')
print("semilla" in "banana")

#Comparando cadenas
palabra = 'banana'
if palabra == 'banana':
    print('Muy bien, bananas.')

palabra = "zanahoria"
if palabra < 'banana':
    print('Tu palabra, ' + palabra + ', está antes de banana.')
elif palabra > 'banana':
    print('Tu palabra, ' + palabra + ', está después de banana.')
else:
    print('Muy bien, bananas.')

# Analizando cadenas
# Se quiere obtener la parte de la direccion de correo electronico que está
# despues de la @ 'uct.ac.za'
dato = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
arrobapos = dato.find('@')
print(f"Posicion @ {arrobapos}")

espos = dato.find(' ',arrobapos)
print(f"Posicion espacio despues de @ {espos}")

direccion = dato[arrobapos+1:espos] # rebanando la cadena para obtener 'uct.ac.za'
print(direccion)

# Operador formato %.
camellos = 42
mystr = "%d" % camellos
print(mystr, type(mystr))
print('Yo he visto %d camellos.' % camellos) # se puede insertar un valor a la cadena.
print('En %d años yo he visto %g %s.' % (3, 0.1, 'camellos'))# se pueden insertar diferentes valores a la cadena usando una tupla.

#Ejercicio 5: Toma el siguiente código en Python que almacena una cadena:
mystr = 'X-DSPAM-Confidence:0.8475'
#Utiliza find y una parte de la cadena para extraer la porción de la cadena
#después del carácter dos puntos y después utiliza la función float para
#convertir la cadena extraída en un número de punto flotante.
pos = mystr.find(":")
myfloat = float(mystr[pos+1:])
print(f"El tipo de dato es: {type(myfloat)} ", myfloat)
