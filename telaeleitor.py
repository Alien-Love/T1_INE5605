class TelaEleitor:
    #nome deve ser uma string de 3 ou mais caracteres
    #cpf deve ser um inteiro de 11 digitos
    #tipo sera um inteiro de 1 a 3: {1: 'aluno', 2: 'professor', 3: 'tecnico administrativo'}
    def cadastro_eleitor(self):
       a = input("nome do eleitor:")
       b = input("cpf:")
       c = input("tipo:")
       dados = a, b, c
       return dados