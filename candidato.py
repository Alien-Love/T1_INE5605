class Candidato:

    def __init__(self, codigo = str,
                 chapa = str,
                 nome = str,
                 cargo = str):
        self.__codigo = codigo
        self.__chapa = chapa
        self.__nome = nome
        self.__cargo = cargo


    @property
    def codigo(self):
        return self.__codigo


    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor


    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, valor):
        self.__nome = valor


    @property
    def cargo(self):
        return self.__cargo


    @cargo.setter
    def cargo(self, valor):
        self.__cargo = valor