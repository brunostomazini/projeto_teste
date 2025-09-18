from .base_manager import BaseManager
from ..models import Pessoa


class PessoaManager(BaseManager):

    def find_by_name(self,nome:str)->list['Pessoa']:
        if isinstance(nome,str) and len(nome)>0:
            consulta=self.filter(name__icontains='nome')
            return list(consulta)
        else:
            raise TypeError('O nome deve ser string e nao...')
