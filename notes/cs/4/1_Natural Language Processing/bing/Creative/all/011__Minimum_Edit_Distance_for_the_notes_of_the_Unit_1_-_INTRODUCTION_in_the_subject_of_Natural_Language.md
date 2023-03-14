### Minimum Edit Distance for the notes of the Unit 1 - INTRODUCTION in the subject of Natural Language Processing

- Minimum edit distance is a string metric that measures how dissimilar two strings are by counting the minimum number of edit operations required to transform one string into the other. 
- Edit operations can include insertion, deletion, substitution, and transposition of single symbols or characters. 
- Different types of edit distance allow different sets of edit operations, such as Levenshtein distance, Hamming distance, Damerau-Levenshtein distance, and Jaro distance. 
- Each edit operation can be assigned a cost or weight, which can be constant or variable depending on the context. 
- The minimum edit distance can be computed using a dynamic programming algorithm that fills a matrix with the optimal costs for all possible substrings. 
- The minimum edit distance has applications in natural language processing, such as spelling correction, text similarity, and machine translation.  

#### Example

- Suppose we want to compute the minimum edit distance between the strings "intention" and "execution" using the Levenshtein distance, which allows insertion, deletion, and substitution with unit cost. 
- We can use the following algorithm to fill a matrix M with the optimal costs:

```
# Initialize the matrix with zeros
M = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]

# Fill the first row and column with the costs of deleting or inserting all characters
for i in range(1, len(a)+1):
  M[i][0] = i # cost of deleting i characters from a
for j in range(1, len(b)+1):
  M[0][j] = j # cost of inserting j characters to a

# Fill the rest of the matrix with the minimum costs of transforming substrings
for i in range(1, len(a)+1):
  for j in range(1, len(b)+1):
    # If the characters are the same, no cost is incurred
    if a[i-1] == b[j-1]:
      M[i][j] = M[i-1][j-1]
    # Otherwise, choose the minimum cost of the three possible operations
    else:
      M[i][j] = min(M[i-1][j] + 1, # deletion
                    M[i][j-1] + 1, # insertion
                    M[i-1][j-1] + 1) # substitution
```

- The resulting matrix M looks like this:

|   |   | e | x | e | c | u | t | i | o | n |
|---|---|---|---|---|---|---|---|---|---|---|
|   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| i | 1 | 1 | 2 | 3 | 4 | 5 | 6 | 6 | 7 | 8 |
| n | 2 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 8 |
| t | 3 | 3 | 3 | 3 | 4 | 5 | 5 | 6 | 8 | 8 |
| e | 4 | 3 | 4 | 4 | 4 | 5 | 6 | 6 | 7 | 8 |
| n | 5 | 4 | 4 | 5 | 5 | 5 | 6 | 7 | 7 | 8 |
| t | 6 | 5 | 5 | 5 | 6 | 6 | 6 | 7 | 8 | 8 |
| i | 7 | 6 | 6 | 6 | 7 | 7 | 7 | 7 | 8 | 9 |
| o | 8 | 7 | 7 | 7 | 8 | 8 | 8 | 8 | 8 | 9 |
| n | 9 | 8 | 8 | 8 | 9 | 9 | 9 | 9 | 9 | 9 |

- The minimum edit distance between the two