from pickle import load, UnpicklingError, dump
from typing import Union

class File:
    @staticmethod
    def existe(arquivo: str, lista: bool = False) -> Union[dict, list]:
        try:
            arq = open(arquivo,'r')
            arq.close()
        except:
            print(f'Erro {arquivo}')
            return {} if not lista else []
        else:
            return File.load(arquivo) if not lista else File.load(arquivo, True)


    @staticmethod
    def load(arquivo: str, lista: bool = False) -> Union[dict, list]:
        try:
            with open(arquivo,'rb') as arq:
                return load(arq)
        except (EOFError, FileNotFoundError):
            print(f"O arquivo '{arquivo}' está vazio ou não foi encontrado. Retornando um dicionário vazio.")
            return {} if not lista else []
        except UnpicklingError:
            print(f"O arquivo '{arquivo}' está corrompido. Retornando um dicionário vazio.")
            return {} if not lista else []


    @staticmethod
    def save(produtos: Union[dict, list], arquivo: str, lista: bool = False) -> None:
        try:
            with open(arquivo, 'wb') as arq:
                dump(produtos, arq)
        except:
            print(f'Erro ao salvar {arquivo}')
            pr = {} if not lista else []
            with open(arquivo, 'wb') as arq:
                dump(pr, arq)
