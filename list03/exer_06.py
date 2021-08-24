#Faça um programa que leia 5 números e informe o maior número.

maior = 0
for n in range(1,6):
    x = int(input("Número:"))
    if x > maior:
        maior = x
print("Maior - ",maior)