# nome=input("Digite o nome: ")
# idade=int(input("Digite a idade: "))
# prioridade="NÃO"
# if idade>=65:
#     prioridade="SIM"
# print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)

nome = input("Digite o nome do paciente: ").upper()
idade = int(input("Digite a idade do paciente: ")


if idade >= 65:
    print(f"O paciente {nome} possui atendimento prefencial")
else:
    print(f"O paciente {nome} não possui atendimento prefencial")