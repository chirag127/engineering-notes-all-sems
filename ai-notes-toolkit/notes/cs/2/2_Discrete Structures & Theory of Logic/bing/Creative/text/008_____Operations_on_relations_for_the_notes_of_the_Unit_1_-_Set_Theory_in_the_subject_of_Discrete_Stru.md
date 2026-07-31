### Operations on Relations

- A relation is a subset of the Cartesian product of two sets, denoted by R ⊆ A × B.
- The domain of a relation R is the set of elements in A that appear in the first coordinates of some ordered pairs, denoted by dom(R).
- The range of a relation R is the set of elements in B that appear in the second coordinates of some ordered pairs, denoted by ran(R).
- A relation can be represented using a directed graph, where the vertices are the elements of the sets and the edges are the ordered pairs in the relation.
- Some common operations on relations are:
  - Union: R ∪ S is the relation that contains all the ordered pairs that are in either R or S.
  - Intersection: R ∩ S is the relation that contains all the ordered pairs that are in both R and S.
  - Complement: R' is the relation that contains all the ordered pairs that are in A × B but not in R.
  - Converse: R^-1^ is the relation that contains all the ordered pairs that are obtained by reversing the order of the elements in R, i.e., (a, b) ∈ R iff (b, a) ∈ R^-1^.
  - Composition: R ∘ S is the relation that contains all the ordered pairs that are obtained by joining the second element of a pair in R with the first element of a pair in S, i.e., (a, b) ∈ R ∘ S iff there exists c such that (a, c) ∈ R and (c, b) ∈ S.
  - Inverse: R^-1^ is the relation that contains all the ordered pairs that are obtained by swapping the elements in R, i.e., (a, b) ∈ R iff (b, a) ∈ R^-1^.
- Some properties of relations are:
  - Reflexive: A relation R on a set A is reflexive if (a, a) ∈ R for all a ∈ A.
  - Symmetric: A relation R on a set A is symmetric if (a, b) ∈ R implies (b, a) ∈ R for all a, b ∈ A.
  - Transitive: A relation R on a set A is transitive if (a, b) ∈ R and (b, c) ∈ R implies (a, c) ∈ R for all a, b, c ∈ A.
  - Antisymmetric: A relation R on a set A is antisymmetric if (a, b) ∈ R and (b, a) ∈ R implies a = b for all a, b ∈ A.
  - Equivalence: A relation R on a set A is an equivalence relation if it is reflexive, symmetric and transitive.
  - Partial order: A relation R on a set A is a partial order if it is reflexive, antisymmetric and transitive.