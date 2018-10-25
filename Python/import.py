import pandas as pd
from Python.DatosOrg import engine, meta, hogar, viajes, miembros, medios

# Hogar
t = pd.read_csv("./OriginalDat/POS_Hogar.csv")
# cleaning few features
t = t.replace(['NULL        '], [None]) # removendo texto NULL por NaN
t = t.replace(["NULL                                                                                                                                                                                                                                                           "], [None]) # removendo texto NULL por NaN
t = t.replace(["^ *|(?<= ) | *$]", ""])

t.head()
t.tail()
# converting to dict
tDict = t.to_dict(orient='records')
# importing to sqlite
engine.execute(hogar.insert(), tDict)

# Miembros
t = pd.read_csv("./OriginalDat/POS_Miembros.csv")
# cleaning few features
t = t.replace(['NULL        '], [None]) # removendo texto NULL por NaN
t = t.replace(["NULL                                                                                                                                                                                                                                                           "], [None]) # removendo texto NULL por NaN
t = t.replace(["^ *|(?<= ) | *$]", ""])

t.head()
t.tail()

# convert to dict
tDict = t.to_dict(orient='records')
# insert sqlite
engine.execute(miembros.insert(), tDict)

# Viajes
t = pd.read_csv("./OriginalDat/POS_Viajes.csv")
# cleaning few features
t = t.replace(['NULL        '], [None]) # removendo texto NULL por NaN
t = t.replace(["NULL                                                                                                                                                                                                                                                           "], [None]) # removendo texto NULL por NaN
t = t.replace(["^ *|(?<= ) | *$]", ""])

t = t.replace(["NA"], [None]) # removendo texto NULL por NaN

t.head()
t["NivelEstudioCursando"].head()
t["Barrio"].tail()
t.tail()

t.head().isnull()
# converting to dict
tDict = t.to_dict(orient='records')
# insert SQLite
engine.execute(viajes.insert(), tDict)

# Medios
t = pd.read_csv("./OriginalDat/POS_Medios.csv")
# cleaning few features
t = t.replace(['NULL        '], [None]) # removendo texto NULL por NaN
t = t.replace(["NULL                                                                                                                                                                                                                                                           "], [None]) # removendo texto NULL por NaN
t = t.replace(["^ *|(?<= ) | *$]", ""])
t = t.replace(["0                                                                                                                                                                                                                                                              "], [0]) # removendo texto NULL por NaN

t.head()
t.tail()

t.head().isnull()

# conver to dict
tDict = t.to_dict(orient='records')
# insert SQLite
engine.execute(medios.insert(), tDict)
