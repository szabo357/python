"""
Este programa lee todos los datos que recibe de la red y los almacena en la variable img en la memoria principal de la computadora. Después, abre el archivo
portada.jpg y escribe los datos en el disco. El argumento wb en la función open()
abre un archivo binario en modo de escritura solamente. Este programa funcionará
siempre y cuando el tamaño del archivo sea menor que el tamaño de la memoria
de la computadora.
Aún asi, si es un archivo grande de audio o video, este programa podría fallar o al
menos ejecutarse sumamente lento cuando la memoria de la computadora se haya
agotado. Para evitar que la memoria se termine, almacenamos los datos en bloques
(o buffers) y luego escribimos cada bloque en el disco antes de obtener el siguiente
bloque. De esta forma, el programa puede leer archivos de cualquier tamaño sin
utilizar toda la memoria disponible en la computadora.

"""

import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
man_a = open('portada.jpg','wb')
man_a.write(img)
man_a.close()
