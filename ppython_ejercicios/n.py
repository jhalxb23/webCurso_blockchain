# Determinar el estado del estudiante (Aprobado/Reprobado) basado en n notas

# Solicitar la cantidad de notas
n = int(input("¿Cuántas notas desea ingresar? "))

# Inicializar una lista para guardar las notas
notas = []

# Pedir las notas y almacenarlas en la lista
for i in range(n):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

# Calcular el promedio
DefiNota = sum(notas) / n

# Determinar el estado
if DefiNota > 5:
    print("Aprobado")
else:
    print("Reprobado")
