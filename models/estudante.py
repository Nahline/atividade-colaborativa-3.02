from models.pessoa import Pessoa


class Estudante(Pessoa):
    __matricula = str

    def __init__(self, nome, telefone, idade, matricula):
        self.__matricula = matricula
        super().__init__(nome, telefone, idade)

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, value):
        self.__matricula = value

    def __str__(self) -> str:
        return f'nome={self.nome}, telefone={self.telefone}, idade={self.idade}, matricula={self.matricula}'

    def toString(self):
        return self.__str__()