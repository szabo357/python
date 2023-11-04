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