from telas.abstracttela import AbstractTela
import PySimpleGUI as sg

class TelaConfiguracao(AbstractTela):
    
    #as entradas deverao ser numeros inteiros
    #a quantidade de eleitores deve ser um inteiro positivo
    #a quantia de candidatos para o primeiro turno deve ser um inteiro positivo ate 99
    def __init__(self):
        super().__init__()
        self.__window = None
        self.init_components()

    def le_inteiro(self):
        return super().le_inteiro()

    def config_(self):
        self.init_components()
        button, values = self.__window.Read()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
        
    def close(self):
        self.__window.Close()

    def init_components(self):
        #sg.theme_previewer()
        sg.ChangeLookAndFeel("DarkAmber")
        layout = [
            [sg.Text('Configurações da Urna', font=("Helvica",25))],
            [sg.Text('Selecione o Turno', font=("Helvica",15))],
            [sg.Radio('1º Turno',"RD1", key='1')],
            [sg.Radio('2º Turno',"RD1", key='2')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('URNA ELETRÔNICA').Layout(layout)
    
    def dados_turno_1(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
        [sg.Text('Configurações - 1º Turno', font=("Helvica", 25))],
        [sg.Text('Total de Eleitores', size=(15, 1)), sg.Slider(range=(2, 99), default_value=2, orientation='h', key='slider_1')],
        [sg.Text('Total de Candidatos', size=(15, 1)), sg.Slider(range=(2, 99), default_value=2, orientation='h', key='slider_2')],   
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Configurações').Layout(layout)

        button, values = self.__window.Read()
        total_eleitores = values['slider_1']
        total_candidatos = values['slider_2']

        self.close()
        return {"total_eleitores": total_eleitores, "total_candidatos": total_candidatos}

    def dados_turno_2(self):
        sg.ChangeLookAndFeel('DarkAmber')
        layout = [
        [sg.Text('Configurações - 2º Turno', font=("Helvica", 25))],
        [sg.Text('Total de Eleitores', size=(15, 1)), sg.Slider(range=(2, 99), default_value=2, orientation='h', key='slider_1')],
        [sg.Text('Total de Candidatos', size=(15, 1)), sg.Slider(range=(2, 98), default_value=2, orientation='h', key='slider_2')],   
        [sg.Text('Categorias de candidatura', size=(15, 1))], 
        [sg.Text('Reitoria', size=(15, 1)), sg.Checkbox('Reitoria', key='cb_1')],
        [sg.Checkbox('Graduação', key='cb_2')],
        [sg.Text('Pró-Reitorias'), sg.Checkbox('Pesquisa', key='cb_3')],
        [sg.Checkbox('Reitoria', key='cb_4')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Configurações').Layout(layout)

        button, values = self.__window.Read()
        total_eleitores = values['slider_1']
        total_candidatos = values['slider_2']
        checkbox = [values['cb_1'], values['cb_2'], values['cb_3'], values['cb_4']]
        reitorias_list = ['reitoria', 'propes', 'prograd', 'proex']
        reitorias = []
        for reitoria in reitorias_list:
            if checkbox[reitorias_list.index(reitoria)] == True:
                reitorias.append(reitoria)
        self.close()
        return {"total_eleitores": total_eleitores, "total_candidatos": total_candidatos, "reitorias": reitorias}
