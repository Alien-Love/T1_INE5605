from entidades.candidato import Candidato
from telas.telacandidato import TelaCandidato
from entidades.urna import Urna

class ControladorCandidato:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__candidatos_reitor = [Candidato(32, "b", "c", "d")]
        self.__candidatos_prograd = []
        self.__candidatos_propes = []
        self.__candidatos_proex = []
        self.__tela_candidato = TelaCandidato()
        self.__urna = Urna
        self.__controlador_urna = self.__controlador_principal.controlador_urna

    def mostra_tela_candidato(self):
        opcoes = {0: self.voltar, 1: self.adicionar_candidato,
                  2: self.remover_candidato, 3: self.listar_candidatos,
                  4: self.__tela_candidato.validar_dados,
                  5: self.mudar_candidato}

        while True:
            opcao = (self.__tela_candidato.mostrar_tela())
            opcoes[opcao]()

    def adicionar_candidato(self):
        info = self.__tela_candidato.adicionar_candidato()
        candidato = Candidato(info[0], info[1], info[2], info[3])
        self.__controlador_urna.urna.add_candidatos(candidato)
        # Adiciona candidato com as informações recebidas na tela de adicionar
        # candidato.


    def mudar_candidato(self):
        try:
            info = self.__tela_candidato.alterar_candidato()
            codigo = info[0]
            opcao = info[1]
            novo_valor = info[2]
            if opcao == '1':
                self.mostrar_candidato(codigo).__codigo = novo_valor
            elif opcao == '2':
                self.mostrar_candidato(codigo).__chapa = novo_valor
            elif opcao == '3':
                self.mostrar_candidato(codigo).__nome = novo_valor
            elif opcao == '4':
                self.mostrar_candidato(codigo).__cargo = novo_valor
        except Exception:
            pass
            # setter de diferentes atributos baseado na opção escolhida no menu de
            # alteração de candidato.


    def remover_candidato(self):
    # remove o candidato escolhido na tela de exclusão de candidatos.
        codigo_do_candidato = self.__tela_candidato.remover_candidato()
        candidato = self.mostrar_candidato(codigo_do_candidato)
        try:
            self.__controlador_urna.urna.remover_candidatos(candidato)
        except ValueError:
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
        pass
