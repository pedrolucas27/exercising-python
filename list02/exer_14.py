#Faça um Programa que leia um número inteiro menor que 1000 e imprima a 
# quantidade de centenas, dezenas e unidades do mesmo.
#    - Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#       -> 326 = 3 centenas, 2 dezenas e 6 unidades
#       -> 12 = 1 dezena e 2 unidades

c = 0
d = 0
u = 0

n = int(input("INFORME UM NÚMERO MENOR QUE 1000:"))
if n < 1000 and n > 0:
    if n >= 100:
        c = int(n / 100)
        d = int((n - (c * 100)) / 10)
        u = n - ((c * 100) + (d * 10))
    else:
        d = int(n / 10)
        u = n - (d * 10)
print(n,"=",c,"centenas,",d,"dezenas,",u,"unidades")



