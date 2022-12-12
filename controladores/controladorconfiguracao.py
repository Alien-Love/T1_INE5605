from entidades.configuracao import Configuracao
from telas.telaconfiguracao import TelaConfiguracao

class ControladorConfiguracao:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_configuracao = TelaConfiguracao()
        self.__configuracao = None

    @property
    def configuracao(self):
        return self.__configuracao
    
    def configurar(self):
        turno = self.__tela_configuracao.config_()
        rei_torias = {1: "reitoria", 2: "prograd", 3: "propes", 4: "proex"}
        lista_reitorias = []

        if turno == 1:
            dados = self.__tela_configuracao.dados_turno_1()
            configuracao = Configuracao(int(turno), dados["total_candidatos"], dados["total_eleitores"], list(rei_torias.values()))
            #instancia configuracao com todas as categorias de candidato para voto 
            self.__configuracao = configuracao
            configuracao.urna_configurada = True
        
        elif turno == 2: #configuracao para o segundo turno
            dados = self.__tela_configuracao.dados_turno_2()
            configuracao = Configuracao(int(turno), dados["total_candidatos"], dados["total_eleitores"], dados["reitorias"])
            lista_eleitores = self.__controlador_principal.controlador_eleitor.eleitores
            for eleitor in lista_eleitores:
                eleitor.ja_votou = False #alterna o estado do parametro, permitindo que os eleitores votem novamente
            self.__configuracao = configuracao
            lista_cargos = dados["reitorias"] #recebe os cargos desejados pelo input da tela
            lista_reitorias.clear() #limpa lista que armazena os cargos participantes
            #lista_eleitores.clear() #limpa lista para receber possiveis eleitores nao votantes no primeiro turno
            print("dados", dados["reitorias"])
            for i in range(len(lista_cargos)):
                lista_reitorias.append(lista_cargos[i])
                #o objeto sera passado para a declaracao if dentro da funcao 'adiciona_voto'
                self.__configuracao.reitorias = lista_reitorias
            print(self.__configuracao.reitorias)
            configuracao.urna_configurada = True

    def retornar(self):
        self.__controlador_principal.inicia()