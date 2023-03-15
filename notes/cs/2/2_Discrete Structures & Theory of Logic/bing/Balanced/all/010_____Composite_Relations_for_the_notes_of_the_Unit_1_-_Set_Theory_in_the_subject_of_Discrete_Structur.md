# Composite Relations

- A composite relation is a relation that is obtained by combining two or more existing relations using the operation of composition.
- The operation of composition is defined as follows: given two relations R and S, the composite relation R ○ S is the set of all ordered pairs (a, c) such that there exists an element b in the common domain of R and S for which (a, b) ∈ R and (b, c) ∈ S.
- In other words, R ○ S is the set of all pairs that can be formed by joining the first element of a pair in R with the second element of a pair in S, provided that the second element of the pair in R matches the first element of the pair in S.
- For example, if R = {(1, 2), (2, 3), (3, 4)} and S = {(2, 5), (3, 6), (4, 7)}, then R ○ S = {(1, 5), (2, 6), (3, 7)}.
- The operation of composition is not commutative, that is, R ○ S is not necessarily equal to S ○ R. For instance, in the above example, S ○ R = {(5, 3), (6, 4)}.
- The operation of composition is associative, that is, (R ○ S) ○ T = R ○ (S ○ T) for any three relations R, S, and T.
- A relation R is called transitive if R ○ R ⊆ R, that is, if whenever (a, b) ∈ R and (b, c) ∈ R, then (a, c) ∈ R. For example, the relation {(1, 2), (2, 3), (1, 3)} is transitive, but the relation {(1, 2), (2, 3), (3, 1)} is not.
- A relation R is called reflexive if the identity relation I ⊆ R, that is, if (a, a) ∈ R for every element a in the domain of R. For example, the relation {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)} is reflexive, but the relation {(1, 2), (2, 3), (3, 1)} is not.
- A relation R is called symmetric if R = R<sup>-1</sup>, that is, if (a, b) ∈ R implies (b, a) ∈ R. For example, the relation {(1, 2), (2, 1), (3, 3)} is symmetric, but the relation {(1, 2), (2, 3), (3, 1)} is not.