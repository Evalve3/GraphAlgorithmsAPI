from AdjacencyMatrixCheckers import CorrectAdjacencyMatrixChecker, CycledChecker
from expections import CycledException, MatrixException


class HeightsGraph:
    def __init__(self, matrix: list) -> None:
        # выполняет шаг 0 в т.ч
        HeightsGraph.check_matrix(matrix)
        self.matrix: list = matrix
        for i in range(len(self)):
            self.matrix[i].insert(0, None)
        self.marked_lines = set()

    @staticmethod
    def check_matrix(matrix):
        if not CorrectAdjacencyMatrixChecker(matrix).check():
            raise MatrixException("Матрица не является матрицей смежности")
        if CycledChecker(matrix).check():
            raise CycledException("Граф цикличен")

    def __check_column(self, column_number: int) -> bool:
        # column_number не должен быть меньше 1
        if column_number < 1:
            raise IndexError('column_number не должен быть меньше 1')
        column = [int(self.matrix[line][column_number]) for line in range(len(self.matrix))]  # список столбца
        return any(column)  # если столбец ненулевой,то вернет True

    def __stage0(self) -> None:
        for column in range(1, len(self) + 1):  # все столбцы кроме 0(он добавочный)
            if not self.__check_column(column):
                self.matrix[column - 1][
                    0] = '0'  # в данном случае помечаем строку,которая соотвествует column в добавленном столбце
                self.marked_lines.add(column - 1)  # возврат к нумерации с 0

    def __stage1(self, k: int) -> int:
        tmp_list = []
        for column in range(1, len(self) + 1):
            flag = True
            for line in range(len(self)):
                if (self.matrix[line][column] == 1) and (
                        line not in self.marked_lines):  # все нулевые в шаге 2 помечаются
                    flag = False
            if flag and ((column - 1) not in self.marked_lines):
                tmp_list.append(column - 1)
                self.matrix[column - 1][0] = str(k)
        for x in tmp_list:
            self.marked_lines.add(x)
        k += 1
        return k

    def calc_all_heights(self) -> None:
        self.__stage0()
        k = 1
        while self.__check_add_column():
            k = self.__stage1(k)

    def __check_add_column(self) -> bool:
        # проверяет,что в добавленном столбце еще есть незаполненные вершины
        add_column = [self.matrix[line][0] for line in range(len(self))]
        return not all(add_column)

    def print_matrix(self) -> None:
        print()
        for i in range(len(self)):
            for j in range(len(self)):
                if self.matrix[i][j] is None:
                    print('-', end=' ')
                else:
                    print(self.matrix[i][j], end=' ')
            print()

    def __len__(self) -> int:
        return len(self.matrix)
