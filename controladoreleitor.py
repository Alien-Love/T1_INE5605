from eleitor import Eleitor
from telaeleitor import TelaEleitor
#from controladorurna import ControladorUrna

class ControladorEleitor:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_eleitor = TelaEleitor()
        #self.__controlador_urna = ControladorUrna(self)
        self.__eleitores = []
        self.__eleitor = None  #armazena o eleitor atual, que sera passado como argumento na funcao ja_votou

    def inclui_eleitor(self):
        dados = self.__tela_eleitor.cadastro_eleitor()
        eleitor = Eleitor(dados[0], dados[1], dados[2]) #pega dados do eleitor a partir da tela de cadastro
        self.__eleitores.append(eleitor)
        self.__eleitor = eleitor
        print(self.__eleitores) #teste
        print(eleitor.tipo) #teste


    def ja_votou(self, eleitor):
        eleitor = self.__eleitor
        eleitor.votou = True
        print(eleitor.votou)
    
    @property
    def eleitores(self):
        return self.__eleitores

    @property
    def eleitor(self):
        return self.__eleitor
