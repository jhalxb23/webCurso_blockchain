#parecida a una lista pero estas son inmutables

ciudades =("cali", "medellin","bogota", "villavicencio", "neiva", "Ibague")
print(ciudades)
for i in range(0, len(ciudades)):  #imprimir posiciones de mi tupla
    print(i, ciudades[i])

print(ciudades[2])
print(type(ciudades)) #devuelve el tipo de elemento en este caso devuelve tupla
print()
print(ciudades.count("cali"))

'''m = ('sol', "rosa")
x, y=m #permite asignacion de izquiera a derecha
print(x, y, x) #imprimir valores de la tupla'''

print()
tecnologias=('zope','plone', 'pyramid')
for i in range(0, len(tecnologias)):
    print(i, tecnologias[i])


