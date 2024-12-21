#determinar año bisiesto

anho=int(input("Ingrese el año: "))

if (anho % 4 == 0 and  anho % 100 !=0) or (anho%400==0):
    print("El año es bisiesto")

else:
    print("el año no es bisiesto")