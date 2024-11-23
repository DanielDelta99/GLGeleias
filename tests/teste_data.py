from datetime import datetime, timedelta

from datetime import datetime, timedelta
from colorama import Fore, Style


def escolher_data():
    while True:
        data_input = input("Digite a data para o agendamento (formato dd/mm/aaaa): ")
        try:
            # Converte a string para um objeto datetime no formato esperado
            data = datetime.strptime(data_input, "%d/%m/%Y")

            # Limite máximo de 30 dias no futuro
            limite_maximo = datetime.now() + timedelta(days=30)
            if data > limite_maximo:
                print(Fore.RED + "A data não pode ser mais de 30 dias no futuro." + Style.RESET_ALL)
                continue

            # Verifica se a data é no futuro
            if data > datetime.now():
                print(f"Data agendada para {data.strftime('%d/%m/%Y')}.")
                return data.strftime('%d/%m/%Y')
            else:
                print(Fore.RED + "A data deve ser no futuro. Tente novamente." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Formato de data inválido. Use o formato dd/mm/aaaa." + Style.RESET_ALL)


data = escolher_data()
print(data)