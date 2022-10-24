from controladorprincipal import ControladorPrincipal
from telavoto import TelaVoto

class ControladorEleitor:
    def __init__(self, controlador_principal, tela_voto):
        self.__controlador_principal = controlador_principal
        self.__tela_voto = tela_voto

    def inclui_eleitor(self, eleitor):
        pass

    def ja_votou(self, eleitor):
        pass