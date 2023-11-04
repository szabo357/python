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