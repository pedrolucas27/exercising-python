#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# A - o produto do dobro do primeiro com metade do segundo .
# B - a soma do triplo do primeiro com o terceiro.
# C - o terceiro elevado ao cubo. 
from decimal import Decimal
n1 = int(input("Informe um número inteiro:"))
n2 = int(input("Informe outro número inteiro:"))
n3 = Decimal(input("Informe um número real:"))


a = (2 * n1) * (n2 / 2)
b = (3 * n1) + n3
c = n3 ** 3

print("A = ",a)
print("B = ",b)
print("C = ",c)