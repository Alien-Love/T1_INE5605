class Candidato:

    def __init__(self, codigo = str,
                 chapa = str,
                 nome = str,
                 cargo = str):
        self.codigo = codigo
        self.chapa = chapa
        self.nome = nome
        self.cargo = cargo


    @property
    def codigo(self):
        return self.__codigo


    @codigo.setter
    def codigo(self, codigo):
        if codigo is 'valido':
            self.__codigo = codigo
        else:
            print('Por favor, insira um código válido')


    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, nome):
        if nome is 'valido':
            self.__nome = nome
        else:
            print('Por favor, insira um nome válido')


    @property
    def cargo(self):
        return self.__cargo


    @cargo.setter
    def cargo(self, cargo):
        if cargo is 'valido':
            self.__cargo = cargo
        else:
            print('Por favor, insira um cargo válido')