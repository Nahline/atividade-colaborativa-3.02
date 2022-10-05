class Pessoa:
    # Atributos protegidos para que sejam herdados
    _nome: str
    _telefone: str
    _idade: int

    def __init__(self, nome, telefone, idade):
        self._nome = nome
        self._telefone = telefone
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, value):
        self._telefone = value

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        self._idade = value

    def __str__(self) -> str:
        return f'nome={self.nome}, telefone={self.telefone}, idade={self.idade}'
    
    def toString(self):
        return self.__str__()