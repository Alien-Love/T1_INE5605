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
        self.__tela_voto.voto_reitor()
        #implementar votos de reitor e pro reitores
        self.__controlador_eleitor.ja_votou()  
        

