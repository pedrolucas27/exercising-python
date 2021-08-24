#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação
# ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que 
# diga se o número é:
#   - par ou ímpar;
#   - positivo ou negativo;

num = int(input("Dígite um número:"))
print("1 - VERIFICAR SE O N É PAR OU ÍMPAR")
print("2 - VERIFICAR SE O N É POSITIVO OU NEGATIVO")
op = int(input("Escolha uma opção:"))

if op == 1:
    if (num % 2) == 0:
        print("PAR")
    else:
        print("ÍMPAR")
elif op == 2:
    if num >= 0:
        print("POSITIVO")
    else:
        print("NEGATIVO")
else:
    print("INFORME UMA OPÇÃO VÁLIDA")
