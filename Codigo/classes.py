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

class Car:
    def __init__(self, started=False, speed=0):
        self.speed = speed
        self.started = started

    def start(self):
        self.started = True
        print("Car started, let's ride!")

    def increase_speed(self,delta):
        if self.started:
            self.speed+= delta
            print("Vrooooom!")
        else:
            print("You need to start the car first")

    def stop(self):
        self.speed = 0
        print("Halting")
    

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

car= Car()
car.increase_speed(10)
car.start()
car.increase_speed(40)
car.stop()