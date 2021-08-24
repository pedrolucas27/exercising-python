#Faça um programa que calcule o mostre a média aritmética de N notas. 

n = int(input("Informe o número de notas:"))
somatorio = 0
for c in range(1,n+1):
    nc = float(input("Informe a nota {}:".format(c)))
    somatorio += nc

m = somatorio / n
print("Médiaa das {} é = {}".format(n,m))