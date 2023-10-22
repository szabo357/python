"""
  Crea una función que calcule el número de la columna de una hoja de Excel
  teniendo en cuenta su nombre.
  - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
  - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""

def calculate_excel_column(column_name: str)->int:
     column_number = 0
     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
     
     for letter in column_name.upper():
        column_number = (column_number * len(alphabet)) + (alphabet.index(letter) + 1)

     return column_number  
      
      
print(calculate_excel_column("AZZ"))
print(calculate_excel_column("A"))
print(calculate_excel_column("AA"))
print(calculate_excel_column("AB"))
print(calculate_excel_column("BA"))
print(calculate_excel_column("CA"))