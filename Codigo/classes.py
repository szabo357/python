#### Classes ####

class Myclass:
    pass


print(Myclass)
print(Myclass())

class Person:
    def __init__(self,name,surname) -> None:
        self.__name    = name
        self.__surname = surname            
        self.fullname= f"{name} {surname}"

    def walk(self):
        print(f"{self.__name} {self.__surname} está caminando")

    def get_fullname(self):
        return f"{self.__name} {self.__surname}"


my_person = Person("Jose","Avila")
print(my_person.get_fullname())
print(my_person.walk())
my_person.walk()

other_person = Person("Miklos","Szabo")
other_person.walk()
other_person.fullname = "Roberto Rivas"
other_person.walk()
other_person.__name="Mike" # no es modificable desde afuera
other_person.__surname="Avila"#no es modificable desde afuera
print(other_person.fullname)#fullname es propiedad publica
print(other_person.get_fullname())