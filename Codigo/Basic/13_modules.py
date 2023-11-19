
import my_module as md

md.printValue("Test")
print(md.sumValue(1,2,3))

from my_module import printValue,sumValue
printValue("Testing 1")
sumValue(5,4,1)

import math 

print(math.pi)

from math import pi, tau

print(pi)
print(tau)
print(math.pow(2,8))