class Animal():
    def __init__(self, especie, nombre, sonido):
        self.especie= especie
        self.nombre=nombre
        self.sonido=sonido

    def que_escucha(self):
        self.sonido= input("ingrese alguno de estos sonidos: guau, miau, kuku:  ")
        return self.sonido   


    def hablar(self):
        if self.sonido =="guau":
            print ("Acaba de escuchar un perro")
        elif self.sonido =="miau":
            print ("Acaba de escuchar un gato")
        else:
            print ("Este es un animal desconocido")

perro =Animal("perro","Colita","sonido")

perro.que_escucha()
perro.hablar()
