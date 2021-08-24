#Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#   - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   - A mensagem "Reprovado", se a média for menor do que sete;
#   - A mensagem "Aprovado com Distinção", se a média for igual a dez.
from decimal import Decimal
nota1 = Decimal(input("Informe sua primeira nota:"))
nota2 = Decimal(input("Informe sua segunda nota:"))

media = (nota1 + nota2) / 2

if media == 10.0:
    print("Aprovado com Distinção")
elif media >= 7.0 and media < 10.0:
    print("Aprovado !!")
elif media < 7.0:
    print("Reprovado !!")
else:
    print("Nota não suportada!")
