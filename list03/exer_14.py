#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
# Faça um programa capaz de gerar a série até o n−ésimo termo. 
from time import sleep
t = int(input("Informe o números de termos da série:"))
x = 0
for c in range(1,t+1):
    if c == 1:
        print(c,end=" ")
    else:
        print(x,end=" ")
        x = x + (c - 2)

#INCOMPLETOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO