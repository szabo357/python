'''
  Escribe un programa donde al ingresar un número natural "n" calcule el factorial del número y lo imprima en pantalla.
  - En Matemáticas la función factorial se representa con un signo de exclamación “!” detrás de un número. 
  - Esta exclamación quiere decir que hay que multiplicar todos los números enteros positivos que hay entre ese número y el 1.
  - por ejemplo el factorial de 4 se calcula : 1x2x3x4 = 24
  - 1 factorial es, lógicamente, 1, ya que multiplicamos 1 x 1
  - por convención 0 factorial es, 1.
'''
def factorial(numero):
        
    if numero == 0 or numero == 1 :
        return 1
    else :
        i = 1
        facto = 1
        while i <= numero:
            facto = facto* i
            i+=1

        return facto

print(factorial(5))
