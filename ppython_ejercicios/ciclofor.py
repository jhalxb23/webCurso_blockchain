#uso del for

#for x in range(101):
 #   print(x)

#for x in range(1,100,2):
 #   print(x)
# -------------------------------   
    
#suma=0
#for f in range(10):
 #       valor=int(input("Ingrese un valor: "))
  #      suma = suma+valor
   #5
   # print("la suma es: ", suma)
        
#-----------------------------

#aprobados =0
#reprobrados =0

#for i in range (10):
 #   nota = int(input("Ingrese la nota: "))
    
  #  if nota >=7:
    #    aprobados=aprobados+1
   # else:
     #   reprobrados=reprobrados+1
        
    #print("Cantidad de alumnos aprobrados: ", aprobados)
    
    #print("cantidad de alumnos reprobrados: ", reprobrados)
#-------------------------------------------
mul3=0
mul5=0

    
for f in range(10):
        valor=int(input("Ingrese un valor: "))
        if valor%3==0:
            mul3=mul3+1
        if valor%5==0:
            mul5=mul5+1
print("Cantidad de valores ingresados multiplos de 3: ", mul3)
print("Cantidad de valores ingresados multiplos de 5:  ", mul5)
    
        