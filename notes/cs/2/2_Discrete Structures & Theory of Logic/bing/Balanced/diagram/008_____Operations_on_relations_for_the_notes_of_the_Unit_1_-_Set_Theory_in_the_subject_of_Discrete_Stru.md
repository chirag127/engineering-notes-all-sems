### Operations on relations

A relation is a set of ordered pairs that relates elements of one set to elements of another set. For example, if A = {1, 2, 3} and B = {a, b, c}, then a possible relation from A to B is R = {(1, a), (2, b), (3, c)}.

Operations on relations are ways of combining or modifying relations to obtain new relations. Some common operations on relations are:

- **Union**: The union of two relations R and S, denoted by R ∪ S, is the relation that contains all the ordered pairs that belong to either R or S or both. For example, if R = {(1, a), (2, b), (3, c)} and S = {(2, c), (3, a), (4, b)}, then R ∪ S = {(1, a), (2, b), (2, c), (3, a), (3, c), (4, b)}.
- **Intersection**: The intersection of two relations R and S, denoted by R ∩ S, is the relation that contains all the ordered pairs that belong to both R and S. For example, if R = {(1, a), (2, b), (3, c)} and S = {(2, c), (3, a), (4, b)}, then R ∩ S = {(3, a)}.
- **Complement**: The complement of a relation R, denoted by R', is the relation that contains all the ordered pairs that do not belong to R. For example, if R = {(1, a), (2, b), (3, c)} and A = {1, 2, 3, 4} and B = {a, b, c, d}, then R' = {(1, b), (1, c), (1, d), (2, a), (2, c), (2, d), (3, a), (3, b), (3, d), (4, a), (4, b), (4, c), (4, d)}.
- **Converse**: The converse of a relation R, denoted by R<sup>-1</sup>, is the relation that contains all the ordered pairs obtained by reversing the order of the pairs in R. For example, if R = {(1, a), (2, b), (3, c)}, then R<sup>-1</sup> = {(a, 1), (b, 2), (c, 3)}.
- **Composition**: The composition of two relations R and S, denoted by R ∘ S, is the relation that contains all the ordered pairs (a, c) such that there exists an element b in the common domain of R and S for which (a, b) ∈ R and (b, c) ∈ S. For example, if R = {(1, a), (2, b), (3, c)} and S = {(a, x), (b, y), (c, z)}, then R ∘ S = {(1, x), (2, y), (3, z)}.

These operations on relations satisfy some algebraic properties, such as:

- **Commutativity**: R ∪ S = S ∪ R and R ∩ S = S ∩ R for any relations R and S.
- **Associativity**: (R ∪ S) ∪ T = R ∪ (S ∪ T) and (R ∩ S) ∩ T = R ∩ (S ∩ T) for any relations R, S, and T.
- **Distributivity**: R ∪ (S ∩ T) = (R ∪ S) ∩ (R ∪ T) and R ∩ (S ∪ T) = (R ∩ S) ∪ (R ∩ T) for any relations R, S, and T.
- **Identity**: R ∪ ∅ = R and R ∩ A × B = R for any relation R and sets A and B.
- **Complementation**: R ∪ R' = A × B and R ∩ R' = ∅ for any relation R and sets A and B.
- **Involution**: (R')' = R for any relation R.
- **De Morgan's laws**: (