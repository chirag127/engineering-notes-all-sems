### Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are, based on the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, each with a certain cost.
- For example, the minimum edit distance between "kitten" and "sitting" is 3, because we can transform "kitten" into "sitting" by substituting "k" with "s", inserting "i" after "t", and substituting "e" with "g".
- The minimum edit distance can be computed using a dynamic programming algorithm that fills a matrix with the optimal costs for each substring pair.
- The algorithm works as follows:

  - Initialize the first row and column of the matrix with the costs of inserting or deleting the characters of the strings.
  - For each cell in the matrix, compute the minimum cost of transforming the substring up to that cell, by taking the minimum of three possible costs:
    - The cost of the cell above plus the cost of deleting a character from the first string.
    - The cost of the cell to the left plus the cost of inserting a character to the second string.
    - The cost of the cell diagonally above and to the left plus the cost of substituting a character if the characters are different, or zero if they are the same.
  - The minimum edit distance is the value of the bottom-right cell of the matrix.

- Here is an example of computing the minimum edit distance between "intention" and "execution" with unit costs for each operation:

|       |   | e | x | e | c | u | t | i | o | n |
| ----- | - | - | - | - | - | - | - | - | - | - |
|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| i     | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| n     | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 6 | 7 |
| t     | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 7 | 7 |
| e     | 4 | 3 | 4 | 3 | 4 | 5 | 6 | 7 | 8 | 8 |
| n     | 5 | 4 | 5 | 4 | 5 | 6 | 7 | 8 | 8 | 8 |
| t     | 6 | 5 | 6 | 5 | 6 | 7 | 6 | 7 | 8 | 9 |
| i     | 7 | 6 | 7 | 6 | 7 | 8 | 7 | 6 | 7 | 8 |
| o     | 8 | 7 | 8 | 7 | 8 | 9 | 8 | 7 | 6 | 7 |
| n     | 9 | 8 | 9 | 8 | 9 | 10| 9 | 8 | 7 | 6 |

- The minimum edit distance is 6, and one possible sequence of operations is:

  - Substitute "i" with "e"
  - Substitute "n" with "x"
  - Substitute "t" with "e"
  - Insert "c"
  - Insert "u"
  - Substitute "i" with "o"