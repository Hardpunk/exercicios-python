from funcionario import Funcionario

class Gerente(Funcionario):

    def __init__(self, ctps, nome, qthoras, vlhora, adicional):
        super().__init__(ctps, nome, qthoras, vlhora)
        self.adicional = adicional

    def calc_salario(self):
        return self.qthoras * self.vlhora * (1 + self.adicional / 100)

    def obter_adicional_porcentagem(self):
        return str(self.adicional) + "%"