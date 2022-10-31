from urna import Urna
from telaurna import TelaUrna
from controladorvoto import ControladorVoto

class ControladorUrna:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_urna = TelaUrna()
        self.__urna = Urna()
        self.__controlador_voto = ControladorVoto


    #def incluir_eleitor(self, Eleitor):
    #    self.__urna.__eleitores = Eleitor


    #def incluir_candidato(self, Candidato):
    #    self.__urna.__candidatos = Candidato


    #def incluir_voto(self, Voto):
    #    self.__urna.__votos = Voto


    #def excluir_candidato(self, candidato):
    #    pass


    def exibir_candidatos(self):
        self.__urna.candidatos()


    def exibir_votos_categorias(self):
        votos = self.__controlador_voto.lista_votos
        candidatos = self.__urna.candidatos
        resultados = []
        for candidato in candidatos:
            votos_aluno = 0
            votos_professor = 0
            votos_tecnico = 0
            for voto in votos:
                if voto.candidato_escolhido == candidato.nome:
                    if voto.tipo_eleitor == 'aluno':
                        votos_aluno += 1
                    elif voto.tipo_eleitor == 'professor':
                        votos_professore += 1
                    elif voto.tipo_eleitor == 'tecnico':
                        votos_tecnico += 1
            resultado = [candidato.nome, candidato.cargo, votos_aluno, votos_professor, votos_tecnico]
            resultados.append(resultado)
        self.__tela_urna.exibe_votos_categorias(resultados)


    def calcular_resultado_final(self):
        #cria os dicionários para os resultados finais
        votos = self.__controlador_voto.lista_votos
        candidatos = self.__urna.candidatos
        resultado_final_reitor = {}
        resultado_final_prograd = {}
        resultado_final_propes = {}
        resultado_final_proex = {}
        for candidato in candidatos:
            #zera os contadores de voto para cada candidato
            votos_aluno_reitor = 0
            votos_professores_reitor = 0
            votos_tecnicos_reitor = 0
            votos_aluno_prograd = 0
            votos_professores_prograd = 0
            votos_tecnicos_prograd = 0
            votos_aluno_propes = 0
            votos_professores_propes = 0
            votos_tecnicos_propes = 0
            votos_aluno_proex = 0
            votos_professores_proex = 0
            votos_tecnicos_proex = 0
            for voto in votos:
                if voto.candidato_escolhido == candidato.nome:
                    if voto.tipo_eleitor == 'aluno':
                        votos_aluno_reitor += 1
                    elif voto.tipo_eleitor == 'professor':
                        votos_professores_reitor += 1
                    elif voto.tipo_eleitor == 'tecnico':
                        votos_tecnicos_reitor += 1
            if candidato.cargo == 'reitor':
                porcentagem = ((votos_aluno_reitor / 40000) * (1 / 3)) + (
                            (votos_professores_reitor / 2500) * (1 / 3)) + (
                                          (votos_tecnicos_reitor / 3100) * (
                                              1 / 3))
                resultado_final_reitor[candidato.nome] = porcentagem
            elif candidato.cargo == 'prograd':
                porcentagem = ((votos_aluno_prograd / 40000) * (1 / 3)) + (
                            (votos_professores_prograd / 2500) * (1 / 3)) + (
                                          (votos_tecnicos_prograd / 3100) * (
                                              1 / 3))
                resultado_final_prograd[candidato.nome] = porcentagem
            elif candidato.cargo == 'propes':
                porcentagem = ((votos_aluno_propes / 40000) * (1 / 3)) + (
                            (votos_professores_propes / 2500) * (1 / 3)) + (
                                          (votos_tecnicos_propes / 3100) * (
                                              1 / 3))
                resultado_final_propes[candidato.nome] = porcentagem
            elif candidato.cargo == 'proex':
                porcentagem = ((votos_aluno_proex / 40000) * (1 / 3)) + (
                            (votos_professores_proex / 2500) * (1 / 3)) + (
                                          (votos_tecnicos_proex / 3100) * (
                                              1 / 3))
                resultado_final_proex[candidato.nome] = porcentagem
        self.__tela_urna.exibe_resultado(resultado_final_reitor,
                                         resultado_final_prograd,
                                         resultado_final_propes,
                                         resultado_final_proex)


    def escolher_turno(self):
        turno = self.__tela_urna.escolha_turno()
        self.__urna.turno(turno)