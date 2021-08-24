#Faça um programa que leia e valide as seguintes informações:
#   - Nome: maior que 3 caracteres;
#   - Idade: entre 0 e 150;
#   - Salário: maior que zero;
#   - Sexo: 'f' ou 'm';
#   - Estado Civil: 's', 'c', 'v', 'd'; 
from decimal import Decimal

nome = str(input("INFORME SEU NOME:"))
idade = int(input("INFORME SUA IDADE:"))
salario = Decimal(input("SALÁRIO R$:"))
sexo = str(input("SEXO:"))[0]
estado_civil = str(input("ESTADO CIVIL:"))[0]

flag = False
while flag != True:
    if len(nome) <= 3:
        nome = str(input("INFORME SEU NOME, nome maior que 3 caracteres:"))
    elif (idade < 0) or (idade > 150):
        idade = int(input("INFORME SUA IDADE, idade tem que ser entre 0 e 150:"))
    elif salario < 0:
        salario = Decimal(input("SALÁRIO R$, maior que 0:"))
    elif (sexo.lower() != "f") and (sexo.lower() != "m"):
        sexo = str(input("SEXO, 'f' ou 'm':"))[0]
    elif (estado_civil.lower() != "s") and (estado_civil.lower() != "c") and (estado_civil.lower() != "v") and (estado_civil.lower() != "d"):
        estado_civil = str(input("ESTADO CIVIL, 's', 'c', 'v', 'd' :"))[0]
    else:
        flag = True
print("FIMMMMMMMMM!")
