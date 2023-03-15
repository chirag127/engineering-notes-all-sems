### Recursive definition of relation for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation is a set of ordered pairs, where each pair consists of an element from a set A and an element from a set B.
- A relation can be defined recursively by specifying a base case and a recursive step.
- A base case is a relation that contains a finite number of ordered pairs, or no ordered pairs at all.
- A recursive step is a rule that generates new ordered pairs from existing ones, using operations such as union, intersection, complement, inverse, or composition.
- For example, let A = {a, b, c} and B = {1, 2, 3}. A base case for a relation R from A to B is R = {(a, 1), (b, 2)}.
- A recursive step for R is to add the inverse of each ordered pair in R, that is, (x, y) -> (y, x). This generates new ordered pairs such as (1, a) and (2, b).
- Applying the recursive step repeatedly, we can obtain the relation R* = {(a, 1), (b, 2), (1, a), (2, b), (c, 3), (3, c)}.
- R* is the smallest relation that contains R and is closed under the inverse operation.