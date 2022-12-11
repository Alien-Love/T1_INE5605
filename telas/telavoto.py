from telas.abstracttela import AbstractTela

class TelaVoto(AbstractTela):

    def __init__(self):
        super().__init__()

    def le_inteiro(self, cargo: str = ""):
        while True:
            numero = input(cargo)
            try:
                nmro = int(numero)
                print("voto:", nmro)
                return int(nmro)
            except ValueError:
                nmro = 00
                return nmro

    def pega_cpf_eleitor(self):
        cpf = input("Informe seu CPF:")
        return int(cpf)

    def voto_reitor(self):
        print("Digite Seu Voto")
        numero = self.le_inteiro("reitoria: ")
        return numero

    def voto_proreitor_grad(self):
        numero = self.le_inteiro("Pro-Reitoria de Graduação: ")
        return numero

    def voto_proreitor_pes(self):
        numero = self.le_inteiro("Pro-Reitoria de Pesquisa e Inovacao: ")
        return numero
    
    def voto_proreitor_ext(self):
        numero = self.le_inteiro("Pro-Reitoria de Extensão: ")
        return numero
    
    def categoria_vazia(self):
        print("Categoria nao possui candidatos!")

