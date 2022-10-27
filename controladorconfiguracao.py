from configuracao import Configuracao
from controladorprincipal import ControladorPrincipal
from telaconfiguracao import TelaConfiguracao

class ControladorConfiguracao:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_configuracao = TelaConfiguracao(self)
        self.__configuracao = None

    def configurar(self):
        dados = self.__tela_configuracao.config_()
        configuracao = Configuracao(dados[0], dados[1])
        self.__configuracao = configuracao