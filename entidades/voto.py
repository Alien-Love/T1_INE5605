class Voto:
    def __init__(self):
        self.__tipo_eleitor = None
        self.__candidato_escolhido = None
        self.__cargo = None

    @property
    def candidato_escolhido(self):
        return self.__candidato_escolhido

    @candidato_escolhido.setter
    def candidato_escolhido(self, candidato):
        self.__candidato_escolhido = candidato

    @property
    def tipo_eleitor(self):
        return self.__tipo_eleitor

    @tipo_eleitor.setter
    def tipo_eleitor(self, tipo_eleitor):
        self.__tipo_eleitor = tipo_eleitor

    @property
    def cargo_voto(self):
        return self.__cargo

    @cargo_voto.setter
    def cargo_voto(self, cargo):
        self.__cargo = cargo
    
    
    
