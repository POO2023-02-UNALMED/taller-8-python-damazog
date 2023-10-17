from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre, edad, altura, sexo, deporte, añosPracticando):
        super().__init__(nombre, edad, altura, sexo)
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def get_deporte(self):
        return self._deporte

    def set_deporte(self, deporte):
        self._deporte = deporte

    def get_añosPracticando(self):
        return self._añosPracticando

    def set_añosPracticando(self, añosPracticando):
        self._añosPracticando = añosPracticando