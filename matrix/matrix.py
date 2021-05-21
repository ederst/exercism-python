from typing import List


class Matrix:
    __matrix: List[List[int]]

    def __init__(self, matrix_string: str):
        self.__matrix = [list(map(int, row.split(' '))) for row in matrix_string.splitlines()]

    def row(self, index: int) -> List[int]:
        return self.__matrix[index - 1]

    def column(self, index: int) -> List[int]:
        return [row[index - 1] for row in self.__matrix]
