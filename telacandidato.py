#import controladorcandidato
from abstracttela import AbstractTela

class TelaCandidato(AbstractTela):

    def __init__(self):
        super().__init__()

    def le_inteiro(self, valor):
        return super().le_inteiro(valor)

    def mostrar_tela(self):
        while True:
            print("""
            a = adicionar novo candidato
            b = remover um candidato já cadastrado
            c = listar todos os candidatos
            d = validar dados
            e = alterar candidato existente
            """)
            option = input('digite a opção desejada: ')
            if option in ['a', 'b', 'c', 'd', 'e']:
                return option
            else:
                print('Digite uma opção válida.')


    def adicionar_candidato(self):
        nome_candidato = input('Digite o nome do novo candidato: ')
        codigo_candidato = input(f'Digite o código do candidato {nome_candidato}: ')
        chapa_candidato = input(f'Digite a chapa do candidato {nome_candidato}: ')
        cargo_candidato = input(f'digite o cargo do candidato {nome_candidato}: ')
        return (codigo_candidato, chapa_candidato, nome_candidato, cargo_candidato)


    def remover_candidato(self):
        codigo_candidato_removido = input('Digite o codigo do candidato a ser removido: ')
        return codigo_candidato_removido


    def listar_candidatos(self, candidatos):
        for candidato in candidatos:
            print(f'Candidato: {candidato.nome} - Cargo: {candidato.cargo}')
        pass


    def alterar_candidato(self):
        while True:
            a = input('Digite o código do candidato a ser alterado: ')
            confirm = input(f'Esse é o código do candidato que deseja alterar? {a} Digite SIM para confirmar: ')
            while True:
                if confirm == 'SIM':
                    print("""
                    a = codigo
                    b = chapa
                    c = nome
                    d = cargo
                    """)
                    resposta = input('Qual dado gostaria de alterar? ')
                    if resposta in ['a', 'b', 'c', 'd']:
                        if resposta == 'a':
                            return(a, 'a', input('Digite o novo código: '))
                        elif resposta == 'b':
                            return(a, 'b', input('Digite a nova chapa: '))
                        elif resposta == 'c':
                            return(a, 'c', input('Digite o novo nome: '))
                        elif resposta == 'd':
                            return(a, 'd', input('Digite o novo cargo: '))
                    else:
                        print('Digite uma opção válida.')


    def validar_dados(self):
       pass