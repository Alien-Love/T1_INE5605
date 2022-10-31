from abstracttela import AbstractTela

class TelaVoto(AbstractTela):

    def __init__(self):
        super().__init__()

    def le_inteiro(self):
        return super().le_inteiro()

    def voto_reitor(self):
        print("Digite Seu Voto")
        try:
            nmro = int(input("Reitoria: "))
            return nmro
        except ValueError:
            nmro = 00
            return nmro

    def voto_proreitor_grad(self):
        numero = input("Pro-Reitoria de Graduação: ")
        return numero

    def voto_proreitor_pes(self):
        numero = input("Pro-Reitoria de Pesquisa e Inovacao: ")
        return numero
    
    def voto_proreitor_ext(self):
        numero = input("Pro-Reitoria de Extensão: ")
        return numero
    
    def categoria_vazia(self):
        print("Categoria nao possui candidatos!")

