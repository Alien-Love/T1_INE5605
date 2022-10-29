from telavoto import TelaVoto
from voto import Voto

class ControladorVoto:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_voto = TelaVoto()
        
    def adiciona_voto(self):

        reitorias = {"reitoria": self.__tela_voto.voto_reitor, "prograd": self.__tela_voto.voto_proreitor_grad,
        "propes": self.__tela_voto.voto_proreitor_pes, "proex": self.__tela_voto.voto_proreitor_ext}
        
        for reitoria in reitorias:
            if reitoria in self.__controlador_principal.controlador_configuracao.configuracao.reitorias:
            #se a chave estiver presente na lista de cargos participantes
                voto = Voto()
                voto.tipo_eleitor = self.__controlador_principal.controlador_eleitor.eleitor.tipo
                reitorias[reitoria]()
                #ainda falta receber voto da tela e armazenar no objeto 'voto'
            
            else:
                self.__tela_voto.categoria_vazia()
        