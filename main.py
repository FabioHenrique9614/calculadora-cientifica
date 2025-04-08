import math

# MATHEUS
def soma():
    try:
        num1 = float(input("Digite um valor: "))
        num2 = float(input("Digite outro valor: "))
        resultado = num1 + num2
        print(f"A soma entre {num1} e {num2} é igual a {resultado}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

# GUI
def subtracao():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"A subtração de {num1} e {num2} é: {resultado}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

# DANIEL
def multiplicacao():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"\n{'-'*30}\nA multiplicação de {num1} e {num2} vale {resultado}.\n{'-'*30}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

# DANIEL
def divisao():
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        if n2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            resultado = n1 / n2
            print(f"A divisão de {n1} por {n2} vale {resultado:.2f}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

# FABIO
def bhaskara():
    while True:
        try:
            a = float(input("Digite o valor de a: "))
            if a == 0:
                print('"a" não pode ser 0. Tente novamente.')
                continue
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
        except ValueError:
            print("Erro: Digite apenas números.")
            continue

        delta = (b**2) - 4 * a * c
        print(f"Valor de DELTA é {delta}")

        if delta < 0:
            print("Delta negativo. Não há raízes reais. Tente outros coeficientes.\n")
            continue
        break

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Duas raízes reais: X1 = {x1:.2f}, X2 = {x2:.2f}")
    else:
        x = -b / (2 * a)
        print(f"Raiz dupla: x = {x:.2f}")

# MATEUS
def expressoes_algebricas():
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        resultado = (a + b) * c
        print(f"O resultado da expressão (a + b) * c é: {resultado:.2f}")
    except ValueError:
        print("Erro: Digite apenas números válidos.")

# FABIO
def proporcoes():
    try:
        ocorrencias = int(input("Número de ocorrências: "))
        total = int(input("Total de observações: "))
        if total == 0:
            print("Erro: O total não pode ser zero.")
            return
        proporcao = ocorrencias / total
        print(f"A proporção é: {proporcao:.2f}")
    except ValueError:
        print("Erro: Digite apenas números inteiros.")

#todos
def sistemas_lineares():
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        d = float(input("Digite o valor de d: "))
        e = float(input("Digite o valor de e: "))
        f = float(input("Digite o valor de f: "))
    except ValueError:
        print("Erro: Digite apenas números.")
        return

    det = a * d - b * c
    if det == 0:
        print("O sistema não possui solução única.")
    else:
        x = (e * d - b * f) / det
        y = (a * f - e * c) / det
        print(f"Solução do sistema: x = {x:.2f}, y = {y:.2f}")

# MATHEUS
def regra_de_tres():
    try:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        porcentagem = float(input("Digite a porcentagem: "))
        resultado = (valor2 * porcentagem) / valor1
        print(f"O resultado da regra de três é: {resultado:.2f}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

# MATHEUS
def calcular_porcentagem():
    try:
        numero = float(input("Digite o número base: "))
        porcentagem = float(input("Digite a porcentagem que deseja calcular: "))
        resultado = (porcentagem / 100) * numero
        print(f"{porcentagem}% de {numero} é igual a {resultado:.2f}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

# GUI
def conjuntos():
    def calcular_conjuntos(conjunto1, conjunto2):
        c1 = set(conjunto1)
        c2 = set(conjunto2)
        return {
            "união": c1 | c2,
            "interseção": c1 & c2,
            "diferença (c1 - c2)": c1 - c2,
            "diferença (c2 - c1)": c2 - c1,
            "diferença simétrica": c1 ^ c2,
            "c1 é subconjunto de c2": c1.issubset(c2),
            "c2 é subconjunto de c1": c2.issubset(c1),
            "são disjuntos": c1.isdisjoint(c2)
        }
# MENU INTERATIVO COM WHILE
def menu():
    while True:
        print("\n--- MENU DE OPERAÇÕES ---")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Bhaskara")
        print("6 - Expressões Algébricas")
        print("7 - Proporções")
        print("8 - Sistemas Lineares")
        print("9 - Regra de Três")
        print("10 - Calcular Porcentagem")
        print("11 - Conjuntos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            soma()
        elif opcao == '2':
            subtracao()
        elif opcao == '3':
            multiplicacao()
        elif opcao == '4':
            divisao()
        elif opcao == '5':
            bhaskara()
        elif opcao == '6':
            expressoes_algebricas()
        elif opcao == '7':
            proporcoes()
        elif opcao == '8':
            sistemas_lineares()
        elif opcao == '9':
            regra_de_tres()
        elif opcao == '10':
            calcular_porcentagem()
        elif opcao == '11':
            conjuntos()
        elif opcao == '0':
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
# INICIAR O PROGRAMA
menu()
