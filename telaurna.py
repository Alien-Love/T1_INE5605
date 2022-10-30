

class Urna:

    def __init__(self):
        pass


    def escolha_turno(self):
        print("""1 - primeiro turno
        2 - segundo turno""")
        return input('Escolha o turno atual da eleição:')


    def exibe_resultado(self, resultado_reitor, resultado_pr_grad, resultado_pr_pesq, resultado_pr_ext):
        print(f"O candidato {resultado_reitor[0]} ganhou para {resultado_reitor[1]} com {resultado_reitor[2]} votos")
        print(f"O candidato {resultado_pr_grad[0]} ganhou para {resultado_pr_grad[1]} com {resultado_pr_grad[2]} votos")
        print(f"O candidato {resultado_pr_pesq[0]} ganhou para {resultado_pr_pesq[1]} com {resultado_pr_pesq[2]} votos")
        print(f"O candidato {resultado_pr_ext[0]} ganhou para {resultado_pr_ext[1]} com {resultado_pr_ext[2]} votos")