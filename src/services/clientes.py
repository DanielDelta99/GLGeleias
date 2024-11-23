from src.repositories.repositories_data import File
from src.utils.data_validation import Valid
from src.utils.id_generator import Id
from src.interfaces.icliente import ICliente


class Clientes:
    def __init__(self, cliente: ICliente) -> None:
        self.__save = cliente.save_nome()
        self.__lista = File.existe(self.__save, True)
        self.__cliente = cliente


    def listar(self) -> bool:# testar
        if not self.__lista:
            print(f'Lista vazia')
            Valid.linha()
            return False
        print(f'{"ID":<3} - {"Nome":<25}{"Saldo":<10}')
        Valid.linha()
        for n, cliente in enumerate(self.__lista):
            print(f'{n:<3} - {cliente.nome:<25}|R$ {cliente.saldo:<10}')
            Valid.linha()
        return True


    def detalhes(self) -> ICliente:# testar
        while True:
            indice = Valid.escolha('Indice: ', self.__lista)
            try:
                cliente = self.__lista[indice]
                Valid.linha()
                print(cliente.detalhes())
                Valid.linha()
                return cliente
            except:
                print('Id não encontrado')


    def pesquisar(self) -> ICliente:# testar
        filtro = []
        nome = Valid.leianome('Nome: ')
        for objeto in self.__lista:
            if nome in objeto.nome:
                filtro.append(objeto)
        if not filtro:
            print('Não encontramos no banco de dados.')
            option = Valid.opcoes('Quer ver a lista? ', ['Sim', 'Não'], True)
            if option == 'Sim':
                return self.listar_return()
            else:
                cliente = self.__cliente.cadastrar(idd = 0, nome = 'Desconhecido', cpf = '000', endereco = '')
                return cliente
        else:
            for n, objeto in enumerate(filtro):
                print(n, objeto.nome)
            indice = Valid.escolha('', filtro)
            cliente = filtro[indice]
            return cliente


    def listar_return(self) -> ICliente:
        for n, objeto in enumerate(self.__lista):
            print(n, objeto.nome)
        indice = Valid.escolha('', self.__lista)
        return self.__lista[indice]


    def cadastrar_none(self) -> ICliente:
        return self.__cliente.cadastrar(idd = 0, nome = 'Desconhecido', cpf = '000', endereco = '')

    def cadastrar(self) -> None:
        while True:
            nome = Valid.leianome('Nome: ')
            if nome not in self.__lista:
                cpf = Valid.leianome('CPF: ')
                endereco = Valid.leianome('Endereço: ')
                idd = Id.retorne()
                cliente = self.__cliente.cadastrar(idd = idd, nome = nome, cpf = cpf, endereco = endereco)
                self.__lista.append(cliente)
                print(f'{cliente.tipo} cadastrado com sucesso')
                self.save()
            else:
                print(f'\033[31mEsse {self.__cliente.tipo} já existe em nosso banco de dados.\033[m')
            break


    def deletar(self, cliente) -> None:# testar
        try:
            for n, cliente1 in enumerate(self.__lista):
                if cliente1.idd == cliente.idd:
                    option = Valid.opcoes(f'Excluir {cliente.tipo}',['Confirmar','Cancelar'])
                    if option == 'Confirmar':
                        del self.__lista[n]
                        print(f'{cliente.nome} removido com sucesso.')
                        Valid.linha()
                        self.save()
                        return
                    else:
                        return
            print(f'{cliente.nome} não foi encontrado.')
        except:
            print('Erro ao  deletar')


    def atualizar(self, cliente: ICliente) -> None:# testar

        nome = Valid.leianome('Nome: ')
        cpf = Valid.leianome('CPF: ')
        endereco = Valid.leianome('Endereço: ')
        option = Valid.opcoes('', ['Confirmar', 'Cancelar'])
        if option == 'Confirmar':
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.endereco = endereco
            print(f'{cliente.nome} atualizado com sucesso.')
            self.save()
        else:
            print('Atualização cancelada.')


    def save(self) -> None:
        File.save(self.__lista, self.__save, True)


    def load(self) -> None:
        try:
            self.__lista = File.load(self.__save, True)
            print('Load clientes sucesso')
        except:
            print('Erro load clientes')

