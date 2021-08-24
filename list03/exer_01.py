#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
# seja inválido e continue pedindo até que o usuário informe um valor válido. 

flag = True
while flag:
    n = float(input("INFORME UMA NOTA DE 0 - 10: "))
    if n >= 0 and n <= 10:
        flag = False
    else:
        print("NOTA INVÁLIDA, POR FAVOR TENTE NOVAMENTE!!")
print("NOTA VÁLIDA !!")