# Declaração da função exibirMensagem(nome)
def exibirMensagem(nome, idade) :
    print(f"Olá, {nome} com {idade} anos!")


def somar( a, b):
    return a + b


def calcularAreaCirculo(raio):
    area = 3.1415 * raio**2
    return area


# inicio do meu algoritmo
nome = input("Digite o seu nome:")
idade = input("Digite sua idade: ")


# chamando função com retorno
valorA = int(input("Digite o primeiro número: "))
valorB = int(input("Digite o segundo número: "))
resultado = somar(valorA, valorB)
print(f"O resultado da soma = {resultado}")


# calcular area do circuito
print("Area do circuito!!")
raio = float(input("Digite o valor do raio: "))
area = calcularAreaCirculo(raio)
print(f"A área do circulo : (area:.2f)")
