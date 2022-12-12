from telas.abstracttela import AbstractTela
import PySimpleGUI as sg

class TelaVoto(AbstractTela):

    def __init__(self):
        super().__init__()
        self.__window = None

    def le_inteiro(self, numero):
        while True:
            try:
                nmro = int(numero)
                return int(nmro)
            except ValueError:
                nmro = 00
                return nmro

    def pega_cpf_eleitor(self):
        sg.ChangeLookAndFeel('DarkTeal9')
        layout = [
        [sg.Text('Eleitor, informe seu CPF', font=("Helvica", 25))],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Votação em Andamento').Layout(layout)
        button, values = self.__window.Read()
        cpf = values['cpf']
        self.close()
        return int(cpf)

    def voto_reitor(self):
        sg.ChangeLookAndFeel('DarkTeal9')
        layout = [
        [sg.Text('Digite Seu Voto', font=("Helvica", 25))],
        [sg.Text('Cargo: Reitoria', font=("helvica", 20))],
        [sg.Text('Voto', size=15), sg.InputText('', key='voto')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Votação em Andamento').Layout(layout)
        button, values = self.__window.Read()
        voto = values['voto']
        numero = self.le_inteiro(voto)
        self.close()        
        return numero

    def voto_proreitor_grad(self):
        sg.ChangeLookAndFeel('DarkTeal9')
        layout = [
        [sg.Text('Digite Seu Voto', font=("Helvica", 25))],
        [sg.Text('Cargo: Pro-Reitoria de Graduação', font=("helvica", 20))],
        [sg.Text('Voto', size=15), sg.InputText('', key='voto')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Votação em Andamento').Layout(layout)
        button, values = self.__window.Read()
        voto = values['voto']
        numero = self.le_inteiro(voto)
        self.close()
        return numero


    def voto_proreitor_pes(self):
        sg.ChangeLookAndFeel('DarkTeal9')
        layout = [
        [sg.Text('Digite Seu Voto', font=("Helvica", 25))],
        [sg.Text('Cargo: Pro-Reitoria de Pesquisa', font=("helvica", 20))],
        [sg.Text('Voto', size=15), sg.InputText('', key='voto')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Votação em Andamento').Layout(layout)
        button, values = self.__window.Read()
        voto = values['voto']
        numero = self.le_inteiro(voto)
        self.close()
        return numero
    
    def voto_proreitor_ext(self):
        sg.ChangeLookAndFeel('DarkTeal9')
        layout = [
        [sg.Text('Digite Seu Voto', font=("Helvica", 25))],
        [sg.Text('Cargo: Pro-Reitoria de Extensão', font=("helvica", 20))],
        [sg.Text('Voto', size=15), sg.InputText('', key='voto')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Votação em Andamento').Layout(layout)
        button, values = self.__window.Read()
        voto = values['voto']
        numero = self.le_inteiro(voto)
        self.close()
        return numero

    def categoria_vazia(self):
        print("Categoria nao possui candidatos!")

    def close(self):
        self.__window.Close()
