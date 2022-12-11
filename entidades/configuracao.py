class Configuracao:
    def __init__(self, turno, quantia_candidatos, quantia_eleitores, reitorias):
        self.__turno = turno
        self.__quantia_cadidatos = quantia_candidatos
        self.__quantia_eleitores = quantia_eleitores
        self.__reitorias = reitorias
        self.__urna_configurada = False

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

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
    
    @property
    def reitorias(self):
        return self.__reitorias

    @reitorias.setter
    def reitorias(self, reitorias):
        self.__reitorias = reitorias

    @property
    def urna_configurada(self):
        return self.__urna_configurada
    
    @urna_configurada.setter
    def urna_configurada(self, boolean):
        self.__urna_configurada = boolean