"""
  Crea una función que calcule el número de la columna de una hoja de Excel
  teniendo en cuenta su nombre.
  - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
  - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""

def columna_excel(nombre_columna: str)->int:
     numero_columna = 0
     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     
     for letra in nombre_columna.upper():
        numero_columna = (numero_columna * len(alphabet)) + (alphabet.index(letra) + 1)

     return numero_columna  
       # print(f"Letra: {alphabet[i]} indice: {i+1} ")

    
print(columna_excel("AZZ"))
print(columna_excel("A"))
print(columna_excel("AA"))
print(columna_excel("AB"))
print(columna_excel("BA"))
print(columna_excel("CA"))
