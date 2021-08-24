#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
# cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
# ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades de tinta 
# a serem compradas e os respectivos preços em 3 situações:
#  - comprar apenas latas de 18 litros;
#  - comprar apenas galões de 3,6 litros;
#  - misturar latas e galões, de forma que o preço seja o menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, 
# considere latas cheias.

a = int(input("Informe a área em (m)^2 a ser pintada:"))
qtdL_area = a / 6
n_latas = qtdL_area / 18
n_galoes = qtdL_area / 3.6
precoLatas = n_latas * 80.00
precoGaloes = n_latas * 25.00

print("Número de litros a serem adquiridos",qtdL_area,"L")
print("Valor a ser pago nas latas R$",precoLatas)
print("Valor a ser pago nos galões R$",precoGaloes)