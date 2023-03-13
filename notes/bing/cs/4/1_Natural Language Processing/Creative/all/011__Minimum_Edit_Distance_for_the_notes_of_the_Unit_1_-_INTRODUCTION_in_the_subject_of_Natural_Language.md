### Minimum Edit Distance for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Minimum edit distance is a measure of how similar or dissimilar two strings are by counting the minimum number of operations required to transform one string into another .
- The operations are usually insertion, deletion, and substitution of a single character, but they can also include transposition of two adjacent characters.
- Minimum edit distance is useful for natural language processing tasks such as spelling correction, text classification, information extraction, and machine translation .
- The algorithm for computing the minimum edit distance between two strings is based on dynamic programming, which breaks down the problem into smaller subproblems and stores the solutions in a matrix  .
- The matrix has one row for each character of the source string and one column for each character of the target string. The matrix is initialized with the edit distance of the empty string to each prefix of the source and target strings, which is equal to the number of insertions or deletions needed  .
- The matrix is filled in row by row, from left to right, by applying the following recurrence relation for each cell:

  - If the source and target characters are the same, the edit distance is the same as the diagonal cell above and to the left.
  - If the source and target characters are different, the edit distance is the minimum of the three adjacent cells (above, left, and diagonal) plus one for the operation needed to match the characters (insertion, deletion, or substitution).
  - The minimum edit distance is the value in the bottom right corner of the matrix  .

- The following is an example of computing the minimum edit distance between the strings "intention" and "execution" with the cost of each operation being one :

  ```
  |   |   | e | x | e | c | u | t | i | o | n |
  |---|---|---|---|---|---|---|---|---|---|---|
  |   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
  | i | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
  | n | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 8 |
  | t | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 8 | 8 |
  | e | 4 | 3 | 4 | 4 | 4 | 5 | 6 | 7 | 8 | 9 |
  | n | 5 | 4 | 5 | 5 | 5 | 5 | 6 | 7 | 8 | 9 |
  | t | 6 | 5 | 6 | 6 | 6 | 6 | 6 | 7 | 8 | 9 |
  | i | 7 | 6 | 7 | 7 | 7 | 7 | 7 | 7 | 8 | 9 |
  | o | 8 | 7 | 8 | 8 | 8 | 8 | 8 | 8 | 8 | 9 |
  | n | 9 | 8 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 8 |
  ```

  - The minimum edit distance is 8, which can be obtained by the following sequence of operations:

    - Substitute "i" with "e"
    - Substitute "n" with "x"
    - Substitute "t" with "e"
    - Insert "c"
    - Insert "u"
    - Substitute "e" with "t"
    - Delete "i"
    - Delete "o"

- A possible mnemonic to remember the algorithm is:

  - **M**inimum **E**dit **D**istance is **M**atrix **E**ntry in the **D**own-right corner
  - **M