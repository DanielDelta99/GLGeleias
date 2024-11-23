from management_system.src.interfaces.iproduto import IProduto
from management_system.src.repositories.repositories_data import File
from management_system.src.utils.data_validation import Valid
from management_system.src.utils.id_generator import Id


class Estoque:
    def __init__(self, objeto: IProduto) -> None:
        self._save = objeto.save_nome()
        self._lista = File.existe(self._save, True)
        self.__objeto = objeto


    def listar(self) -> bool:# testar
        if not self._lista:
            print('Nenhum produto foi listado')
            Valid.linha()
            return False
        print(f'{"ID":<3} - {"Nome":<23}     {"Total":<10}')
        Valid.linha()
        for n, produto in enumerate(self._lista):
            print(f'{n:<3} - {produto.nome:<27}|un: {produto.quantidade:<10}')
            Valid.linha()
        return True


    def detalhes(self) -> IProduto:# testar
        while True:
            indice = Valid.escolha('Indice: ', self._lista)
            produto = self._lista[indice]
            Valid.linha()
            print(produto.detalhes())
            Valid.linha()
            return produto


    def cadastrar(self) -> None:# testar
        while True:
            nome = Valid.leianome('Nome: ')
            if nome not in self._lista:
                peso = Valid.leiaint('Peso: ')
                valor = Valid.leiafloat('Valor: ')
                quantidade = Valid.leiaint('Quantidade: ')
                idd = Id.retorne()
                produto = self.__objeto.cadastrar(idd = idd, nome = nome, peso = peso ,valor = valor, quantidade = quantidade)
                self._lista.append(produto)
                print(f'produto Cadastrado com sucesso')
                self.__save()
            else:
                print('\033[31mEsse produto já existe em nosso banco de dados.\033[m')
            break


    def deletar(self, produto: IProduto) -> None:# testar
        try:
            for n, cliente1 in enumerate(self._lista):
                if cliente1.idd == produto.idd:
                    option = Valid.opcoes(f'Excluir {produto.tipo}', ['Confirmar', 'Cancelar'])
                    if option == 'Confirmar':
                        del self._lista[n]
                        print(f'{produto.nome} removido com sucesso.')
                        Valid.linha()
                        self.__save()
                        return
                    else:
                        return
            print(f'{produto.nome} não foi encontrado.')
        except:
            print('Erro ao  deletar')


    def atualizar(self, produto: IProduto) -> None: #incompleto

        nome = Valid.leianome('Nome: ')
        peso = Valid.leiaint('Peso: ')
        valor = Valid.leiafloat('Valor: ')
        quantidade = Valid.leiaint('Quantidade: ')
        option = Valid.opcoes('',['Confirmar','Cancelar'])
        if option == 'Confirmar':
            if nome != '':
                produto.nome = nome
            if peso != '':
                produto.peso = peso
            if valor != '':
                produto.valor = valor
            if quantidade != '':
                produto.quantidade = quantidade
            print(f'Produto {produto.nome} atualizado com sucesso.')
            self.__save()
        else:
            print('Atualização cancelada.')


    def produção(self) -> None: # testar
        for n, produto in enumerate(self._lista):
            print(f'{n:>3} - {produto.nome:28}',end='')
            produto.quantidade += Valid.leiaint(' - un: ')
        print('Estoque atualizado com sucesso')
        self.__save()


    def escolher(self) -> list:
        lista = []
        for n, produto in enumerate(self._lista):
            dicio = {}
            print(f'{n:<2} - {produto.nome:30}', end='')
            dicio['Nome'] = produto.nome
            dicio['Quantidade']  = Valid.leiaint('Un: ')
            dicio['Valor'] = produto.valor * dicio['Quantidade']
            lista.append(dicio)
        return lista


    def conferir(self, lista: list) -> bool:
        for produto_estoque in self._lista:
            for produto_cliente in lista:
                if produto_estoque.nome == produto_cliente['Nome'] and produto_estoque.quantidade < produto_cliente['Quantidade']:
                    return False
        return True


    def retirar(self, lista: list) -> None:
        for produto_estoque in self._lista:
            for produto_cliente in lista:
                if produto_estoque.nome == produto_cliente['Nome']:
                    produto_estoque.quantidade -= produto_cliente['Quantidade']
        print('Produtos retirados do estoque')
        self.__save()


    def __save(self) -> str:
        try:
            File.save(self._lista, self._save,True)
            return 'Salvamento comcluido'
        except:
            return 'Falha no salvamento'


    def load(self) -> str:
        try:
            self._lista = File.load(self._save, True)
            print('Load estoque sucesso')
        except:
            print('Erro no load do estoque')

