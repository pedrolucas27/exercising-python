#ex:01
#contagem de 0 -> 10
#obs: na repetição contador máximo é desconsiderado
for c in range(0,10):
    print(c)
print("--------------------")
#ex:02
#contagem de 0 -> 10, pulando de 3 em 3
#obs: na repetição contador máximo é desconsiderado
for c in range(0,10,3):
    print(c)
print("--------------------")
#ex:04
#contagem 10 -> 1
#percorrendo a estrutura na ordem decrescente
for c in range(10,0,-1):
    print(c)
print("--------------------")
#ex:04
#contagem de acordo com as entradas para as propriedades do (for)
#obs: na repetição contador máximo é desconsiderado
i = int(input("INFORME O ÍNICIO:"))
f = int(input("INFORME O FIM:"))
p = int(input("INFORME O PULO:"))
for c in range(i,f,p):
    print(c)
print("---------------------")
#ex:05
#contagem regressiva
from time import sleep
for cont in range(10,-1,-1):
    print(cont)
    sleep(1.5)
print("POOOWWWW")




