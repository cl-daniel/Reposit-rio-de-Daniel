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
  escreva("Voc� est� s� a capa.")
  senao se(imc>18.5)
  escreva("Voc� est� no peso ideal. ")
  senao se(imc>25)
  escreva("Voc� est� pesado. ")
  senao se(imc>35)
  escreva("Voc� est� gordasso. ")



  }
}
