from telas.abstracttela import AbstractTela

class TelaInicial(AbstractTela):

    def __init__(self):
        super().__init__()

    #a opcao deve ser um numero entre 0 e 4
    def le_inteiro(self, msg: str = "",):
        while True:
            numero = input(msg)
            try:
                if int(numero) not in [0, 1, 2, 3, 4]:
                    raise ValueError
                return numero
            except ValueError:
                print("Entrada Invalida")
                
    def tela_opcoes(self):
        print("*"*20)
        print("Urna Eletronica")
        print("1 - Iniciar Voto")
        print("2 - Cadastro de Candidato")
        print("3 - Resultados")
        print("4 - Configurar Urna")
        print("0 - Sair")
        opcao = self.le_inteiro("Digite a Opcao: ")
        print("*"*20)
        return int(opcao)

    def erro_configuracao(self):
        print("A urna nao foi configurada")

    def votacao_encerrada(self):
        print("votacao Encerrada")