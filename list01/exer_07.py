#Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário. 
from decimal import Decimal
lado = Decimal(input("Informe o lado do quadrado:"))
a = lado ** 2
print("O dobro da área do quadrado é",(a * 2))