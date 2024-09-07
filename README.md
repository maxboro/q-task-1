# Task 1

As part of this task I created script `islands.py` that counts number of islands for matrix provided using depth-first search (recursive implementation).

Cell considered to be part of island if it has island's cell as neighbour (up, down, left,
right, but not diagonal neighbour). Time complexity: O(number of cells * number of rows), because
script visit each cell of matrix only once (in terms of fully processing cell; visit and check if
it is visited can be done multiple times).

## Usage

1. Set shape of matrix in form of '{number of rows} {number of cells}' after "Set shape of matrix:"
2. Set matrix after "Set matrix:". Cells in a row should be separated by 1 whitespace, each new
   row should start at a new line (hit Enter, or insert previously copied multiline matrix altogether).

```bash
$ python islands.py
Set shape of matrix: 3 4
Set matrix:
0 0 0 1
0 0 1 1
0 1 0 1
Provided matrix has 2 islands.
```
