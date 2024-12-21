#determinar sueldo empledado

sue=float(input("Ingrese el sueldo del empleado: "))
nuevosue= sue+(sue*0.15)


if sue < 1000:
    print("El sueldo es: ",nuevosue)
else:
    print(sue)