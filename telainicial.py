from abstracttela import AbstractTela

class TelaInicial(AbstractTela):

    def __init__(self):
        super().__init__()
    #a opcao deve ser um numero entre 0 e 4
    def le_inteiro(self):
        return super().le_inteiro()

    def tela_opcoes(self):
        print("*"*20)
        print("Urna Eletronica")
        print("1 - Iniciar Voto")
        print("2 - Cadastro de Candidato")
        print("3 - Resultados")
        print("4 - Configurar Urna")
        print("0 - Sair")
        opcao = input("digite a opcao: ")
        print("*"*20)
        return int(opcao)