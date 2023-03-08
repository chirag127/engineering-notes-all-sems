### Operations on Relations

- Operations on relations are similar to operations on sets, since relations are subsets of the Cartesian product of two sets.
- Let A and B be two sets and R and S be two relations over A and B, respectively. Then the following operations can be defined on R and S:

  - **Intersection**: The intersection of R and S is the relation R ∩ S, where (a, b) ∈ R ∩ S if and only if (a, b) ∈ R and (a, b) ∈ S.
  - **Union**: The union of R and S is the relation R ∪ S, where (a, b) ∈ R ∪ S if and only if (a, b) ∈ R or (a, b) ∈ S.
  - **Difference**: The difference of R and S is the relation R - S, where (a, b) ∈ R - S if and only if (a, b) ∈ R and (a, b) ∉ S.
  - **Symmetric difference**: The symmetric difference of R and S is the relation R ⊕ S, where (a, b) ∈ R ⊕ S if and only if (a, b) ∈ R and (a, b) ∉ S, or (a, b) ∉ R and (a, b) ∈ S.
  - **Complement**: The complement of R is the relation R̅, where (a, b) ∈ R̅ if and only if (a, b) ∉ R.
  - **Converse**: The converse of R is the relation R⁻¹, where (a, b) ∈ R⁻¹ if and only if (b, a) ∈ R.

- Some special relations are:

  - **Empty relation**: The empty relation is the relation ∅, where no pair of elements is related.
  - **Universal relation**: The universal relation is the relation A × B, where every pair of elements is related.
  - **Identity relation**: The identity relation is the relation Iₐ = {(a, a) | a ∈ A}, where every element is related to itself.

- Some properties of combined relations are:

  - **Commutative**: R ∩ S = S ∩ R, R ∪ S = S ∪ R, R ⊕ S = S ⊕ R, R⁻¹ = (R⁻¹)⁻¹
  - **Associative**: R ∩ (S ∩ T) = (R ∩ S) ∩ T, R ∪ (S ∪ T) = (R ∪ S) ∪ T
  - **Distributive**: R ∩ (S ∪ T) = (R ∩ S) ∪ (R ∩ T), R ∪ (S ∩ T) = (R ∪ S) ∩ (R ∪ T)
  - **De Morgan's laws**: (R ∩ S)̅ = R̅ ∪ S̅, (R ∪ S)̅ = R̅ ∩ S̅
  - **Involution**: (R̅)̅ = R

- Some examples of operations on relations are:

  - Let A = {1, 2, 3, 4} and B = {a, b, c, d}. Let R = {(1, a), (2, b), (3, c), (4, d)} and S = {(1, b), (2, a), (3, d), (4, c)} be two relations over A and B. Then:

    - R ∩ S = ∅
    - R ∪ S = {(1, a), (1, b), (2, a), (2, b), (3, c), (3, d), (4, c), (4, d)}
    - R - S = R
    - R ⊕ S = R ∪ S
    - R̅ = {(1, c), (1, d), (2, c), (2, d), (3, a), (3, b), (4, a), (4, b)}
    - R⁻¹ = {(a, 1), (b, 2), (c, 3), (d, 4)}

  - Let A = {1, 2, 3} and B = {a, b, c}. Let R =

I'm sorry, but I don't know any good mnemonics or learning tricks for the topic of operations on relations. Maybe you can try to make your own based on the definitions and properties of the operations. For example, you can use the acronym CID to remember the commutative, involution and distributive properties. Or you can use the word BAR to remember the operations of intersection, union and difference.