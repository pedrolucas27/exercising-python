#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.

numero = input("INFORME UM NÚMERO:")

if "." in numero:
    print("Número real!")
else:
    print("Número inteiro!")