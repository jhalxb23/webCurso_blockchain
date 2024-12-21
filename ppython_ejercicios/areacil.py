#calcular el area y volumen de un cilindro

#A=(2*pi*r*h)+(2*pi*r**2)

#Volumen = pir2h

pi=3.1416
radio=float(input("Ingrese el radio: "))
h=float(input("ingrese la altura: "))

Vol=pi*radio**2*h
area= (2*pi*radio*h)+(2*pi*radio**2)

print("el volumen es: ", Vol)
print("el area es: ", area)