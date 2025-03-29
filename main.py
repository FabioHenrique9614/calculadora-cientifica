import math # importacao de biblioteca math

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c  # Calcula o delta
    
    if delta < 0:
        return "Não há raízes reais"  # Caso o delta seja negativo
    
    x1 = (-b + math.sqrt(delta)) / (2 * a)  # Primeira raiz
    x2 = (-b - math.sqrt(delta)) / (2 * a)  # Segunda raiz
    
    return x1, x2  # Retorna as raízes"