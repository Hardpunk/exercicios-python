from urna import *
from candidato import *

ze = Candidato(31, "José Silva")
urna = UrnaVotacao("Eleição para Atlética FIPP", 3)
if not urna.add_candidato(ze):
    print("Esgotado o máximo de candidatos.")

if not urna.add_candidato(Candidato(10, 'Jeremias Dias')):
    print("Esgotado o máximo de candidatos.")

if not urna.add_candidato(Candidato(19, 'Clotilda Ramos')):
    print("Esgotado o máximo de candidatos.")

if not urna.add_candidato(Candidato(12, 'Luis Silva')):
    print("Esgotado o máximo de candidatos.")

if not urna.dar_voto(10):
    print('Voto inválido.')

if not urna.dar_voto(12):
    print('Voto inválido.')

if not urna.dar_voto(19):
    print('Voto inválido.')

if not urna.dar_voto(19):
    print('Voto inválido.')

if not urna.dar_voto(31):
    print('Voto inválido.')


print(urna.emitir_bu())
