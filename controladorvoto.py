from telavoto import TelaVoto
from voto import Voto
from controladoreleitor import ControladorEleitor

class ControladorVoto:

    def __init__(self, controlador_principal, controlador_eleitor):
        self.__controlador_principal = controlador_principal
        self.__tela_voto = TelaVoto()
        self.__controlador_eleitor = ControladorEleitor(self)


    def cadastro_eleitor(self):
        self.__controlador_eleitor.inclui_eleitor()
        
    def adiciona_voto(self):

        voto = Voto("a")

        self.__tela_voto.voto_reitor()
        self.__tela_voto.voto_proreitor_grad()
        self.__tela_voto.voto_proreitor_pes()
        self.__tela_voto.voto_proreitor_ext()
        