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

