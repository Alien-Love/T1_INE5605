class Configuracao:
    def __init__(self, quantia_candidatos, quantia_eleitores):
        self.__quantia_cadidatos = quantia_candidatos
        self.__quantia_eleitores = quantia_eleitores

    @property
    def quantia_candidatos(self):
        return self.__quantia_cadidatos

    @quantia_candidatos.setter
    def quantia_candidatos(self, quantia_candidatos):
        self.__quantia_cadidatos = quantia_candidatos

    @property
    def quantia_eleitores(self):
        return self.__quantia_eleitores
    
    @quantia_eleitores.setter
    def quantia_eleitores(self, quantia_eleitores):
        self.__quantia_eleitores = quantia_eleitores