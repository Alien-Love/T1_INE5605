from candidato import Candidato
from telacandidato import TelaCandidato
from controladorprincipal import ControladorCandidato
import urna

class ControladorCandidato:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal


def mostra_tela_candidato(self):
    escolha = TelaCandidato.mostrar_tela()
    if escolha == 'a':
        adicionar_candidato(TelaCandidato.adicionar_candidato())
    elif escolha == 'b':
        adicionar_candidato.deleter(TelaCandidato.remover_candidato())
    elif escolha == 'c':
        TelaCandidato.listar_candidatos()
    elif escolha == 'd':
        TelaCandidato.validar_dados()
    elif escolha == 'e':
        TelaCandidato.alterar_candidato()

    @property
    def adicionar_candidato(self, info):
        Urna.lista_candidatos += Candidato(info[0], info[1], info[2], info[3])


    @adicionar_candidato.setter
    def adicionar_candidato(self, candidato, opcao, novo_valor):
        if opcao == 'a':
            candidato.__codigo = novo_valor
        elif opcao == 'b':
            candidato.__chapa = novo_valor
        elif opcao == 'c':
            candidato.__nome = novo_valor
        elif opcao == 'd':
            candidato.__cargo = novo_valor


    @adicionar_candidato.deleter
    def adicionar_candidato(self, Candidato):
        Urna.lista_candidatos.remove(candidato_removido)


    def listar_candidatos(self):
        candidatos = Urna.lista_candidatos
        return candidatos


    def mostrar_candidato(codigo):
        for candidato in urna.lista_candidatos:
            if candidato.codigo == codigo:
                return candidato