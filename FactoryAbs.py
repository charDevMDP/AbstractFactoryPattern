from abc import ABC, abstractmethod

# Fabrica Abstracta
class Factory(ABC):

    @abstractmethod
    def saludar(self):
        pass

    @abstractmethod
    def preguntar(self):
        pass
