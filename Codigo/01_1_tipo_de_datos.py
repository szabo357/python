# Estos son los diferentes tipos de datos en Python.
print(type("Esta es una cadena de texto!"))             # str        = cadena de texto

print(type(7))                                          # int        = numero entero
print(type(1.6))                                        # float      = numero decimal
print(type(1j))                                         # complex    = numero complejo
print(type(range(6)))                                   # range      = rango

print(type(["apple", "banana", "cherry"]))              # list       = lista
print(type(("apple", "banana", "cherry")))              # tuple      = tupla
print(type({"name" : "John", "age" : 36}))              # dict       = diccionario
print(type({"apple", "banana", "cherry"}))              # set        = conjunto
print(type(frozenset({"apple", "banana", "cherry"})))   # frozenset  = conjunto congelado

print(type(True))                                       # bool       = booleano

print(type(b"Hello"))                                   # bytes      = bytes
print(type(bytearray(5)))                               # bytearray  = arreglo de bytes
print(type(memoryview(bytes(5))))                       # memoryview = vista de memoria
print(type(None))                                       # NoneType   = sin Tipo