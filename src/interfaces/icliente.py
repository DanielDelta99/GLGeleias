from abc import *


class ICliente(ABC):
    @abstractstaticmethod
    def save_nome():
        return str


    @abstractclassmethod
    def cadastrar(cls, idd, nome, cpf, endereco):
        pass


    @abstractmethod
    def detalhes(self):
        pass


