from entidades.urna import Urna
from telas.telaurna import TelaUrna
from controladores.controladorvoto import ControladorVoto

class ControladorUrna:

    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_urna = TelaUrna()
        self.__urna = Urna()
        self.__controlador_voto = controlador_principal.controlador_voto

    @property
    def urna(self):
        return self.__urna

    @property
    def exibir_candidatos(self):
        return self.__urna.candidatos


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
                        votos_professor += 1
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
        aluno_reitor = 0
        professor_reitor = 0
        tecnico_reitor = 0
        aluno_prograd = 0
        professor_prograd = 0
        tecnico_prograd = 0
        aluno_propes = 0
        professor_propes = 0
        tecnico_propes = 0
        aluno_proex = 0
        professor_proex = 0
        tecnico_proex = 0
        for voto in votos:
            if voto.tipo_eleitor == 'aluno' and voto.cargo_voto == 'reitor':
                aluno_reitor += 1
            elif voto.tipo_eleitor == 'professor' and voto.cargo_voto == 'reitor':
                professor_reitor += 1
            elif voto.tipo_eleitor == 'tecnico' and voto.cargo_voto == 'reitor':
                tecnico_reitor += 1
            elif voto.tipo_eleitor == 'aluno' and voto.cargo_voto == 'prograd':
                aluno_prograd += 1
            elif voto.tipo_eleitor == 'professor' and voto.cargo_voto == 'prograd':
                professor_prograd += 1
            elif voto.tipo_eleitor == 'tecnico' and voto.cargo_voto == 'prograd':
                tecnico_prograd += 1
            elif voto.tipo_eleitor == 'aluno' and voto.cargo_voto == 'propes':
                aluno_propes += 1
            elif voto.tipo_eleitor == 'professor' and voto.cargo_voto == 'propes':
                professor_propes += 1
            elif voto.tipo_eleitor == 'tecnico' and voto.cargo_voto == 'propes':
                tecnico_propes += 1
            elif voto.tipo_eleitor == 'aluno' and voto.cargo_voto == 'proex':
                aluno_proex += 1
            elif voto.tipo_eleitor == 'professor' and voto.cargo_voto == 'proex':
                professor_proex += 1
            elif voto.tipo_eleitor == 'tecnico' and voto.cargo_voto == 'proex':
                tecnico_proex += 1
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
                porcentagem = ((votos_aluno_reitor / aluno_reitor) * (1 / 3)) + (
                            (votos_professores_reitor / professor_reitor) * (1 / 3)) + (
                                          (votos_tecnicos_reitor / tecnico_reitor) * (
                                              1 / 3))
                resultado_final_reitor[candidato.nome] = porcentagem
            elif candidato.cargo == 'prograd':
                porcentagem = ((votos_aluno_prograd / aluno_prograd) * (1 / 3)) + (
                            (votos_professores_prograd / professor_prograd) * (1 / 3)) + (
                                          (votos_tecnicos_prograd / tecnico_prograd) * (
                                              1 / 3))
                resultado_final_prograd[candidato.nome] = porcentagem
            elif candidato.cargo == 'propes':
                porcentagem = ((votos_aluno_propes / aluno_propes) * (1 / 3)) + (
                            (votos_professores_propes / professor_propes) * (1 / 3)) + (
                                          (votos_tecnicos_propes / tecnico_propes) * (
                                              1 / 3))
                resultado_final_propes[candidato.nome] = porcentagem
            elif candidato.cargo == 'proex':
                porcentagem = ((votos_aluno_proex / aluno_proex) * (1 / 3)) + (
                            (votos_professores_proex / professor_proex) * (1 / 3)) + (
                                          (votos_tecnicos_proex / tecnico_proex) * (
                                              1 / 3))
                resultado_final_proex[candidato.nome] = porcentagem
        self.__tela_urna.exibe_resultado(resultado_final_reitor,
                                         resultado_final_prograd,
                                         resultado_final_propes,
                                         resultado_final_proex)

    def exibir_turno(self):
        return self.__controlador_principal.controlador_configuracao.configuracao.turno