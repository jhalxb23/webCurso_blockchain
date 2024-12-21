#determinar estado del estudiante aprobado/no aprobado

nota=float(input("Ingrese nota del alumno"))
nota2=float(input("Ingrese nota del alumno"))
nota3=float(input("Ingrese nota del alumno"))
nota4=float(input("Ingrese nota del alumno"))
DefiNota=(nota+nota2+nota3+nota4)/4


if DefiNota>5:
    print("Aprobado")

else:
    print("Reprobado")