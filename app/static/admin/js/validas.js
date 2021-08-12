/*--------validação cadastro de pizza----------------*/
let inputSabor = document.querySelector('#pizza_name')
let inputIngredientes = document.querySelector('#ingredient')
let inputPreco = document.querySelector('#price')
let inputImagem = document.querySelector('#url_image')
let vaiPizza = document.querySelector('#submit')

let saborOk = false
let ingredientesOk = false
let precoOk = false
let imagemOk = false
vaiPizza.disabled = true

inputSabor.addEventListener('keydown', () => { 
   /* Verifica se o tamanho do valor do inputSabor é menor que 2 */
   if(inputSabor.value.length < 2){
      inputSabor.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      saborOk = false
   } else {
      inputSabor.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      saborOk = true
   }

   if(inputSabor.value == '' || inputSabor.value == undefined || inputSabor.value == null) {
      inputSabor.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (saborOk && ingredientesOk && precoOk && imagemOk) {
      vaiPizza.disabled = false
   } else { /* se não, desabilita */
      vaiPizza.disabled = true
   }

})


inputIngredientes.addEventListener('keydown', () => { 
   /* Verifica se o tamanho do valor do inputIngredientes é menor que 2 */
   if(inputIngredientes.value.length < 2){
      inputIngredientes.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      ingredientesOk = false
   } else {
      inputIngredientes.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      ingredientesOk = true
   }

   if(inputIngredientes.value == '' || inputIngredientes.value == undefined || inputIngredientes.value == null) {
      inputIngredientes.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (saborOk && ingredientesOk && precoOk && imagemOk) {
      vaiPizza.disabled = false
   } else { /* se não, desabilita */
      vaiPizza.disabled = true
   }

})

inputPreco.addEventListener('keydown', () => { 
   /* Verifica se o tamanho do valor do inputPreco é menor que 2 */
   if(inputPreco.value.length < 2){
      inputPreco.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      precoOk = false
   } else {
      inputPreco.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      precoOk = true
   }

   if(inputPreco.value == '' || inputPreco.value == undefined || inputPreco.value == null) {
      inputPreco.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (saborOk && ingredientesOk && precoOk && imagemOk) {
      vaiPizza.disabled = false
   } else { /* se não, desabilita */
      vaiPizza.disabled = true
   }

})

inputImagem.addEventListener('keydown', () => { 
   /* Verifica se o tamanho do valor do inputImagem é menor que 2 */
   if(inputImagem.value.length < 2){
      inputImagem.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      imagemOk = false
   } else {
      inputImagem.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      imagemOk = true
   }

   if(inputImagem.value == '' || inputImagem.value == undefined || inputImagem.value == null) {
      inputImagem.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (saborOk && ingredientesOk && precoOk && imagemOk) {
      vaiPizza.disabled = false
   } else { /* se não, desabilita */
      vaiPizza.disabled = true
   }

})

vaiPizza.addEventListener('click', () => {
   /* Pega a div de carregamento */
   let carregamento = document.querySelector('#carregamento')
   /* Mostra a div de carregamento, adicionando o 'flex' ao display */
   carregamento.style.display = 'flex'

   /* Pega o Form */
   let form = document.querySelector('#cadastro--pizza')
   /* Esconde o Form, mudando o display pra 'none' */
   form.style.display = 'none'
})

/*----------------validação cadastro de admin-------------------*/
let inputNome = document.querySelector('#nome')
let inputSobrenome = document.querySelector('#sobrenome')
let inputEmail = document.querySelector('#email')
let inputTelefone = document.querySelector('#telefone')
let inputEndereco = document.querySelector('#endereco')
let inputSenha = document.querySelector('#senha')
let vaiAdmin = document.querySelector('#btn-do-cadastro-admin')

let nomeOk = false
let sobrenomeOk = false
let emailOk = false
let telefoneOk = false
let enderecoOk = false
let senhaOk = false
vaiAdmin.disabled = true

inputNome.addEventListener('keydown', () => { 
   /* Verifica se o tamanho do valor do inputNome é menor que 2 */
   if(inputNome.value.length < 2){
      inputNome.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      nomeOk = false
   } else {
      inputNome.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      nomeOk = true
   }

   if(inputNome.value == '' || inputNome.value == undefined || inputNome.value == null) {
      inputNome.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (nomeOk && sobrenomeOk && emailOk && telefoneOk && enderecoOk && senhaOk) {
      vaiAdmin.disabled = false
   } else { /* se não, desabilita */
      vaiAdmin.disabled = true
   }

})

inputSobrenome.addEventListener('keydown', () => { 
   /* Verifica se o tamanho do valor do inputSobrenome é menor que 2 */
   if(inputSobrenome.value.length < 2){
      inputSobrenome.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      sobrenomeOk = false
   } else {
      inputSobrenome.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      sobrenomeOk = true
   }

   if(inputSobrenome.value == '' || inputSobrenome.value == undefined || inputSobrenome.value == null) {
      inputSobrenome.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (nomeOk && sobrenomeOk && emailOk && telefoneOk && enderecoOk && senhaOk) {
      vaiAdmin.disabled = false
   } else { /* se não, desabilita */
      vaiAdmin.disabled = true
   }

})

inputEmail.addEventListener('keyup', () => {
   /* 
   O indexOf procura um caractere no valor do inputEmail, se esse valor não existir ele retorna -1. 
   Então essa expressão inputEmail.value.indexOf('@') == -1 é a mesmo coisa que:
   Se no valor de inputEmail não existir @, faça...

   || é o operador OU em JavaScript
   && é o operador E em JavaScript
   */
   if(inputEmail.value.indexOf('@') == -1 || inputEmail.value.indexOf('.') == -1){
      inputEmail.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      emailOk = false
   } else {
      inputEmail.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      emailOk = true
   }  

   /* Se todas as variáveis forem true habilita o botão */
   if (nomeOk && sobrenomeOk && emailOk && telefoneOk && enderecoOk && senhaOk) {
      vaiAdmin.disabled = false
   } else { /* se não, desabilita */
      vaiAdmin.disabled = true
   }
})

inputTelefone.addEventListener('keydown', () => { 
   /* Verifica se o tamanho do valor do inputTelefone é menor que 2 */
   if(inputTelefone.value.length < 2){
      inputTelefone.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      telefoneOk = false
   } else {
      inputTelefone.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      telefoneOk = true
   }

   if(inputTelefone.value == '' || inputTelefone.value == undefined || inputTelefone.value == null) {
      inputTelefone.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (nomeOk && sobrenomeOk && emailOk && telefoneOk && enderecoOk && senhaOk) {
      vaiAdmin.disabled = false
   } else { /* se não, desabilita */
      vaiAdmin.disabled = true
   }

})

inputEndereco.addEventListener('keydown', () => { 
   /* Verifica se o tamanho do valor do inputEndereco é menor que 2 */
   if(inputEndereco.value.length < 2){
      inputEndereco.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      enderecoOk = false
   } else {
      inputEndereco.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      enderecoOk = true
   }

   if(inputEndereco.value == '' || inputEndereco.value == undefined || inputEndereco.value == null) {
      inputEndereco.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (nomeOk && sobrenomeOk && emailOk && telefoneOk && enderecoOk && senhaOk) {
      vaiAdmin.disabled = false
   } else { /* se não, desabilita */
      vaiAdmin.disabled = true
   }

})

inputEndereco.addEventListener('keydown', () => { 
   /* Verifica se o tamanho do valor do inputEndereco é menor que 2 */
   if(inputEndereco.value.length < 2){
      inputEndereco.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      enderecoOk = false
   } else {
      inputEndereco.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      enderecoOk = true
   }

   if(inputEndereco.value == '' || inputEndereco.value == undefined || inputEndereco.value == null) {
      inputEndereco.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (nomeOk && sobrenomeOk && emailOk && telefoneOk && enderecoOk && senhaOk) {
      vaiAdmin.disabled = false
   } else { /* se não, desabilita */
      vaiAdmin.disabled = true
   }

})

inputSenha.addEventListener('keydown', () => { 
   /* Verifica se o tamanho do valor do inputSenha é menor que 2 */
   if(inputSenha.value.length < 2){
      inputSenha.style.borderColor = 'red' /* Troca a cor da borda do input para red */
      senhaOk = false
   } else {
      inputSenha.style.borderColor = 'green' /* Troca a cor da borda do input para green */
      senhaOk = true
   }

   if(inputSenha.value == '' || inputSenha.value == undefined || inputSenha.value == null) {
      inputSenha.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (nomeOk && sobrenomeOk && emailOk && telefoneOk && enderecoOk && senhaOk) {
      vaiAdmin.disabled = false
   } else { /* se não, desabilita */
      vaiAdmin.disabled = true
   }

})

vaiAdmin.addEventListener('click', () => {
   /* Pega a div de carregamento */
   let carregamento = document.querySelector('#carregamento')
   /* Mostra a div de carregamento, adicionando o 'flex' ao display */
   carregamento.style.display = 'flex'

   /* Pega o Form */
   let form = document.querySelector('#cadastro--admin')
   /* Esconde o Form, mudando o display pra 'none' */
   form.style.display = 'none'
})