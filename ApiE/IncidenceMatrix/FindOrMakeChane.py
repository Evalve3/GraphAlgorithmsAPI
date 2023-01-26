from ApiE.IncidenceMatrix import IncidenceMatrixCheckers
from ApiE.Algorithm import Algorithm
from ApiE.expections import MatrixException


class ChaneCreate(Algorithm):
    def do_algorithm(self, *args, **kwargs):
        self.find()

    def check_matrix(self, *args, **kwargs):

        if not IncidenceMatrixCheckers.CorrectMatrixChecker(self.matrix, self.__columns, self.__rows).check():
            raise MatrixException("Матрица не корректна")

    __rows: int
    __columns: int

    def __init__(self, incident_matrix: list) -> None:
        self.__rows = len(incident_matrix)
        self.__columns = len(incident_matrix[0])
        super().__init__(incident_matrix)

    def __remove(self, node_index: int) -> None:
        self.__rows -= 1
        tmp = self.matrix.pop(node_index)
        edge_index = []
        for i in range(len(tmp)):
            if tmp[i]:
                edge_index.append(i)
        for index in edge_index:
            for rows in range(self.__rows):
                self.matrix[rows][index] = 0
        self.__del_zero_columns()

    def __del_zero_columns(self) -> None:
        tmp = []
        for columns in range(self.__columns):
            k = 0
            for rows in range(self.__rows):
                if not self.matrix[rows][columns]:
                    k += 1
            if k == self.__rows:
                tmp.append(columns)
        k = 0
        for column in tmp:
            for row in range(self.__rows):
                self.matrix[row].pop(column - k)
            self.__columns -= 1
            k += 1

    def show(self) -> None:
        print(*[row for row in self.matrix], sep='\n')

    def find(self) -> None:
        checker = IncidenceMatrixCheckers.CycledChecker(self.matrix, self.__rows, self.__columns)
        answer = checker.dfs(0)
        answer.sort()
        break_flag = False
        k = 0

        for i in answer:
            self.__remove(i - k)
            k += 1
            for j in range(self.__rows):
                checker = IncidenceMatrixCheckers.CycledChecker(self.matrix, self.__rows, self.__columns)
                if not checker.dfs(j):
                    break_flag = True
                    break
            if break_flag:
                break
