### Minimum Edit Distance for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

In Natural Language Processing, we often need to compare two strings to check for their similarity or dissimilarity. One way to do this is through Minimum Edit Distance (MED) algorithm. MED is the minimum number of operations required to transform one string into another. These operations include insertion, deletion and substitution of characters.

#### Algorithm for Minimum Edit Distance:

1. Initialize the matrix of size (m+1) x (n+1) where m and n are the lengths of the two strings to be compared.
2. Fill the first row and column of the matrix with their corresponding indices.
3. For each cell (i,j), calculate the cost of converting the character at string1[i-1] to string2[j-1].
4. The cost of conversion can be calculated using the following formula:
   - If string1[i-1] == string2[j-1], cost = 0
   - Else, cost = 1
5. Choose the minimum cost value from the three possibilities:
   - Deletion: (i-1, j)
   - Insertion: (i, j-1)
   - Substitution: (i-1, j-1)
6. Fill the current cell (i,j) with the minimum cost value.
7. The minimum edit distance is the value in the bottom-right corner of the matrix.

#### Advantages of Minimum Edit Distance:

- It is a simple and easy-to-implement algorithm.
- It can be used for various NLP tasks such as spell checking, machine translation, and speech recognition.

#### Disadvantages of Minimum Edit Distance:

- It has a high time complexity of O(mn), where m and n are the lengths of the two strings to be compared.
- It does not take into account the context of the words.

#### Mnemonic for Minimum Edit Distance:

One possible mnemonic for remembering the steps of the algorithm is "Fill, Calculate, Choose, Fill, Repeat". This emphasizes the iterative nature of the algorithm and the importance of choosing the minimum cost value at each step.

#### Example:

Let's compare the strings "kitten" and "sitting".

1. Initialize the matrix of size 6x7 with row and column indices.
```
  |  | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
--| -|---|---|---|---|---|---|---|
  | 0| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
  | 1| 1 |   |   |   |   |   |   |
  | 2| 2 |   |   |   |   |   |   |
  | 3| 3 |   |   |   |   |   |   |
  | 4| 4 |   |   |   |   |   |   |
  | 5| 5 |   |   |   |   |   |   |
```
2. Calculate the cost of converting "k" to "s".
```
cost = 1
```
3. Choose the minimum cost value from the three possibilities: 1, 0, 1.
```
min(1, 0, 1) = 0
```
4. Fill the current cell with the minimum cost value.
```
  |  | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
--| -|---|---|---|---|---|---|---|
  | 0| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
  | 1| 1 | 0 |   |   |   |   |   |
  | 2| 2 |   |   |   |   |   |   |
  | 3| 3 |   |   |   |   |   |   |
  | 4| 4 |   |   |   |   |   |   |
  | 5| 5 |   |   |   |   |   |   |
```
5. Repeat steps 2-4 for the remaining cells.
```
  |  | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
--| -|---|---|---|---|---|---|---|
  | 0| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
  | 1| 1 | 0 | 1 | 2 | 3 | 4 | 5 |
  | 2| 2 | 1 | 1 | 2 |