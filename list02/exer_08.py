#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.
from decimal import Decimal
p1 = Decimal(input("Quanto custa o produto 1:"))
p2 = Decimal(input("Quanto custa o produto 2:"))
p3 = Decimal(input("Quanto custa o produto 3:"))

if (p1 < p2) and (p1 < p3):
    print("O produto a ser comprado é o (1)")
elif (p2 < p1) and (p2 < p3):
    print("O produto a ser comprado é o (2)")
else:
    print("O produto a ser comprado é o (3)")