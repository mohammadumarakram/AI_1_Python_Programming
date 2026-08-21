#install:- pip install package name
#upgrade:- pip install --upgrade requests
#uninstall :-pip uninstall requests

#show all packages :- pip list


#like in github a project will contain a requiremnts file of all packages 
#install multiple packages create a file inside the directory requirements.txt then run
# pip install -r requirements.txt


#using a package


import pandas as pd

data = {
    "name": ["Ali", "Umar", "John"],
    "age": [20, 25, 30]
}

df = pd.DataFrame(data)

print(df)