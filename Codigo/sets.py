# Aprendiendo sobre sets.

my_set = set()
my_other_set = {'item1', 'item2', 'item3', 'item4'}

print( len(my_set) )
print( len(my_other_set) )



#Agregando elementos a un Set. La funcion Add solo permite agregar un elemento a la vez.
my_set.add('Libro')
my_set.add('Libro1')
print(my_set)
my_other_set.add('Libro')

#Update permite agregar varios elementos a la vez. toma una lista de argumentos.
my_other_set.update(['item5','item6','item7'])
print(my_other_set)


#Verificando si un elemento existe en un set
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True

#Remover elementos de un Set
my_other_set.remove('item2') # remover elemento especifico.
print(my_other_set)

#Remover un elemento aleatoriamente
print(my_other_set.pop())

# Borrando el contenido del Set. 
my_other_set.clear()
print(f"El contenido del set es: {my_other_set}")

# Eliminando un Set.
del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined. El set fue eliminado.

#Convirtiendo una lista en Set
# syntax
mi_lista = ['item1', 'item2', 'item3', 'item4', 'item1']
nuevo_set = set(mi_lista) 
print(nuevo_set)

#Convirtiendo un set en una lista
nueva_lista = list(nuevo_set)
print(nueva_lista)

#uniendo Sets. 
# La funcion union sirve para unir 2 sets diferentes. pero devuelve un nuevo set. 
# asi que debe ser almacenado en una nueva variable.
miset1 = {'item1', 'item2', 'item3', 'item4'}
miset2 = {'item5', 'item6', 'item7', 'item8'}
miset3 = miset1.union(miset2)
print( miset3)

# Uniendo Sets. con la funcion update. En este caso los valores de miset2 se agregan a miset1.
miset1.clear()
miset1 = {'item1', 'item2', 'item3', 'item4'}
miset1.update(miset2)
print(miset1)

# Encontrando la intersección de 2 Sets.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st1.intersection(st2)) # Devuelve la interseccion como un nuevo Set {'item3', 'item2'}

# 1 Probando si un Set es Subset de otro Set.  El Subset es parte de un Super Set.
# 2 Probando si un Set es Super Set de otro Set. El Super Set contiene a todo un Subset 
numeros_enteros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_pares = {0, 2, 4, 6, 8, 10}
print(numeros_enteros.issubset(numeros_pares)) # False, Porque numeros_enteros es un super set
print(numeros_enteros.issuperset(numeros_pares)) # True

#Encontrando la diferencia entre 2 sets
print(st1.difference(st2))
print(numeros_enteros.difference(numeros_pares))