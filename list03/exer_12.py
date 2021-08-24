#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
# elevado ao segundo número. Não utilize a função de potência da linguagem. 

base = int(input("INFORME A BASE:"))
exp = int(input("INFORME O EXPOENTE:"))

x = base
for c in range(1,exp):
    x *= base


print("Resultado:",x)