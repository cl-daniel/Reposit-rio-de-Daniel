print("bem vindo a votação 2024, 100% atualizada!!!")

idade = int(input("digite sua idade vei!: "))

if idade >= 18 and idade < 65:
    print("Voto obrigatório!")
elif idade >= 16 and idade <= 17 or idade >= 65:
    print("Voto opcional!")
else:
    print("Não vota!")