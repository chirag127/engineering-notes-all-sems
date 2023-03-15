### Composite Relations

- A composite relation is a relation that is obtained by combining two or more existing relations using the operation of composition.
- The composition of two relations R and S is denoted by R ∘ S and is defined as follows:

  - R ∘ S = {(a, c) | ∃b such that (a, b) ∈ R and (b, c) ∈ S}

  - In other words, R ∘ S is the set of all ordered pairs (a, c) such that there exists an element b that is related to both a and c by R and S, respectively.

- For example, if R = {(1, 2), (2, 3), (3, 4)} and S = {(2, 5), (3, 6), (4, 7)}, then R ∘ S = {(1, 5), (2, 6), (3, 7)}.

- The composition of relations is not commutative, i.e., R ∘ S ≠ S ∘ R in general.
- The composition of relations is associative, i.e., (R ∘ S) ∘ T = R ∘ (S ∘ T) for any three relations R, S, and T.
- The composition of relations can be used to model various concepts, such as:

  - Transitive closure: The transitive closure of a relation R is the smallest transitive relation that contains R. It can be obtained by composing R with itself repeatedly until no new pairs are added.

  - Functional composition: If R and S are functions, then R ∘ S is the function that maps x to R(S(x)) for every x in the domain of S.

  - Matrix multiplication: If R and S are binary relations on a finite set A, then R ∘ S can be represented by the matrix product of the adjacency matrices of R and S.