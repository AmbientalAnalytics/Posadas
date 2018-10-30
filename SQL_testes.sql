select LugarOrigen, Barrio, CalleOrigen, EsquinaOrigen, LugarDestino, BarrioDestino, CalleDestino, EsquinaDestino, Loc_viaje from viajes limit 1;


with nombresMerge as (select LugarOrigen as nombre, Barrio as nombre, CalleOrigen as nombre, EsquinaOrigen as nombre, LugarDestino as nombre, BarrioDestino as nombre, CalleDestino as nombre, EsquinaDestino as nombre, Loc_viaje as nombre from viajes)
select distinct(nombre) from nombresMerge;

with nombresMerge as (select v1.LugarOrigen as nombre from viajes v1 union select v2.Barrio as nombre from viajes v2 union select v3.CalleOrigen as nombre from viajes v3 union select v4.EsquinaOrigen as nombre from viajes v4 union select v5.LugarDestino as nombre from viajes v5 union select v6.BarrioDestino as nombre  from viajes v6 union select v7.CalleDestino as nombre  from viajes v7 union  select v8.EsquinaDestino as nombre from viajes v8 union select v9.Loc_viaje from viajes v9)
select distinct(nombre) from nombresMerge;
