import math

#MATHEUS
def soma():
    #codigo aqui
    ...

#GUI
def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print(f"A subtração de {num1} e {num2} é: {resultado}")


#DANIEL
def multiplicacao():
    #codigo aqui
    ...

#DANIEL
def divisao():
    #codigo aqui
    ...

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
    #codigo aqui
    ...
    
#FABIO
def proporcoes():
    #codigo aqui
    ...
#TODOS
def sistemas_lineares():
    #codigo aqui
    ...

#MATHEUS
def regra_de_tres():
    #codigo aqui
    ...
    
#MATEUS
def porcentagem():
    #codigo aqui
    ...

#GUI
def conjuntos():
    
    ...