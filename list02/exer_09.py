#Faça um Programa que leia três números e mostre-os em ordem decrescente. 
n1 = int(input("Informe o 1 número:"))
n2 = int(input("Informe o 2 número:"))
n3 = int(input("Informe o 3 número:"))

if (n1 < n2) and (n2 < n3):
    print(n3,n2,n1)
elif (n2 < n1) and (n1 < n3):
    print(n3,n1,n2)
elif (n3 < n1) and (n1 < n2):
    print(n2,n1,n3)
elif (n1 < n3) and (n3 < n2):
    print(n2,n3,n1)
elif (n2 < n3) and (n3 < n1):
    print(n1,n3,n2)
elif (n3 < n2) and (n2 < n1):
    print(n1,n2,n3)
else:
    print("Número iguais!!")