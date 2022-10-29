from configuracao import Configuracao
from telaconfiguracao import TelaConfiguracao

class ControladorConfiguracao:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_configuracao = TelaConfiguracao()
        self.__configuracao = None

    @property
    def configuracao(self):
        return self.__configuracao

    def configurar(self):
        dados = self.__tela_configuracao.config_()
        rei_torias = {1: "reitoria", 2: "prograd", 3: "propes", 4: "proex"}
        lista_reitorias = []

        if dados[0] == 1:
            configuracao = Configuracao(dados[0], dados[1], dados[2], list(rei_torias.values()))
            #instancia configuracao com todas as categorias de candidato para voto 
            self.__configuracao = configuracao
        
        else: #configuracao para o segundo turno
            configuracao = Configuracao(dados[0], dados[1], dados[2], [])
            self.__configuracao = configuracao
            lista_cargos = dados[3] #recebe os cargos desejados pelo input da tela
            lista_reitorias.clear() #limpa lista que armazena os cargos participantes

            for i in range(len(lista_cargos)):
                lista_reitorias.append(rei_torias.get(lista_cargos[i]))
                #o objeto sera passado para a declaracao if dentro da funcao 'adiciona_voto'
                self.__configuracao.reitorias = lista_reitorias
