from Saludos import Saludos
from Preguntas import Preguntas
from FactoryAbs import Factory


class FactoryES(Factory):

    def preguntar(self):
        return PregES()
    
    def saludar(self):
        return SaludarES()


class PregES(Preguntas):
    def preguntaHora(self):
        return "¿qué hora es?"

    def preguntaTiempo(self):
        return "¿qué tiempo hace?"
    

class SaludarES(Saludos):
    def buenosDias(self):
        return "buenos días"

    def buenasTardes(self):
        return "buenas tardes"
