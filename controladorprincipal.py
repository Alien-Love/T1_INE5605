from telainicial import TelaInicial
from controladoreleitor import ControladorEleitor
from controladorvoto import ControladorVoto
from controladorurna import ControladorUrna
from controladorcandidato import ControladorCandidato
from resultado import Resultado

class ControladorPrincipal:

    def __init__(self):
        self.__tela_inicial = TelaInicial(self)
        self.__controlador_eleitor = ControladorEleitor(self)
        self.__controlador_voto = ControladorVoto
        self.__controlador_urna = ControladorUrna
        self.__controlador_candidato = ControladorCandidato
        self.__resultado = Resultado

    def inicia(self):    #inicia opçao de voto, cadastro, ou resultado
        pass

    def inicia_voto(self):
        pass

    def inicia_cadastro(self):
        pass

    def inicia_resultado(self):
        pass