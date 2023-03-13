#------------------------------------------
# IMPORT DES MODULES
#------------------------------------------
import os #Utilisation du module OS (operating system)


#Utilisation du module Pandas
import pandas as pnd
import os

pnd.set_option('display.max_columns',None)

nosPokemons = pnd.read_csv("datas/pokedex.csv", encoding='cp1252')

print(nosPokemons.columns.values)
print(nosPokemons.head(10))