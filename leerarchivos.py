man_archivo = open('mbox.txt')
contador = 0

for linea in man_archivo:
    contador = contador + 1
print('Contador de líneas:', contador)

manejador_archivo = open('mbox.txt')
inp = manejador_archivo.read()

print(len(inp)) # 6687001 caracteres
print(inp[:20]) # From stephen.marquar

#Ejemplo del uso de la funcion .read() del manejador de archivos.
manejador = open('mbox.txt')
print(len(manejador.read()))

print(len(manejador.read()))# el contenido de manejador.read() se vacía despues de cada llamada.
# asi que es buena idea almacenar el contenido de manejador.read() en una variable.


# realizando una busqueda sencilla en el archivo. se imprimen todas las lineas que comienzan con "From:"
man_a = open('mbox.txt')
contador = 0
for linea in man_a:
    if linea.startswith('From:'):
        print(linea)
        contador+=1
print(f"Se encontraron {contador} coincidencias.")

# realizando busqueda de "From:" y eliminando el salto de linea \n al final de cada linea del archivo.
# esto se hace usando .rstrip() que elimina los espacios vacios a la derecha de la cadena.
contador = 0
man_a = open('mbox.txt')
for linea in man_a:
    linea = linea.rstrip()
    if linea.startswith('From:'): #Termino de busqueda.
        print(linea)
        contador+=1
print(f"Se encontraron {contador} coincidencias.")

# Ejercicio de busqueda #3. Estamos ignorando todas las lineas que no comienzan con "From"
# usando continue dentro del for para saltar a la siguiente iteracion dentro del ciclo.
contador = 0
man_a = open('mbox.txt')
for linea in man_a:
    linea = linea.rstrip()
    # Ignorar 'líneas que no nos interesan'
    if not linea.startswith('From:'):
        continue
    else:# Procesar la línea que nos 'interesa'
        print(linea)
        contador+=1
print(f"Se encontraron {contador} coincidencias.")


# Simulando un buscador de un editor de texto.
contador = 0
man_a = open('mbox.txt')
for linea in man_a:
    linea = linea.rstrip()
    if linea.find('@uct.ac.za') == -1: continue
    else:
        print(linea)
        contador+=1
print(f"Se encontraron {contador} coincidencias.")


# Permitiendo que el usuario ingrese el nombre del archivo desde consola.
# Este programa tiene un defecto. si el usuario ingresa un nombre de archivo 
# que no existe. este fallara mostrando un error
# FileNotFoundError: [Errno 2] No such file or directory: 'nothere.txt'
narchivo = input('Ingresa un nombre de archivo: ')
man_a = open(narchivo)
contador = 0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador = contador + 1
print('Hay', contador, 'líneas de asunto (subject) en', narchivo)


# Una mejor manera de tratar de solventar el problema es agregando la estructura
# try except que nos permite capturar excepciones. y evitar el fallo antes mencionado.m
narchivo = input('Ingresa un nombre de archivo: ')
try:
    man_a = open(narchivo)
except:
    print('No se puede abrir el archivo:', narchivo)
    exit()
contador = 0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador = contador + 1
print('Hay', contador, 'líneas de asunto (subject) en', narchivo)


# Escribiendo en un archivo de texto. 
escribe = open("salida.txt",'w')

escribe.write("Esta es otra linea de texto en el archivo\n")
escribe.write("Esta es una segunda linea de texto en el archivo\n")
escribe.close()