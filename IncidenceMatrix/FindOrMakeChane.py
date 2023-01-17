from IncidenceMatrix import IncidenceMatrixCheckers


class ChaneCreate:
    __incident_matrix: list
    __rows: int
    __columns: int

    def __init__(self, incident_matrix: list) -> None:
        self.__incident_matrix = list(incident_matrix)
        self.__rows = len(incident_matrix)
        self.__columns = len(incident_matrix[0])

    def __remove(self, node_index: int) -> None:
        self.__rows -= 1
        tmp = self.__incident_matrix.pop(node_index)
        edge_index = []
        for i in range(len(tmp)):
            if tmp[i]:
                edge_index.append(i)
        for index in edge_index:
            for rows in range(self.__rows):
                self.__incident_matrix[rows][index] = 0
        self.__del_zero_columns()

    def __del_zero_columns(self) -> None:
        tmp = []
        for columns in range(self.__columns):
            k = 0
            for rows in range(self.__rows):
                if not self.__incident_matrix[rows][columns]:
                    k += 1
            if k == self.__rows:
                tmp.append(columns)
        k = 0
        for column in tmp:
            for row in range(self.__rows):
                self.__incident_matrix[row].pop(column - k)
            self.__columns -= 1
            k += 1

    def show(self) -> None:
        print(*[row for row in self.__incident_matrix], sep='\n')

    def find(self) -> None:
        checker = IncidenceMatrixCheckers.CycledChecker(self.__incident_matrix, self.__rows, self.__columns)
        answer = checker.dfs(0)
        answer.sort()
        break_flag = False
        k = 0

        for i in answer:
            self.__remove(i - k)
            k += 1
            for j in range(self.__rows):
                checker = IncidenceMatrixCheckers.CycledChecker(self.__incident_matrix, self.__rows, self.__columns)
                if not checker.dfs(j):
                    break_flag = True
                    break
            if break_flag:
                break
