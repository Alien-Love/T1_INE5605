from telainicial import TelaInicial
from controladoreleitor import ControladorEleitor
from controladorvoto import ControladorVoto
from controladorurna import ControladorUrna
from controladorcandidato import ControladorCandidato
from resultado import Resultado
from eleitor import Eleitor

class ControladorPrincipal:

    def __init__(self):
        self.__tela_inicial = TelaInicial()
        self.__controlador_eleitor = ControladorEleitor(self)
        self.__controlador_voto = ControladorVoto(self, self.__controlador_eleitor) #tentar fazer com getter do controlador principal
        self.__controlador_urna = ControladorUrna(self)
        self.__controlador_candidato = ControladorCandidato(self)
        self.__resultado = Resultado(self)

    def inicia(self):    #inicia opçao de voto, cadastro, ou resultado
        opcoes = {1: self.inicia_voto, 2: self.inicia_cadastro, 0: self.inicia_resultado}

        while True:
            opcao = (self.__tela_inicial.tela_opcoes())
            opcoes[opcao]()

    def inicia_voto(self):
        self.__controlador_voto.cadastro_eleitor()
        self.__controlador_voto.adiciona_voto()


    def inicia_cadastro(self):
        self.__controlador_candidato.mostra_tela_candidato()

    def inicia_resultado(self):
        self.__resultado.calcular_resultado()