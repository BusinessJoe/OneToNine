from rules import Rule
from sudoku import Sudoku
import itertools


class AntiKnight9x9(Rule):
    def primary_dlx_constraints(self, sudoku: Sudoku) -> list[list[int]] | None:
        return None

    def secondary_dlx_constraints(self, sudoku: Sudoku) -> list[list[int]] | None:
        constraints = []
        knight_offsets = [[(2, 1), (2, -1)], [(1, 2), (1, -2)]]
        for val, row, col, offset_group in itertools.product(
            range(9), range(9), range(9), knight_offsets
        ):
            constraint = [False] * sudoku.num_rows * sudoku.num_cols * sudoku.max_val
            for drow, dcol in offset_group:
                if 0 <= row + drow < 9 and 0 <= col + dcol < 9:
                    constraint[self.matrix_row_idx(sudoku, row, col, val)] = True
                    constraint[
                        self.matrix_row_idx(sudoku, row + drow, col + dcol, val)
                    ] = True
            constraints.append(constraint)
        return constraints
