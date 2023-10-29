#
#  Crea una función que reciba dos cadenas como parámetro (str1, str2)
#  e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO
#   estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO
#    estén presentes en str1.
# 

def unique_strs(str1, str2):
    st1 = set()
    st2 = set()
    
    for item in str1:
       st1.add(item)

    for item in str2:
        st2.add(item)

    out1 = str(st1.difference(st2))
    out2 = str(st2.difference(st1))

    print(out1)
    print(out2)

unique_strs("Ana","Juana")