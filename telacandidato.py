import controladorcandidato
from controladorcandidato import mostrar_candidato, listar_candidatos as lc, ControladorCandidato


class TelaCandidato:

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
            if option.lower in ('a', 'b', 'c', 'd', 'e'):
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
        confirm = input(f'Digite SIM para remover o candidato {mostrar_candidato(codigo_candidato_removido).nome}:')
        if confirm == 'SIM':
            return codigo_candidato_removido
        else:
            return ('Nenhum candidato foi removido')


    def listar_candidatos(self):
        candidatos = lc()
        for candidato in candidatos:
            print(f'Candidato: {candidato.nome} - Código: {candidato.codigo}')
        pass


    def alterar_candidato(self):
        while True:
            a = input('Digite o código do candidato a ser excluído: ')
            confirm = input(f'Esse é o candidato que deseja alterar? {mostrar_candidato(a).nome} Digite SIM para confirmar: ')
            while True:
                if confirm == 'SIM':
                    print("""
                    a = codigo
                    b = chapa
                    c = nome
                    d = cargo
                    """)
                    resposta = input('Qual dado gostaria de alterar? ')
                    if resposta.lower in ('a', 'b', 'c', 'd'):
                        if resposta == 'a':
                            mostrar_candidato(a).codigo = input('Digite o novo código: ')
                        elif resposta == 'b':
                            mostrar_candidato(a).chapa = input('Digite a nova chapa: ')
                        elif resposta == 'c':
                            mostrar_candidato(a).nome = input('Digite o novo nome: ')
                        elif resposta == 'd':
                            mostrar_candidato(a).cargo = input('Digite o novo cargo: ')
                    else:
                        print('Digite uma opção válida.')



#    def validar_dados():
#       pass

