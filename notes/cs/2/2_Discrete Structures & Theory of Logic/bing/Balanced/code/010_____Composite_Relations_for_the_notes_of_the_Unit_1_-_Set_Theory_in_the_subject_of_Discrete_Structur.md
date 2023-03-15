Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here are some notes on composite relations for the unit 1 - set theory in the subject of discrete structures and theory of logic.

### Composite Relations

- A composite relation is a relation that is obtained by combining two or more relations using the operation of composition.
- The composition of two relations R and S is denoted by R ∘ S and defined as follows:

  - R ∘ S = {(a, c) | ∃b such that (a, b) ∈ R and (b, c) ∈ S}

  - In other words, R ∘ S is the set of ordered pairs (a, c) such that there exists an element b that is related to a by R and to c by S.

- For example, if R = {(1, 2), (2, 3), (3, 4)} and S = {(2, 5), (3, 6), (4, 7)}, then R ∘ S = {(1, 5), (2, 6), (3, 7)}.

- The composition of relations is not commutative, that is, R ∘ S ≠ S ∘ R in general.
- The composition of relations is associative, that is, (R ∘ S) ∘ T = R ∘ (S ∘ T) for any three relations R, S, and T.
- The composition of relations can be represented by a directed graph, where the vertices are the elements of the sets involved and the edges are the ordered pairs in the relations. The composite relation R ∘ S can be obtained by following the paths of length two from R to S in the graph.

- For example, the following graph shows the relations R, S, and R ∘ S from the previous example:

  ```
  1 --> 2 --> 5
  |     |     ^
  |     |     |
  v     v     |
  2 --> 3 --> 6
  |     |     ^
  |     |     |
  v     v     |
  3 --> 4 --> 7
  ```

- A relation R on a set A is called transitive if R ∘ R ⊆ R, that is, whenever (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R.
- For example, the relation R = {(1, 2), (2, 3), (3, 4), (1, 3), (2, 4), (1, 4)} on the set A = {1, 2, 3, 4} is transitive, because R ∘ R = R.
- A relation R on a set A is called reflexive if I ⊆ R, where I is the identity relation on A, that is, I = {(a, a) | a ∈ A}.
- For example, the relation R = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (2, 3), (3, 4)} on the set A = {1, 2, 3, 4} is reflexive, because I ⊆ R.
- A relation R on a set A is called symmetric if R = R^T, where R^T is the transpose of R, that is, R^T = {(b, a) | (a, b) ∈ R}.
- For example, the relation R = {(1, 1), (2, 2), (3, 3), (4, 4), (1, 2), (2, 1), (3, 4), (4, 3)} on the set A = {1, 2, 3, 4} is symmetric, because R = R^T.