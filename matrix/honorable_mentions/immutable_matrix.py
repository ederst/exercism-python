from typing import List, Tuple

# From mentor:
# Fun fact. If someone does: matrix.row(3)[0] = 5, this will alter the data stored in the matrix.
# Conversely, if they did matrix.column(3)[0] = 5, this would not update the matrix.
# Making row() behave like column() is simple.
# The reverse is a fair bit more tricky. Something to think about :)


class Matrix:

    __matrix: Tuple[Tuple[int]]

    def __init__(self, matrix_string: str):
        self.__matrix = tuple([tuple([int(x) for x in row.split()]) for row in matrix_string.splitlines()])

    def row(self, index: int) -> List[int]:
        return list(self.__matrix[index - 1])

    def column(self, index: int) -> List[int]:
        return [row[index - 1] for row in self.__matrix]
