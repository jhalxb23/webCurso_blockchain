import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('ventas_anuales.csv')

#print(df.head(10))  #muestra los diez primeros registros
#print(df.describe()) #da un resumen estadistico de los datos.

'''df_electronica=df[df['Categoría']=='Electrónica']
print(df_electronica)'''    #imprimi el filtro de los datos por el filtro electronica

#print(df[['Mes', 'Ventas Totales', 'Ganancia']])  #imprime vaentas  y ganancias filtradas por mes, 

'''df['Porcentaje Ganancia'] =(df['Ganancia']/df['Ventas Totales'])*100
print(df.head(4))''' #crea y calcula el porcentaje de ganacia 


#df['Porcentaje Ganancia'] =(df['Ganancia']/df['Ventas Totales'])*100
#print(df.head(4))

#ventas_por_categoria=df.groupby("Mes")["Ganancia"].mean()
#print(ventas_por_categoria)

#top_productos=df.sort_values(by="Ventas Totales", ascending=False).head(5)
#print(top_productos)

'''ventas_por_categoria.plot(kind="bar")
plt.title("Ventas Totales por Categoria")
plt.xlabel("Categoría")
plt.ylabel("Ventas Totales")
# Guardar el gráfico
plt.savefig("ventas_por_categoria.png", dpi=300, bbox_inches="tight") #guardar el grafico en formato png
plt.show()'''

#df.to_excel("Ventas_anuales_actualizado.xlsx", index=False)

