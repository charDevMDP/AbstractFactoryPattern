from Saludos import Saludos
from Preguntas import Preguntas
from FactoryAbs import Factory


class FactoryEN(Factory):

    def preguntar(self):
        return PregEN()
    
    def saludar(self):
        return SaludarEN()


class PregEN(Preguntas):
    def preguntaHora(self):
        return "what time is it?"

    def preguntaTiempo(self):
        return "how is the weather?"
    

class SaludarEN(Saludos):
    def buenosDias(self):
        return "good morning"

    def buenasTardes(self):
        return "good afternoon"
