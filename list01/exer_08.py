#Faça um Programa que pergunte quanto você ganha por hora e 
# o número de horas trabalhadas no mês. Calcule e mostre o total
# do seu salário no referido mês.
from decimal import Decimal
valor_hora = Decimal(input("Informe o valor recebido por hora:"))
n_hora = int(input("Número de horas trabalhadas por mês:"))

s = valor_hora * n_hora

print("Salário de R$",s)