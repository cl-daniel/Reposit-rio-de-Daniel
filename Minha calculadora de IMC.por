programa {
  funcao inicio() {
  //Calduladora de IMC
  real  imc, altura, peso
  escreva("Digite sua altura: ")
  leia(altura)
   escreva("Digite seu peso: ")
  leia(peso)

  imc = peso / (altura * altura)
  se(imc<18.5)
  escreva("Você está só a capa.")
  senao se(imc>18.5)
  escreva("Você está no peso ideal. ")
  senao se(imc>25)
  escreva("Você está pesado. ")
  senao se(imc>35)
  escreva("Você está gordasso. ")



  }
}
