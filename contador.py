# Atividade: Aula de tabuada
# Fazer um programa de tabuada
numero = int(input("Digite um número para ver a tabuada: "))
contador = 0
while contador <=10:
    resultador = numero * contador
    print(f"{numero} X {contador} = {resultador}")
    contador +=1
    