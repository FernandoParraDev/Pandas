import pandas as pd
import numpy as np

# Crear un data frame de ejemplo
data = {
    'Nombre': ['Juan', 'María', 'Pedro'],
    'Edad': [25, 30, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']
}

df = pd.DataFrame(data)

# Escribir el data frame en un archivo CSV
df.to_csv('ejemplo.csv', index=False)  # index=False para evitar escribir el índice de fila en el archivo
print(df)

#Más ejemplos

data2 = {
    'Nombre': ['Juan', 'María', 'Pedro'],
    'Edad': [np.nan, 30, 35],
    'Ciudad': ['Madrid', 'N/A', 'Sevilla']
}
df2 = pd.DataFrame(data2)
print("\n"*2)
print(df2)

print(df2.info()) #Con esto hacemos un summary de df2

## Estadisticas

#Aqui eliminamos la fila que tenga el na numerico
ejemplo=pd.DataFrame(df2)
ejemplo.dropna(how="any",inplace=True)
print(ejemplo)

print("\n"*2)


#Un summary más estadistico
#print(df2.describe()) 

#Corregimos el dato faltante
ejemplo1=pd.DataFrame(df2)
ejemplo1=ejemplo1.replace(np.nan,"0") 


#Eliminamos la fila que no tenga dato en ciudad

ejemplo3=df2[df2["Ciudad"]!="N/A"]
print("\n"*2)
print(ejemplo3)

#Convertimos a tipo int 
ejemplo1["Edad"]=ejemplo1.Edad.astype("int")

print(ejemplo1.describe())

#Estadisticas individuales
print("\n"*2)
print("Promedio",ejemplo1['Edad'].mean())