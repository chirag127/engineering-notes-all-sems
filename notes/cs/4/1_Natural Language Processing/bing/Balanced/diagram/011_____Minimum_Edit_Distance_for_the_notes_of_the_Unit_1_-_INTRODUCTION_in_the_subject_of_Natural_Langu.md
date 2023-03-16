Hello, I am Sydney, your AI assistant. I can help you with your study material for Natural Language Processing. Here is the content for the topic of Minimum Edit Distance for the notes of Unit 1 - INTRODUCTION.

### Minimum Edit Distance

- Minimum edit distance is a measure of how similar two strings are by counting the minimum number of operations required to transform one string into another.
- The operations are usually insertion, deletion, and substitution of a single character, or transposition of two adjacent characters.
- The cost of each operation can be assigned a weight, which can vary depending on the application or the language.
- For example, the minimum edit distance between "intention" and "execution" is 5, with the following sequence of operations (assuming equal unit costs):

  - intention -> **e**ntention (substitution of "i" with "e")
  - entention -> **ex**tention (substitution of "n" with "x")
  - extention -> exten**s**ion (substitution of "t" with "s")
  - extension -> execu**t**ion (insertion of "t")
  - execution -> execution (no operation)

- The minimum edit distance can be computed using a dynamic programming algorithm that fills in a matrix that stores the optimal solutions for the subproblems.
- The matrix has one row for each letter of the source string and one column for each letter of the target string, plus an extra row and column for the empty string.
- The matrix is initialized as follows:

  - The top left cell is 0, representing the cost of transforming the empty string into the empty string.
  - The first row is filled with the cumulative costs of inserting each letter of the target string into the empty string.
  - The first column is filled with the cumulative costs of deleting each letter of the source string from the empty string.

- The rest of the matrix is filled by applying the following recurrence relation for each cell:

  - If the source letter and the target letter are the same, the cost is the same as the cost of transforming the previous source and target letters, which is the value in the upper left diagonal cell.
  - If the source letter and the target letter are different, the cost is the minimum of the following three options:
    - The cost of transforming the previous source and target letters, plus the cost of substituting the source letter with the target letter, which is the value in the upper left diagonal cell plus the substitution cost.
    - The cost of transforming the source letter and the previous target letter, plus the cost of inserting the target letter, which is the value in the left cell plus the insertion cost.
    - The cost of transforming the previous source letter and the target letter, plus the cost of deleting the source letter, which is the value in the upper cell plus the deletion cost.
  - Optionally, if the source letter and the target letter are adjacent and swapped, the cost can also be the minimum of the above options and the following option:
    - The cost of transforming the previous two source and target letters, plus the cost of transposing the source letter and the target letter, which is the value in the upper left diagonal cell of the previous row and column plus the transposition cost.

- The minimum edit distance is the value in the bottom right cell of the matrix, which represents the cost of transforming the entire source string into the entire target string.
- The sequence of operations can be obtained by backtracking from the bottom right cell to the top left cell, following the pointers that indicate which option was chosen to fill each cell.

- Here is an example of the matrix filled for the strings "intention" and "execution", assuming equal unit costs for all operations:

|       |   | e | x | e | c | u | t | i | o | n |
| ----- | - | - | - | - | - | - | - | - | - | - |
|       | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| **i** | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| **n** | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 8 |
| **t** | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 8 | 8 |
| **e** | 4 | 3 | 4 | 4 | 4 | 5 |