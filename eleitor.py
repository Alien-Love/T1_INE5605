

class Eleitor:

    def __init__(self, nome, codigo, tipo: str):
        self.__nome = nome
        self.__codigo = codigo
        self.__tipo = tipo
        self.__votou = False

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

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
