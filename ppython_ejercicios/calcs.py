#ejercicio 14

n=int(input("Ingrese valores: "))
num=int(input("Tipo de calculo: "))
V=int(input("Ingrese V: "))


funcion={
    1:n*V,
    2: n**V,
    3: n/V
}

VAL = funcion.get(num,0)

print("\nSALIDA: ")
print(VAL)