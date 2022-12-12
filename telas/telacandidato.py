from telas.abstracttela import AbstractTela
import PySimpleGUI as sg

class TelaCandidato(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__window = None
        self.init_components()
        self.adicionar_candidatos()

    def le_inteiro(self, valor):
        return super().le_inteiro(valor)

    def mostrar_tela(self):
        self.init_components()
        button, values = self.__window.Read()
        for value in range(0, 5):
            if values[f'{value}'] == True:
                return value

    def adicionar_candidato(self):
        self.adicionar_candidatos()
        button, values = self.__window.Read()
        self.close()
        return values



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

    def adicionar_candidatos(self):
        sg.ChangeLookAndFeel("DarkAmber")
        layout = [
            [sg.Text('Candidatos - 2022', font=("Helvica", 25))],
            [sg.Text('Dados do candidato', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
            [sg.Text('Chapa:', size=(15, 1)), sg.InputText('', key='chapa')],
            [sg.Radio('Proex','RD1', key='1'), sg.Radio('Prograd', 'RD1', key='2'), sg.Radio('Reitor', 'RD1', key='3'), sg.Radio('Propes', 'RD1', key='4')],
            [sg.Radio('Sair', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('URNA ELETRÔNICA').Layout(layout)

    def init_components(self):
        sg.ChangeLookAndFeel("DarkAmber")
        layout = [
            [sg.Text('Urna Eletrônica - 2022', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Adicionar novo candidato', "RD1", key='1')],
            [sg.Radio('Remover um Candidato', "RD1", key='2')],
            [sg.Radio('Listar todos os candidatos', "RD1", key='3')],
            [sg.Radio('Alterar candidato existente', "RD1", key='4')],
            [sg.Radio('Sair', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('URNA ELETRÔNICA').Layout(layout)

    def close(self):
        self.__window.Close()
