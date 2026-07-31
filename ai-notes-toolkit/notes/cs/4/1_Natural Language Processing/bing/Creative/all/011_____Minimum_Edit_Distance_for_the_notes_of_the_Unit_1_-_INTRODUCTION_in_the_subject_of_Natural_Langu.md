# Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are, based on the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, each with a certain cost.
- For example, the minimum edit distance between "cat" and "bat" is 1, because we can substitute "c" with "b" with a cost of 1. The minimum edit distance between "cat" and "cart" is also 1, because we can insert "r" with a cost of 1.
- To compute the minimum edit distance between two strings, we can use a dynamic programming algorithm that fills a matrix with the optimal costs for each substring pair.
- The algorithm works as follows:

  - Initialize the first row and column of the matrix with the costs of deleting or inserting each character from the source or target string.
  - For each cell in the matrix, starting from the top-left corner, compute the minimum cost of reaching that cell from one of its three neighbors: the cell above, the cell to the left, or the cell diagonally above and to the left.
  - The cost of reaching a cell from the cell above or to the left is the cost of the corresponding insertion or deletion operation, plus the cost of the neighbor cell.
  - The cost of reaching a cell from the diagonal cell is the cost of the substitution operation, if the characters in the source and target strings are different, or zero, if they are the same, plus the cost of the diagonal cell.
  - The minimum cost of reaching a cell is the minimum of the three costs computed from the neighbors.
  - The minimum edit distance between the two strings is the value in the bottom-right corner of the matrix.

- For example, the matrix for computing the minimum edit distance between "intention" and "execution" is:

|   |   | e | x | e | c | u | t | i | o | n |
|---|---|---|---|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| i | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| n | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 7 |
| t | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 8 | 8 |
| e | 4 | 3 | 4 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| n | 5 | 4 | 5 | 4 | 5 | 6 | 7 | 7 | 8 | 8 |
| t | 6 | 5 | 6 | 5 | 6 | 7 | 6 | 7 | 9 | 9 |
| i | 7 | 6 | 7 | 6 | 7 | 8 | 7 | 6 | 8 | 9 |
| o | 8 | 7 | 8 | 7 | 8 | 9 | 8 | 7 | 7 | 8 |
| n | 9 | 8 | 9 | 8 | 9 | 10| 9 | 8 | 8 | 8 |

- The minimum edit distance is 8, which can be achieved by the following sequence of operations:

  - Substitute "i" with "e"
  - Substitute "n" with "x"
  - Substitute "t" with "e"
  - Insert "c"
  - Insert "u"
  - Substitute "e" with "t"
  - Delete "i"
  - Delete "o"