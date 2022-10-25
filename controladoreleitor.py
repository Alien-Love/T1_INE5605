from controladorprincipal import ControladorPrincipal
from eleitor import Eleitor
from telavoto import TelaVoto

class ControladorEleitor:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_voto = TelaVoto()
        self.__controlador_urna = ControladorUrna(self)

    def inclui_eleitor(self):
        self.__tela_voto.cadastra_eleitor()
        eleitor = Eleitor("", 0, "") #pegar dados do eleitor a partir da tela de cadastro
        eleitor.tipo
        self.__controlador_urna.inclui_eleitor(eleitor)

    def ja_votou(self):
        