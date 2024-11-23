class Valid:
    @staticmethod
    def linha(tipo='-', tamanho=75):
        print(tipo * tamanho)

    @staticmethod
    def cabecalho(msg=''):
        Valid.linha()
        print(f'{msg:^75}')
        Valid.linha()

    @staticmethod
    def opcoes(msg, lista, simples = False):
        if msg and simples:
            print(msg)
        if msg and not simples:
            Valid.cabecalho(msg)
        for i, l in enumerate(lista):
            print(f'[{i + 1}] - {l}')
        while True:
            n = Valid.leiaint('Opção: ')
            if 0 < n <= len(lista):
                Valid.linha()
                return lista[n-1]
            else:
                print('\033[31mDigite uma opção válida.\033[m')


    @staticmethod
    def escolha(msg, lista):
        while True:
            n = Valid.leiaint(msg if msg != '' else 'Opção: ')
            if 0 <= n < len(lista):
                Valid.linha()
                return n
            else:
                print('Digite uma opção valida')


    @staticmethod
    def leianome(msg):  # gpt melhorado
        while True:
            nome = str(input(msg)).strip().lower()
            divisao = nome.split()
            nome = ''.join(divisao)
            if not nome:
                print('\033[31mERRO: Caracteres inválidos.\033[m')
            elif nome.isalnum():
                nome = ' '.join(divisao)
                return nome.title()
            else:
                print('\033[31mERRO: Caracteres inválidos.\033[m')

    @staticmethod
    def leiaint(msg):  # gpt melhorado
        while True:
            try:
                n = input(msg).strip()
                if n in '':
                    n = 0
                return int(n)
            except ValueError:
                print('\033[31mERRO: por favor, digite um número válido.\033[m')

    @staticmethod
    def leiafloat(msg):  # gpt melhorado
        while True:
            try:
                n = input(msg).replace(',', '.').strip()
                if n in '':
                    n = 0
                return float(n)
            except ValueError:
                print('\033[31mERRO: por favor, digite um número válido\033[m')


    @staticmethod
    def busca_objetos(lista):
        filtro = []
        nome = Valid.leianome('Nome: ')
        for objeto in lista:
            if nome in objeto.nome:
                filtro.append(objeto)
        if not filtro:
            print('Não encontramos no banco de dados.')
            option = Valid.opcoes('Quer ver a lista? ', ['Sim', 'Não'], True)
            if option == 'Sim':
                for n, objeto in enumerate(lista):
                    print(n + 1, objeto.nome)
                indice = Valid.escolha(lista)
                return lista[indice]
            else:
                return
        else:
            for n, objeto in enumerate(filtro):
                print(n + 1, objeto.nome)
            indice = Valid.escolha(filtro)
            return filtro[indice]