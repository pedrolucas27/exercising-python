#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120

n = int(input("INFORME UM NÚMERO:"))
f = 1
for x in range(n,0,-1):
    f = f * x
print("{}! = {} ".format(n,f))