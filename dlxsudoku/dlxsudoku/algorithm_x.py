from __future__ import annotations

class Node:
    left: Node
    right: Node
    up: Node
    down: Node
    header: ColumnHeaderNode

    def __init__(self, header: ColumnHeaderNode) -> None:
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.header = header

    def hook_right(self, node: Node):
        self.right = node
        node.left = self

    def hook_down(self, node: Node):
        self.down = node
        node.up = self

class ColumnHeaderNode(Node):
    left: ColumnHeaderNode
    right: ColumnHeaderNode
    size: int
    label: str

    def __init__(self, label: str) -> None:
        super().__init__(self)
        self.size = 0
        self.label = label

    def cover(self):
        self.right.left = self.left
        self.left.right = self.right

        i = self.down
        while i is not self:
            j = i.right
            while j is not i:
                j.down.up = j.up
                j.up.down = j.down
                j.header.size -= 1

                j = j.right   

            i = i.down

    def uncover(self):
        i = self.up
        while i is not self:
            j = i.left
            while j is not i:
                j.header.size += 1
                j.down.up = j
                j.up.down = j

                j = j.left

            i = i.up

        self.right.left = self
        self.left.right = self


class Matrix:
    root: ColumnHeaderNode
    row_mapping: dict[tuple[int], int]

    def __init__(self, grid: list[list[bool]]) -> None:
        self.root = self._make_graph(grid)
        self.row_map = self._make_row_mapping(grid)

    @staticmethod
    def _make_graph(grid: list[list[bool]]) -> ColumnHeaderNode:
        root = ColumnHeaderNode("root")

        column_headers: list[ColumnHeaderNode] = []

        num_cols = len(grid[0])
        for i in range(num_cols):
            column_header = ColumnHeaderNode(label=str(i))
            root.left.hook_right(column_header)
            column_header.hook_right(root)
            column_headers.append(column_header)
            

        for row in grid:
            leftmost_node = None

            for col_idx, val in enumerate(row):
                if not val:
                    continue

                col_head = column_headers[col_idx]

                node = Node(col_head)

                # link vertically
                col_head.up.hook_down(node)
                node.hook_down(col_head)
                col_head.size += 1

                # link horizontally
                if leftmost_node is None:
                    leftmost_node = node
                else:
                    leftmost_node.left.hook_right(node)
                    node.hook_right(leftmost_node)

        return root
    
    @staticmethod
    def _make_row_mapping(grid: list[list[bool]]) -> dict[tuple[int], int]:
        row_map = dict()

        for row_idx, row in enumerate(grid):
            key = tuple(i for i, val in enumerate(row) if val)
            row_map[key] = row_idx

        return row_map

    def search(self, solution = None):
        # Handle mutable default arguments
        if solution is None:
            solution = []

        # Algorithm start
        if self.root.right is self.root:
            yield self.print_solution(solution)
            return
        
        c = self.choose_column()
        c.cover()

        r = c.down
        while r is not c:
            solution.append(r)
            j = r.right
            while j is not r:
                j.header.cover()
                
                j = j.right
            
            yield from self.search(solution)
            solution.pop()

            j = r.left
            while j is not r:
                j.header.uncover()

                j = j.left

            r = r.down

        c.uncover()


    def choose_column(self) -> ColumnHeaderNode:
        min_column = self.root.right
        column = min_column.right
        while column is not self.root:
            if column.size < min_column.size:
                min_column = column
            column = column.right

        # TODO: choose column with smallest size
        return min_column
    
    def print_solution(self, data_objects: list[Node]) -> list[int]:
        rows = []
        for o in data_objects:
            solution = [int(o.header.label)]
            node = o.right
            while node is not o:
                solution.append(int(node.header.label))
                node = node.right
            key = tuple(sorted(solution))
            rows.append(self.row_map[key])
        return rows
    # def __str__(self) -> str:
    #     display_list = []

    #     for row_idx, row in enumerate(self.A):
    #         if not self.rows[row_idx]:
    #             continue

    #         display_row = []
    #         for col_idx, val in enumerate(row):
    #             if not self.columns[col_idx]:
    #                 continue

    #             display_row.append("1" if self.A[row_idx][col_idx] else "0")
    #         display_list.append(" ".join(display_row))
    #     return "\n".join(display_list)


if __name__ == "__main__":
    A = [
        [1, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1],
        [0, 1, 0, 0, 0, 0, 1]
    ]

    matrix = Matrix(A)

    for solution in matrix.search():
        print(solution)