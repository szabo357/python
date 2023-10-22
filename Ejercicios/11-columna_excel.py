"""
  Crea una función que calcule el número de la columna de una hoja de Excel
  teniendo en cuenta su nombre.
  - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
  - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""

def columna_excel(nombre_columna):
     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     nombre_columna = str(nombre_columna.upper())
     search_list = []

     for i in range(len(alphabet)):
        print(alphabet[i])
     
    

columna_excel("A")
#columna_excel("AA")
