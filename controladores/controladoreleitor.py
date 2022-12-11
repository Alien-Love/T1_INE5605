from entidades.eleitor import Eleitor
from telas.telaeleitor import TelaEleitor
#from controladorurna import ControladorUrna

class ControladorEleitor:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_eleitor = TelaEleitor()
        self.__eleitores = []

    def inclui_eleitor(self):
        dados = self.__tela_eleitor.cadastro_eleitor()
        eleitor = Eleitor(dados[0], dados[1], dados[2]) #pega dados do eleitor a partir da tela de cadastro
        self.__eleitores.append(eleitor)       
            
    def ja_votou(self, eleitor):
        eleitor.votou = True
           
    @property
    def eleitores(self):
        return self.__eleitores

    @eleitores.setter
    def eleitores(self, eleitor):
        self.__eleitores.append(eleitor)

    def busca_por_cpf(self, cpf):
        for eleitor in self.__eleitores:
            if eleitor.cpf == cpf:
                return eleitor
        return None