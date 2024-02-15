import pandas as pd
import numpy as np

#https://www.youtube.com/watch?v=aVOIC4g75JA&list=PLgHCrivozIb0ULMKfJVV-rFdRG2OeEgfq&index=2

datos=pd.read_csv("ATP.csv")
"""
print(datos.info())
print(datos.head())

"""
nuevo=pd.DataFrame(datos)
nuevo=nuevo.replace(np.nan,"0") #reemplazamos nan por "0"

#Estadisticas para revisar solo los numeros
print(nuevo.describe(include=[np.number]))

nuevo=nuevo.replace("N/A","0")
nuevo=nuevo.replace("NR","0")

