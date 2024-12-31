#ejercicios sobre clases

class Celular():
    def __init__(self, marca, modelo, camara):
        self.marca=marca
        self.modelo =modelo
        self.camara =camara
        pass
    
Celular1=Celular("Samsung", "s23", "48MP")  #instancia de la clase celular
Celular2=Celular("Apple", "Iphone 15 Pro", "96MP")
Celular3=Celular("Xiaomi", "C12", "58MP")

print(Celular3.camara)

    