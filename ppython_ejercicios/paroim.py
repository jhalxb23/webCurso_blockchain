# -*- coding: utf-8 -*-
#Decoración: Nombre del Algoritmo
print("-------------------------------------------------------")
print("Ejercicio15: PAR O IMPAR.")
print("-------------------------------------------------------")
#Entradas
NUM = int( input("Ingrese número:" ))
#Proceso
#Usando un diccionario
par_Impar = {
1 : 'Impar',
3 : 'Impar',
5 : 'Impar',
7 : 'Impar',
9 : 'Impar',
2 : 'Par',
4 : 'Par',
6 : 'Par',
8 : 'Par',
10 : 'Par'
}

print("\nSALIDA: ")
print("-------------------------------------------------------")
print(par_Impar.get(NUM, "Numero fuera de Rango"))