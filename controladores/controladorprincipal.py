import sys
from telas.telainicial import TelaInicial
from controladores.controladoreleitor import ControladorEleitor
from controladores.controladorvoto import ControladorVoto
from controladores.controladorurna import ControladorUrna
from controladores.controladorcandidato import ControladorCandidato
from entidades.resultado import Resultado
from controladores.controladorconfiguracao import ControladorConfiguracao
from entidades.configuracaoexception import ConfiguracaoException

class ControladorPrincipal:

    def __init__(self):
        self.__tela_inicial = TelaInicial()
        self.__controlador_eleitor = ControladorEleitor(self)
        self.__controlador_voto = ControladorVoto(self)
        self.__controlador_urna = ControladorUrna(self)
        self.__controlador_candidato = ControladorCandidato(self)
        self.__controlador_configuracao = ControladorConfiguracao(self)
        self.__resultado = Resultado(self)

    def inicia(self):    #inicia opçao de voto, cadastro, ou resultado
        opcoes = {
            0: self.finaliza_sistema, 1: self.inicia_voto, 2: self.cadastro_candidato,
            3: self.cadastro_eleitor, 4: self.inicia_resultado, 5: self.inicia_configuracao
            }

        while True:
            opcao = (self.__tela_inicial.tela_opcoes())
            try:
                if (opcao == 1):
                    if self.__controlador_configuracao.configuracao is not None:
                        if (self.__controlador_configuracao.configuracao.urna_configurada == False):
                            raise ConfiguracaoException
                    elif self.__controlador_configuracao.configuracao == None:
                        raise ConfiguracaoException
                opcoes[opcao]()
            except ConfiguracaoException:
                self.__tela_inicial.erro_configuracao()

    @property
    def controlador_eleitor(self):
        return self.__controlador_eleitor

    @property
    def controlador_configuracao(self):
        return self.__controlador_configuracao

    @property
    def controlador_candidato(self):
        return self.__controlador_candidato

    @property
    def controlador_urna(self):
        return self.__controlador_urna

    @property
    def controlador_voto(self):
        return self.__controlador_voto

    @property
    def resultado(self):
        return self.__resultado

    def inicia_voto(self):
        self.__controlador_voto.adiciona_voto()
        self.__controlador_eleitor.ja_votou(self.__controlador_voto.eleitor_atual)            

    def cadastro_candidato(self):
        self.__controlador_candidato.mostra_tela_candidato()

    def cadastro_eleitor(self):
        self.controlador_eleitor.inclui_eleitor()

    def inicia_resultado(self):
        self.__controlador_urna.exibir_votos_categorias()
        self.__controlador_urna.calcular_resultado_final()

    def inicia_configuracao(self):
        self.__controlador_configuracao.configurar()

    def finaliza_sistema(self):
        sys.exit()