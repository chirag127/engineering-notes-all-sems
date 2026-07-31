# Minimum Edit Distance

- Minimum edit distance is a measure of how similar or dissimilar two strings are by counting the minimum number of operations required to transform one string into another .
- The operations can be insertion, deletion, or substitution of a single character, or transposition of two adjacent characters.
- Minimum edit distance can be used for various natural language processing tasks, such as spelling correction, text classification, information extraction, and machine translation  .
- To calculate the minimum edit distance between two strings, we can use a dynamic programming algorithm that fills a matrix with the costs of the operations  .
- The algorithm works as follows :
  - Initialize the first row and column of the matrix with the costs of deleting or inserting characters from the source string to the target string.
  - For each cell in the matrix, compute the cost of the three possible operations: deletion, insertion, or substitution, and choose the minimum one.
  - If the characters in the source and target strings are the same, the cost of substitution is zero; otherwise, it is one.
  - If the characters in the source and target strings are adjacent and swapped, the cost of transposition is one; otherwise, it is infinity.
  - The minimum edit distance is the value in the bottom-right corner of the matrix.
  - To find the optimal alignment of the two strings, we can backtrack from the bottom-right corner to the top-left corner, following the pointers that indicate the chosen operation for each cell.
- Here is an example of calculating the minimum edit distance between the strings "intention" and "execution" with the costs of insertion, deletion, and substitution being 1, and the cost of transposition being infinity:

|   |   | e | x | e | c | u | t | i | o | n |
|---|---|---|---|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| i | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| n | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 8 |
| t | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 8 | 8 |
| e | 4 | 3 | 4 | 3 | 4 | 5 | 6 | 7 | 7 | 8 |
| n | 5 | 4 | 5 | 4 | 5 | 5 | 6 | 7 | 8 | 8 |
| t | 6 | 5 | 6 | 5 | 6 | 6 | 6 | 7 | 8 | 9 |
| i | 7 | 6 | 7 | 6 | 7 | 7 | 7 | 6 | 7 | 8 |
| o | 8 | 7 | 8 | 7 | 8 | 8 | 8 | 7 | 7 | 8 |
| n | 9 | 8 | 9 | 8 | 9 | 9 | 9 | 8 | 8 | 8 |

- The minimum edit distance is 8, and one possible alignment is:

| i | n | t | e | n | t | i | o | n |
|---|---|---|---|---|---|---|---|---|
|   |   |   | e |   |   |   |   |   |
|   |   |   |   | x |   |   |   |   |
|   |   |   |   |   | e |   |   |   |
|   |   |   |   |   |   | c |   |   |
|   |   |   |   |   |   |   | u |   |
|   |   |   |   |   |   |   |   | t |
|   |   |   |   |   |   |