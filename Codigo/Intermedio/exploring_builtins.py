# references
# https://www.w3schools.com/python/python_ref_functions.asp
# https://docs.python.org/3/library/functions.html
# 
import _03lambdas

def test():
    """
    This is a short description of the functionality in this method
    it doesn't do anything.
    >>> test()

    """
    pass

funclist:[str] = ['__bool__', 
                  '__class__', 
                  '__delattr__', 
                  '__dir__', 
                  '__doc__', 
                  '__eq__', 
                  '__format__', 
                  '__ge__', 
                  '__getattribute__', 
                  '__getstate__', 
                  '__gt__', 
                  '__hash__', 
                  '__init__', 
                  '__init_subclass__', 
                  '__le__', 
                  '__lt__', 
                  '__ne__', 
                  '__new__', 
                  '__reduce__', 
                  '__reduce_ex__', 
                  '__repr__', 
                  '__setattr__', 
                  '__sizeof__', 
                  '__str__', 
                  '__subclasshook__']


class Animal:
    pass

classlist:[str] = ['__class__', 
                   '__delattr__', 
                   '__dict__', 
                   '__dir__', 
                   '__doc__', 
                   '__eq__', 
                   '__format__', 
                   '__ge__', 
                   '__getattribute__', 
                   '__getstate__', 
                   '__gt__', 
                   '__hash__', 
                   '__init__', 
                   '__init_subclass__', 
                   '__le__', 
                   '__lt__', 
                   '__module__', 
                   '__ne__', 
                   '__new__', 
                   '__reduce__', 
                   '__reduce_ex__', 
                   '__repr__', 
                   '__setattr__', 
                   '__sizeof__', 
                   '__str__', 
                   '__subclasshook__', 
                   '__weakref__']

modulelist:[str] = ['__builtins__', 
                    '__cached__', 
                    '__doc__', 
                    '__file__', 
                    '__loader__', 
                    '__name__', 
                    '__package__', 
                    '__spec__', 
                    'multiply_values', 
                    'sum_three_values', 
                    'sum_two_values']

#print(dir(test()))
#print(test.__doc__)

#print(dir(Animal()))
print(dir(_03lambdas))