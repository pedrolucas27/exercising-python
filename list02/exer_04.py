#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

l = str(input("Dígite uma letra:"))

if l.lower() == "a" or l.lower() == "e" or l.lower() == "i" or l.lower() == "o" or l.lower() == "u":
    print("Letra informada é uma vogal !!")
else:
    print("Letra informada é uma consoante !!")