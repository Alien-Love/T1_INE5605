import PySimpleGUI as sg
from telas.abstracttela import AbstractTela

class TelaInicial(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__window = None
#        self.init_components()

    #a opcao deve ser um numero entre 0 e 4
    def le_inteiro(self, msg: str = "",):
        while True:
            numero = input(msg)
            try:
                if int(numero) not in [0, 1, 2, 3, 4, 5]:
                    raise ValueError
                return numero
            except ValueError:
                print("Entrada Invalida")
                
    def tela_opcoes(self):
        self.init_components()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def erro_configuracao(self):
        print("A urna nao foi configurada")

    def votacao_encerrada(self):
        print("votacao Encerrada")

    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel("DarkAmber")
        layout = [
            [sg.Text('Urna Eletrônica - 2022', font=("Helvica",25))],
            [sg.Text('Escolha sua opção', font=("Helvica",15))],
            [sg.Radio('Votar',"RD1", key='1')],
            [sg.Radio('Cadastro de Candidato',"RD1", key='2')],
            [sg.Radio('Cadastro de Eleitor',"RD1", key='3')],
            [sg.Radio('Resultados',"RD1", key='4')],
            [sg.Radio('Configurar Urna', "RD1", key='5')],
            [sg.Radio('Sair', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('URNA ELETRÔNICA').Layout(layout)