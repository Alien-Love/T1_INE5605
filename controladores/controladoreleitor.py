from entidades.eleitor import Eleitor
from telas.telaeleitor import TelaEleitor
from persistencia.eleitordao import EleitorDAO

class ControladorEleitor:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_eleitor = TelaEleitor()
        self.__eleitordao = EleitorDAO()

    def inclui_eleitor(self):
        dados = self.__tela_eleitor.cadastro_eleitor()
        if  dados == 0:
            self.__controlador_principal.inicia()
        elif dados == 1:
            self.__tela_eleitor.cpf_invalido()
            self.__controlador_principal.inicia()
        else:
            eleitor = Eleitor(dados["nome"], int(dados["cpf"]), dados["categoria"]) #pega dados do eleitor a partir da tela de cadastro       
            self.__eleitordao.add(int(dados["cpf"]), eleitor)

    def ja_votou(self, eleitor):
        eleitor.votou = True
           
    @property
    def eleitores(self):
        eleitores = self.__eleitordao.get_all
        return eleitores

    def busca_por_cpf(self, cpf):
        eleitor = self.__eleitordao.get(int(cpf))
        if eleitor == None:
            return None
        return eleitor