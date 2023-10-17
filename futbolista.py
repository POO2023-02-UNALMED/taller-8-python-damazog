from deportista import Deportista

class Futbolista(Deportista):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, deporte="Futbol", golesMarcados=0, tarjetasRojas=0, piernaHabil=""):
        super().__init__(nombre, edad, altura, sexo, deporte, 0)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def getGolesMarcados(self):
        return self._golesMarcados

    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    def __str__(self):
        return f"Mi nombre es {self.get_nombre()}. Soy profesional en el deporte {self.get_deporte()}. Tengo {self.get_edad()} años de edad y llevo {self.get_añosPracticando()} años en el deporte."

futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")   
print(futbolista.getNO)