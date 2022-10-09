class Candidato:
    __numero = 0
    __nome = ""
    __votos = 0

    def __init__(self, number, name):
        self.__numero = number
        self.__nome = name

    def get_numero(self):
        return self.__numero

    def set_numero(self, value):
        if value >= 0:
            self.__numero = value

    def get_nome(self):
        return self.__nome

    def set_nome(self, value):
        self.__nome = value

    def get_votos(self):
        return self.__votos
    
    def votar(self):
        self.__votos += 1

    def __str__(self):
        return "Candidato: " + self.__nome + "\nNúmero: " + self.__numero
