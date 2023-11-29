import urllib.request

man_a = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for linea in man_a:
    print(linea.decode().strip())

"""
Output: 
But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already sick and pale with grief
"""