import pandas as pd

data = {
    
    "kilometros": [20,10,7],
    "metros":[100,40,200],
    "centimetros":[15,60,32]
}

myvar=pd.DataFrame(data, index=["a","b","c"])
print(myvar)