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

