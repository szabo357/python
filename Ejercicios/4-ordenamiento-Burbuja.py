'''4-Implementa el algoritmo de ordenamiento de Burbuja imprime en consola
 el resultado del ordenamiento. El algoritmo de ordenamiento lo que hace es ordenar
 una lista de menor a Mayor. y lo hace comparando los primeros 2 valores de la lista,
 si el primer valor es mayor que el segundo valor entonces se intercambian los valores de la lista.
 se repite la comparacion hasta llegar al final de la lista.
  '''


def bubblesort(arr):
    
    n= len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [24,5,10,60,40,1]

print(bubblesort(arr))
