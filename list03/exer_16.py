#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1. 

n = int(input("Informe um número:"))
c = 0

for i in range(1,n+1):
    if n % i == 0:
        c += 1
if c == 2:
    print("{} é primo!".format(n))
else:
    print("{} não é primo!".format(n))
