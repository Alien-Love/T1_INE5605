from abstracttela import AbstractTela

class TelaConfiguracao(AbstractTela):
    
    #as entradas deverao ser numeros inteiros
    #a quantidade de eleitores deve ser um inteiro positivo
    #a quantia de candidatos para o primeiro turno deve ser um inteiro positivo ate 99
    def __init__(self):
        super().__init__()

    def le_inteiro(self):
        return super().le_inteiro()

    def config_(self):

        a = int(input("Selecione o Turno:"))
        
        if a == 1:
            b = int(input("quantidade de eleitores:"))
            c = int(input("quantidade de candidatos:"))
            dados = a, b, c
            return dados

        elif a == 2:
            b = int(input("quantidade de eleitores:"))
            c = 2
            print("-"*20)
            print("Categorias de Candidatos:")
            print("1 - Reitoria")
            print("2 - Pro-Reitoria de Graduacao")
            print("3 - Pro-Reitoria de Pesquisa e Extensao")
            print("4 - Pro-Reitoria de Extensao")
            print("")
            d = [int(cargo) for cargo in input("Digite as categorias participantes:").split(" ")]
            #tratar input em d(limpar valores repetidos e raise exception em valores fora dos limites)

            dados = a, b, c, d
            return dados

        else:
            print("turno errado")
        