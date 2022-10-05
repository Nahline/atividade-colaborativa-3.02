from typing import List
from models.pessoa import Pessoa
from view import View


class Controller:
    __model: List[Pessoa]
    __view: View

    def __init__(self, model, view) -> None:
        self.__model = model
        self.__view = view

    @staticmethod
    def main():
        return Controller(model=[], view=View())

    def run(self):
        comando = None
        while comando != 5:
            print(self.__view.exibirMenu())
            comando = int(input('Insira sua opção: ') or '0')

            match (comando):
                case 2:
                    estudante = self.__view.cadastrarEstudante()
                    self.__model.append(estudante)
                case 3:
                    docente = self.__view.cadastrarDocente()
                    self.__model.append(docente)
                case 4:
                    self.__view.listarPessoas(self.__model)
                case 1 | 5:
                    continue
                case _:
                    print('Comando não implementado, tente novamente.')
        
        print('Encerrando...')
