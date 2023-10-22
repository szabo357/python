"""
  Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
  Podrás configurar generar contraseñas con los siguientes parámetros:
  - Longitud: Entre 8 y 16.
  - Con o sin letras mayúsculas.
  - Con o sin números.
  - Con o sin símbolos.
  (Pudiendo combinar todos estos parámetros entre ellos)
"""
import string 
import random

def generar_pwd(length = 8 , upper = False, adddigits = False, addsymbols = False )->str:
    try:
        password = ""
        characters = []

        characters += string.ascii_lowercase 

        if upper :
            characters += string.ascii_uppercase
        if adddigits:
            characters += string.digits
        if addsymbols:
            characters += string.punctuation

        final_length = 8 if length < 8 else 16 if length > 16 else length  
        i = 0
        while i < final_length:
            password+= random.choice(characters)
            i+=1

        return str(password)
    
    except ValueError:
        print("Error Generating Password")


print(generar_pwd(8,False,True,True))
print(generar_pwd(16,True,True,True))