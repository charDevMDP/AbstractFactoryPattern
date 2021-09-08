from abc import ABC, abstractmethod

class Preguntas(ABC):

    @abstractmethod
    def preguntaHora(self):
        pass

    @abstractmethod
    def preguntaTiempo(self):
        pass

