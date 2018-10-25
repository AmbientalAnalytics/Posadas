install.packages("RSQLite")
library("RSQLite")
# connect to the sqlite file
con = dbConnect(RSQLite::SQLite(), dbname="../sqlalchemy_example.db")
# get a list of all tables
alltables = dbListTables(con)
# get the populationtable as a data.frame
p1 = dbGetQuery( con,'select * from hogar limit 3' )

barrios = dbGetQuery( con,'select distinct(BarrioDestino) from viajes' )
calles = dbGetQuery( con,'select count(CalleDestino), CalleDestino from viajes group by CalleDestino' )
dim(calles)
head(calles)