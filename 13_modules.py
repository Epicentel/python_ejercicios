### Modules ###
 
import my_module
my_module.sumValue(10,5,30)
my_module.printValue("Hola Python")

from my_module import sumValue, printValue
sumValue(2,4,60)
printValue("Que onda")

import math
print(math.pi)
print(math.pow(3,4))

from math import pi as PI_VALUE
print(PI_VALUE)