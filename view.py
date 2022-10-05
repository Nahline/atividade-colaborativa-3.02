from typing import List

from models import Pessoa, Estudante, Docente

class View:

    def exibirMenu(self):
        return '''1. Exibir Menu
2. Cadastrar Estudante
3. Cadastrar Docente
4. Listar Pessoas
5. Sair'''

    def cadastrarEstudante(self):
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        idade = int(input('Idade: '))
        matricula = input('Matrícula: ')

        estudante = Estudante(
            nome=nome,
            telefone=telefone,
            idade=idade,
            matricula=matricula)
        return estudante

    def cadastrarDocente(self):
        nome = input('Nome: ')
        telefone = input('Telefone: ')
        idade = int(input('Idade: '))
        turma = input('Turma: ')

        docente = Docente(
            nome=nome,
            telefone=telefone,
            idade=idade,
            turma=turma)
        return docente

    def listarPessoas(self, pessoas: List[Pessoa]):
        for pessoa in pessoas:
            print(pessoa.toString())