from entidades.candidato import Candidato
from telas.telacandidato import TelaCandidato
from entidades.urna import Urna

class ControladorCandidato:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__candidatos_reitor = []
        self.__candidatos_prograd = []
        self.__candidatos_propes = []
        self.__candidatos_proex = []
        self.__tela_candidato = TelaCandidato()
        self.__urna = Urna
        self.__controlador_urna = self.__controlador_principal.controlador_urna

    def mostra_tela_candidato(self):
        opcoes = {0: self.voltar,
                  1: self.adicionar_candidato,
                  2: self.remover_candidato,
                  3: self.listar_candidatos,
                  4: self.mudar_candidato}
        opcao = 1
        while opcao != 0:
            opcao = (self.__tela_candidato.mostrar_tela())
            opcoes[opcao]()

    def adicionar_candidato(self):
        values = self.__tela_candidato.adicionar_candidato()
        nome = values['nome']
        cpf = values['cpf']
        chapa = values['chapa']
        cargo = ''
        for value in range(1, 4):
            if values[f'{value}'] == True:
                if value == 1:
                    cargo = 'proex'
                elif value == 2:
                    cargo = 'prograd'
                elif value == 3:
                    cargo = 'reitor'
                else:
                    cargo = 'propes'
        candidato = Candidato(cpf, chapa, nome, cargo)
        self.__controlador_urna.urna.add_candidatos(candidato)



    def mudar_candidato(self):
        values = self.__tela_candidato.adicionar_candidato()
        nome = values['nome']
        cpf = values['cpf']
        chapa = values['chapa']
        cargo = ''
        for value in range(1, 4):
            if values[f'{value}'] == True:
                if value == 1:
                    cargo = 'proex'
                elif value == 2:
                    cargo = 'prograd'
                elif value == 3:
                    cargo = 'reitor'
                else:
                    cargo = 'propes'
        try:
            self.mostrar_candidato(cpf).__chapa = chapa
            self.mostrar_candidato(cpf).__nome = nome
            self.mostrar_candidato(cpf).__cargo = cargo
        except Exception:
            pass

    def remover_candidato(self):
        values = self.__tela_candidato.adicionar_candidato()
        cpf = values['cpf']
        candidato = self.mostrar_candidato(cpf)
        try:
            self.__controlador_urna.urna.remover_candidatos(candidato)
        except ValueError:
            '''candidato nao existe'''
            pass

    def listar_candidatos(self):
        candidatos = self.__controlador_urna.exibir_candidatos
        self.__tela_candidato.listar_candidatos(candidatos)


    def mostrar_candidato(self, codigo):
        for candidato in self.__controlador_urna.exibir_candidatos:
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

    def voltar(self):
        return
