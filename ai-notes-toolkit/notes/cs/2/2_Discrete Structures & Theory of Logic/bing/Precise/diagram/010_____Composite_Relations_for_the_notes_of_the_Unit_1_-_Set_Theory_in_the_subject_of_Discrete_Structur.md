### Composite Relations

- A composite relation is a relation that is obtained by combining two or more other relations.
- Let R be a relation from set A to set B and S be a relation from set B to set C. The composite of R and S, denoted by S ◦ R, is a relation from set A to set C.
- The composite relation S ◦ R is defined as: S ◦ R = {(a, c) ∈ A × C | ∃b ∈ B such that (a, b) ∈ R and (b, c) ∈ S}.
- The composition of relations is associative, meaning that for three relations R, S, and T, we have (T ◦ S) ◦ R = T ◦ (S ◦ R).
- The composition of relations is not commutative, meaning that for two relations R and S, we generally have S ◦ R ≠ R ◦ S.
- The identity relation on a set A is the relation I = {(a, a) | a ∈ A}. For any relation R from set A to set B, we have R ◦ I = R and I ◦ R = R.
- The inverse of a relation R from set A to set B is the relation R⁻¹ from set B to set A defined as R⁻¹ = {(b, a) | (a, b) ∈ R}. For any relation R, we have (R⁻¹)⁻¹ = R and R⁻¹ ◦ R = I.