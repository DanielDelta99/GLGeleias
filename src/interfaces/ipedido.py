from abc import *


class IPedido(ABC):

    @property
    @abstractmethod
    def idd(self):
        pass

    @idd.setter
    @abstractmethod
    def idd(self, idd):
        pass

    @property
    @abstractmethod
    def produtos(self):
        pass

    @produtos.setter
    @abstractmethod
    def produtos(self, lista):
        pass

    @staticmethod
    @abstractmethod
    def save_nome():
        return str

    @classmethod
    @abstractmethod
    def cadastrar(cls, idd, cliente, lista, data):
        pass

    @abstractmethod
    def detalhes(self):
        pass