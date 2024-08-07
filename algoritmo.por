programa {
  funcao inicio() {
// Algoritmo do voto obrigatório
  inteiro idade

  escreva("Qual é a sua idade?")
  leia(idade)

  se (idade >=18 e idade >=65)
  escreva("\nVocê vota se preferir.")

  senao se(idade >=16 e idade<18 ou idade< 65)
  escreva("\nVocê precisa votar!")

  senao se(idade <16)
  escreva("\nVocê não vota!")
  

  }
}
