class Eleitor:

    def __init__(self, nome, cpf, tipo: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__tipo = tipo
        self.__votou = False

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
    
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo
    
    @property
    def votou(self):
        return self.__votou

    @votou.setter
    def votou(self, votou):
        self.__votou = True
