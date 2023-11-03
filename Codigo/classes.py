#### Classes ####
import random as rd

class Person:
    def __init__(self,name,surname):
        self.__name    = name
        self.__surname = surname            
        self.fullname= f"{name} {surname}"

    def __str__(self) -> str:
        return f"{self.__name} {self.__surname} acaba de ser creado"
        

    def walk(self):
        print(f"{self.__name} {self.__surname} está caminando")

    def get_fullname(self):
        return f"{self.__name} {self.__surname}"

    # Example of a function developed by Guido Van Rossum.
    # taken from the random module. random.randrange().
    #def randrange(self, start, stop=None, step=_ONE):
        """Choose a random item from range(stop) or range(start, stop[, step]).

        Roughly equivalent to ``choice(range(start, stop, step))`` but
        supports arbitrarily large ranges and is optimized for common cases.

        """

        # This code is a bit messy to make it fast for the
        # common case while still doing adequate error checking.
    """
        try:
            istart = _index(start)
        except TypeError:
            istart = int(start)
            if istart != start:
                _warn('randrange() will raise TypeError in the future',
                      DeprecationWarning, 2)
                raise ValueError("non-integer arg 1 for randrange()")
            _warn('non-integer arguments to randrange() have been deprecated '
                  'since Python 3.10 and will be removed in a subsequent '
                  'version',
                  DeprecationWarning, 2)
        if stop is None:
            # We don't check for "step != 1" because it hasn't been
            # type checked and converted to an integer yet.
            if step is not _ONE:
                raise TypeError('Missing a non-None stop argument')
            if istart > 0:
                return self._randbelow(istart)
            raise ValueError("empty range for randrange()")

        # stop argument supplied.
        try:
            istop = _index(stop)
        except TypeError:
            istop = int(stop)
            if istop != stop:
                _warn('randrange() will raise TypeError in the future',
                      DeprecationWarning, 2)
                raise ValueError("non-integer stop for randrange()")
            _warn('non-integer arguments to randrange() have been deprecated '
                  'since Python 3.10 and will be removed in a subsequent '
                  'version',
                  DeprecationWarning, 2)
        width = istop - istart
        try:
            istep = _index(step)
        except TypeError:
            istep = int(step)
            if istep != step:
                _warn('randrange() will raise TypeError in the future',
                      DeprecationWarning, 2)
                raise ValueError("non-integer step for randrange()")
            _warn('non-integer arguments to randrange() have been deprecated '
                  'since Python 3.10 and will be removed in a subsequent '
                  'version',
                  DeprecationWarning, 2)
        # Fast path.
        if istep == 1:
            if width > 0:
                return istart + self._randbelow(width)
            raise ValueError("empty range for randrange() (%d, %d, %d)" % (istart, istop, width))

        # Non-unit step argument supplied.
        if istep > 0:
            n = (width + istep - 1) // istep
        elif istep < 0:
            n = (width + istep + 1) // istep
        else:
            raise ValueError("zero step for randrange()")
        if n <= 0:
            raise ValueError("empty range for randrange()")
        return istart + istep * self._randbelow(n)
        """
# Main Class that will be inherited by Car and Motorcycle classes.
class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    
    def start(self):
        self.started = True
        print("Started, let's ride!")
    
    def stop(self):
        self.speed = 0
        print("Halt!")
    
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooom!")
        else:
            print("You need to start me first")


class Car(Vehicle):
    trunk_open = False
    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False


class Motorcycle(Vehicle):
    def __init__(self,started = False, speed = 0, center_stand_out = False): #overrides the vehicule constructor.
        self.center_stand_out = center_stand_out
        super().__init__(self,started = False, speed = 0) # calls the vehicule constructor with super()
    def __len__(self):
        return 60
    def start(self):
        print("Sorry, out of fuel!")    


class Usuario:
    def __init__(self,name:str="",**kwargs):
        self.name = name
        self.datapack = kwargs

    def introduce_yourself(self):
        return f"Hello my name is {self.name}"
    pass   


# Below of this line instantiation of the classes will be done.
# will be creating objects of our recently created classes.
usr = Usuario()
my_person = Person("Jose","Avila")
print(my_person)
print(my_person.get_fullname())
print(my_person.walk())
my_person.walk()

other_person = Person("Miklos","Szabo")
print(other_person)
other_person.walk()
other_person.fullname = "Roberto Rivas"
other_person.walk()
other_person.__name="Mike" # no es modificable desde afuera
other_person.__surname="Avila"#no es modificable desde afuera
print(other_person.fullname)#fullname es propiedad publica
print(other_person.get_fullname())

#Adding multiple instances of Car class.
car= Car()
c2 = Car(True)
c3 = Car(True,50)
c4 = Car(started=True, speed=100)
m1 = Motorcycle(True,10,True)

m1.increase_speed(30)
print(f"Motorcycle speed is {m1.speed}")

#print(f"Length of Motorcycle is {len(m1)}") #TypeError: object of type 'Motorcycle' has no len()
print(f"Length of Motorcycle is {len(m1)}")

car.increase_speed(10)
car.start()
car.increase_speed(40)
car.stop()

print(f"Car  speed {car.speed}")
print(f"car2 speed {c2.speed}")
print(f"car3 speed {c3.speed}")
print(f"car4 speed {c4.speed}")

print(dir(object)) # dir() Returns a list of the specified object's properties and methods
print(dir(c2))
print(c2.speed)
print(delattr(c2,"speed")) # delattr() deletes an attribute from an object.
print(dir(c2))
print(setattr(c2,"speed",50)) #setattr() sets an attribute to an object.
print(dir(c2))
print(c2.speed)
print(type(object)) # type is <class 'type'>
print(type(Car))    # type is <class 'type'> Car Class.
print(type(c2))     # type is <class '__main__.Car'> Car class instance.
print(type(rd))     # type is <class 'module'>
print(type(dir))    # type is <class 'builtin_function_or_method'>
print(type(type))   #<class 'type'>
print(dir(rd)) # prints random class object structure.
print(hasattr(c2,"speed")) # returns True if attribute exist.
#class
#delattr
#dict  # Present in Car class, not in object.
#dir
#doc
#eq
#format
#ge
#getattribute
#getstate
#gt
#hash
#init
#init_subclass
#le
#lt
#module    "Is present in Car class, not in object."
#ne
#new
#reduce
#reduce_ex
#repr
#setattr
#sizeof
#str
#subclasshook
#weakref     "Is present in Car class, not in object"
