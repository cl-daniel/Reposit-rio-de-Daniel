programa {
  funcao inicio() {
// Algoritmo do voto obrigat�rio
  inteiro idade

  escreva("Qual � a sua idade?")
  leia(idade)

  se (idade >=18 e idade >=65)
  escreva("\nVoc� vota se preferir.")

  senao se(idade >=16 e idade<18 ou idade< 65)
  escreva("\nVoc� precisa votar!")

  senao se(idade <16)
  escreva("\nVoc� n�o vota!")
  

  }
}
