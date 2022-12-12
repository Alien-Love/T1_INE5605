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
                print(value)
                self.close()
                return value

    def adicionar_candidato(self):
        self.adicionar_candidatos()
        button, values = self.__window.Read()
        self.close()
        return values



    def remover_candidato(self):
        self.adicionar_candidatos()
        button, values = self.__window.Read()
        self.close()
        return values


    def listar_candidatos(self, candidatos):
        self.listagem_de_candidatos(candidatos)


    def alterar_candidato(self):
        self.adicionar_candidatos()
        button,values = self.__window.Read()
        self.close()
        return values


    def validar_dados(self):
       pass


    def adicionar_candidatos(self):
        sg.ChangeLookAndFeel("DarkTeal9")
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
        sg.ChangeLookAndFeel("DarkTeal9")
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

    def listagem_de_candidatos(self, candidatos):
        sg.ChangeLookAndFeel("DarkTeal9")
        layout = [
            [sg.Text('Urna Eletrônica - 2022', font=("Helvica", 25))],
            [sg.Text('Lista de Candidatos Cadastrados', font=("Helvica", 15))],
            [[sg.Listbox(candidatos, size=(40, 3))]]
        ]
        self.__window = sg.Window('URNA ELETRÔNICA').Layout(layout)
        while True:
            event, values = self.__window.read()
            if event == sg.WINDOW_CLOSED:
                break
            print(event, values)
        self.close()

    def close(self):
        self.__window.Close()
