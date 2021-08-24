#Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% 
# para o sindicato, faça um programa que nos dê:
#   A - salário bruto.
#   B - quanto pagou ao INSS.
#   C - quanto pagou ao sindicato.
#   D - o salário líquido.
#   E - calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   Tabela:
#   + Salário Bruto : R$
#   - IR (11%) : R$
#   - INSS (8%) : R$
#   - Sindicato ( 5%) : R$
#   = Salário Liquido : R$
valor_hora = float(input("Informe o valor recebido por hora:"))
n_hora = int(input("Número de horas trabalhadas por mês:"))

s = valor_hora * n_hora
ir = (11 / 100) * s
inss = (8 / 100) * s
sindicato = (5 / 100) * s
descontos = ir + inss + sindicato
sl = s - descontos

print("Salário Bruto R$",s)
print("Imposto de Renda - R$",ir)
print("INSS - R$",inss)
print("Sindicato - R$",sindicato)
print("Descontos - R$",descontos)
print("Salário Líquido R$",sl)