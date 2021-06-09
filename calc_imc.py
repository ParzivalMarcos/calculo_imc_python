""" Gera um objeto contendo os dados de IMC """
class CalculaIMC():
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura
        self.imc = self.calculo_imc()
        self.status_peso = self.status_peso()

    def calculo_imc(self):
        return round((self.peso) / ((self.altura/100)**2), 2)

    def status_peso(self):
        if self.imc < 18.5:
            return 0
        elif self.imc >= 18.5 and self.imc < 25:
            return 1
        elif self.imc >= 25 and self.imc < 30:
            return 2
        elif self.imc >= 30 and self.imc < 35:
            return 3
        elif self.imc >= 35 and self.imc < 40:
            return 4
        elif self.imc >= 40:
            return 5
