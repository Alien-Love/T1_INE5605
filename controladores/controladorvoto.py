from telas.telavoto import TelaVoto
from voto import Voto

class ControladorVoto:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_voto = TelaVoto()
        self.__lista_votos = []
        
    @property
    def lista_votos(self):
        return self.__lista_votos

    def adiciona_voto(self):

        reitorias = {"reitoria": self.__tela_voto.voto_reitor, "prograd": self.__tela_voto.voto_proreitor_grad,
        "propes": self.__tela_voto.voto_proreitor_pes, "proex": self.__tela_voto.voto_proreitor_ext}
        
        for reitoria in reitorias:
            if reitoria in self.__controlador_principal.controlador_configuracao.configuracao.reitorias:
            #se a chave estiver presente na lista de cargos participantes
                
                voto = Voto()
                voto.tipo_eleitor = self.__controlador_principal.controlador_eleitor.eleitor.tipo
                numero = reitorias[reitoria]()    #recebe o numero do candidato para a reitoria atual
                lista_candidatos = self.__controlador_principal.controlador_candidato.listas_candidatos(reitoria)
                #retorna a lista de candidatos existentes para a reitoria atual

                if numero != 00:
                    for candidato in lista_candidatos:
                        if candidato.codigo == numero or numero == 32:
                            voto.candidato_escolhido = numero
                            break
                        else:   #caso numero digitado nao pertenca a candidato ao cargo
                           voto.candidato_escolhido = 99 
                else:   #caso no aseja informado um numero
                    voto.candidato_escolhido = 00
                
                self.__lista_votos.append(voto)

            else:
                pass
            