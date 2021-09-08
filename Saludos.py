from abc import ABC, abstractmethod

class Saludos(ABC):

    @abstractmethod
    def buenosDias(self):
        pass

    @abstractmethod
    def buenasTardes(self):
        pass

