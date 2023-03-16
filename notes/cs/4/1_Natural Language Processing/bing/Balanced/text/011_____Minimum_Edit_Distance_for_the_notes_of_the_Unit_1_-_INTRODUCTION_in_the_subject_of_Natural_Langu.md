### Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are by counting the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, or transposition of two adjacent characters.
- Each operation has a cost, which can be uniform or weighted depending on the application.
- The minimum edit distance between two strings is the sum of the costs of the operations that transform one string into another.
- For example, the minimum edit distance between "intention" and "execution" is 5, with the following operations and costs:

| Operation | Cost | Result |
|-----------|------|--------|
| Substitute "e" for "i" | 1 | "entention" |
| Substitute "x" for "n" | 1 | "extention" |
| Insert "c" after "x" | 1 | "execution" |
| Delete "n" | 1 | "executio" |
| Insert "n" at the end | 1 | "execution" |

- The minimum edit distance can be computed using a dynamic programming algorithm that fills a matrix with the optimal costs for all possible substrings.
- The algorithm works as follows:

  - Initialize the first row and column of the matrix with the costs of inserting or deleting the characters of the strings.
  - For each cell in the matrix, compute the cost of the three possible operations: insertion, deletion, and substitution (or transposition if allowed), and choose the minimum one.
  - The cost of insertion or deletion is the cost of the operation plus the cost of the previous cell in the same row or column.
  - The cost of substitution is the cost of the operation plus the cost of the previous cell in the diagonal, unless the characters are the same, in which case the cost is zero.
  - The cost of transposition is the cost of the operation plus the cost of the cell two positions back in the diagonal, if the characters are swapped.
  - The minimum edit distance is the value of the last cell in the matrix.

- The minimum edit distance can be used for various applications in natural language processing, such as spelling correction, speech recognition, machine translation, and text similarity.