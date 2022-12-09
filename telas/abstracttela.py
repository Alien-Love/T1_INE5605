from abc import ABC, abstractmethod

class AbstractTela(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def le_inteiro(self, valor):
        pass