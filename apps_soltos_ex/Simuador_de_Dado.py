#Simulador de dado
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Você gostaria de gerar um novo valor para o dado?"

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == "sim" or resposta == "s":
                self.GerarValorDoDado()
            elif resposta == "não" or resposta == "n":
                print("Agradecemos sua participação")
            else:
                print("Por favor, digite sim ou não")
        except:
            print("Ocorreu um erro ao receber sua resposta")

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

