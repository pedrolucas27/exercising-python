#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contraram para desenvolver o programa que calculará os reajustes.Faça um programa 
# que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
# baseado no salário atual:
#    - salários até R$ 280,00 (incluindo) : aumento de 20%
#    - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    - salários de R$ 1500,00 em diante : aumento de 5% 
#Após o aumento ser realizado, informe na tela:
#    - o salário antes do reajuste;
#    - o percentual de aumento aplicado;
#    - o valor do aumento;
#    - o novo salário, após o aumento.

salario = float(input("Nos informe seu salário R$:"))
percentual = 0
aumento = 0

print("================================")

if (salario > 0) and (salario <= 280.00):
    print("Salário antes do reajuste R$",salario)
    aumento = (salario * (20/100))
    salario = salario + aumento
    print("Percentual de aumento aplicado 20%")
elif (salario > 280.00) and (salario <= 700.00):
    print("Salário antes do reajuste R$",salario)
    aumento = (salario * (15/100))
    salario = salario + aumento
    print("Percentual de aumento aplicado 15%")
elif (salario > 700.00) and (salario <= 1500.00):
    print("Salário antes do reajuste R$",salario)
    aumento = (salario * (10/100))
    salario = salario + aumento
    print("Percentual de aumento aplicado 10%")
elif salario > 1500.00:
    print("Salário antes do reajuste R$",salario)
    aumento = (salario * (5/100))
    salario = salario + aumento
    print("Percentual de aumento aplicado 5%")
else:
    print("Informe um valor positivo diferente de 0.")

print("Valor do aumento R$",aumento)
print("Novo salário R$",salario)