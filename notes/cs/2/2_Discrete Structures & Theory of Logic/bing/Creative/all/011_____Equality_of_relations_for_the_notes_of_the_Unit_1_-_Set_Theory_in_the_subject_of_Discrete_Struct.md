# Equality of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself.
- Two relations R and S on a set A are equal if and only if they have the same ordered pairs, that is, R = S if and only if R ⊆ S and S ⊆ R.
- For example, let A = {1, 2, 3} and let R = {(1, 1), (2, 2), (3, 3)} and S = {(x, y) ∈ A x A | x = y}. Then R and S are equal relations on A, since they both contain the same ordered pairs.
- Equality of relations is an equivalence relation on the power set of A x A, that is, it satisfies the following properties for any relations R, S, and T on A:
  - Reflexivity: R = R
  - Symmetry: If R = S, then S = R
  - Transitivity: If R = S and S = T, then R = T
- Equality of relations is also compatible with the operations of union, intersection, complement, and inverse, that is, for any relations R, S, and T on A, the following hold:
  - If R = S, then R ∪ T = S ∪ T
  - If R = S, then R ∩ T = S ∩ T
  - If R = S, then R<sup>c</sup> = S<sup>c</sup>
  - If R = S, then R<sup>-1</sup> = S<sup>-1</sup>