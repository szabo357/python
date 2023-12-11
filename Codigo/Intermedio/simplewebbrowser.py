#
# PEP-3333 WSGI Python Web Server Gateway Interface 
# https://peps.python.org/pep-3333/
#
import socket

misocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
misocket.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
misocket.send(cmd)


while True:
    datos = misocket.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end='')

misocket.close()


"""
server response

HTTP/1.1 200 OK
Date: Wed, 29 Nov 2023 17:54:04 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
"""


