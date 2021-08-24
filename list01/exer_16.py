#Faça um programa para uma loja de tintas. O programa deverá pedir o 
# tamanho em metros quadrados da área a ser pintada. Considere que a 
# cobertura da tinta é de 1 litro para cada 3 metros quadrados e  que 
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
a = int(input("Informe a área em (m)^2:"))
qtdL_area = a / 3
n_latas = qtdL_area / 18
preco = n_latas * 80.00

print("Número de latas a serem gastas ",n_latas)
print("Preço a ser gasto R$",preco)
