import math

#MATHEUS
def soma():    
    numerosoma01 = int(input("digite um valor: "))
    numerosoma02 = int(input("digite outro valor:")) 
    resultado = numerosoma01 + numerosoma02 
    print(f"a soma entre {numerosoma01} e {numerosoma02} Ã© igual a {resultado}")
soma()

#GUI
def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print(f"A subtração de {num1} e {num2} é: {resultado}")


#DANIEL
def multiplicacao():
        while True:
            try:
                num1 = int(input("Digite o primeiro número: "))
                num2 = int(input("Digite o segundo número: "))
    
                resultado = num1 * num2

                print("\n" + "-"*30)
                print(f"A multiplicação de {num1} e {num2} vale {resultado}.")
                print("-"*30)

            except ValueError:
                print("\nErro: Por favor, digite apenas números inteiros.")

#DANIEL
def divisao():
    while True:
        try:
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))

            if n2 == 0:
                print('Erro: divisão por zero não é permitida.')
            else:
                resultado = n1 / n2
                print(f'A divisão de {n1} por {n2} vale {resultado:.2f}')
        except ValueError:
            print('Erro: digite apenas números inteiros.')

#FABIO
def bhaskara():
    while True:
        try:
            a = float(input("Digite o valor de a"))
            if a == 0:
                print('"a" não pode ser 0. Tente novamente')
                continue
            b = float(input("Digite o valor de b"))
            c = float(input("Digite o valor de c"))
        except ValueError:
            print("Erro: Digite apenas números. Tente novamente.")
            continue

        delta = (b**2) -4 * a * c
        print(f"Valor de DELTA é {delta}")

        if delta >= 0:
            break
        else:
            print(f"Delta negativo. Não há raizes reais. Tente outros coeficientes.\n")
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Duas raizes reais: X1 = {x1:.2f}, X2 = {x2:.2f}")
    else:
        x = -b / (2 * a)
        print(f"Raiz dupla: x = {x:.2f}")

bhaskara()

#MATEUS
def expressões_algébricas():
    while True:
        try:
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            break  # Sai do loop se os valores forem válidos
        except ValueError:
            print("Erro: Digite apenas números. Tente novamente!\n")

    resultado = (a + b) * c
    print(f"O resultado da expressão (a + b) * c é: {resultado:.2f}")
    
#FABIO
def proporcoes():
    while True:  # Repete até o usuário digitar valores válidos
        try:
            ocorrencias = int(input("Número de ocorrências: "))
            total = int(input("Total de observações: "))
            if total == 0:
                print("Erro: O total não pode ser zero. Tente novamente!\n")
                continue  # Pula para a próxima iteração do loop
            break  # Sai do loop se os valores forem válidos
        except ValueError:
            print("Erro: Digite apenas números inteiros. Tente novamente!\n")
#TODOS
def sistemas_lineares():
    while True:
        try:
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            d = float(input("Digite o valor de d: "))
            e = float(input("Digite o valor de e: "))
            f = float(input("Digite o valor de f: "))
            break  # Sai do loop se os valores forem válidos
        except ValueError:
            print("Erro: Digite apenas números. Tente novamente!\n")

    det = a * d - b * c

    if det == 0:
        print("O sistema não possui solução única.")
    else:
        x = (e * d - b * f) / det
        y = (a * f - e * c) / det
        print(f"Solução do sistema: x = {x:.2f}, y = {y:.2f}")

#MATHEUS
def regra_de_tres():
    try:
        valor1 = float(input("Digite o primeiro valor: "))
        valor2 = float(input("Digite o segundo valor: "))
        porcentagem = float(input("Digite a porcentagem: "))

        resultado = (valor2 * porcentagem) / valor1
        print(f"O resultado da regra de três é: {resultado:.2f}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")
    
#MATEUS
def calcular_porcentagem():
    try:
        numero = float(input("Digite o número base: "))
        porcentagem = float(input("Digite a porcentagem que deseja calcular: "))
        resultado = (porcentagem / 100) * numero
        print(f"{porcentagem}% de {numero} é igual = {resultado}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")

# Chamar a função
calcular_porcentagem()

#GUI
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
