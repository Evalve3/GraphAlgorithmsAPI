from abc import abstractmethod


class Checker:
    def __init__(self, matrix: list, rows: int, columns: int):
        self.matrix: list = matrix
        self.rows: int = rows
        self.columns: int = columns

    @abstractmethod
    def check(self) -> bool:
        pass

    def __len__(self):
        return len(self.matrix)


class CycledChecker(Checker):
    def check(self) -> bool:
        is_cycled = False
        edges = self.columns
        for i in range(edges):
            if self.dfs(i):
                is_cycled = True
                break
        return is_cycled

    def dfs(self, start: int, answer: list = None, visitedi: list = None, visitedj: list = None,
            colors: list = None) -> list:
        if answer is None:
            visitedi = [0] * self.rows
            visitedj = [0] * self.columns
            colors = ['white'] * self.rows
            answer = []
        if colors[start] == 'grey':
            answer.append(start)
        colors[start] = 'grey'
        if colors[start] != 'black':
            for i in range(self.rows):
                if visitedi[i] == 0:
                    for j in range(self.columns):
                        if visitedj[j] == 0:
                            if self.matrix[i][j] == 1 and colors[i] != 'white':
                                visitedi[i] = 1
                                visitedj[j] = 1
                                self.dfs(self.way(i, j), answer, visitedi, visitedj, colors)
                                colors[i] = 'black'
        colors[start] = 'black'
        return answer

    def way(self, row: int, column: int) -> int:
        for i in range(self.rows):
            if i != row:
                if self.matrix[i][column]:
                    return i
        return 0


class CorrectMatrixChecker(Checker):
    def check(self) -> bool:
        try:
            assert self.is_num_matrix()
            return True
        except AssertionError:
            return False

    def is_num_matrix(self):
        return all([all(map(lambda x: isinstance(x, int) or isinstance(x, float), m)) for m in self.matrix])
