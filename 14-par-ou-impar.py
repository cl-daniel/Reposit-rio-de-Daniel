def par(x):
    return    x % 2 == 0


def par_ou_impar (x):
    if par(x):
        return "par"
    else:
        return "impar"

print(par_ou_impar(7))

valor = 0
while valor != 'S':
    valor = input("Digite um valor ou 'S' para sair: ")
    if valor != 'S':
        print(par_ou_impar(int(valor)))
    else:
        print("Fim do programa!")