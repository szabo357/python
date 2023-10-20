'''El ordenamiento por inserción es una manera muy natural de ordenar para un serhumano y puede usarse 
 fácilmente para ordenar un mazo de cartas numeradas en forma arbitraria. Requiere 
 O(n^2) operaciones para ordenar una lista de "n" elementos.

 Inicialmente, se tiene un solo elemento que, obviamente, es un conjunto ordenado. Después, cuando hay k 
 elementos ordenados de menor a mayor se toma el elemento k+1 y se compara con todos los elementos 
 ya ordenados, deteniéndose cuando se encuentra un elemento menor 
 (todos los elementos mayores han sido desplazados una posición a la derecha) o 
 cuando ya no se encuentran elementos (todos los elementos fueron desplazados y este es el más pequeño). 
 En este punto se inserta el elemento k+1 debiendo desplazarse los demás elementos.
 '''
