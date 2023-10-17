import time
def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            if arr[j] < arr[menor]:
                menor = j
        if menor != i:
            arr[menor], arr[i] = (arr[i], arr[menor])
    print(arr)


lista = [25,10,15,14,1,2,5,8]

ordenamiento_seleccion(lista)