from Animal import Animal
class Ave(Animal): 
    def __init__(self, nombre1, peso1, año_nacimiento, propietario):
        self.año_nacimiento1= año_nacimiento
        self.propietario1= propietario
        super().__init__(nombre1, peso1)

    def Calculador(self):
        edad= 2024 - self.año_nacimiento1
        print("el nombre del animal: ", self.nombre1)
        print("el propietario es:", self.propietario1)
        print("edad:", edad)
        if (edad>=5):
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
        
               
Ave2= Ave("Mia", 30, 2017, "Brenda")
Ave2.Calculador()

