from urna import Urna
from telaurna import TelaUrna

class ControladorUrna:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__urna = Urna()


    #def incluir_eleitor(self, Eleitor):
    #    self.__urna.__eleitores = Eleitor


    #def incluir_candidato(self, Candidato):
    #    self.__urna.__candidatos = Candidato


    #def incluir_voto(self, Voto):
    #    self.__urna.__votos = Voto


    #def excluir_candidato(self, candidato):
    #    #não sei como chamar o deleter daqui (encontra-se em urna.py)
    #    pass


    def exibir_candidatos(self):
        return self.__urna.__candidatos()