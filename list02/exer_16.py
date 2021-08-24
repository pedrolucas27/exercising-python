#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo 
# de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 
#   Média de Aproveitamento  Conceito
#       Entre 9.0 e 10.0        A
#       Entre 7.5 e 9.0         B
#       Entre 6.0 e 7.5         C
#       Entre 4.0 e 6.0         D
#       Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem 
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

from decimal import Decimal
n1 = Decimal(input("Informe sua primeira nota:"))
n2 = Decimal(input("Informe sua segunda nota:"))

m = (n1 + n2) / 2

if m >= 9.0 and m <= 10.0:
    print("CONCEITO (A)")
    print("N1-",n1,"\nN2-",n2,"\nMÉDIA-",m,"\nAPROVADO!")
elif m >= 7.5 and m < 9.0:
    print("CONCEITO (B)")
    print("N1-",n1,"\nN2-",n2,"\nMÉDIA-",m,"\nAPROVADO!")
elif m >= 6.0 and m < 7.5:
    print("CONCEITO (C)")
    print("N1-",n1,"\nN2-",n2,"\nMÉDIA-",m,"\nAPROVADO!")
elif m >= 4.0 and m < 6.0:
    print("CONCEITO (D)")
    print("N1-",n1,"\nN2-",n2,"\nMÉDIA-",m,"\nREPROVADO!")
elif m >= 0 and m < 4.0:
    print("CONCEITO (E)")
    print("N1-",n1,"\nN2-",n2,"\nMÉDIA-",m,"\nREPROVADO!")
else:
    print("NOS INFORME NOTAS VÁLIDAS (0 - 10)")

#nome = str(input("DÍGITE SEU NOME: "))
#print("SEU NOME É {}!".format(nome))