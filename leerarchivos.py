man_archivo = open('mbox.txt')
contador = 0

for linea in man_archivo:
    contador = contador + 1
print('Contador de líneas:', contador)