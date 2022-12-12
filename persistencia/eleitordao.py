from persistencia.dao import DAO

class EleitorDAO(DAO):
    def __init__(self):
        super().__init__('eleitores.pkl')
    
    def add(self, cpf, eleitor):
        super().add(cpf, eleitor)

    def get(self, key):
        return super().get(key)
    
    def remove(self, key):
        return super().remove(key)
