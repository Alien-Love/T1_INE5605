import PySimpleGUI as sg


class TelaUrna:

    def __init__(self):
        pass

    def exibe_resultado(self, resultado_reitor, resultado_pr_grad, resultado_pr_pesq, resultado_pr_ext):
        sg.ChangeLookAndFeel("DarkTeal9")
        layout = [
            [sg.Text('Urna Eletrônica - 2022', font=("Helvica", 25))],
            [sg.Text('Resultados das eleições', font=("Helvica", 15))],
            [sg.Text('Resultados Reitor:')],
            [sg.Text(f'{resultado_reitor}')],
            [sg.Text('Resultados prograd:')],
            [sg.Text(f'{resultado_pr_grad}')],
            [sg.Text('Resultados propesq:')],
            [sg.Text(f'{resultado_pr_pesq}')],
            [sg.Text('Resultados proext:')],
            [sg.Text(f'{resultado_pr_ext}')]
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

    def exibe_votos_categorias(self, resultados):
        for resultado in resultados:
            print('*' * 20)
            print(f'O candidato {resultado[0]} recebeu os seguintes votos para o cargo {resultado[1]}:')
            print(f'votos de alunos: {resultado[2]}')
            print(f'votos de professores: {resultado[3]}')
            print(f'votos de tecnicos: {resultado[4]}')
            print('*' * 20)
