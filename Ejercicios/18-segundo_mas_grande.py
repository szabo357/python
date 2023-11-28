# Dado un listado de números, encuentra el SEGUNDO más grande.
from random import randint

lista = [ randint(0,200) for _ in range(0,100)]
print(lista)

def segundo_mas_grande(lista:list):
    lista1 = []
    lista1 = lista.copy()
    lista1.sort()

    return lista1[-2], lista1

smg , l = segundo_mas_grande(lista)

print(smg,l)