datos_basicos={
    "nombre":"maria",
    "edad":23,
    "peso":54,
    "Estudia": True,
    "Estatura":1.70
}

print(datos_basicos.values()) #muestra el valor de los elementos del dic
print(datos_basicos["edad"])

copiadatos =datos_basicos.copy() #copia los datos de mi diccionario.
print(copiadatos)