import pandas as pd


df= pd.read_csv('ejemplo_pandas.csv') 

#print(df.to_string()) #imprime los valores del csv

#print(df[["Nombre", "Calificación"]]) #imprime solo los datos de las columnas nombre y calificacion

#print(df[df["Edad"]> 20]) #filtra las edades mayores a 20

#print(df[df["Calificación"]>= 90])  #imprime calificaciones mayores o iguales a 90


df['Calificación x 2']=df['Calificación']*2 #crea nueva columna, con el nombre x2 y multiplicada por2
#print(df)

df_sorted=df.sort_values(by='Calificación', ascending=False) #orderna de manera descendente x calificacion
print(df_sorted)

print("el promedio es: ", df['Calificación'].mean())
print("el mediana es: ", df['Calificación'].median())
print("el suma es: ", df['Calificación'].sum())

df.to_excel("ejemplo_pandas.xlsx", index=False)