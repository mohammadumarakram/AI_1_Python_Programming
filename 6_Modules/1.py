#A module is simply a Python file (.py) containing code that you want to reuse in another Python file. 

#suppose a file contains some functions you want to call

#M-1 importing whole module
import calculator
# import calculator as c named import now use c.

#to call any function use c.function name() or c.variableName

print(calculator.add(5,10))

#can import anything a function variable name

print(calculator.student)


#to import everything
from math import *
#no need to use math. 
print(sqrt(5))