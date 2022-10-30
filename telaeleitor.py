from abstracttela import AbstractTela

class TelaEleitor(AbstractTela):
    def __init__(self):
        super().__init__()
    #nome deve ser uma string de 3 ou mais caracteres
    #cpf deve ser um inteiro de 11 digitos
    #tipo sera um inteiro de 1 a 3: {1: 'aluno', 2: 'professor', 3: 'tecnico administrativo'}
    def le_inteiro(self):
        return super().le_inteiro()

    def cadastro_eleitor(self):
       a = input("nome do eleitor:")
       b = input("cpf:")
       c = input("tipo:")
       dados = a, b, c
       return dados