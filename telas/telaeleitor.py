from telas.abstracttela import AbstractTela
import PySimpleGUI as sg
from entidades.configuracaoexception import CpfInvalidoException

class TelaEleitor(AbstractTela):
    def __init__(self):
        super().__init__()
        self.__window = None

    def le_inteiro(self):
        return super().le_inteiro()

    def cadastro_eleitor(self):
        self.recebe_dados_eleitor()
        button, values = self.__window.Read()
        nome = values['nome']
        cpf = values['cpf']
        if values['1']:
            categoria = "aluno"
        if values['2']:
            categoria = "professor"
        if values['3']:
            categoria = "tecnico"
        if button in (None, 'Cancelar'):
            self.close()
            return 0
        try:
            if isinstance(cpf, int) == False:
                raise CpfInvalidoException
            self.close()
            return {"nome": nome, "cpf": cpf, "categoria": categoria}
        except CpfInvalidoException:
            self.close()
            return 1
        
    def recebe_dados_eleitor(self):
        sg.ChangeLookAndFeel('DarkTeal9')
        layout = [
        [sg.Text('Eleitor, informe seus dados', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('CPF:', size=(15, 1)), sg.InputText('', key='cpf')],
        [sg.Text('Categoria', size=(15, 1), justification='center')],
        [sg.Radio('Aluno','RD1', key='1', default=True), sg.Radio('Professor', 'RD1', key='2'),
        sg.Radio('Tecnico Administrativo', 'RD1', key='3')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Cadastro de Eleitor').Layout(layout)

    def cpf_invalido(self):
        sg.Popup("DIGITE UM CPF VALIDO")

    def close(self):
        self.__window.Close()
