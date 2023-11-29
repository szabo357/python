import socket
import time

SERVIDOR = 'data.pr4e.org'
PUERTO = 80
misocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
misocket.connect((SERVIDOR, PUERTO))
misocket.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
contador = 0
imagen = b""

while True:
    datos = misocket.recv(5120)
    if len(datos) < 1: break
    time.sleep(0.25)
    contador= contador + len(datos)
    print(len(datos), contador)
    imagen = imagen + datos

misocket.close()

pos = imagen.find(b"\r\n\r\n")
print('Header length: ', pos)
print(imagen[:pos].decode())

#Ignorar la cabecera y guardar los datos
imagen = imagen[pos+4:]

fhand = open("cosa.jpg","wb")
fhand.write(imagen)
fhand.close()