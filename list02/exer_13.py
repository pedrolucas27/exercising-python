#Faça um Programa que peça um número correspondente a um determinado ano e em seguida
# informe se este ano é ou não bissexto.

ano = int(input("Informe um ano:"))
t = len(str(ano)) #manipulando a string (tamanho) através da conversão (int -> str)

if t == 4:
    if (ano % 4) == 0:
        print("Ano bissexto!")
    else:
        print("Ano não bissexto!")
else:
    print("Ano inválido !!")
