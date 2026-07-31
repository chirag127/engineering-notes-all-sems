### Composite Relations

- A composite relation is a relation that is formed by combining two or more other relations.
- Let R be a relation from set A to set B and S be a relation from set B to set C. The composite relation S ◦ R is a relation from set A to set C.
- The composite relation S ◦ R is defined as: S ◦ R = {(a, c) ∈ A × C | ∃b ∈ B such that (a, b) ∈ R and (b, c) ∈ S}.
- The composition of relations is associative, meaning that (R ◦ S) ◦ T = R ◦ (S ◦ T) for any three relations R, S, and T.
- The composition of relations is not commutative, meaning that R ◦ S ≠ S ◦ R in general.
- The identity relation I on a set A is defined as I = {(a, a) | a ∈ A}. The identity relation is the identity element for the composition of relations, meaning that R ◦ I = R and I ◦ R = R for any relation R.
- The inverse of a relation R, denoted by R⁻¹, is defined as R⁻¹ = {(b, a) | (a, b) ∈ R}. The inverse of a relation has the property that R⁻¹ ◦ R = I and R ◦ R⁻¹ = I.
- The composition of a relation with its inverse results in the identity relation, meaning that R ◦ R⁻¹ = I and R⁻¹ ◦ R = I for any relation R.