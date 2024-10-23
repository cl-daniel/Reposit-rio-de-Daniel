number = int(input('Digite um número: '))
primo = 0

for i in range(1, (number + 1)):
    if number % i == 0:
        primo += 1

if primo == 2 : 
    print(f'{number} é primo')
else:
    print(f'{number} não é primo')