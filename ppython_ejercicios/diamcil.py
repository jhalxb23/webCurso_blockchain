#determinar diametro de recipiente cilindrico
import math  #importamos libreria math

pi=3.1416
h=float(input("ingrese la altura del recipiente: "))
V=float(input("Ingrese el volumen en metros: "))
V=V*0.001

radio= math.sqrt(V/(pi*h)) 

diametro= 2*radio

print("El diametro es: ", diametro)