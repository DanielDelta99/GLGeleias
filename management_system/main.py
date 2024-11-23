from management_system.src.system import System
from management_system.src.utils.data_validation import Valid


while True:
    Valid.cabecalho('JL GELEIAS')
    option = Valid.opcoes('', ['Cadastrar', 'Clientes', 'Estoque', 'Produção', 'Vendas', 'Sair'])
    if option == 'Cadastrar':
        System.cadastrar()
    elif option == 'Clientes':
        System.clientes()
    elif option == 'Estoque':
        System.estoque()
    elif option == 'Produção':
        System.producao()
    elif option == 'Vendas':
        System.vendas()
    else:
        break


