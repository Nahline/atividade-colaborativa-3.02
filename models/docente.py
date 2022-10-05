from models.pessoa import Pessoa


class Docente(Pessoa):
    __turma = str

    def __init__(self, nome, telefone, idade, turma):
        self.__turma = turma
        super().__init__(nome, telefone, idade)

    @property
    def turma(self):
        return self.__turma

    @turma.setter
    def turma(self, value):
        self.__turma = value

    def __str__(self) -> str:
        return f'nome={self.nome}, telefone={self.telefone}, idade={self.idade}, turma={self.turma}'

    def toString(self):
        return self.__str__()
