# Escribiendo en un archivo de texto. 
# si el programa se ejecuta nuevamente el contenido del archivo se sobreescribe
# debe buscarse la forma de agregar texto y conservar el que habia previamente.
# 'w' como segundo argumento de open. sobrescribe la informacion contenida en el archivo.
#escribe = open("salida.txt",'w')
# 'a'como segundo argumento de open. agrega nueva informacion al archivo.
import os
saved_cwd=os.getcwd()
LIT = str(saved_cwd+"\Codigo\manejo_de_archivos")
os.chdir(LIT)

with open("salida.txt","a") as escribe:    
    escribe.write("Este es nuevo contenido para el archivo\n")
    escribe.write("Esta es una nueva linea de texto en el archivo\n")
    escribe.write("sigue escribiendo en el archivo.\n")
os.chdir(saved_cwd)