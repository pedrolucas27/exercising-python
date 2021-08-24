#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o 
# exemplo abaixo: 

n = int(input("INFORME UM NÚMERO O QUAL VOCÊ DESEJA VER A TABUADA:"))
x = 0
print("TABUADA - ",n)
for n2 in range(1,11):
    x = n * n2
    print("{} * {} = {}".format(n,n2,x))
