#Tendo como dado de entrada a altura (h) de uma pessoa,construa um algoritmo
# que calcule seu peso ideal, utilizando as seguintes fórmulas:
# A - Para homens: (72.7*h) - 58
# B - Para mulheres: (62.1*h) - 44.7 
from decimal import Decimal
sexo = str(input("Informe o seu sexo (F ou M):"))[0] #a variável vai receber a pos 0 da string
h = float(input("Informe a sual altura (m):"))
peso_ideal = 0
if sexo == "m":
    peso_ideal = (72.7 * h) - 58
    print("Peso ideal kg",peso_ideal)
elif sexo == "f":
    peso_ideal = (62.1 * h) - 44.7
    print("Peso ideal kg",peso_ideal)
else:
    print("Informe M ou F para o sexo!")