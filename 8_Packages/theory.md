# A package is a directory containing multiple modules, usually with an __init__.py file
# my_package/
# │
# ├── __init__.py
# ├── math_utils.py
# └── string_utils.py

the individual modules like math.py contains the actual functions like def add(a,b)

the init file simply imports it

init.py:-
from math import add 

Then go to python file in which you wish to import the package

index.py
import package as __
import numpy as np

and directly call functions 
np.array() 

array function maybe in some module of numpy package but its already imported in init.py so thats why this works

there are some functions which are not exposed/imported in init.py so have to call them from submodule



eg: np.lin.function()

lin is a module inside numpy package so access the module first using np.lin
then call function 