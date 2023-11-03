### exceptions.

numberOne = 5
numberTwo = 1
#numberTwo = "23"

# Excepción base: try except

try:
    print(numberOne + numberTwo)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
except:
    print("Se ha producido un error")

# try except else

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else: # Opcional
     # se ejecuta si no se produce una excepción.
    print("La ejecución continua correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")    