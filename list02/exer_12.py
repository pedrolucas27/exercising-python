#Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input("INFORME O DIA DA SEMANA (1 - 7):"))

if dia == 1:
    print(dia," - Domingo")
elif dia == 2:
    print(dia," - Segunda")
elif dia == 3:
    print(dia," - Terça")
elif  dia == 4:
    print(dia," - Quarta")
elif dia == 5:
    print(dia," - Quinta")
elif dia == 6:
    print(dia," - Sexta")
elif dia == 7:
    print(dia," - Sábado")
else:
    print("Valor inválido.")