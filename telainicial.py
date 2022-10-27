class TelaInicial:

    def tela_opcoes(self):
        print("*"*20)
        print("Urna Eletronica")
        print("1 - Iniciar Voto")
        print("2 - Cadastro de Candidato")
        print("3 - Resultados")
        print("0 - Sair")
        opcao = input("digite a opcao:")
        print("*"*20)
        return int(opcao)