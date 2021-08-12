/*ao iniciar a página do admin, mostra inicialmente a tela de cadastro*/
document.querySelector('#cadastro--pizza').style.display = 'flex'
document.querySelector('#tabela--pizzas').style.display = 'none'
document.querySelector('#tabela--pedidos').style.display = 'none'
document.querySelector('#cadastro--admin').style.display = 'none'

const btnCadastrarPizza = document.querySelector('#cadastrarPizza')
const btnListarPizzas = document.querySelector('#listarPizzas')
const btnListarPedidos = document.querySelector('#listarPedidos')
const btnCadastrarAdmin = document.querySelector('#cadastrarAdmin')

btnCadastrarPizza.addEventListener('click', () => {
    document.querySelector('#cadastro--pizza').style.display = 'flex'
    document.querySelector('#tabela--pizzas').style.display = 'none'
    document.querySelector('#tabela--pedidos').style.display = 'none'
    document.querySelector('#cadastro--admin').style.display = 'none'
})

btnListarPizzas.addEventListener('click', () => {
    document.querySelector('#tabela--pizzas').style.display = 'flex'
    document.querySelector('#cadastro--pizza').style.display = 'none'
    document.querySelector('#tabela--pedidos').style.display = 'none'
    document.querySelector('#cadastro--admin').style.display = 'none'
})

btnListarPedidos.addEventListener('click', () => {
    document.querySelector('#tabela--pedidos').style.display = 'flex'
    document.querySelector('#cadastro--pizza').style.display = 'none'
    document.querySelector('#tabela--pizzas').style.display = 'none'
    document.querySelector('#cadastro--admin').style.display = 'none'
})

btnCadastrarAdmin.addEventListener('click', () => {
    document.querySelector('#cadastro--admin').style.display = 'flex'
    document.querySelector('#cadastro--pizza').style.display = 'none'
    document.querySelector('#tabela--pizzas').style.display = 'none'
    document.querySelector('#tabela--pedidos').style.display = 'none'
})