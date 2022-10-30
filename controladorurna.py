#from controladorprincipal import ControladorPrincipal
import urna
import telaurna
from controladorvoto import ControladorVoto

class ControladorUrna:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal


    def incluir_eleitor(self, eleitor):
        urna.__eleitores.append(eleitor)


    def incluir_candidato(self, candidato):
        urna.candidatos.append(candidato)


    def incluir_voto(self, voto):
        urna.voto.append(voto)


    def excluir_candidato(self, candidato):
        urna.candidatos.pop(candidato)