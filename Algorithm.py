from abc import abstractmethod
from expections import GraphException


class Algorithm:
    matrix: list

    def __init__(self, matrix):
        self.matrix = matrix
        self.check_matrix()

    @abstractmethod
    def check_matrix(self, *args, **kwargs):
        # method must rise GraphExceptions
        pass

    @abstractmethod
    def do_algorithm(self, *args, **kwargs):
        # do main algorithm
        pass

    @classmethod
    def get_request(cls, matrix):
        try:
            graph = cls(matrix)
            graph.do_algorithm()
            return {'matrix': graph.matrix}
        except GraphException as e:
            return {'error': e.args[0]}, 400
