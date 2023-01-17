from abc import abstractmethod


class Checker:
    def __init__(self, matrix: list):
        self.matrix: list = matrix

    @abstractmethod
    def check(self) -> bool:
        pass

    def __len__(self):
        return len(self.matrix)


class CycledChecker(Checker):

    def __dfs(self, colors: list, start: int = 0, answer: bool = False) -> bool:
        # проверка на циклы от заданной вершины(по умолчанию 0) путем поиска в глубину
        # и раскраски в 3 цвета. Белые - не посещенные вершины, серые - посещенные, черные - точно не состоят в цикле
        if len(colors) == 0:
            colors = ['white'] * len(self.matrix)
        if colors[start] == 'grey':
            answer = True
            return answer
        colors[start] = 'grey'
        if colors[start] != 'black':
            for i in range(len(self.matrix)):
                if self.matrix[start][i]:
                    answer = self.__dfs(colors, i, answer)
                    colors[i] = 'black'
        colors[start] = 'black'
        return answer

    def check(self) -> bool:
        # Проверяет граф на циклы. Запускает проверку на циклы поиском в глубину от каждой вершины
        try:
            is_cycled = False
            edges = range(len(self))
            for i in edges:
                if self.__dfs(list(), i):
                    is_cycled = True
                    break
            return is_cycled
        # В алгоритме для матрицы смежности какой-то баг
        # Не всегда находит циклы, поэтому костыль временный (или не временный)
        except RecursionError:
            return True


class CorrectAdjacencyMatrixChecker(Checker):
    def check(self) -> bool:
        try:
            assert self.is_num_matrix()
            assert self.is_square_matrix()
            return True
        except AssertionError:
            return False

    def is_square_matrix(self):
        return len(self.matrix) == len(self.matrix[0])

    def is_num_matrix(self):
        return all([all(map(lambda x: isinstance(x, int) or isinstance(x, float), m)) for m in self.matrix])
