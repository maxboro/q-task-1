"""
Counts number of islands for matrix provided using depth-first search (recursive implementation).

Cell considered to be part of island if it has island's cell as neighbour (up, down, left, 
right, but not diagonal neighbour). Time complexity: O(number of cells * number of rows), because 
script visit each cell of matrix only once (in terms of fully processing cell; visit and check if 
it is visited can be done multiple times).


Usage
-----
1. Run a script with `$ python islands.py` command
2. Set shape of matrix in form of '{number of rows} {number of cells}' after "Set shape of matrix:"
3. Set matrix after "Set matrix:". Cells in a row should be separated by 1 whitespace, each new 
row should start at a new line (hit Enter, or insert previously copied multiline matrix altogether).
4. Script would print message: "Provided matrix has [number] islands." with number of islands.

Example
-------
$ python islands.py
Set shape of matrix: 3 4
Set matrix:
0 0 0 1
0 0 1 1
0 1 0 1
Provided matrix has 2 islands.
"""
from typing import List


def get_matrix() -> List[List[int]]:
    """Receive and process input matrix shape and matrix itself."""
    n_rows, _ = map(int, input('Set shape of matrix: ').split())
    print('Set matrix: ')
    return [list(map(int, input().split())) for _ in range(n_rows)]


def count_islands(matrix: List[List[int]]) -> int:
    """Count number of islands for a given matrix."""

    if not matrix or not matrix[0]:
        return 0

    n_rows, n_cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(n_cols)] for _ in range(n_rows)]
   
    def dfs(row_index: int, col_index: int) -> None:
        """Perform iteration of depth first search for provided cell adress."""

        # If out of bounds, or it's ocean, or already visited, return
        if (row_index < 0
            or col_index < 0
            or row_index >= n_rows
            or col_index >= n_cols
            or matrix[row_index][col_index] == 0
            or visited[row_index][col_index]):
            return
        
        # Mark the cell as visited
        visited[row_index][col_index] = True

        # Visit all 4 possible directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row_direction, col_direction in directions:
            dfs(row_index + row_direction, col_index + col_direction)
    
    island_count = 0
    for row_index in range(n_rows):
        for col_index in range(n_cols):
            if matrix[row_index][col_index] == 1 and not visited[row_index][col_index]:
                # Initiate DFS when found a new island
                dfs(row_index, col_index)
                island_count += 1

    return island_count


def main():
    """Run all."""
    matrix = get_matrix()
    n_islands = count_islands(matrix)
    print(f"Provided matrix has {n_islands} islands.")


if __name__ == "__main__":
    main()
