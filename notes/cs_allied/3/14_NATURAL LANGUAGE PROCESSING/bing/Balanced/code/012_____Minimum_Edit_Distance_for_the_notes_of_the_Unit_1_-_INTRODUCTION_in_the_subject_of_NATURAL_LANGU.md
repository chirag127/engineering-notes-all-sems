### Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are, based on the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, each with a certain cost.
- For example, the minimum edit distance between "cat" and "bat" is 1, because we can substitute "c" with "b" with a cost of 1. The minimum edit distance between "cat" and "cut" is also 1, because we can substitute "a" with "u" with a cost of 1.
- To compute the minimum edit distance between two strings, we can use a dynamic programming algorithm that fills a matrix with the optimal costs for each substring pair.
- The algorithm works as follows:

  - Initialize the first row and column of the matrix with the costs of deleting or inserting each character from the source or target string.
  - For each cell in the matrix, compute the minimum cost of transforming the substring up to that cell, based on the previous cells and the cost of substituting, inserting, or deleting the current character.
  - The minimum cost of transforming the whole strings is the value in the bottom-right cell of the matrix.
  - To find the optimal sequence of operations, we can backtrack from the bottom-right cell to the top-left cell, following the pointers that indicate which previous cell was used to compute the current cell.

- Here is an example of computing the minimum edit distance between "intention" and "execution", with a cost of 1 for each operation:

|   |   | e | x | e | c | u | t | i | o | n |
|---|---|---|---|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| i | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| n | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 7 |
| t | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 8 | 8 |
| e | 4 | 3 | 4 | 3 | 4 | 5 | 6 | 7 | 7 | 8 |
| n | 5 | 4 | 5 | 4 | 5 | 6 | 7 | 7 | 8 | 8 |
| t | 6 | 5 | 6 | 5 | 6 | 7 | 6 | 7 | 9 | 9 |
| i | 7 | 6 | 7 | 6 | 7 | 8 | 7 | 6 | 8 | 9 |
| o | 8 | 7 | 8 | 7 | 8 | 9 | 8 | 7 | 7 | 8 |
| n | 9 | 8 | 9 | 8 | 9 | 10| 9 | 8 | 8 | 8 |

- The minimum edit distance is 8, and one possible sequence of operations is:

  - Substitute "i" with "e"
  - Substitute "n" with "x"
  - Substitute "t" with "e"
  - Insert "c"
  - Insert "u"
  - Delete "n"
  - Delete "t"
  - Delete "i"

- Minimum edit distance can be used for various applications in natural language processing, such as spelling correction, speech recognition, machine translation, and text similarity.