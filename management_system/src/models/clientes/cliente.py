from management_system.src.interfaces.icliente import ICliente


class Cliente(ICliente):
    def __init__(self, idd: int = 0, tipo: str = 'Cliente', nome: str = 'Desconhecido', cpf: str = '000', endereco: str = 'Sem endereço' , saldo: float = 0):
        self._idd = idd
        self._tipo = tipo
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
        self._saldo = saldo


    @property
    def idd(self):
        return self._idd

    @idd.setter
    def idd(self,idd):
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
    def nome(self,nome):
        self._nome = nome


    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self,cpf):
        self._cpf = cpf


    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self,endereco):
        self._endereco = endereco


    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        self._saldo = valor


    @staticmethod
    def save_nome():
        return 'C:/Users/Daniel/PycharmProjects/JLGeleias_2.2/management_system/data/clientes/save_cliente.pickle'


    @classmethod
    def cadastrar(cls, idd: int = 0, tipo: str = 'Cliente', nome: str = 'Desconhecido', cpf: str = '000',
                  endereco: str = 'Sem endereço',
                  saldo: float = 0) -> ICliente:
        return cls(idd, tipo, nome, cpf, endereco)


    def detalhes(self):
       return  f'Id: {self.idd}\nNome: {self.nome}\nCPF: {self.cpf}\nEndereço: {self.endereco}\nSaldo: R$ {self.saldo:.2f}'

