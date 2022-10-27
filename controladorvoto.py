from telavoto import TelaVoto
from voto import Voto
from controladoreleitor import ControladorEleitor

class ControladorVoto:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_voto = TelaVoto()
        
    def adiciona_voto(self):

        voto = Voto()
        voto.tipo_eleitor = self.__controlador_principal.controlador_eleitor.eleitor.tipo
        print(voto.tipo_eleitor) #teste
'''
        self.__tela_voto.voto_reitor()
        self.__tela_voto.voto_proreitor_grad()
        self.__tela_voto.voto_proreitor_pes()
        self.__tela_voto.voto_proreitor_ext()
        '''