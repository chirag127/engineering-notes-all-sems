# Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are, based on the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, each with a certain cost.
- For example, the minimum edit distance between "cat" and "bat" is 1, because we can substitute "c" with "b" with a cost of 1. The minimum edit distance between "cat" and "cart" is also 1, because we can insert "r" with a cost of 1.
- To compute the minimum edit distance between two strings, we can use a dynamic programming algorithm that fills a matrix with the optimal costs for each substring pair.
- The algorithm works as follows:

  - Initialize the first row and column of the matrix with the costs of deleting or inserting each character from the source or target string.
  - For each cell in the matrix, compute the minimum cost of transforming the substring up to that cell, by taking the minimum of three possible options:
    - The cost of the cell above plus the cost of deleting a character from the source string.
    - The cost of the cell to the left plus the cost of inserting a character to the target string.
    - The cost of the cell diagonally above and to the left plus the cost of substituting a character if the source and target characters are different, or zero if they are the same.
  - The minimum edit distance is the value of the bottom-right cell of the matrix.

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

- The minimum edit distance is 8, which corresponds to the following sequence of operations:

  - Substitute "i" with "e"
  - Substitute "n" with "x"
  - Delete "t"
  - Substitute "e" with "c"
  - Substitute "n" with "u"
  - Insert "t"
  - Delete "i"
  - Insert "o"

- Minimum edit distance can be used for various applications in natural language processing, such as spelling correction, speech recognition, machine translation, and text summarization.