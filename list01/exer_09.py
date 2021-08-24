#Faça um Programa que peça a temperatura em graus Farenheit, 
# transforme e mostre a temperatura em graus Celsius. 
# Formúla : C = (5 * (F-32) / 9). 
temp_far = int(input("Informe a temperatura em Farenheit:"))
temp_cel = (5 * (temp_far - 32) / 9)
print("Temperatura em Celsius:",temp_cel)