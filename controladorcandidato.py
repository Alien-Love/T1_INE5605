from candidato import Candidato
from telacandidato import TelaCandidato
#from controladorprincipal import ControladorCandidato
import urna

class ControladorCandidato:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__candidatos_reitor = []
        self.__candidatos_prograd = []
        self.__candidatos_propes = []
        self.__candidatos_proex = []

    def mostra_tela_candidato(self):
        escolha = TelaCandidato.mostrar_tela()
        if escolha == 'a':
            TelaCandidato.adicionar_candidato()
        elif escolha == 'b':
            TelaCandidato.remover_candidato()
        elif escolha == 'c':
            TelaCandidato.listar_candidatos()
        elif escolha == 'd':
            TelaCandidato.validar_dados()
        elif escolha == 'e':
            TelaCandidato.alterar_candidato()

    @property
    def adicionar_candidato(self, info):
        pass


    @adicionar_candidato.setter
    def adicionar_candidato(self, Candidato):
        pass


    @adicionar_candidato.deleter
    def adicionar_candidato(self, Candidato):
        pass


    def listar_candidatos(self):
        candidatos = Urna.lista_candidatos
        return candidatos


    def mostrar_candidato(codigo):
        for candidato in urna.lista_candidatos:
            if candidato.codigo == codigo:
                return candidato

    def listas_candidatos(self, categoria):
        categorias = {
            "reitoria": self.__candidatos_reitor, "prograd": self.__candidatos_prograd,
            "propes": self.__candidatos_propes, "proex": self.__candidatos_proex
            }
        return categorias[categoria]