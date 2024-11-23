from abc import *


class IProduto(ABC):
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
    def tipo(self):
        pass

    @tipo.setter
    @abstractmethod
    def tipo(self, tipo):
        pass

    @property
    @abstractmethod
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass

    @property
    @abstractmethod
    def peso(self):
        pass

    @peso.setter
    @abstractmethod
    def peso(self, peso):
        pass

    @property
    @abstractmethod
    def valor(self):
        pass

    @valor.setter
    @abstractmethod
    def valor(self, valor):
        pass

    @property
    @abstractmethod
    def quantidade(self):
        pass

    @quantidade.setter
    @abstractmethod
    def quantidade(self, quantidade):
        pass

    @staticmethod
    @abstractmethod
    def save_nome():
        return str

    @classmethod
    @abstractmethod
    def cadastrar(cls,idd,nome,valor,peso,quantidade) -> object:
        pass

    @abstractmethod
    def detalhes(self):
        pass