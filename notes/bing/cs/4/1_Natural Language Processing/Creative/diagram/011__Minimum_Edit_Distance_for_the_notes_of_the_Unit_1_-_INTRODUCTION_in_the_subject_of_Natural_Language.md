The minimum edit distance is a measure of how similar two strings are, based on the minimum number of operations (insertion, deletion, or substitution) required to transform one string into another. It is useful for natural language processing tasks such as spelling correction, speech recognition, and machine translation.

One way to compute the minimum edit distance is to use dynamic programming, which is a technique of breaking down a complex problem into simpler subproblems and storing the results of the subproblems in a table. The following diagram illustrates the basic algorithm of dynamic programming for minimum edit distance:

### Minimum Edit Distance for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

```
Let X = "INTENTION" and Y = "EXECUTION"

Step 1: Initialize a matrix D of size (|X|+1) x (|Y|+1), where |X| and |Y| are the lengths of X and Y respectively.

Step 2: Fill the first row and column of D with the values of i and j, where i and j are the indices of the row and column.

Step 3: For each cell D[i][j], where i > 0 and j > 0, compute the minimum of the following three values:

- D[i-1][j] + 1, which is the cost of deleting a character from X
- D[i][j-1] + 1, which is the cost of inserting a character to X
- D[i-1][j-1] + diff(X[i], Y[j]), where diff(X[i], Y[j]) is 0 if X[i] == Y[j], and 1 otherwise. This is the cost of substituting a character in X with a character in Y.

Step 4: The minimum edit distance is the value of D[|X|][|Y|], which is the bottom-right corner of the matrix.

The matrix D looks like this:

    |   |   | E | X | E | C | U | T | I | O | N |
    |---|---|---|---|---|---|---|---|---|---|---|
    |   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
    | I | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
    | N | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 8 |
    | T | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 8 | 8 |
    | E | 4 | 3 | 4 | 4 | 4 | 5 | 6 | 7 | 7 | 8 |
    | N | 5 | 4 | 4 | 5 | 5 | 5 | 6 | 7 | 8 | 8 |
    | T | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 7 | 8 | 9 |
    | I | 7 | 6 | 6 | 6 | 7 | 7 | 7 | 6 | 7 | 8 |
    | O | 8 | 7 | 7 | 7 | 8 | 8 | 8 | 7 | 7 | 8 |
    | N | 9 | 8 | 8 | 8 | 9 | 9 | 9 | 8 | 8 | 8 |

Therefore, the minimum edit distance between "INTENTION" and "EXECUTION" is 8.
```