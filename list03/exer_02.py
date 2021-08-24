#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
# igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

user = str(input("INFORME SEU USER: "))
password = str(input("INFORME SUA SENHA: "))

flag = False

while flag != True:
    if user.lower() == password.lower():
        print("ERRORR, O USER DEVE SER DIFERENTE DO PASSWORD!")
        user = str(input("INFORME SEU USER: "))
        password = str(input("INFORME SUA SENHA: "))
    else:
        flag = True
        print("FIMMMM !")
        

