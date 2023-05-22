nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infecto-contagiosa? ").upper()
if idade >=60:
    print("Paciente COM prioridade.")
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para a sala AMARELA.")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para a sala BRANCA.")
    else:
        print("Responda 'suspeita de doença infecto-contagiosa' com 'SIM' ou 'NAO' para saber a sala para encaminhamento do paciente.")
else:
    if doenca_infectocontagiosa=="SIM":
        print("Encaminhe o paciente para a sala AMARELA.")
    elif doenca_infectocontagiosa=="NAO":
        print("Encaminhe o paciente para a sala BRANCA.")
    else:
        print("Responda 'suspeita de doença infecto-contagiosa' com 'SIM' ou 'NAO' para saber a sala para encaminhamento do paciente.")
