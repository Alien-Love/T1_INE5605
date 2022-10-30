class Urna:

    def __init__(self,
                 serie = int,
                 turno = int
                 ):
        self.__lista_candidatos = []
        self.__lista_votos = []
        self.__eleitores = []
        self.__serie = serie
        self.__turno = turno


    @property
    def candidatos(self):
        return self.__lista_candidatos


    @candidatos.setter
    def candidatos(self, Candidato):
        self.__lista_candidatos.append(Candidato)


    @property
    def votos(self):
        return self.__lista_votos


    @votos.setter
    def votos(self, Voto):
        self.__lista_votos.append(Voto)


    @property
    def serie(self):
        return self.__serie


    @serie.setter
    def serie(self, serie):
        self.__serie = serie


    @property
    def eleitores(self):
        return self.__eleitores


    @eleitores.setter
    def eleitores(self, eleitor):
        self.eleitores.append(eleitor)