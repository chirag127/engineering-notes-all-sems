### Operations on Relations

- A relation is a subset of the Cartesian product of two sets, denoted by R ⊆ A × B.
- The domain of a relation is the set of elements in A that appear in the first coordinates of some ordered pairs, and the range is the set of elements in B that appear in the second coordinates of some ordered pairs.
- A relation can be represented using a directed graph, where the vertices are the elements of the sets and the edges are the ordered pairs in the relation.
- Since relations are sets, they can be manipulated using set operations, such as union, intersection, complement, and difference.
- Union: The union of two relations R and S over the sets A and B is the relation R ∪ S = {(a, b) | (a, b) ∈ R or (a, b) ∈ S}.
- Intersection: The intersection of two relations R and S over the sets A and B is the relation R ∩ S = {(a, b) | (a, b) ∈ R and (a, b) ∈ S}.
- Complement: The complement of a relation R over the sets A and B is the relation R' = {(a, b) | (a, b) ∉ R}.
- Difference: The difference of two relations R and S over the sets A and B is the relation R - S = {(a, b) | (a, b) ∈ R and (a, b) ∉ S}.
- In addition to set operations, there are some other operations on relations, such as converse, composition, and closure.
- Converse: The converse of a relation R over the sets A and B is the relation R^-1 = {(b, a) | (a, b) ∈ R}.
- Composition: The composition of two relations R and S over the sets A, B, and C is the relation R ∘ S = {(a, c) | ∃b ∈ B such that (a, b) ∈ R and (b, c) ∈ S}.
- Closure: The closure of a relation R over a set A is the smallest relation that contains R and satisfies some property, such as reflexivity, symmetry, transitivity, or equivalence.
- Reflexive closure: The reflexive closure of a relation R over a set A is the relation R* = R ∪ {(a, a) | a ∈ A}.
- Symmetric closure: The symmetric closure of a relation R over a set A is the relation R** = R ∪ R^-1.
- Transitive closure: The transitive closure of a relation R over a set A is the relation R+ = R ∪ R ∘ R ∪ R ∘ R ∘ R ∪ ....
- Equivalence closure: The equivalence closure of a relation R over a set A is the relation R*** = R* ∩ R** ∩ R+.