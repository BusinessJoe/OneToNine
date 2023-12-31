from sudoku import Sudoku
from sudoku import Sudoku
from rules import Rule


class Row(Rule):
    def primary_dlx_constraints(self, sudoku: Sudoku) -> list[list[int]]:
        constraints = []
        for row in range(sudoku.num_rows):
            for val in range(sudoku.max_val):
                constraint = (
                    [False] * sudoku.num_rows * sudoku.num_cols * sudoku.max_val
                )
                for col in range(sudoku.num_cols):
                    constraint[self.matrix_row_idx(sudoku, row, col, val)] = True

                constraints.append(constraint)

        return constraints

    def secondary_dlx_constraints(self, sudoku: Sudoku) -> list[list[int]] | None:
        return None


class Col(Rule):
    def primary_dlx_constraints(self, sudoku: Sudoku) -> list[list[int]]:
        constraints = []
        for col in range(sudoku.num_cols):
            for val in range(sudoku.max_val):
                constraint = (
                    [False] * sudoku.num_rows * sudoku.num_cols * sudoku.max_val
                )
                for row in range(sudoku.num_rows):
                    constraint[self.matrix_row_idx(sudoku, row, col, val)] = True

                constraints.append(constraint)

        return constraints

    def secondary_dlx_constraints(self, sudoku: Sudoku) -> list[list[int]] | None:
        return None


class StandardBox(Rule):
    def primary_dlx_constraints(self, sudoku: Sudoku) -> list[list[int]]:
        constraints = []
        for val in range(9):
            for row_corner in [0, 3, 6]:
                for col_corner in [0, 3, 6]:
                    constraint = (
                        [False] * sudoku.num_rows * sudoku.num_cols * sudoku.max_val
                    )
                    for row in range(row_corner, row_corner + 3):
                        for col in range(col_corner, col_corner + 3):
                            constraint[
                                self.matrix_row_idx(sudoku, row, col, val)
                            ] = True

                    constraints.append(constraint)

        return constraints

    def secondary_dlx_constraints(self, sudoku: Sudoku) -> list[list[int]] | None:
        return None
