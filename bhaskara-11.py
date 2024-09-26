a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

delta = (b ** 2) - 4 * a * c
if a == 0:
    print("O valor de A, não pode ser 0!")
elif delta < 0:
    print("Sem raízes!")
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2:{}".format(x1, x2))