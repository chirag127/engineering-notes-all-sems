### Equality of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself.
- Two relations R and S on a set A are equal if and only if they have the same elements, that is, R = S if and only if R ⊆ S and S ⊆ R.
- The equality of relations is reflexive, symmetric and transitive, meaning that for any relations R, S and T on a set A, the following properties hold:
  - R = R (reflexivity)
  - If R = S, then S = R (symmetry)
  - If R = S and S = T, then R = T (transitivity)
- The equality of relations is also an equivalence relation, meaning that it partitions the set of all relations on A into equivalence classes, where each class contains all the relations that are equal to each other.
- An example of an equivalence class of relations on a set A = {1, 2, 3} is the class of all reflexive relations on A, which contains the following four relations:
  - R1 = {(1, 1), (2, 2), (3, 3)}
  - R2 = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
  - R3 = {(1, 1), (2, 2), (3, 3), (1, 3), (3, 1)}
  - R4 = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (1, 3), (3, 1)}
- All these relations are equal to each other because they have the same reflexive pairs, and any other relation on A that has the same reflexive pairs will also belong to this class.