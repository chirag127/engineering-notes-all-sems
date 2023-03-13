### Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are by counting the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, or transposition of two adjacent characters.
- The cost of each operation can be assigned a positive value, depending on the application. For example, substitution may have a higher cost than insertion or deletion, and transposition may have a lower cost than two substitutions.
- To compute the minimum edit distance between two strings, a common algorithm is to use a dynamic programming approach that fills a matrix with the optimal costs of transforming prefixes of the strings.
- The matrix has one row for each character of the source string and one column for each character of the target string. The first row and column are initialized with the costs of inserting or deleting the characters up to that point.
- The rest of the matrix is filled by applying the following recursive formula for each cell:

  - If the source and target characters are the same, the cost is the same as the previous diagonal cell.
  - Otherwise, the cost is the minimum of the three possible operations: insertion, deletion, or substitution, plus the cost of that operation.
  - Optionally, if the source and target characters are adjacent and swapped, the cost is the minimum of the above or the previous diagonal cell of the previous row and column, plus the cost of transposition.

- The minimum edit distance is the value of the bottom-right cell of the matrix, which corresponds to the optimal cost of transforming the entire strings.
- To recover the sequence of operations that leads to the minimum edit distance, a backtracking procedure can be used that starts from the bottom-right cell and follows the pointers to the previous cells until the top-left cell is reached. The pointers are determined by which of the possible operations gave the minimum cost for each cell.