from abc import ABC, abstractmethod

from sudoku import Sudoku


class Rule(ABC):
    @staticmethod
    def matrix_row_idx(sudoku: Sudoku, row: int, col: int, val: int):
        return row * (sudoku.num_cols * sudoku.max_val) + col * (sudoku.max_val) + val

    @abstractmethod
    def primary_dlx_constraints(self, sudoku: Sudoku) -> list[list[int]] | None:
        pass

    @abstractmethod
    def secondary_dlx_constraints(self, sudoku: Sudoku) -> list[list[int]] | None:
        pass
