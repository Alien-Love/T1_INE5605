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
        return self.__codigo = valor

#        if codigo is 'valido':
#            self.__codigo = codigo
#        else:
#            print('Por favor, insira um código válido')


    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, valor):
        self.__nome = valor

#        if nome is 'valido':
#            self.__nome = nome
#        else:
#            print('Por favor, insira um nome válido')


    @property
    def cargo(self):
        return self.__cargo


    @cargo.setter
    def cargo(self, valor):
        self.__cargo = valor

#        if cargo is 'valido':
#            self.__cargo = cargo
#        else:
#            print('Por favor, insira um cargo válido')