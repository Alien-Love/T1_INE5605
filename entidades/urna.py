class Urna:

    def __init__(self,
                 #serie = int,
                 turno = int
                 ):
        self.__lista_candidatos = []
        self.__lista_votos = []
        #self.__eleitores = []
        #self.__serie = serie
        self.__turno = turno


    @property
    def candidatos(self):
        return self.__lista_candidatos


    def add_candidatos(self, candidato):
        self.__lista_candidatos.append(candidato)


    def remover_candidatos(self, candidato):
        self.__lista_candidatos.remove(candidato)


    @property
    def votos(self):
        return self.__lista_votos


    @votos.setter
    def votos(self, Voto):
        self.__lista_votos.append(Voto)


    @property
    def turno(self):
        return self.__turno


    @turno.setter
    def turno(self, turno):
        self.__turno = turno


    #@property
    #def serie(self):
    #    return self.__serie


    #@serie.setter
    #def serie(self, serie):
    #    self.__serie = serie


    #@property
    #def eleitores(self):
    #    return self.__eleitores


    #@eleitores.setter
    #def eleitores(self, eleitor):
    #    self.eleitores.append(eleitor)