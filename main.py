import math
import os
import platform
import sympy as sym

# Lista de histórico
historico = []

# Função para limpar a tela
def limpar_tela():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# Função para adicionar ao histórico
def adicionar_ao_historico(operacao):
    historico.append(operacao)

# 1. Soma
def soma():
    try:
        num1 = int(input("Digite um valor: "))
        num2 = int(input("Digite outro valor: "))
        resultado = num1 + num2
        operacao = f"{num1} + {num2} = {resultado}"
        print(operacao)
        adicionar_ao_historico(operacao)
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
    input("\nPressione Enter para continuar...")
    limpar_tela()

# 2. Subtração
def subtracao():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        operacao = f"{num1} - {num2} = {resultado}"
        print(operacao)
        adicionar_ao_historico(operacao)
    except ValueError:
        print("Erro: Digite apenas números válidos.")
    input("\nPressione Enter para continuar...")
    limpar_tela()

# 3. Multiplicação
def multiplicacao():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 * num2
        operacao = f"{num1} * {num2} = {resultado}"
        print(operacao)
        adicionar_ao_historico(operacao)
    except ValueError:
        print("Erro: Digite apenas números inteiros.")
    input("\nPressione Enter para continuar...")
    limpar_tela()

# 4. Divisão
def divisao():
    try:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        if n2 == 0:
            print('Erro: divisão por zero não é permitida.')
        else:
            resultado = n1 / n2
            operacao = f"{n1} / {n2} = {resultado:.2f}"
            print(operacao)
            adicionar_ao_historico(operacao)
    except ValueError:
        print('Erro: digite apenas números inteiros.')
    input("\nPressione Enter para continuar...")
    limpar_tela()

# 5. Bhaskara
def bhaskara():
    while True:
        try:
            a = float(input("Digite o valor de a: "))
            if a == 0:
                print('"a" não pode ser 0. Tente novamente')
                continue
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            break
        except ValueError:
            print("Erro: Digite apenas números.")

    delta = (b ** 2) - 4 * a * c
    print(f"Valor de DELTA é {delta}")

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        operacao = f"Bhaskara com a={a}, b={b}, c={c}: x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif delta == 0:
        x = -b / (2 * a)
        operacao = f"Bhaskara com raiz dupla: x = {x:.2f}"
    else:
        operacao = f"Delta negativo: sem raízes reais."

    print(operacao)
    adicionar_ao_historico(operacao)
    input("\nPressione Enter para continuar...")
    limpar_tela()

# 6. Expressões algébricas
# Função principal do módulo de expressões algébricas
def expressoes_algebricas_avancadas():
    # Função interna que exibe o menu específico para expressões algébricas
    def menu_expressao():
        print("\n--- MÓDULO DE EXPRESSÕES ALGÉBRICAS ---")
        print("1. Simplificar expressão")
        print("2. Resolver equação")
        print("3. Fatorar expressão")
        print("4. Voltar ao menu principal")

    while True:
        menu_expressao()
        opcao = input("Escolha uma opção: ")

        # Opção 1: simplificação de expressões (ex: x + x -> 2x)
        if opcao == '1':
            expressao = input("Digite a expressão para simplificar: ")
            try:
                resultado = sym.simplify(sym.sympify(expressao))  # Converte texto para expressão simbólica e simplifica
                print("Resultado simplificado:", resultado)
                adicionar_ao_historico(f"Simplificado: {expressao} = {resultado}")  # Adiciona ao histórico
            except Exception as erro:
                print(f"Erro ao simplificar: {erro}")

        # Opção 2: resolução de equações (ex: x**2 - 4 = 0)
        elif opcao == '2':
            equacao = input("Digite a equação (ex: x**2 - 4 = 0): ")
            try:
                # Divide a equação em lado esquerdo e direito
                esquerda, direita = equacao.split('=')
                # Resolve a equação subtraindo os dois lados e igualando a zero
                resultado = sym.solve(sym.sympify(esquerda) - sym.sympify(direita))
                print("Soluções:", resultado)
                adicionar_ao_historico(f"Equação: {equacao} -> Soluções: {resultado}")
            except Exception as erro:
                print(f"Erro ao resolver: {erro}")

        # Opção 3: fatoração de expressões (ex: x**2 - 9 -> (x - 3)(x + 3))
        elif opcao == '3':
            expressao = input("Digite a expressão para fatorar: ")
            try:
                resultado = sym.factor(sym.sympify(expressao))  # Fatora a expressão algébrica
                print("Expressão fatorada:", resultado)
                adicionar_ao_historico(f"Fatorado: {expressao} = {resultado}")
            except Exception as erro:
                print(f"Erro ao fatorar: {erro}")

        # Opção 4: sair do menu e voltar ao principal
        elif opcao == '4':
            limpar_tela()
            break

        # Qualquer outro valor: entrada inválida
        else:
            print("Opção inválida. Escolha entre 1 e 4.")

