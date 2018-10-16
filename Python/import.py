import pandas as pd

# Hogar
t = pd.read_csv("./OriginalDat/POS_Hogar.csv")
t = t.replace(['NULL        '], [None]) # removendo texto NULL por NaN
t.head()

t.tail()
t.head().to_dict(orient='records')
t.head().isnull()

tDict = t[0:1].to_dict(orient='records')
tDict = t.to_dict(orient='records')
engine.execute(hogar.insert(), tDict)

# Miembros
t = pd.read_csv("./OriginalDat/POS_Miembros.csv")
#t = t.replace(['NULL        '], [None]) # removendo texto NULL por NaN
t.head()
t.tail()
t.head().to_dict(orient='records')
t.head().isnull()

tDict = t.to_dict(orient='records')
engine.execute(miembros.insert(), tDict)

# Viajes
t = pd.read_csv("./OriginalDat/POS_Viajes.csv")
t = t.replace(["NULL                                                                                                                                                                                                                                                           "], [None]) # removendo texto NULL por NaN
t = t.replace(["NA"], [None]) # removendo texto NULL por NaN

t.head()
t["NivelEstudioCursando"].head()
t["Barrio"].tail()
t.tail()

t.head().isnull()

tDict = t.to_dict(orient='records')
engine.execute(viajes.insert(), tDict)

# Medios
t = pd.read_csv("./OriginalDat/POS_Medios.csv")
t = t.replace(["0                                                                                                                                                                                                                                                              "], [0]) # removendo texto NULL por NaN
t.head()
t.tail()

t.head().isnull()

tDict = t.to_dict(orient='records')
engine.execute(medios.insert(), tDict)
