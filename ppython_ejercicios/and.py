#permitir ingresos a chico 
#and operator


Edad=int(input(" Ingrese su edad: "))
Altura=float(input(" Ingrese su estatura: "))
peso=int(input("Escriba el peso del niño en kg"))

if Edad>14 and Altura>=1.60 and peso<50:
    print("Usted  puede ingresar")
    
else:
    print("Usted no puede ingresar")
    