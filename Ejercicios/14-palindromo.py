"""
  Escribe una función que reciba un texto y retorne verdadero o
  falso (Boolean) según sean o no palíndromos.
  Un Palíndromo es una palabra o expresión que es igual si se lee
  de izquierda a derecha que de derecha a izquierda.
  NO se tienen en cuenta los espacios, signos de puntuación y tildes.
  Ejemplo: Ana lleva al oso la avellana. 
"""

def palindromo(cadena="")->bool:
    new_cadena= cadena.lower().replace(" ","")
    return new_cadena == new_cadena[::-1]

#print(string.punctuation,string.ascii_letters)
print(palindromo("Ana lleva al oso la avellana"))
print(palindromo("Miklos"))
print(palindromo("Ada"))