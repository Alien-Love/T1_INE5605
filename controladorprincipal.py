import sys
from telainicial import TelaInicial
from controladoreleitor import ControladorEleitor
from controladorvoto import ControladorVoto
#from controladorurna import ControladorUrna
from controladorcandidato import ControladorCandidato
from resultado import Resultado
from eleitor import Eleitor
from controladorconfiguracao import ControladorConfiguracao

class ControladorPrincipal:

    def __init__(self):
        self.__tela_inicial = TelaInicial()
        self.__controlador_eleitor = ControladorEleitor(self)
        self.__controlador_voto = ControladorVoto(self)
        #self.__controlador_urna = ControladorUrna(self)
        self.__controlador_candidato = ControladorCandidato(self)
        self.__controlador_configuracao = ControladorConfiguracao(self)
        self.__resultado = Resultado(self)

    def inicia(self):    #inicia opçao de voto, cadastro, ou resultado
        opcoes = {0: self.finaliza_sistema, 1: self.inicia_voto, 2: self.inicia_cadastro, 3: self.inicia_resultado, 4: self.inicia_configuracao}

        while True:
            opcao = (self.__tela_inicial.tela_opcoes())
            opcoes[opcao]()

    @property
    def controlador_eleitor(self):
        return self.__controlador_eleitor

    @property
    def controlador_configuracao(self):
        return self.__controlador_configuracao

    def inicia_voto(self):
        self.__controlador_eleitor.inclui_eleitor()
        self.__controlador_voto.adiciona_voto()
        self.__controlador_eleitor.ja_votou(self.__controlador_eleitor.eleitor)

    def inicia_cadastro(self):
        self.__controlador_candidato.mostra_tela_candidato()

    def inicia_resultado(self):
        self.__resultado.calcular_resultado()

    def inicia_configuracao(self):
        self.__controlador_configuracao.configurar()
    
    def finaliza_sistema(self):
        sys(exit)