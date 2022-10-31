class TelaUrna:

    def __init__(self):
        pass


    def escolha_turno(self):
        print("""1 - primeiro turno
        2 - segundo turno""")
        return input('Escolha o turno atual da eleição:')


    def exibe_resultado(self, resultado_reitor, resultado_pr_grad, resultado_pr_pesq, resultado_pr_ext):
        print('Resultados - reitor')
        print(resultado_reitor)
        print('*'*20)
        print('Resultados - prograd')
        print(resultado_reitor)
        print('*' * 20)
        print('Resultados - propesq')
        print(resultado_reitor)
        print('*' * 20)
        print('Resultados - proext')
        print(resultado_reitor)
        print('*' * 20)

        [candidato.nome, candidato.cargo, votos_aluno, votos_professor, votos_tecnico]
    def exibe_votos_categorias(self, resultados):
        for resultado in resultados:
            print('*' * 20)
            print(f'O candidato {resultado[0]} recebeu os seguintes votos para o cargo {resultado[1]}:')
            print(f'votos de alunos: {resultado[2]}')
            print(f'votos de professores: {resultado[3]}')
            print(f'votos de tecnicos: {resultado[4]}')
            print('*'*20)