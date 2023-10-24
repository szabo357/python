# En este archivo se agregaran algunos ejercicios relacionados a sets
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Ejercicios Nivel 1
#1 Encuentra la longitus del Set it_companies
print(len(it_companies))
#2 Agrega 'Twitter' a it_companies
it_companies.add("Twitter")
print(it_companies)
#3 Agrega multiples compañias de IT de un solo a it_companies
it_companies.update({"Sap","Accenture","DXC"})
print(it_companies)
#4 Remueve una de las compañias de it_companies
it_companies.remove("Sap")
print(it_companies)
#5 Cual es la diferencia entre las funciones remove y discard
# La funcion remove se utiliza para remover un elemento de un Set. El elemento debe pertenecer 
# obligatoriamente al set, sino un error es mostrado en consola. 
# La funcion discard tambien remueve un elemento de un set con la diferencia de que el elemento
# puede o no pertenecer al set. discard no emitira un mensaje de error si el elemento no existe en
# el set.

# Ejercicios nivel 2
#1 Une A y B
print(A.union(B))
#2 Encuentra A interseccion de B
print(A.intersection(B))
#3 Es A un subset de B
print(A.issubset(B))
#4 Estan desunidos los sets A y B ?
print(A.isdisjoint(B))
#5 Unir A con B y B con A
print(A.union(B))
print(B.union(A))
#6 Cual es la diferencia simetrica entre A y B
print(A.symmetric_difference(B))
#7 Eliminar los sets completamente
del A 
del B

# Ejercicios nivel 3
#1 convertir ages a un set y comparar la longitud de la lista y el set, cual es mas grande?
nuevo_set = set(age)
print(len(age),len(nuevo_set))
#2 Explicar la diferencia entre los siguientes tipos de datos: string, list, tuple and set
# - Un String es una cadena de Caracteres. Basicamente es un arreglo indexado de caracteres unicode.
# - es posible iterar entre cada caracter de un String.
# - Una Lista es una coleccion de tipos de datos distintos ordenados e indexados que es mutable y actualizable.
# - Una tupla es una coleccion de tipos de datos distintos, ordenados e indexados que es inmutable. 
# -Un Set es un conjunto de elementos unicos que no estan ordenados e indexados. una vez
# se ha creado un Set.los elementos no pueden ser modificados. Pero si se pueden hacer operaciones
# de conjuntos con ellos.

#3 cuantas palabras unicas se usaron en la oracion: Soy profesor y me encanta inspirar y enseñar a la gente. 
#  utiliza el metodo split para obtener las palabras unicas.
oracion = "Soy profesor y me encanta inspirar y enseñar a la gente"
palabras_unicas = set(oracion.split()) 
print(len(palabras_unicas))