# Source: https://www.pythoncentral.io/introductory-tutorial-python-sqlalchemy/
# Script to organize data from .sav to sqlite

#loading modules
from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey, create_engine, MetaData

# Creating sqlite database engine
engine = create_engine('sqlite:///sqlalchemy_example.db')
meta = MetaData(bind=engine)

# Creating table
hogar = Table('hogar', meta,
    # Here we define columns for the table hogar
    # Notice that each column is also a normal Python instance attribute.
    Column('FORMULARIO', Integer, primary_key=False),
    Column('Depto', Integer, nullable=False),
    Column('Mun', Integer, nullable=False),
    Column('Fraccion', Integer, nullable=False),
    Column('Radio', Integer, nullable=False),
    Column('Viv', Integer, nullable=False),
    Column('NroHogar', Integer, nullable=False),
    Column('PM', Integer, nullable=False),
    Column('Zon', Integer, nullable=False),
    Column('Tip_viv', String, nullable=True),
    Column('CantidadPersonas', Integer, nullable=False),
    Column('PersonaMayorCuatro', Integer, nullable=False),
    Column('Personas_temporales', Integer, nullable=False),
    Column('CantidadCochera', Integer, nullable=False),
    Column('Hogar_Vehículo', String, nullable=False),
    Column('CantidadVehículos', String, nullable=True),
    Column('Tipo_vehículo_1', String, nullable=True),
    Column('Propiedad_vehículo_1', String, nullable=True),
    Column('MarcaVehículo_1', String, nullable=True),
    Column('Combustible_1', String, nullable=True),
    Column('Gasto_combustible_1', String, nullable=True),
    Column('GastoCochera_1', String, nullable=True),
    Column('GastoPatente_1', String, nullable=True),
    Column('GastoSeguro_1', String, nullable=True),
    Column('GastosTotal_1', String, nullable=True),
    Column('MarcaVehículo_2', String, nullable=True),
    Column('MarcaVehículo_3', String, nullable=True),
    Column('HogarMoto', String, nullable=False),
    Column('CantidadMotos', Integer, nullable=True),
    Column('HogarCiclomotor', String, nullable=False),
    Column('CantidadCiclomotores', String, nullable=True),
    Column('HogarBicicleta', String, nullable=False),
    Column('CantidadBicicletas', Integer, nullable=True),
    Column('Plan_social', String, nullable=False),
    Column('HogarIngresos', String, nullable=True),
    Column('RangoIngresos', String, nullable=True),
    Column('promedio_ingreso', String, nullable=True),
    Column('IngresoT1', String, nullable=True),
    Column('IngresoT2', String, nullable=True),
    Column('HogarGastoTotal', String, nullable=True),
    Column('RangoGastoTotal', String, nullable=True),
    Column('promedio_gastototal', String, nullable=True),
    Column('GastoT1', String, nullable=True),
    Column('GastoT2', String, nullable=True),
    Column('HogarGastosAlimentos', String, nullable=True),
    Column('RangoGastosAlimentos', String, nullable=True),
    Column('promedio_gasto_alimentos', String, nullable=True),
    Column('GastoA1', String, nullable=True),
    Column('HogarGastosTransporte', String, nullable=True),
    Column('RangoGastosTransporte', String, nullable=True),
    Column('Ingresoagregado_pers', String, nullable=True),
    Column('IngresoTotalFinal', String, nullable=True),
    Column('bienestar', String, nullable=False),
    Column('FEX', Float(3), nullable=False)
              )

meta.create_all(engine)
