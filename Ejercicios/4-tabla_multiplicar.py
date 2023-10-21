"""
  Crea un programa que sea capaz de solicitarte un número y se
  encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
  - Debe visualizarse qué operación se realiza y su resultado.
    Ej: 2 x 1 = 2
        2 x 2 = 4
        2 x 3 = 6
        ... 
 
"""
1
def tabla_multiplicar(numero):
    for i in range(1,11):
        print("%d X %d =  %d"%(numero, i , numero*i ))

num= int(input("Ingrese un Numero: "))
tabla_multiplicar(num)