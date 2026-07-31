# Equality of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself.
- Two relations R and S on a set A are equal if and only if R and S are subsets of each other, that is, R ⊆ S and S ⊆ R.
- This means that R and S have exactly the same ordered pairs in A x A.
- For example, let A = {1, 2, 3} and let R = {(1, 1), (2, 2), (3, 3)} and S = {(x, x) | x ∈ A}. Then R and S are equal relations on A, since they both contain the same diagonal elements of A x A.
- Another way to check if two relations are equal is to use their matrix representations. A relation R on a set A can be represented by a matrix M_R with rows and columns indexed by the elements of A, such that M_R[i, j] = 1 if (i, j) ∈ R and M_R[i, j] = 0 otherwise.
- Two relations R and S on a set A are equal if and only if their matrices M_R and M_S are identical, that is, M_R[i, j] = M_S[i, j] for all i, j ∈ A.
- For example, let A = {a, b, c} and let R = {(a, a), (b, b), (c, c), (a, b), (b, a)} and S = {(x, y) | x = y or x and y are adjacent in the alphabet}. Then R and S are equal relations on A, since their matrices are:

|   | a | b | c |
|---|---|---|---|
| a | 1 | 1 | 0 |
| b | 1 | 1 | 0 |
| c | 0 | 0 | 1 |

- Note that the order of the elements in A does not affect the equality of the relations, as long as the same order is used for both rows and columns of the matrices.