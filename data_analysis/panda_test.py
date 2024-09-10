import pandas as pd
from pandas import Series, DataFrame

# Series
obj = pd.Series([4, 7, -5, 3])
print (obj)
print (obj.array)
print (obj.index)

print (obj[obj > 2])
sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
obj3 = pd.Series(sdata)

print (obj3)
