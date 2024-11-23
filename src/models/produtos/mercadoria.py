from src.interfaces.iproduto import IProduto


class Mercadoria(IProduto):
    def __init__(self, idd: int = 0, tipo: str = 'Mercadoria', nome: str = 'Desconhecido', peso: float = 0, valor: float = 0, quantidade: int = 0):
        self._idd = idd
        self._tipo = tipo
        self._nome = nome
        self._peso = peso
        self._valor = valor
        self._quantidade = quantidade

    @property
    def idd(self):
        return self._idd

    @idd.setter
    def idd(self, idd):
        self._idd = idd

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        if peso > 0:
            self._peso = peso
        else:
            raise ValueError("Peso deve ser positivo.")

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor >= 0:
            self._valor = valor
        else:
            raise ValueError("Valor não pode ser negativo.")

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade


    @staticmethod
    def save_nome():
        return 'C:/Users/Daniel/PycharmProjects/JLGeleias_2.2/management_system/data/estoque/save_mercadorias.pickle'

    @classmethod
    def cadastrar(cls, idd: int = 0, tipo: str = 'Mercadoria', nome: str = 'Desconhecido', peso: float = 0, valor: float = 0, quantidade: int = 0) -> IProduto:
        return cls(idd, tipo, nome, peso, valor, quantidade)

    def detalhes(self):
        return f'Id: {self.idd}\nTipo: {self.tipo}\nNome: {self.nome}\nPeso: {self.peso} g\nValor: R$ {self.valor:.2f}\nQuantidade: {self.quantidade}'



