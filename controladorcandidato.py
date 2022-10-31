from candidato import Candidato
from telacandidato import TelaCandidato

class ControladorCandidato:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__candidatos_reitor = []
        self.__candidatos_prograd = []
        self.__candidatos_propes = []
        self.__candidatos_proex = []
        self.__tela_candidato = TelaCandidato()
        self.__controlador_urna = self.__controlador_principal.controlador_urna

    def mostra_tela_candidato(self):
        # Chama a tela baseado na resposta escolhida no menu de candidatos.
        escolha = self.__tela_candidato.mostrar_tela()
        if escolha == 'a':
            self.__tela_candidato.adicionar_candidato()
        elif escolha == 'b':
            self.__tela_candidato.remover_candidato()
        elif escolha == 'c':
            self.__tela_candidato.listar_candidatos()
        elif escolha == 'd':
            self.__tela_candidato.validar_dados()
        elif escolha == 'e':
            self.__tela_candidato.alterar_candidato()

    @property
    def adicionar_candidato(self, info):
        self.__controlador_urna.incluir_candidato(Candidato(info[0], info[1],
                                                            info[2], info[3]))
        # Adiciona candidato com as informações recebidas na tela de adicionar
        # candidato.


    @adicionar_candidato.setter
    def adicionar_candidato(self, codigo, opcao, novo_valor):
        if opcao == 'a':
            self.mostrar_candidato(codigo).__codigo = novo_valor
        elif opcao == 'b':
            self.mostrar_candidato(codigo).__chapa = novo_valor
        elif opcao == 'c':
            self.mostrar_candidato(codigo).__nome = novo_valor
        elif opcao == 'd':
            self.mostrar_candidato(codigo).__cargo = novo_valor
        # setter de diferentes atributos baseado na opção escolhida no menu de
        # alteração de candidato.


    @adicionar_candidato.deleter
    def adicionar_candidato(self):
    # remove o candidato escolhido na tela de exclusão de candidatos.
        codigo_do_candidato = self.__tela_candidato.remover_candidato()
        candidato = self.mostrar_candidato(codigo_do_candidato)
        self.__controlador_urna.excluir_candidato(candidato)


    def listar_candidatos(self):
        candidatos = self.__controlador_urna.exibir_candidatos()
        self.__tela_candidato.listar_candidatos(candidatos)


    def mostrar_candidato(self, codigo):
        for candidato in self.__controlador_urna.exibir_candidatos():
            if candidato.codigo == codigo:
                return candidato

    def listas_candidatos(self, categoria):
        #retorna a lista referente a chave fornecida;
        #a lista retornada eh passada para a funcao 'adiciona voto', onde e verificado se
        #o numero do voto corresponde ao numero de algum candidato da categoria especificada
        categorias = {
            "reitoria": self.__candidatos_reitor, "prograd": self.__candidatos_prograd,
            "propes": self.__candidatos_propes, "proex": self.__candidatos_proex
            }
        return categorias[categoria]