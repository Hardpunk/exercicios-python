from tabulate import tabulate


class UrnaVotacao():
    __tipo = ""
    __lista = []
    __max = 0
    __qtd = 0

    def __init__(self, tipo, max):
        self.__type = tipo
        self.__max = max

    def add_candidato(self, candidato):
        if len(self.__lista) < self.__max:
            self.__lista.append(candidato)
            return True
        return False

    def dar_voto(self, numero_candidato):
        votou = False
        self.__qtd += 1
        for c in self.__lista:
            if c.get_numero() == numero_candidato:
                c.votar()
                votou = True
        return votou

    def emitir_bu(self):
        bu = []
        for c in self.__lista:
            nome = c.get_nome()
            votos = c.get_votos()
            porcentagem = f"{(votos / self.__qtd) * 100}%"
            bu.append([nome, votos, porcentagem])
        bu.append(["Total", self.__qtd, "100%"])
        return tabulate(bu, tablefmt="fancy_grid")
