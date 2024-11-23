from pickle import load, dump


class Id:
    @staticmethod
    def retorne():
        try:
            with open('C:/Users/Daniel/PycharmProjects/JLGeleias_2.2/management_system/data/id_generator/save_id.pickle', 'rb') as arq:
                idd = int(load(arq))
        except FileNotFoundError:
            idd = 0
        finally:
            idd += 1
            Id.save_id(idd)
            return idd

    @staticmethod
    def save_id(idd):
        try:
            with open('C:/Users/Daniel/PycharmProjects/JLGeleias_2.2/management_system/data/id_generator/save_id.pickle', 'wb') as f:
                dump(idd, f)
        except:
            print(f'Erro ao salvar id')