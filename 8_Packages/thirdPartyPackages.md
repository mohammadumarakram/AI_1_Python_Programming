#Built-in modules and standard library packages live directly inside your system's Python installation directory on your hard drive, organized in specific folders like lib/ and site-packages/.
#1. Where Are They Stored?
# Python modules are divided into three physical categories depending on how they are written:

# Standard Library Modules (.py files): Written in pure Python (like os.py, random.py, http/). Stored in the Lib/ folder inside your Python installation directory.

# Third-Party Packages (via pip): Installed libraries (like numpy, pandas, requests). Stored inside the Lib/site-packages/ directory.

# Built-in C-Modules: Built directly into the Python interpreter binary itself (like sys, math, time). They do not exist as separate .py files on your disk because they are compiled C code.

#pip (short for "Pip Installs Packages") is Python’s official package manager. It connects to the PyPI (Python Package Index) repository on the internet, downloads third-party packages, and extracts them into your system's site-packages/ folder.

#can check where a package is stored by pip show packagename
# Location: C:\Python312\Lib\site-packages


#----------------------------------------------------------
How Python Searches for Modules/packages Step-by-Step
When you run import my_module, Python checks four locations in exact order until it finds a match:

The Current Working Directory: Python always checks the folder where your script is currently running first.

PYTHONPATH (Environment Variable): Any extra directory paths you manually added to your computer's system environment settings.

Standard Library Directory (Lib/): Built-in pure Python modules like random.py, os.py, datetime.py, or json/.

Third-Party Directory (site-packages/): The folder where pip installs packages like requests, numpy, or pandas.

Note: Built-in C-modules (like sys and math) are compiled directly into the Python interpreter itself, so Python accesses them instantly in memory before checking sys.path.


thats why dont name local python files as math.py because python will search it first 
