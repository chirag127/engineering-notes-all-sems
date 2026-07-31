### Recursive definition of relation for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation is a set of ordered pairs, where each pair consists of an element from a set A and an element from a set B.
- A relation can be defined recursively by specifying a base case and a recursive step.
- A base case is a relation that contains a finite number of ordered pairs, or no ordered pairs at all.
- A recursive step is a rule that generates new ordered pairs from existing ones, using operations such as union, intersection, complement, inverse, or composition.
- For example, let A = {a, b, c} and B = {1, 2, 3}. A base case for a relation R from A to B is R = {(a, 1), (b, 2)}.
- A recursive step for R is to add the inverse of each pair in R to R. That is, R = R ∪ {(1, a), (2, b)}.
- Applying the recursive step again, we get R = R ∪ {(a, 2), (b, 1), (1, b), (2, a)}.
- And so on, until no new pairs can be generated. The final relation R is {(a, 1), (a, 2), (b, 1), (b, 2), (1, a), (1, b), (2, a), (2, b)}.
- This is an example of a recursive definition of a relation. It specifies how to construct the relation from a base case and a recursive step.