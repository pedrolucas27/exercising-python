#Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = int(input("Informe o 1 número:"))
n2 = int(input("Informe o 2 número:"))
n3 = int(input("Informe o 3 número:"))

if (n1 < n2) and (n1 < n3):
    print("Menor - ",n1)
elif (n2 < n1) and (n2 < n3):
    print("Menor - ",n2)
else:
    print("Menor - ",n3)