"""
  Escribe una función que reciba un texto y retorne verdadero o
  falso (Boolean) según sean o no palíndromos.
  Un Palíndromo es una palabra o expresión que es igual si se lee
  de izquierda a derecha que de derecha a izquierda.
  NO se tienen en cuenta los espacios, signos de puntuación y tildes.
  Ejemplo: Ana lleva al oso la avellana. 
"""
import string
def palindromo(cadena="")->bool:

    characters= string.punctuation
    characters +=string.digits
    cadena.lower().replace(characters,"")

    return cadena == cadena[::-1]

print(palindromo("Ana lleva al oso la avellana"))