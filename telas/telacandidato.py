from telas.abstracttela import AbstractTela

class TelaCandidato(AbstractTela):

    def __init__(self):
        super().__init__()

    def le_inteiro(self, valor):
        return super().le_inteiro(valor)

    def mostrar_tela(self):
        opcoes = ('1', '2', '3', '4', '5', '0')
        print('*'*20)
        print("""
1 = adicionar novo candidato
2 = remover um candidato já cadastrado
3 = listar todos os candidatos
4 = validar dados
5 = alterar candidato existente
0 = sair
        """)
        option = input('digite a opção desejada: ')
        print('*' * 20)
        while option not in opcoes:
            print('*' * 20)
            option = input('Digite uma opção válida')
            print('*' * 20)
        return int(option)


    def adicionar_candidato(self):
        nome_candidato = input('Digite o nome do novo candidato: ')
        codigo_candidato = input(f'Digite o código do candidato {nome_candidato}: ')
        chapa_candidato = input(f'Digite a chapa do candidato {nome_candidato}: ')
        cargo_candidato = input(f'digite o cargo do candidato {nome_candidato}(reitor, prograd, propes, proex): ')
        return (codigo_candidato, chapa_candidato, nome_candidato, cargo_candidato)


    def remover_candidato(self):
        while True:
            codigo_candidato_removido = input('Digite o codigo do candidato a ser removido: ')
            confirmacao = input(f'Digite CONFIRMA para excluir o candidato de código {codigo_candidato_removido}: ')
            if confirmacao == 'CONFIRMA':
                return codigo_candidato_removido


    def listar_candidatos(self, candidatos):
        info_candidatos = candidatos
        for candidato in info_candidatos:
            print(f'Candidato: {candidato.nome} - Cargo: {candidato.cargo}')
        pass


    def alterar_candidato(self):
        print('*' * 20)
        while True:
            codigo = input('Digite o código do candidato a ser alterado: ')
            confirm = input(f'Esse é o código do candidato que deseja alterar? {a} Digite SIM para confirmar: ')
            if confirm == 'SIM':
                print("""
                    1 = codigo
                    2 = chapa
                    3 = nome
                    4 = cargo
                    """)
                resposta = int(input('Qual dado gostaria de alterar? '))
                if resposta in (1, 2, 3, 4):
                    if resposta == 1:
                        info = (codigo, 1, input('Digite o novo código: '))
                        return info
                    elif resposta == 2:
                        info = (codigo, 2, input('Digite a nova chapa: '))
                        return info
                    elif resposta == 3:
                        info = (codigo, 3, input('Digite o novo nome: '))
                        return info
                    elif resposta == 4:
                        info = (codigo, 4, input('Digite o novo cargo: '))
                        return info
                else:
                    print('Digite uma opção válida.')


    def validar_dados(self):
       pass