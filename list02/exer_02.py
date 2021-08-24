#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 
valor = int(input("Dígite um número:"))

if valor < 0:
    print("O número",valor,"é negativo!")
else:
    print("O número",valor,"é positivo!")