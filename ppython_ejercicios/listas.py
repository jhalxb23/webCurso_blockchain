campistas=["jhon bedoya", "daniel maldonado","gina alvarez","alberto romero", "oscar javier",5, True]
campistas.append("camilo sanchez")
campistas.append(False)
campistas.append("derivando")
campistas.append(8828)
campistas.append(False) #añade valores a la lista, solo permite un argumento
campistas.extend(range(5,9)) #añades valores int desde el 5 al 8
print()
print("La posicion de la primera aparicion en la lista es la posicion: ",campistas.index(False)) #devuel el valor de la posicion de su primera aparicion en la lista
print()
print()
print(campistas) #imprime lso valores guardados en la lista, si no se le entrega un parametro de busqueda entrega todos los valores
print()
campistas.insert(1, "Socrates")  #insera un elemento en una posicion dada
print(campistas)
print()

campistas.remove(False) #borra la primera aparicion del elemento en la lista
print(campistas) 
print()

campistas.reverse()  #invierte la posicion de los elements de a lista de la lista
print(campistas)

#print()
#campistas.sort() #ordena la lista pero con elementos iguales, str o int
print()
#print(campistas)

print("el ultimo elemtos de la lista es: ",campistas.pop())  #muestra el ultimo elemento de la lista y lo borra
print(campistas)




'''longitud=len(campistas)-1
print("la longitud de las lista es:", longitud)
print(campistas[longitud])'''


'''nombre = input("ingrese un nombre: ")
edad=int(input("Ingrese la edad: "))
datos=[nombre, edad]
print(datos)
datos.append("soy el valor adiccionado con append")
print(datos)'''