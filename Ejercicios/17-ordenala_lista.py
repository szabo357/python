 #* Crea una función que ordene y retorne una matriz de números.
 #* - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro
 #*   adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor
 #*   o de mayor a menor.
 #* - No se pueden utilizar funciones propias del lenguaje que lo resuelvan
 #*   automáticamente.

def sortlist(args,ascending=True):
    n= len(args)        
    for i in range(n):
        for j in range(0,n-i-1):
            if ascending:
                if args[j] > args[j + 1] :
                    args[j], args[j + 1] = args[j + 1], args[j]
            else:
                if args[j] < args[j + 1] :
                    args[j], args[j + 1] = args[j + 1], args[j]
    return args
            


mylist = [20,4,10,5,8,15]
print(sortlist(mylist,"Asc"))
print(sortlist(mylist,"Desc"))