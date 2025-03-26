print("Bem vindo(a)!")

def menu():
    while True:
        escolha_usuario = int(input("1 - Soma 2 - Subtração 3 - Multiplicacao 4 - Divisão "))
        if escolha_usuario == 1:
            print("soma")
        elif escolha_usuario == 2:
            print("Subtração")
        elif escolha_usuario == 3:
            print("Multiplicação")
        elif escolha_usuario == 4:
            print("Divisão")
        else:
            continue
menu()

print("teste")