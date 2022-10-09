from funcionario import *
from gerente import *

equipe = []
equipe.append(Funcionario(123, "João", 40, 35))
equipe.append(Funcionario(523, "Mari", 20, 35))
equipe.append(Gerente(999, "Gustavo", 40, 35, 50))

for pessoa in equipe:
    print(f"{pessoa.nome} salário R$ {pessoa.calc_salario()}")
    if isinstance(pessoa, Gerente):
        print(pessoa.obter_adicional_porcentagem())