# 7. Proporções
def proporcoes():
    try:
        ocorrencias = int(input("Número de ocorrências: "))
        total = int(input("Total de observações: "))
        if total == 0:
            print("Erro: O total não pode ser zero.")
        else:
            resultado = (ocorrencias / total) * 100
            operacao = f"{ocorrencias}/{total} = {resultado:.2f}%"
            print(f"Proporção: {resultado:.2f}%")
            adicionar_ao_historico(operacao)
    except ValueError:
        print("Erro: Digite apenas números inteiros.")
    input("\nPressione Enter para continuar...")
    limpar_tela()

# 8. Sistemas Lineares (2x2)
def sistemas_lineares():
    try:
        a = float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        d = float(input("Digite o valor de d: "))
        e = float(input("Digite o valor de e: "))
        f = float(input("Digite o valor de f: "))

        det = a * d - b * c
        if det == 0:
            operacao = "Sistema sem solução única."
        else:
            x = (e * d - b * f) / det
            y = (a * f - e * c) / det
            operacao = f"Sistema: x = {x:.2f}, y = {y:.2f}"
        print(operacao)
        adicionar_ao_historico(operacao)
    except ValueError:
        print("Erro: Digite apenas números.")
    input("\nPressione Enter para continuar...")
    limpar_tela()

# 9. Regra de três
def regra_de_tres():
    try:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        porcentagem = float(input("Digite a porcentagem: "))
        resultado = (valor2 * porcentagem) / valor1
        operacao = f"({valor2} * {porcentagem}) / {valor1} = {resultado:.2f}"
        print(f"Resultado: {resultado:.2f}")
        adicionar_ao_historico(operacao)
    except ValueError:
        print("Por favor, digite apenas números válidos.")
    input("\nPressione Enter para continuar...")
    limpar_tela()

# 10. Calcular porcentagem
def calcular_porcentagem():
    try:
        numero = float(input("Digite o número base: "))
        porcentagem = float(input("Digite a porcentagem: "))
        resultado = (porcentagem / 100) * numero
        operacao = f"{porcentagem}% de {numero} = {resultado:.2f}"
        print(operacao)
        adicionar_ao_historico(operacao)
    except ValueError:
        print("Por favor, digite apenas números válidos.")
    input("\nPressione Enter para continuar...")
    limpar_tela()
    
    def conjuntos():
        def calcular_conjuntos(conjunto1, conjunto2):
        # Convertendo listas para conjuntos (caso o usuário passe listas)
            c1 = set(conjunto1)
            c2 = set(conjunto2)
        
            resultado = {
                "união": c1 | c2,
                "interseção": c1 & c2,
                "diferença (c1 - c2)": c1 - c2,
                "diferença (c2 - c1)": c2 - c1,
                "diferença simétrica": c1 ^ c2,
                "c1 é subconjunto de c2": c1.issubset(c2),
                "c2 é subconjunto de c1": c2.issubset(c1),
                "são disjuntos": c1.isdisjoint(c2)
            }

        return resultado

# 11. Ver histórico
def mostrar_historico():
    print("\n--- HISTÓRICO DE OPERAÇÕES ---")
    if not historico:
        print("Nenhuma operação registrada ainda.")
    else:
        for i, item in enumerate(historico, 1):
            print(f"{i}. {item}")
    input("\nPressione Enter para voltar ao menu...")
    limpar_tela()

# Menu principal
def menu():
    while True:
        print("=== CALCULADORA MULTIFUNÇÕES ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Bhaskara")
        print("6 - Expressões algébricas")
        print("7 - Proporções")
        print("8 - Sistemas lineares")
        print("9 - Regra de três")
        print("10 - Calcular porcentagem")
        print("11 - conjuntos")
        print("12 - Ver histórico")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        limpar_tela()

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
            expressoes_algebricas_avancadas()
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
        elif opcao == '12':
            mostrar_historico()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")
            limpar_tela()

# Executar o programa
menu()
