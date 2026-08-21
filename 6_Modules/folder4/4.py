
#type-4 python file in one folder and module in another both are sibling folders 


#dont use run button here instead go to 6_modules folder in path and use this command
# PS C:\Users\Umar\OneDrive\Desktop\5_AI\1_Python\6_modules> python -m folder4.4

# now it can find the path to folder fns because 6_modules contain fns directly 
from fns import web as w

print(w.l)