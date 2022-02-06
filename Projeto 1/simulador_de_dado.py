# simulador de dado de 6 lados - simular o uso de um dados, gerando um valor de 1 até 6
import random
import pysimplegui


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
        # layout
        layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]
        # criar uma janela
        janela = sg.Window('Simulador de Dado (6 lados)', layout=layout)
        # ler os valores da tela
        self.eventos, self.valores = janela.Read()
        # fazer algo com os valores

    def Iniciar(self):
        try:
            resposta = input(self.mensagem)
            if resposta == 'sim':
                self.GerarValorDoDado()
            if resposta == 'não':
                print('Agradecemos a sua participação')
            else:
                print('favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()
