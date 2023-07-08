from typing import Self
from dlxsudoku.algorithm_x import Matrix


class Sudoku6x6:
    grid: list[list[int | None]]
    MATRIX_ROWS = 6 * 6 * 6

    def __init__(self, grid) -> None:
        self.grid = grid

    def to_matrix(self) -> Matrix:
        """
        Rows of the matrix are in the order 
        R1C1#1, R1C1#2, ..., R1C2#1, R1C2#2, ...
        """

        matrix = self._row_column_constraints() + self._row_number_constraints() + self._col_number_constraints() + self._box_number_constraints()

        matrix_transpose = [list(i) for i in zip(*matrix)]
        return Matrix(matrix_transpose)

    def _matrix_row_idx(self, row: int, col: int, val: int) -> int:
        return row * 36 + col * 6 + val

    def _row_column_constraints(self) -> list[list[bool]]:
        constraints = []
        for row in range(6):
            for col in range(6):
                constraint = [False] * self.MATRIX_ROWS

                if self.grid[row][col] is None:
                    for val in range(6):
                        constraint[self._matrix_row_idx(row, col, val)] = True
                else:
                    constraint[self._matrix_row_idx(row, col, self.grid[row][col] - 1)] = True

                constraints.append(constraint)

        return constraints
    
    def _row_number_constraints(self) -> list[list[bool]]:
        constraints = []
        for row in range(6):
            for val in range(6):
                constraint = [False] * self.MATRIX_ROWS
                for col in range(6):
                    constraint[self._matrix_row_idx(row, col, val)] = True

                constraints.append(constraint)

        return constraints
    
    def _col_number_constraints(self) -> list[list[bool]]:
        constraints = []
        for col in range(6):
            for val in range(6):
                constraint = [False] * self.MATRIX_ROWS
                for row in range(6):
                    constraint[self._matrix_row_idx(row, col, val)] = True

                constraints.append(constraint)

        return constraints
    
    def _box_number_constraints(self) -> list[list[bool]]:
        constraints = []
        for val in range(6):
            for row_corner in [0, 2, 4]:
                for col_corner in [0, 3]:
                    constraint = [False] * self.MATRIX_ROWS
                    for row in range(row_corner, row_corner + 2):
                        for col in range(col_corner, col_corner + 3):
                            constraint[self._matrix_row_idx(row, col, val)] = True
                
            constraints.append(constraint)

        return constraints
    
    @classmethod
    def from_algorithm_x_solution(cls, solution: list[int]) -> Self:
        grid = [[None] * 6 for _ in range(6)]

        for solution_row in solution:
            row, col, val = cls._algorithm_x_solution_row_to_grid_value(solution_row)
            grid[row][col] = val + 1
        
        return cls(grid)

    @staticmethod
    def _algorithm_x_solution_row_to_grid_value(solution_row) -> tuple[int, int, int]:
        val = solution_row % 6
        col = solution_row // 6 % 6
        row = solution_row // 36
    
        return row, col, val
    
    def __str__(self) -> str:
        display_list = []
        for row in self.grid:
            display_list.append(" ".join(str(x) if x is not None else '_' for x in row))
        return "\n".join(display_list)

