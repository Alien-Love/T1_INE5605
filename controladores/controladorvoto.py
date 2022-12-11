from telas.telavoto import TelaVoto
from voto import Voto

class ControladorVoto:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_voto = TelaVoto()
        self.__lista_votos = []
        self.__eleitor_atual = None
    
    @property
    def lista_votos(self):
        return self.__lista_votos

    @property
    def eleitor_atual(self):
        return self.__eleitor_atual
    
    @eleitor_atual.setter
    def eleitor_atual(self, eleitor):
        self.__eleitor_atual = eleitor

    def adiciona_voto(self):

        cpf_eleitor = self.__tela_voto.pega_cpf_eleitor()
        
        self.eleitor_atual = self.__controlador_principal.controlador_eleitor.busca_por_cpf(cpf_eleitor)
        
        if self.eleitor_atual == None:
            pass #implementar eleitorinvalidoexception

        reitorias = {"reitoria": self.__tela_voto.voto_reitor, "prograd": self.__tela_voto.voto_proreitor_grad,
        "propes": self.__tela_voto.voto_proreitor_pes, "proex": self.__tela_voto.voto_proreitor_ext}
        
        eleitor_atual = self.eleitor_atual

        for reitoria in reitorias:
            if reitoria in self.__controlador_principal.controlador_configuracao.configuracao.reitorias:
            #se a chave estiver presente na lista de cargos participantes
                
                voto = Voto()
                voto.tipo_eleitor = eleitor_atual.tipo
                numero = reitorias[reitoria]()    #recebe o numero do candidato para a reitoria atual
                lista_candidatos = self.__controlador_principal.controlador_candidato.listas_candidatos(reitoria)
                #retorna a lista de candidatos existentes para a reitoria atual

                if numero != 00:
                    for candidato in lista_candidatos:
                        if candidato.codigo == numero:
                            voto.candidato_escolhido = numero
                            break
                        else:   #caso numero digitado nao pertenca a candidato ao cargo
                           voto.candidato_escolhido = 99 
                else:   #caso no aseja informado um numero
                    voto.candidato_escolhido = 00
                
                self.__lista_votos.append(voto)
            
