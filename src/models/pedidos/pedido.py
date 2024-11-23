from src.interfaces.ipedido import IPedido


class Pedido(IPedido):
    def __init__(self, idd, cliente, lista, data):
        self._idd = idd
        self._cliente = cliente
        self._produtos = lista
        self._status = "Em andamento"
        self._data = data
        self._valor_total = self.somar_total()


    @property
    def idd(self):
        return self._idd

    @idd.setter
    def idd(self, idd):
        self._idd = idd


    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente


    @property
    def produtos(self):
        return self._produtos

    @produtos.setter
    def produtos(self, lista):
        self._produtos = lista


    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status


    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data


    @property
    def valor_total(self):
        return self._valor_total


    def somar_total(self):
        total = 0
        for produto in self.produtos:
            total += produto['Valor']
        return total


    @staticmethod
    def save_nome() -> str:
        return 'C:/Users/Daniel/PycharmProjects/JLGeleias_2.2/management_system/data/pedidos/save_pedidos.pickle'


    @classmethod
    def cadastrar(cls, idd, cliente, lista, data) -> IPedido:
        return cls(idd, cliente, lista, data)


    def detalhes(self) -> None:
        print(f'Id: {self.idd}\nCliente: {self.cliente.nome}\nData: {self.data}\nStatus: {self.status}')
        print('Lista de produtos:')
        for produto in self.produtos:
            print(f'un:{produto['Quantidade']:4} - {produto['Nome']:20} = R$ {produto['Valor']:.2f}')

        print(f'Valor Total: R$ {self.valor_total:.2f}')
        return