from eleitor import Eleitor

class Voto:
    def __init__(self, tipo_eleitor: str):
        self.__tipo_eleitor = str
        self.__candidato = None

    @property
    def candidato(self):
        return self.__candidato

    @candidato.setter
    def candidato(self, candidato):
        self.__candidato = candidato

    @property
    def tipo_eleitor(self):
        return self.__tipo_eleitor

    @tipo_eleitor.setter
    def tipo_eleitor(self, tipo_eleitor):
        self.__tipo_eleitor = tipo_eleitor
    
    
    
