class Funcionario:
    def __init__(self, ctps, nome, qthoras, vlhora):
        self.ctps = ctps
        self.nome = nome
        self.qthoras = qthoras
        self.vlhora = vlhora

    def calc_salario(self):
        return self.qthoras * self.vlhora

    def obter_recibo(self):
        return "%s recebe R$ %.2f" % (self.nome, self.calc_salario())