# Aprendiendo sobre sets.

my_set = set()
my_other_set = {'items1', 'items2', 'items3', 'items4'}

print( len(my_set) )
print( len(my_other_set) )

my_set.add('Libro')
my_set.add('Lapiz')
my_set.add('Papel')
my_set.add('Borrador')
print(my_set)

my_set.add('Libro')
print(my_set)
print(len(my_set))
