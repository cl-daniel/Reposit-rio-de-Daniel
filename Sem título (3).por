programa {
  funcao inicio() {
  real dividendo, divisor, resultado

  escreva("Digite o dividendo: ")
  leia(dividendo)

  escreva("Digite o divisor: ")
  leia(divisor)

  se (divisor == 0){
  escreva("Não é possivel dividir por 0." )
  } senao{
     resultado = (dividendo / divisor)
     
  escreva("\nseu resultado foi de: ", resultado)
  }

  }
}
