#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Informe um número:"))
n2 = int(input("Informe outro número:"))

s = 0

for i in range(n1+1,n2):
    s += i
    print(i,end=" ")
print()
print("SOMA = ",s)