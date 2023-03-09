 Here is the content in markdown format for the given topic:

### Set-Theoretic Operations

The following set-theoretic operations can be performed on relations:

1. Union: The union of two relations R and S, written as R U S, contains all tuples that are either in R or in S or in both R and S. Duplicate tuples are eliminated.
- Example: Let R = {a, b, c} and S = {c, d, e}. Then, R U S = {a, b, c, d, e}.
- The schema of the result relation must be the same as that of R and S.
- The tuples in the result are the concatenation of tuples of R and S with duplicate tuples removed.

2. Intersection: The intersection of two relations R and S, written as R ∩ S, contains all tuples that are in both R and S.
- Example: Let R = {a, b, c} and S = {c, d, e}. Then, R ∩ S = {c}.
- The schema of the result relation must be the same as that of R and S.
- The tuples in the result are the common tuples in both R and S.

3. Difference: The difference of two relations R and S, written as R - S, contains all tuples that are in R but not in S.
- Example: Let R = {a, b, c} and S = {c, d, e}. Then, R - S = {a, b}.
- The schema of the result relation must be the same as that of R.
- The tuples in the result are those tuples in R that do not appear in S.

[Detailed explanations, examples, diagrams, code snippets, advantages, disadvantages, applications, etc. can be added here for better understanding and learning.]