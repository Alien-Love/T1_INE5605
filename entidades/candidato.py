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
    def codigo(self, codigo):
        self.__codigo = codigo


    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def cargo(self):
        return self.__cargo


    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo


    @property
    def chapa(self):
        return self.__chapa


    @chapa.setter
    def chapa(self, chapa):
        self.__chapa = chapa