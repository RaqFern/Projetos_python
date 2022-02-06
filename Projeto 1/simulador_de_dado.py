# simulador de dado de 6 lados - simular o uso de um dados, gerando um valor de 1 até 6
import random


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'

    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == 'sim':
            self.GerarValorDoDado()
        if resposta == 'não':
            print('Agradecemos a sua participação')
        else:
            print('favor digitar sim ou não')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()
