print("Calculadora de IMC em python!")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura **2)
print(imc)

if (imc <18.5):
    print("Você está abaixo do seu peso ideal.")

elif (imc >= 18.5 and  imc <=24.9):
    print("Você está no seu peso ideal!")

elif (imc >= 25.0 and imc <= 34.9):
    print("Você está acima do peso!")
else:    
    print("Você está obeso!")
    