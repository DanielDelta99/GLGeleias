from management_system.src.interfaces import IPedido
from management_system.src.models.pedidos import Pedido
from management_system.src.utils.data_validation import Valid
from management_system.src.models.clientes import Cliente, Fornecedor
from management_system.src.models.produtos import Mercadoria, Materia_Prima
from management_system.src.services import Clientes, Estoque, Pedidos

lista_clientes = [Cliente(), Fornecedor()]
lista_produtos = [Mercadoria(), Materia_Prima()]
lista_pedidos = []


class System:
    @staticmethod
    def cadastrar():
        option = Valid.opcoes('', ['Clientes', 'Produtos'])
        if option == 'Clientes':
            cliente = System.config(lista_clientes)
            Clientes(cliente).cadastrar()
        else:
            produto = System.config(lista_produtos)
            Estoque(produto).cadastrar()


    @staticmethod
    def clientes():
        #cliente = System.config(lista_clientes)
        clientes = Clientes(Cliente())
        clientes.load()
        while True:
            teste = clientes.listar()
            if teste:
                option = Valid.opcoes('', ['Detalhes', 'Sair'])
            else:
                break
            if option == 'Detalhes':
                cliente = clientes.detalhes()
                option = Valid.opcoes('', ['Continuar', 'Atualizar', 'Deletar'])
                if option == 'Atualizar':
                    clientes.atualizar(cliente)
                    continue
                elif option == 'Deletar':
                    clientes.deletar(cliente)
                    continue
                else:
                    continue
            else:
                break


    @staticmethod
    def estoque():
        estoque = Estoque(Mercadoria())
        estoque.load()
        while True:
            lista = estoque.listar()
            if lista:
                option = Valid.opcoes('', ['Detalhes', 'Sair'])
            else:
                break
            if option == 'Detalhes':
                produto = estoque.detalhes()
                option = Valid.opcoes('', ['Continuar', 'Atualizar', 'Deletar',])
                if option == 'Atualizar':
                    estoque.atualizar(produto)
                    continue
                elif option == 'Deletar':
                    estoque.deletar(produto)
                    continue
            else:
                break


    @staticmethod
    def producao():
        estoque = Estoque(Mercadoria())
        estoque.load()
        estoque.produção()


    @staticmethod
    def vendas():# Em obras
        pedidos = Pedidos(Pedido(idd=0, cliente=None, lista=[], data=None))
        clientes = Clientes(Cliente())
        estoque = Estoque(Mercadoria())

        estoque.load()
        option = Valid.opcoes('Pedidos', ['Fazer Pedido', 'Lista de Pedidos'])
        if option == 'Fazer Pedido':
            option  = Valid.opcoes('Definir cliente',['Pesquisar','Listar','None'])
            if option == 'Pesquisar':
                cliente = clientes.pesquisar()
            elif option == 'Listar':
                cliente = clientes.listar_return()
            else:
                cliente = clientes.cadastrar_none()
            Valid.cabecalho('Escolher produtos')
            lista = estoque.escolher()
            Valid.linha()
            pedidos.fazer(cliente = cliente, lista = lista, estoque = estoque)
        else:
            pedido = pedidos.return_pedido()
            if pedido:
                option = Valid.opcoes('', ['Detalhes', 'Sair'])
                if option == 'Detalhes':
                    pedidos.detalhar(pedido)
                    option = Valid.opcoes('Pedidos', ['Atualizar', 'Finalizar', 'Excluir', 'Sair'])
                    if option == 'Atualizar':
                        pedidos.atualizar(pedido)
                    elif option == 'Finalizar':
                        pedidos.finalizar(pedido, estoque)
                    elif option == 'Excluir':
                        pedidos.deletar(pedido)
                    else:
                        pass


    @staticmethod
    def config(classes: list):
        for n, classe in enumerate(classes):
            print(f'{n} - {classe.tipo}')
        indice = Valid.escolha('', classes)
        return classes[indice]


    @staticmethod
    def config2(classes: list, classes2: list):
        for n, classe in enumerate(classes):
            print(f'{n} - {classe.tipo}')
        indice = Valid.escolha('', classes)
        return classes[indice], classes2[indice]


