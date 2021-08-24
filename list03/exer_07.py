#Faça um programa que leia 5 números e informe a soma e a média dos números. 
from decimal import Decimal
s = 0
for c in range (0,5):
    n = Decimal(input("INFORME UM NÚMERO:"))
    s += n

m = s / 5
print("Soma = ",s)
print("Média = ",m)