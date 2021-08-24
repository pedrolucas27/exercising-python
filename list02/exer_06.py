#Faça um Programa que leia três números e mostre o maior deles. 
n1 = int(input("Informe o 1 número:"))
n2 = int(input("Informe o 2 número:"))
n3 = int(input("Informe o 3 número:"))

if (n1 > n2) and (n1 > n3):
    print("Maior - ",n1)
elif (n2 > n1) and (n2 > n3):
    print("Maior - ",n2)
else:
    print("Maior - ",n3)