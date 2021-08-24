#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

l = str(input("Informe seu sexo (F ou M):"))[0]

if l.lower() == "m":
    print("M - Masculino")
elif l.lower() == "f":
    print("F - Feminino")
else:
    print("Sexo Inválido")