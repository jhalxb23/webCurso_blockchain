#determinar si la tienda obtuvo ganancias

ingresos = float(input("Escriba el valor de los ingresos del mes: "))
gastos=float(input("Escriba el valor de los gastos del mes:"))

if ingresos ==gastos:
    
    print("la tienda no tuvo ni perdidas ni ganancias")
    
elif ingresos > gastos:
    
    resultado = ingresos-gastos
    print("la tienda obtuvo ganancias durante el mes por el valor de:", resultado)

else:
    resultado = gastos - ingresos
    print("la tienda obtuvo perdidas durante el mes po valor de: ", resultado)