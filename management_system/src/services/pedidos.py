from datetime import datetime, timedelta
from management_system.src.repositories.repositories_data import File
from management_system.src.services.estoque import Estoque
from management_system.src.utils.data_validation import Valid
from management_system.src.utils.id_generator import Id
from management_system.src.interfaces.ipedido import IPedido


class Pedidos:
    def __init__(self, pedido: IPedido) -> None:
        self._pedido = pedido
        self._save = pedido.save_nome()
        self._lista = File.existe(self._save, True)


    def fazer(self, cliente ,lista, estoque): # ver essa parte de agendar direito em
        option = Valid.opcoes('',['Agendar','Finalizar'])
        idd = Id.retorne()
        if option == 'Agendar':
            data = self.escolher_data()
            pedido = self._pedido.cadastrar(idd,cliente, lista, data)
        else:
            pedido = self._pedido.cadastrar(idd,cliente,lista, data = datetime.now().strftime('%d/%m/%Y'))
            self.finalizar(pedido, estoque)
        self._lista.append(pedido)
        self.save()


    def listar(self) -> bool:
        if not self._lista:
            print('Nenhum pedido foi listado')
            Valid.linha()
            return False
        print(f'{'n°':3}|{'nome':25}|{'valor':15}|{'data':15}|{'status':15}')
        Valid.linha()
        for n, pedido in enumerate(self._lista):
            print(f'{n:<3}|{pedido.cliente.nome:25}|R$ {pedido.valor_total:<12.2f}|{pedido.data:<15}|{pedido.status:<15}')
        Valid.linha()
        return True


    def detalhar(self,pedido: IPedido) -> None:
        pedido.detalhes()


    @staticmethod
    def escolher_data() -> type(datetime):
        # Loop para coletar e validar uma data de agendamento
        while True:
            data_input = input('Digite a data para o agendamento (formato dd/mm/aaaa): ')
            try:
                # Converte a string para um objeto datetime no formato esperado
                data = datetime.strptime(data_input, '%d/%m/%Y')
                # verifica quantidade de dias no futuro
                limite_maximo = datetime.now() + timedelta(days=30)
                if data > limite_maximo:
                    print('\033[31mA data não pode ser mais de 30 dias no futuro.\033[m')
                    continue
                # Verifica se a data é no futuro
                if data > datetime.now():
                    print(f'Data agendada para {data.strftime('%d/%m/%Y')}.')
                    return data.strftime('%d/%m/%Y')
                else:
                    print('\033[31mA data deve ser no futuro. Tente novamente.\033[m')
            except ValueError:
                print('\033[31mFormato de data inválido. Use o formato dd/mm/aaaa.\033[m')


    def return_pedido(self):# nao é para retornar o que nao existe
        try:
            pedido = self.listar()
            if pedido:
                indice = Valid.escolha('Numero: ', self._lista)
                return self._lista[indice]
            else:
                return False
        except:
            print('Erro ao retornar pedido')


    def finalizar(self, pedido: IPedido, estoque: type(Estoque)) -> None: # inclementar a parte de pagamento
        if pedido.status == 'Finalizado':
            print('O pedido já foi finalizado')
            return
        lista = pedido.produtos
        teste = estoque.conferir(lista)
        if teste:
            estoque.retirar(lista)
            pedido.status = 'Finalizado'
            self.save()
            print('Pedido Finalizado com sucesso')
        else:
            print('Estoque insuficiente')


    def atualizar(self,pedido): #Tem que inclementar muita coisa em
        self.detalhar(pedido)
        pass


    def deletar(self, pedido: IPedido) -> None:
        try:
            for n, pedido1 in enumerate(self._lista):
                if pedido1.idd == pedido.idd:
                    option = Valid.opcoes(f'Excluir pedido?', ['Confirmar', 'Cancelar'])
                    if option == 'Confirmar':
                        del self._lista[n]
                        print(f'pedido removido com sucesso.')
                        Valid.linha()
                        self.save()
                        return
                    else:
                        return
            print(f'pedido não foi encontrado.')
        except:
            print('Erro ao deletar pedido')


    def save(self) -> None:
        try:
            File.save(self._lista, self._save, True)
        except:
            print('Erro ao salvar pedido')

    def load(self) -> None:
        try:
            self._lista = File.load(self._save, True)
            print('Load pedidos sucesso')
        except:
            print('Erro load pedidos')