import pandas as pd

t = pd.read_csv("./OriginalDat/POS_Hogar.csv")
t = t.replace(['NULL        '], [None]) # removendo texto NULL por NaN
t.head()

t.tail()
t.head().to_dict(orient='records')
t.head().isnull()

tDict = t[0:1].to_dict(orient='records')
engine.execute(hogar.insert(), tDict)
