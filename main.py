import math as m # importacao de biblioteca math
print("Bem vindo(a)!")


def soma():
    num01soma = float(input("Digite um numero:"))
    num02soma = float(input("Digite um numero:"))
    resultado_soma = num01soma + num02soma
    print(f"Sua soma entre {num01soma} e {num02soma} é {resultado_soma}")

def menu():
    while True:
        escolha_usuario = int(input("1 - Soma 2 - Subtração 3 - Multiplicacao 4 - Divisão "))
        if escolha_usuario == 1:
            soma()
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
print("mateus Logado")