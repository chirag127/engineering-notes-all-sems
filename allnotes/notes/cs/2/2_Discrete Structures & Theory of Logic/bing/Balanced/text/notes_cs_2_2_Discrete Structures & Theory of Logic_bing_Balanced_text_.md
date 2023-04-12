

## Unit 1 - Set Theory

- A set is a collection of well-defined and distinct objects, such as numbers, letters, shapes, etc.
- A set can be represented by listing its elements inside curly braces, such as {1, 2, 3} or {a, b, c}.
- A set can also be described by a rule that specifies the property that its elements must satisfy, such as {x | x is an even integer} or {y | y is a vowel}.
- The order and repetition of elements in a set do not matter, such as {1, 2, 3} = {3, 1, 2} = {1, 1, 2, 3}.
- An element is said to belong to a set if it is one of the objects in the set, such as 2 belongs to {1, 2, 3} but 4 does not belong to {1, 2, 3}.
- The symbol ∈ is used to denote the membership relation, such as 2 ∈ {1, 2, 3} and 4 ∉ {1, 2, 3}.
- A set that contains no elements is called the empty set or the null set, and is denoted by ∅ or {}.
- The number of elements in a set is called the cardinality of the set, and is denoted by |A| for a set A, such as |{1, 2, 3}| = 3 and |∅| = 0.
- Two sets are said to be equal if they have exactly the same elements, such as {1, 2, 3} = {3, 2, 1} and {a, b, c} = {c, a, b}.
- A set A is said to be a subset of another set B if every element of A is also an element of B, such as {1, 2} is a subset of {1, 2, 3} but {1, 4} is not a subset of {1, 2, 3}.
- The symbol ⊆ is used to denote the subset relation, such as {1, 2} ⊆ {1, 2, 3} and {1, 4} ⊈ {1, 2, 3}.
- A set A is said to be a proper subset of another set B if A is a subset of B and A is not equal to B, such as {1, 2} is a proper subset of {1, 2, 3} but {1, 2, 3} is not a proper subset of {1, 2, 3}.
- The symbol ⊂ is used to denote the proper subset relation, such as {1, 2} ⊂ {1, 2, 3} and {1, 2, 3} ⊄ {1, 2, 3}.
- A set A is said to be a superset of another set B if B is a subset of A, such as {1, 2, 3} is a superset of {1, 2} but {1, 2} is not a superset of {1, 4}.
- The symbol ⊇ is used to denote the superset relation, such as {1, 2, 3} ⊇ {1, 2} and {1, 2} ⊉ {1, 4}.
- A set A is said to be a proper superset of another set B if A is a superset of B and A is not equal to B, such as {1, 2, 3} is a proper superset of {1, 2} but {1, 2} is not a proper superset of {1, 2}.
- The symbol ⊃ is used to denote the proper superset relation, such as {1, 2, 3} ⊃ {1, 2} and {1, 2} ⊅ {1, 2}.
- The universal set is the set that contains all the elements under consideration, and is usually denoted by U, such as U = {1, 2, 3, 4, 5, 6} for the set of natural numbers up to 6.
- The complement of a set A is the set of all the elements in the universal set that are not in A, and is denoted by A' or A^c, such as {1, 2, 3}' = {4, 5, 6} and



### Introduction for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- Set theory is a branch of mathematics that studies collections of objects, called sets, and the relationships between them.
- Set theory is the foundation of many other fields of mathematics, such as logic, algebra, geometry, topology, and analysis.
- Set theory also has applications in computer science, such as in data structures, algorithms, databases, and artificial intelligence.
- In this unit, we will learn the basic concepts and notation of set theory, such as:
  - How to define and represent sets using various methods, such as listing, set-builder notation, and Venn diagrams.
  - How to perform operations on sets, such as union, intersection, difference, and complement, and how to use them to express logical statements and properties of sets.
  - How to compare sets using relations, such as subset, superset, equality, and inclusion-exclusion, and how to use them to prove statements and theorems about sets.
  - How to classify sets based on their size, such as finite, infinite, countable, and uncountable, and how to use them to measure the cardinality of sets and the power of different levels of infinity.
  - How to construct and manipulate special sets, such as the empty set, the universal set, the power set, and the set of all subsets of a given set, and how to use them to explore the paradoxes and limitations of set theory.



### Combination of sets

- A combination of sets is a way of forming a new set from existing sets using some operations.
- The most common operations on sets are union, intersection, difference, and complement.
- The union of two sets A and B, denoted by A ∪ B, is the set of all elements that belong to either A or B or both. For example, if A = {1, 2, 3} and B = {3, 4, 5}, then A ∪ B = {1, 2, 3, 4, 5}.
- The intersection of two sets A and B, denoted by A ∩ B, is the set of all elements that belong to both A and B. For example, if A = {1, 2, 3} and B = {3, 4, 5}, then A ∩ B = {3}.
- The difference of two sets A and B, denoted by A - B, is the set of all elements that belong to A but not to B. For example, if A = {1, 2, 3} and B = {3, 4, 5}, then A - B = {1, 2}.
- The complement of a set A, denoted by A', is the set of all elements that do not belong to A. For example, if A = {1, 2, 3} and the universal set U = {1, 2, 3, 4, 5, 6}, then A' = {4, 5, 6}.
- The operations on sets can be combined using parentheses to indicate the order of evaluation. For example, (A ∪ B) ∩ C means to first take the union of A and B, and then take the intersection with C.
- The operations on sets obey some properties, such as commutativity, associativity, distributivity, identity, and complementation. For example, A ∪ B = B ∪ A (commutativity of union), A ∪ (B ∪ C) = (A ∪ B) ∪ C (associativity of union), A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) (distributivity of intersection over union), A ∪ ∅ = A (identity of union), and A ∪ A' = U (complementation of union).



### Multisets

- A multiset is a collection of objects that allows for multiple occurrences of the same element.
- A multiset can be represented by listing its elements within curly braces, with repetition as needed. For example, {a, a, b, c, c, c} is a multiset with six elements, two of which are a, one of which is b, and three of which are c.
- Alternatively, a multiset can be represented by using a function that maps each element to its multiplicity, which is the number of times it appears in the multiset. For example, the multiset {a, a, b, c, c, c} can be represented by the function f such that f(a) = 2, f(b) = 1, f(c) = 3, and f(x) = 0 for any other element x.
- The size of a multiset is the sum of the multiplicities of its elements. For example, the size of the multiset {a, a, b, c, c, c} is 2 + 1 + 3 = 6.
- Two multisets are equal if they have the same elements with the same multiplicities. For example, {a, a, b, c, c, c} and {c, c, c, a, b, a} are equal multisets, but {a, a, b, c, c, c} and {a, b, b, c, c, c} are not.
- A multiset A is a subset of a multiset B if every element of A has a multiplicity that is less than or equal to the multiplicity of the same element in B. For example, {a, b, c} and {a, a, b} are subsets of {a, a, b, c, c, c}, but {a, a, a, b} and {a, b, d} are not.
- The union of two multisets A and B is the multiset that contains every element of A and B with the maximum multiplicity of the two multisets. For example, the union of {a, a, b, c, c, c} and {a, b, b, c, d, d} is {a, a, b, b, c, c, c, d, d}.
- The intersection of two multisets A and B is the multiset that contains every element of A and B with the minimum multiplicity of the two multisets. For example, the intersection of {a, a, b, c, c, c} and {a, b, b, c, d, d} is {a, b, c}.
- The difference of two multisets A and B is the multiset that contains every element of A with the multiplicity of A minus the multiplicity of B, if it is positive, and zero otherwise. For example, the difference of {a, a, b, c, c, c} and {a, b, b, c, d, d} is {a, c, c}.
- The complement of a multiset A with respect to a multiset B is the difference of B and A. For example, the complement of {a, a, b, c, c, c} with respect to {a, b, b, c, d, d} is {b, d, d}.
- The Cartesian product of two multisets A and B is the multiset of all ordered pairs (a, b) where a is an element of A and b is an element of B, with the multiplicity of (a, b) being the product of the multiplicities of a and b. For example, the Cartesian product of {a, a, b} and {c, c, c, d} is {(a, c), (a, c), (a, d), (a, d), (a, c), (a, c), (a, d), (a, d), (b, c), (b, c), (b, c), (b, d)}.
- The power multiset of a multiset A is the multiset of all subsets of A, with the multiplicity of a subset being the number of ways to form it from A. For example, the power multiset of {a, a, b} is {{}, {a}, {a}, {a, a}, {b}, {a, b}, {a, b}, {a, a, b}}.



### Ordered pairs for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- An ordered pair is a pair of two objects that are written inside parentheses and separated by a comma, such as (a, b).
- The order of the objects in an ordered pair is important, as changing the order may result in a different ordered pair, unless the objects are equal. For example, (a, b) is not the same as (b, a) unless a = b.
- An ordered pair can be used to represent a point on a coordinate plane, where the first object is the x-coordinate and the second object is the y-coordinate. For example, (3, 4) represents the point with x = 3 and y = 4.
- An ordered pair can also be used to represent an element of a relation or a cartesian product, which are concepts in set theory. A relation is a set of ordered pairs that show how two sets are related. A cartesian product is a set of all possible ordered pairs that can be formed from two sets. For example, if A = {1, 2} and B = {3, 4}, then A × B = {(1, 3), (1, 4), (2, 3), (2, 4)} is the cartesian product of A and B.



### Proofs of some general identities on sets

- A set is a collection of distinct objects, such as numbers, letters, or shapes.
- An identity is a statement that is true for all possible values of the variables involved, such as x + 0 = x or x * 1 = x.
- A set identity is a statement that is true for all possible sets involved, such as A ∪ ∅ = A or A ∩ A = A.
- To prove a set identity, we need to show that the two sets on either side of the equality sign have the same elements, that is, they are subsets of each other.
- One way to prove a set identity is to use the element method, which involves taking an arbitrary element from one set and showing that it belongs to the other set, and vice versa.
- Another way to prove a set identity is to use the set algebra method, which involves manipulating the sets using the definitions and properties of set operations, such as union, intersection, complement, and difference.
- Here are some examples of set identities and their proofs using both methods:

#### Identity 1: A ∪ A = A
- Element method: Let x be an arbitrary element of A ∪ A. Then x ∈ A or x ∈ A, by the definition of union. But this implies that x ∈ A, by the law of excluded middle. Therefore, A ∪ A ⊆ A. Conversely, let x be an arbitrary element of A. Then x ∈ A and x ∈ A, by the reflexivity of equality. Therefore, x ∈ A ∪ A, by the definition of union. Hence, A ⊆ A ∪ A. Since we have shown that A ∪ A ⊆ A and A ⊆ A ∪ A, we can conclude that A ∪ A = A, by the definition of set equality.
- Set algebra method: A ∪ A = A ∪ (A ∩ A), by the identity property of intersection. Then, A ∪ A = (A ∪ A) ∩ (A ∪ A), by the distributive law of union over intersection. Finally, A ∪ A = A, by the idempotent law of union.

#### Identity 2: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
- Element method: Let x be an arbitrary element of A ∩ (B ∪ C). Then x ∈ A and x ∈ B ∪ C, by the definition of intersection. This means that x ∈ A and (x ∈ B or x ∈ C), by the definition of union. Therefore, (x ∈ A and x ∈ B) or (x ∈ A and x ∈ C), by the distributive law of and over or. Hence, x ∈ (A ∩ B) ∪ (A ∩ C), by the definitions of intersection and union. Therefore, A ∩ (B ∪ C) ⊆ (A ∩ B) ∪ (A ∩ C). Conversely, let x be an arbitrary element of (A ∩ B) ∪ (A ∩ C). Then x ∈ A ∩ B or x ∈ A ∩ C, by the definition of union. This means that (x ∈ A and x ∈ B) or (x ∈ A and x ∈ C), by the definition of intersection. Therefore, x ∈ A and (x ∈ B or x ∈ C), by the distributive law of and over or. Hence, x ∈ A ∩ (B ∪ C), by the definitions of intersection and union. Thus, (A ∩ B) ∪ (A ∩ C) ⊆ A ∩ (B ∪ C). Since we have shown that A ∩ (B ∪ C) ⊆ (A ∩ B) ∪ (A ∩ C) and (A ∩ B) ∪ (A ∩ C) ⊆ A ∩ (B ∪ C), we can conclude that A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C), by the definition of set equality.
- Set algebra method: A ∩ (B ∪ C) = (A ∩ A) ∩ (B ∪ C), by the identity property of intersection. Then, A ∩ (B ∪ C) = A ∩ [(A ∩ B) ∪ (A ∩ C)], by the distributive law of intersection over union. Finally, A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C), by the absorption law of intersection.



### Relations

- A relation is a way of describing a connection or association between two or more sets of elements.
- A relation can be represented by a set of ordered pairs, where the first element of each pair belongs to the first set and the second element belongs to the second set.
- For example, if A = {1, 2, 3} and B = {a, b, c}, then a possible relation between A and B is R = {(1, a), (2, b), (3, c)}.
- The domain of a relation is the set of all the first elements of the ordered pairs, and the range is the set of all the second elements of the ordered pairs.
- For example, if R = {(1, a), (2, b), (3, c)}, then the domain of R is {1, 2, 3} and the range of R is {a, b, c}.
- A relation can also be represented by a mapping diagram, where the elements of the sets are shown as points and the ordered pairs are shown as arrows connecting the points.
- For example, the relation R = {(1, a), (2, b), (3, c)} can be shown as:

Mapping diagram of R

- A relation can also be represented by a matrix, where the rows correspond to the elements of the first set and the columns correspond to the elements of the second set. A 1 in the matrix indicates that the corresponding ordered pair is in the relation, and a 0 indicates that it is not.
- For example, the relation R = {(1, a), (2, b), (3, c)} can be shown as:

|   | a | b | c |
|---|---|---|---|
| 1 | 1 | 0 | 0 |
| 2 | 0 | 1 | 0 |
| 3 | 0 | 0 | 1 |

- A relation can have different properties, such as reflexivity, symmetry, transitivity, antisymmetry, and equivalence. These properties depend on how the ordered pairs are related to each other and to themselves.
- For example, a relation R on a set A is reflexive if for every element x in A, (x, x) is in R. A relation R on a set A is symmetric if for every pair (x, y) in R, (y, x) is also in R. A relation R on a set A is transitive if for every pair (x, y) and (y, z) in R, (x, z) is also in R. A relation R on a set A is antisymmetric if for every pair (x, y) and (y, x) in R, x = y. A relation R on a set A is an equivalence relation if it is reflexive, symmetric, and transitive.



### Definition for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A **set** is a collection of distinct objects, called **elements** or **members** of the set.
- A set can be represented by listing its elements between braces, such as {1, 2, 3}, or by using a rule or a description to specify its elements, such as {x | x is an even positive integer less than 10}.
- Two sets are **equal** if they have exactly the same elements, regardless of the order or repetition of the elements.
- A set is a **subset** of another set if every element of the first set is also an element of the second set. The notation A ⊆ B means that A is a subset of B. Every set is a subset of itself, and the empty set {} is a subset of any set.
- A set is a **proper subset** of another set if it is a subset of the second set and not equal to it. The notation A ⊂ B means that A is a proper subset of B.
- The **union** of two sets A and B, denoted by A ∪ B, is the set of all elements that belong to either A or B or both.
- The **intersection** of two sets A and B, denoted by A ∩ B, is the set of all elements that belong to both A and B.
- The **difference** of two sets A and B, denoted by A - B, is the set of all elements that belong to A but not to B.
- The **complement** of a set A, denoted by A<sup>c</sup>, is the set of all elements that do not belong to A. The complement of A is relative to some universal set U, which contains all the elements under consideration.
- Two sets are **disjoint** if they have no elements in common, that is, if their intersection is the empty set.
- The **cardinality** of a set A, denoted by |A|, is the number of elements in A. The cardinality of the empty set is zero. A set is **finite** if it has a finite cardinality, and **infinite** otherwise.
- A **power set** of a set A, denoted by P(A), is the set of all subsets of A, including the empty set and A itself. The cardinality of the power set of A is 2<sup>|A|</sup>.
- A **Cartesian product** of two sets A and B, denoted by A × B, is the set of all ordered pairs (a, b) such that a ∈ A and b ∈ B. The cardinality of the Cartesian product of A and B is |A| × |B|.



### Operations on relations

- A relation is a subset of a Cartesian product of two or more sets. For example, if A = {1, 2, 3} and B = {a, b, c}, then a relation R from A to B is a subset of A x B, such as R = {(1, a), (2, b), (3, c)}.
- There are some operations that can be performed on relations, such as union, intersection, complement, inverse, composition, and power.
- The union of two relations R and S from A to B is the relation that contains all the ordered pairs that are in either R or S. For example, if R = {(1, a), (2, b)} and S = {(2, c), (3, a)}, then R ∪ S = {(1, a), (2, b), (2, c), (3, a)}.
- The intersection of two relations R and S from A to B is the relation that contains all the ordered pairs that are in both R and S. For example, if R = {(1, a), (2, b)} and S = {(2, b), (3, a)}, then R ∩ S = {(2, b)}.
- The complement of a relation R from A to B is the relation that contains all the ordered pairs that are in A x B but not in R. For example, if A = {1, 2, 3} and B = {a, b, c} and R = {(1, a), (2, b)}, then R' = {(1, b), (1, c), (2, a), (2, c), (3, a), (3, b), (3, c)}.
- The inverse of a relation R from A to B is the relation that contains all the ordered pairs that are obtained by reversing the order of the elements in R. For example, if R = {(1, a), (2, b)}, then R^-1 = {(a, 1), (b, 2)}.
- The composition of two relations R from A to B and S from B to C is the relation that contains all the ordered pairs (a, c) such that there exists an element b in B for which (a, b) is in R and (b, c) is in S. For example, if R = {(1, a), (2, b)} and S = {(a, x), (b, y)}, then R ∘ S = {(1, x), (2, y)}.
- The power of a relation R from A to A is the relation that contains all the ordered pairs that are obtained by applying R repeatedly. For example, if R = {(1, 2), (2, 3), (3, 1)}, then R^2 = {(1, 3), (2, 1), (3, 2)} and R^3 = {(1, 1), (2, 2), (3, 3)}.



### Properties of relations

A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself. A relation R can have some properties that describe how the elements of A are related to each other. Some common properties of relations are:

- Reflexive: A relation R is reflexive if for every element a in A, (a, a) belongs to R. This means that every element is related to itself.
- Symmetric: A relation R is symmetric if for every pair of elements (a, b) in R, (b, a) also belongs to R. This means that the order of the elements does not matter in the relation.
- Transitive: A relation R is transitive if for every pair of elements (a, b) and (b, c) in R, (a, c) also belongs to R. This means that if a is related to b and b is related to c, then a is also related to c.
- Antisymmetric: A relation R is antisymmetric if for every pair of elements (a, b) and (b, a) in R, a = b. This means that the only way two elements can be related in both directions is if they are the same element.
- Irreflexive: A relation R is irreflexive if for every element a in A, (a, a) does not belong to R. This means that no element is related to itself.
- Asymmetric: A relation R is asymmetric if for every pair of elements (a, b) in R, (b, a) does not belong to R. This means that the order of the elements matters in the relation and no element can be related to itself.
- Equivalence: A relation R is an equivalence relation if it is reflexive, symmetric and transitive. This means that the relation partitions the set A into disjoint subsets, called equivalence classes, such that every element in a class is related to every other element in the same class, and no element in a class is related to any element in a different class.
- Partial order: A relation R is a partial order if it is reflexive, antisymmetric and transitive. This means that the relation imposes a hierarchy among the elements of A, such that some elements are comparable and some are not, and there is no circularity in the relation.
- Total order: A relation R is a total order if it is a partial order and for every pair of elements a and b in A, either (a, b) or (b, a) belongs to R. This means that the relation imposes a linear order among the elements of A, such that every element is comparable to every other element, and there is a unique smallest and largest element in the set.



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



### Equality of relations

- A relation is a set of ordered pairs that represents a connection or association between two sets, called the domain and the codomain of the relation.
- Two relations are said to be equal if they have the same domain, the same codomain, and the same set of ordered pairs.
- In other words, two relations are equal if they have the same extension, that is, the same collection of elements that satisfy the relation.
- Equality of relations is an example of an equivalence relation, which is a relation that is reflexive, symmetric, and transitive.
- Reflexive means that every element is related to itself, symmetric means that if one element is related to another, then the other is related to the first, and transitive means that if one element is related to a second, and the second is related to a third, then the first is related to the third.
- The identity relation is the simplest equivalence relation, which relates every element to itself and nothing else.
- Equality of relations is important in set theory, because it allows us to define sets as well-determined collections that are completely characterized by their elements. Thus, two sets are equal if and only if they contain the same elements. The basic relation in set theory is that of elementhood, or membership.



### Recursive definition of relation for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation is a set of ordered pairs, where each pair consists of an element from a set A and an element from a set B.
- A relation can be defined recursively by specifying a base case and a recursive step.
- A base case is a relation that contains a finite number of ordered pairs, or no ordered pairs at all.
- A recursive step is a rule that generates new ordered pairs from existing ones, using operations such as union, intersection, complement, inverse, or composition.
- For example, let A = {a, b, c} and B = {1, 2, 3}. A base case for a relation R from A to B is R = {(a, 1), (b, 2)}.
- A recursive step for R is to add the inverse of each pair in R to R. That is, R = R ∪ {(1, a), (2, b)}.
- Applying the recursive step again, we get R = R ∪ {(a, 2), (b, 1), (1, b), (2, a)}.
- And so on, until no new pairs can be generated. The final relation R is {(a, 1), (a, 2), (b, 1), (b, 2), (1, a), (1, b), (2, a), (2, b)}.
- This is an example of a recursive definition of a relation. It specifies how to construct the relation from a base case and a recursive step.



### Order of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation R on a set S is a subset of S × S, that is, a set of ordered pairs of elements from S.
- A relation R on a set S is an ordering relation if R is reflexive, anti-symmetric and transitive.
- Reflexive means that for any x in S, xRx holds.
- Anti-symmetric means that for any distinct x and y in S, if xRy then not yRx .
- Transitive means that for any x, y and z in S, if xRy and yRz then xRz.
- A set with an ordering relation is called a partially ordered set or a poset.
- A poset with every pair of distinct elements comparable is called a totally ordered set or a chain.
- Comparable means that for any distinct x and y in S, either xRy or yRx holds.
- A total ordering is also called a linear ordering.



### Functions

- A function is a special kind of relation between two sets, called the domain and the codomain, that assigns exactly one element of the codomain to each element of the domain  .
- A function can be represented by a set of ordered pairs, a table, a graph, or a formula .
- The notation f:A→B means that f is a function from the set A to the set B  .
- The element of A that is mapped by f to an element of B is called the argument or input of f, and the element of B that is assigned to it is called the value or output of f  .
- The notation f(a) = b means that the value of f at a is b, or equivalently, that f maps a to b  .
- The set of all possible arguments of f is called the domain of f, and the set of all possible values of f is called the range of f  .
- The range of f is always a subset of the codomain of f, but it may not be equal to it  .
- A function is said to be well-defined if it assigns a unique value to each argument in its domain .
- A function is said to be one-to-one or injective if it maps different arguments to different values, that is, if f(a) = f(b) implies a = b for any a and b in the domain of f  .
- A function is said to be onto or surjective if its range is equal to its codomain, that is, if every element of the codomain is mapped by f to some element of the domain  .
- A function is said to be bijective or invertible if it is both one-to-one and onto, that is, if it establishes a one-to-one correspondence between the elements of its domain and codomain  .
- A function f has an inverse function f^-1 if f is bijective, and f^-1 maps each element of the codomain of f to the unique element of the domain of f that is mapped to it by f, that is, if f^-1(f(a)) = a and f(f^-1(b)) = b for any a in the domain of f and b in the codomain of f  .
- Two functions f and g are said to be equal if they have the same domain, the same codomain, and the same value for every argument in their domain, that is, if f(a) = g(a) for any a in the domain of f and g  .
- Two functions f and g are said to be compatible if they have the same codomain  .
- The composition of two compatible functions f and g, denoted by f∘g, is a function that maps each element of the domain of g to the value of f at the value of g at that element, that is, if f∘g(a) = f(g(a)) for any a in the domain of g  .
- The identity function on a set A, denoted by id_A, is a function that maps each element of A to itself, that is, if id_A(a) = a for any a in A  .
- A function f is said to be an identity function if f = id_A for some set A  .
- A function f is said to be constant if it has the same value for every argument in its domain, that is, if f(a) = f(b) for any a and b in the domain of f  .
- A function f is said to be periodic if there exists a positive number



### Definition for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A **set** is a collection of distinct objects, called **elements** or **members** of the set.
- A set can be defined by listing its elements between braces, such as {1, 2, 3}, or by using a rule or a description, such as {x | x is an even positive integer less than 10}.
- Two sets are **equal** if they have exactly the same elements, regardless of the order or repetition of the elements.
- A set is a **subset** of another set if every element of the first set is also an element of the second set. The notation A ⊆ B means that A is a subset of B. Every set is a subset of itself, and the empty set is a subset of any set.
- A set is a **proper subset** of another set if it is a subset of the second set and not equal to it. The notation A ⊂ B means that A is a proper subset of B.
- The **union** of two sets is the set of all elements that belong to either set or both. The notation A ∪ B means the union of A and B.
- The **intersection** of two sets is the set of all elements that belong to both sets. The notation A ∩ B means the intersection of A and B.
- The **difference** of two sets is the set of all elements that belong to the first set but not the second set. The notation A \ B means the difference of A and B.
- The **complement** of a set is the set of all elements that do not belong to the set. The notation A^c means the complement of A.
- Two sets are **disjoint** if they have no elements in common, that is, their intersection is the empty set.
- A **universal set** is a set that contains all the elements under consideration in a given context. The notation U is often used for the universal set.
- A **Venn diagram** is a graphical representation of sets using circles or other shapes. The universal set is usually represented by a rectangle, and the sets are represented by regions inside the rectangle. The union, intersection, difference, and complement of sets can be shown by shading or labeling the regions appropriately.



### Classification of functions

- A function is a relation that assigns to each element of a set A exactly one element of a set B.
- A function can be classified into different types based on various criteria, such as:
  - The number of sets involved
  - The cardinality of the sets involved
  - The type of elements in the sets involved
  - The properties of the function itself
- Some common types of functions are:

  - **Unary, binary, and n-ary functions**: These are functions that have one, two, or n sets as their domain, respectively. For example, the factorial function is a unary function, the addition function is a binary function, and the maximum function is an n-ary function.
  - **Injective, surjective, and bijective functions**: These are functions that have different relationships between the elements of their domain and codomain. An injective function maps distinct elements of the domain to distinct elements of the codomain. A surjective function maps every element of the codomain to some element of the domain. A bijective function is both injective and surjective, and has a one-to-one correspondence between the elements of the domain and codomain.
  - **Constant, identity, and inverse functions**: These are functions that have special values or operations. A constant function maps every element of the domain to the same element of the codomain. An identity function maps every element of the domain to itself. An inverse function reverses the mapping of another function, such that f^-1(f(x)) = x for every x in the domain of f.
  - **Polynomial, rational, and algebraic functions**: These are functions that involve arithmetic operations on the elements of the domain. A polynomial function is a function of the form f(x) = a_n x^n + a_n-1 x^n-1 + ... + a_1 x + a_0, where a_i are constants and n is a non-negative integer. A rational function is a function of the form f(x) = p(x) / q(x), where p(x) and q(x) are polynomial functions and q(x) is not zero. An algebraic function is a function that can be expressed using a finite number of arithmetic operations, roots, and fractions.
  - **Exponential, logarithmic, and trigonometric functions**: These are functions that involve special mathematical constants or ratios. An exponential function is a function of the form f(x) = a^x, where a is a positive constant. A logarithmic function is a function of the form f(x) = log_a x, where a is a positive constant and x is positive. A trigonometric function is a function of the form f(x) = sin x, cos x, tan x, etc., where x is an angle measured in radians or degrees.



### Operations on functions

- A function is a relation that assigns to each element of a set A (called the domain) exactly one element of a set B (called the codomain).
- A function can be represented by a set of ordered pairs, a table, a graph, or a formula.
- The notation f: A -> B means that f is a function from A to B.
- The notation f(a) = b means that b is the value of the function f at a, or the image of a under f.
- The set of all images of the elements of A under f is called the range of f, and it is a subset of B.
- Two functions f and g are equal if they have the same domain, codomain, and value for every element of the domain.
- Some common types of functions are:
  - Identity function: f(x) = x for all x in the domain.
  - Constant function: f(x) = c for some constant c and all x in the domain.
  - Linear function: f(x) = ax + b for some constants a and b and all x in the domain.
  - Quadratic function: f(x) = ax^2 + bx + c for some constants a, b, and c and all x in the domain.
  - Polynomial function: f(x) = a_n x^n + a_(n-1) x^(n-1) + ... + a_1 x + a_0 for some constants a_0, a_1, ..., a_n and all x in the domain.
  - Exponential function: f(x) = a^x for some constant a > 0 and all x in the domain.
  - Logarithmic function: f(x) = log_a x for some constant a > 0 and all x in the domain.
  - Trigonometric function: f(x) = sin x, cos x, tan x, etc. for all x in the domain.
  - Inverse function: f^(-1)(x) is the function that satisfies f(f^(-1)(x)) = x and f^(-1)(f(x)) = x for all x in the domain of f^(-1) and the range of f, respectively.
- Operations on functions are ways of combining two or more functions to create a new function.
- Some common operations on functions are:
  - Composition: (f o g)(x) = f(g(x)) for all x in the domain of g such that g(x) is in the domain of f.
  - Addition: (f + g)(x) = f(x) + g(x) for all x in the domain of both f and g.
  - Subtraction: (f - g)(x) = f(x) - g(x) for all x in the domain of both f and g.
  - Multiplication: (f * g)(x) = f(x) * g(x) for all x in the domain of both f and g.
  - Division: (f / g)(x) = f(x) / g(x) for all x in the domain of both f and g such that g(x) is not zero.
- Operations on functions have some properties, such as:
  - Associativity: (f o g) o h = f o (g o h) for all functions f, g, and h with compatible domains and codomains.
  - Commutativity: f + g = g + f and f * g = g * f for all functions f and g with compatible domains and codomains.
  - Distributivity: f * (g + h) = (f * g) + (f * h) and (g + h) * f = (g * f) + (h * f) for all functions f, g, and h with compatible domains and codomains.
  - Identity: f o i = i o f = f for all functions f and the identity function i with compatible domains and codomains.
  - Inverse: f o f^(-1) = f^(-1) o f = i for all functions f and their inverses f^(-1) with compatible domains and codomains.



### Recursively defined functions

- A recursively defined function is a function that its value at any point can be calculated from the values of the function at some previous points .
- A recursively defined function consists of two parts: a base case and a recursive step.
- The base case specifies the value of the function for some initial values of the variable, usually the smallest or simplest ones.
- The recursive step specifies how to compute the value of the function for any other value of the variable, using the values of the function for smaller or simpler values of the variable.
- For example, the factorial function n! can be defined recursively as follows:
  - Base case: 0! = 1
  - Recursive step: For any positive integer n, n! = n * (n-1)!
- A recursively defined function can also be represented by a recurrence relation, which is an equation that expresses the value of the function in terms of its previous values.
- For example, the recurrence relation for the factorial function is: a_n = n * a_(n-1), with a_0 = 1
- A recurrence relation can be solved to find an explicit formula for the function, which does not depend on its previous values.
- For example, the explicit formula for the factorial function is: n! = n * (n-1) * (n-2) * ... * 2 * 1
- Some methods to solve recurrence relations are: substitution, iteration, characteristic equation, generating functions, etc.



### Growth of Functions

- A function f(n) is said to grow faster than a function g(n) if there exists a positive constant c and a positive integer N such that f(n) > c g(n) for all n > N.
- The growth of a function is a measure of how quickly its values increase as the input variable increases.
- The growth of a function can be compared using asymptotic notation, such as big O, big Omega, and big Theta, which describe the upper, lower, and tight bounds of a function respectively.
- Asymptotic notation is useful for analyzing the efficiency and complexity of algorithms, as well as the behavior of sequences and series.
- Some examples of common functions and their growth rates are:

| Function | Growth Rate |
| -------- | ----------- |
| Constant | O(1)        |
| Logarithmic | O(log n)   |
| Linear | O(n)         |
| Linearithmic | O(n log n) |
| Quadratic | O(n^2)      |
| Cubic | O(n^3)        |
| Exponential | O(2^n)     |
| Factorial | O(n!)       |

- The growth rate of a function can be determined by applying some rules, such as:

  - If f(n) and g(n) are positive functions, then O(f(n) + g(n)) = O(max(f(n), g(n))).
  - If f(n) and g(n) are positive functions, then O(f(n) g(n)) = O(f(n)) O(g(n)).
  - If f(n) and g(n) are positive functions, then O(f(g(n))) = O(g(n)) if f(n) is O(1), and O(f(n)) if g(n) is O(1).
  - If f(n) and g(n) are positive functions, then O(f(n)^g(n)) = O(2^g(n) log f(n)).
  - If f(n) and g(n) are positive functions, then O(log f(n)) = O(log g(n)) if f(n) and g(n) have the same asymptotic growth rate.



### Natural Numbers

- Natural numbers are the numbers that are used to count objects or quantities. They are also called counting numbers or positive integers.
- The set of natural numbers is denoted by N = {1, 2, 3, ...}.
- Natural numbers have the following properties:
  - They are infinite, meaning there is no largest natural number.
  - They are ordered, meaning there is a natural way to compare them using the symbols <, >, =, ≤, and ≥.
  - They are closed under addition and multiplication, meaning the sum and product of any two natural numbers is also a natural number.
  - They have an identity element for both addition and multiplication, meaning there is a natural number that does not change the value of any other natural number when added or multiplied to it. This number is 1.
  - They have an associative property for both addition and multiplication, meaning the order of grouping does not affect the result of adding or multiplying natural numbers. For example, (a + b) + c = a + (b + c) and (a × b) × c = a × (b × c) for any natural numbers a, b, and c.
  - They have a commutative property for both addition and multiplication, meaning the order of operands does not affect the result of adding or multiplying natural numbers. For example, a + b = b + a and a × b = b × a for any natural numbers a and b.
  - They have a distributive property of multiplication over addition, meaning the product of a natural number and the sum of two natural numbers is equal to the sum of the products of the natural number and each of the two natural numbers. For example, a × (b + c) = (a × b) + (a × c) for any natural numbers a, b, and c.
  - They do not have a closure property under subtraction and division, meaning the difference and quotient of any two natural numbers may not be a natural number. For example, 3 - 5 and 5 / 3 are not natural numbers.
  - They do not have an inverse element for either subtraction or division, meaning there is no natural number that can be subtracted or divided from any other natural number to get 0. For example, there is no natural number x such that 5 - x = 0 or 5 / x = 0.
  - They do not have a zero element, meaning there is no natural number that represents nothing or emptiness. The number 0 is not a natural number, but a whole number.



### Introduction for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- Set theory is a branch of mathematics that studies collections of objects, called sets, and the relationships between them.
- Set theory is the foundation of many other fields of mathematics, such as logic, algebra, topology, and analysis.
- Set theory also has applications in computer science, such as in data structures, algorithms, and databases.
- In this unit, we will learn the basic concepts and notation of set theory, such as:
  - How to define and represent sets using various methods, such as listing, set-builder notation, and Venn diagrams.
  - How to perform operations on sets, such as union, intersection, difference, and complement, and how to use them to express logical statements and properties of sets.
  - How to compare sets using relations, such as subset, superset, equality, and inclusion-exclusion, and how to use them to prove statements and theorems about sets.
  - How to classify sets based on their size, such as finite, infinite, countable, and uncountable sets, and how to use them to measure the cardinality of sets and the power of different levels of infinity.
  - How to construct and manipulate special sets, such as the empty set, the universal set, the power set, and the set of all subsets of a given set, and how to use them to explore the paradoxes and limitations of set theory.



### Mathematical Induction

- Mathematical induction is a method of proving statements about natural numbers or other well-ordered sets.
- The basic idea is to show that a statement is true for some initial element of the set, and then show that if it is true for any element, it is also true for the next element in the order.
- This implies that the statement is true for all elements of the set by the principle of well-ordering, which states that every non-empty subset of a well-ordered set has a least element.
- The method of mathematical induction consists of two steps: the base case and the induction step.
- The base case is to verify that the statement is true for the smallest or first element of the set, usually denoted by 1 or 0.
- The induction step is to assume that the statement is true for some element k of the set, and then show that it is also true for k+1, the next element in the order. This is called the induction hypothesis and the induction conclusion, respectively.
- An example of a statement that can be proved by mathematical induction is the following: for any natural number n, the sum of the first n natural numbers is equal to n(n+1)/2. That is, 1 + 2 + ... + n = n(n+1)/2.
- To prove this by mathematical induction, we first check the base case: for n = 1, the statement is true, since 1 = 1(1+1)/2.
- Then, we assume the induction hypothesis: for some k, the statement is true, that is, 1 + 2 + ... + k = k(k+1)/2.
- Next, we show the induction conclusion: for k+1, the statement is also true, that is, 1 + 2 + ... + (k+1) = (k+1)((k+1)+1)/2.
- To do this, we add k+1 to both sides of the induction hypothesis, and simplify the result using algebra. We get:

1 + 2 + ... + k + (k+1) = k(k+1)/2 + (k+1)

= (k+1)(k/2 + 1)

= (k+1)(k+2)/2

= (k+1)((k+1)+1)/2

- This shows that the statement is true for k+1, and completes the induction step.
- Therefore, by mathematical induction, the statement is true for all natural numbers n.



### Variants of Induction

Induction is a method of proving statements about sets that are well-ordered, meaning that every non-empty subset has a least element. Induction is based on the idea of showing that a statement holds for the least element of a set, and then showing that it holds for any successor element, given that it holds for the predecessor. There are different variants of induction, depending on the type of set and the type of statement involved. Some of the common variants are:

- **Ordinary induction**: This is the most familiar form of induction, where the set is the natural numbers, and the statement is a property that depends on a single natural number. For example, to prove that the sum of the first n natural numbers is n(n+1)/2, one can use ordinary induction on n. The base case is n = 0, where the sum is 0 and the formula is 0(0+1)/2 = 0. The induction step is to assume that the statement holds for n = k, and then show that it holds for n = k+1, by using the assumption and some algebra. This shows that the statement holds for all natural numbers.

- **Strong induction**: This is a variant of ordinary induction, where the set is still the natural numbers, but the statement is a property that depends on all natural numbers less than or equal to a given natural number. For example, to prove that every natural number greater than 1 is either prime or a product of primes, one can use strong induction on n. The base case is n = 2, which is prime. The induction step is to assume that the statement holds for all natural numbers less than or equal to k, and then show that it holds for n = k+1, by using the assumption and the fact that if k+1 is not prime, then it has a divisor less than itself. This shows that the statement holds for all natural numbers greater than 1.

- **Structural induction**: This is a form of induction where the set is a recursively defined set, such as the set of strings, the set of formulas, the set of trees, etc. The statement is a property that depends on the structure of an element of the set. For example, to prove that the number of left parentheses in a well-formed formula is equal to the number of right parentheses, one can use structural induction on the formula. The base case is when the formula is a single variable, which has no parentheses. The induction step is to assume that the statement holds for two formulas A and B, and then show that it holds for the formulas (A), ¬A, A∧B, A∨B, A→B, and A↔B, by using the assumption and counting the parentheses. This shows that the statement holds for all well-formed formulas.

- **Transfinite induction**: This is a generalization of induction where the set is an ordinal number, which is a well-ordered set that is not necessarily countable. The statement is a property that depends on an ordinal number. For example, to prove that every ordinal number has a unique successor, one can use transfinite induction on the ordinal number. The base case is when the ordinal number is 0, which has 1 as its unique successor. The induction step is to assume that the statement holds for an ordinal number α, and then show that it holds for the successor of α, which is α∪{α}, by using the assumption and the definition of ordinal numbers. This shows that the statement holds for all ordinal numbers.



### Induction with Nonzero Base Cases

- Induction is a method of proving statements of the form "for all natural numbers n, P(n) is true", where P is some predicate.
- The basic idea of induction is to show that P(n) is true for some initial value of n (called the base case), and then show that if P(n) is true for some arbitrary value of n, then P(n+1) is also true (called the inductive step).
- The base case does not have to be n = 0. Sometimes, it is more convenient or natural to start the induction from a nonzero value of n, such as n = 1 or n = 5.
- For example, suppose we want to prove that for all natural numbers n greater than or equal to 5, n^2 < 2^n. We can use induction with n = 5 as the base case, and show that if n^2 < 2^n for some n >= 5, then (n+1)^2 < 2^(n+1) for the next value of n.
- When using induction with a nonzero base case, we have to make sure that the statement we want to prove is true for all values of n from the base case onwards. For example, if we want to prove that for all natural numbers n greater than or equal to 1, P(n) is true, we cannot use induction with n = 0 as the base case, because P(0) may not be true or even well-defined.
- Sometimes, we can use a stronger form of induction, called strong induction, to prove statements without a separate base case. In strong induction, we assume that P(n) is true for all values of n less than or equal to some arbitrary value of n, and then show that P(n+1) is true. This way, we can use the smallest value of n for which P(n) is true as the base case, and the induction step will cover all the other values of n. However, strong induction is not always applicable or simpler than ordinary induction.



### Proof Methods for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A proof is a logical argument that establishes the validity of a statement or a theorem.
- A proof consists of a sequence of statements that are either axioms, definitions, or logical consequences of previous statements.
- A proof must be complete, correct, and clear.
- There are different methods of proof, such as direct proof, indirect proof, proof by contradiction, proof by cases, and proof by induction.
- A direct proof is a proof that starts from the given premises and uses logical rules to derive the conclusion.
- An indirect proof is a proof that assumes the negation of the conclusion and shows that it leads to a contradiction with the premises or a known fact.
- A proof by contradiction is a special case of indirect proof, where the negation of the statement to be proved is assumed and a contradiction is derived.
- A proof by cases is a proof that divides the possible cases into mutually exclusive and exhaustive subcases, and proves the statement for each subcase.
- A proof by induction is a proof that establishes a statement for all natural numbers by showing that it holds for the base case (usually n = 0 or n = 1) and that it follows from the induction hypothesis (the statement for n = k) to the induction step (the statement for n = k + 1).



### Proof by counter – example for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A proof by counterexample is a method of disproving a general statement by finding a specific case where the statement is false.
- A counterexample is a specific instance that contradicts a conjecture or a hypothesis.
- To prove a statement by counterexample, we need to find one example that makes the statement false. We do not need to check all possible cases or provide a general argument.
- A proof by counterexample has the following form:

  - Suppose we want to disprove a statement of the form "For all x, P(x) is true", where x is a variable and P(x) is a predicate.
  - We find a specific value of x, say a, such that P(a) is false.
  - We conclude that the statement "For all x, P(x) is true" is false, because it does not hold for x = a.

- Example: Prove by counterexample that the statement "For all natural numbers n, n^2 + n + 41 is prime" is false.

  - To find a counterexample, we need to find a natural number n such that n^2 + n + 41 is not prime.
  - One possible counterexample is n = 40. Then n^2 + n + 41 = 40^2 + 40 + 41 = 1681, which is not prime, because it is divisible by 41.
  - Therefore, the statement "For all natural numbers n, n^2 + n + 41 is prime" is false, because it does not hold for n = 40.



### Proof by contradiction

- A proof by contradiction is a method of proving a statement by assuming that it is false and deriving a contradiction from that assumption.
- The contradiction can be a logical inconsistency, a violation of a known fact, or an absurdity.
- The contradiction implies that the original assumption was wrong, and therefore the statement is true.
- A proof by contradiction can be written in the following form:

  - Suppose that statement P is false. (This is the negation of P, denoted by ¬P)
  - Show that ¬P leads to a contradiction Q.
  - Conclude that P is true.

- For example, to prove that √2 is irrational, we can use a proof by contradiction as follows:

  - Suppose that √2 is rational. (This is the negation of the statement we want to prove)
  - Then √2 can be written as a fraction a/b, where a and b are positive integers with no common factors. (This is the definition of a rational number)
  - Squaring both sides, we get 2 = a^2 / b^2, or 2b^2 = a^2. (This is a simple algebraic manipulation)
  - This implies that a^2 is even, since it is divisible by 2. (This is a property of even numbers)
  - Therefore, a is also even, since the square of an odd number is odd. (This is another property of even numbers)
  - Let a = 2k, where k is some positive integer. (This is how we write an even number as a multiple of 2)
  - Substituting a = 2k into 2b^2 = a^2, we get 2b^2 = (2k)^2, or b^2 = 2k^2. (This is another algebraic manipulation)
  - This implies that b^2 is even, and therefore b is also even. (This is the same reasoning as before)
  - But this contradicts the assumption that a and b have no common factors, since they are both divisible by 2. (This is a contradiction)
  - Hence, √2 is irrational. (This is the conclusion)



## Unit 2 - Algebraic Structures

- An algebraic structure is a set of elements with one or more operations defined on it that satisfy certain properties or axioms.
- Examples of algebraic structures are groups, rings, fields, vector spaces, matrices, etc.
- A group is an algebraic structure that consists of a set G and a binary operation * such that:
  - The operation * is closed, meaning that for any a, b in G, a * b is also in G.
  - The operation * is associative, meaning that for any a, b, c in G, (a * b) * c = a * (b * c).
  - There exists an identity element e in G such that for any a in G, a * e = e * a = a.
  - For every element a in G, there exists an inverse element a^-1 in G such that a * a^-1 = a^-1 * a = e.
- A ring is an algebraic structure that consists of a set R and two binary operations + and * such that:
  - The operation + is closed, associative, commutative, and has an identity element 0 and an inverse element -a for every a in R.
  - The operation * is closed, associative, and has an identity element 1.
  - The operation * is distributive over +, meaning that for any a, b, c in R, a * (b + c) = (a * b) + (a * c) and (b + c) * a = (b * a) + (c * a).
- A field is an algebraic structure that consists of a set F and two binary operations + and * such that:
  - The operation + is closed, associative, commutative, and has an identity element 0 and an inverse element -a for every a in F.
  - The operation * is closed, associative, commutative, and has an identity element 1 and an inverse element a^-1 for every nonzero a in F.
  - The operation * is distributive over +, meaning that for any a, b, c in F, a * (b + c) = (a * b) + (a * c) and (b + c) * a = (b * a) + (c * a).
- A vector space is an algebraic structure that consists of a set V and two operations + and * such that:
  - The operation + is closed, associative, commutative, and has an identity element 0 and an inverse element -v for every v in V.
  - The operation * is a scalar multiplication, meaning that it takes an element from a field F and an element from V and returns an element from V.
  - The operation * is distributive over +, meaning that for any a, b in F and u, v in V, (a + b) * v = (a * v) + (b * v) and a * (u + v) = (a * u) + (a * v).
  - The operation * is compatible with the field operations, meaning that for any a, b in F and v in V, 1 * v = v and (a * b) * v = a * (b * v).
- A matrix is an algebraic structure that consists of a rectangular array of elements from a field F. The size of a matrix is determined by its number of rows and columns. A matrix can be added, subtracted, or multiplied by another matrix of the same size or by a scalar from F. The properties of these operations are similar to those of vector spaces.



### Definition for the notes of the Unit 2 - Algebraic Structures in the subject of Discrete Structures & Theory of Logic

- An **algebraic structure** is a mathematical object that consists of a set of elements and one or more operations that satisfy certain properties or axioms.
- A **set** is a collection of distinct objects, such as numbers, letters, symbols, or other sets.
- An **operation** is a rule that assigns an element of the set to each pair of elements of the set, such as addition, multiplication, or subtraction.
- An **axiom** is a statement that is assumed to be true without proof, such as the commutative, associative, or distributive laws.
- An algebraic structure can be classified into different types based on the number and properties of the operations, such as groups, rings, fields, lattices, etc.
- **Discrete structures** are mathematical objects that are finite or countable, such as graphs, logic, codes, or cryptography.
- **Discrete mathematics** is the branch of mathematics that studies discrete structures and their applications in computer science, logic, combinatorics, etc.
- **Theory of logic** is the study of the principles and methods of reasoning, such as propositional logic, predicate logic, or modal logic.
- **Algebraic structures** are important in discrete mathematics and theory of logic because they can be used to model and analyze various phenomena, such as symmetries, encryption, algorithms, or languages  .



### Groups

- A group is a set G with a binary operation * that satisfies the following properties:
  - Closure: For all a, b in G, a * b is also in G.
  - Associativity: For all a, b, c in G, (a * b) * c = a * (b * c).
  - Identity: There exists an element e in G such that for all a in G, e * a = a * e = a. This element is called the identity element of G.
  - Inverse: For every element a in G, there exists an element b in G such that a * b = b * a = e. This element is called the inverse of a and is denoted by a^-1.
- A group is called abelian or commutative if it also satisfies the following property:
  - Commutativity: For all a, b in G, a * b = b * a.
- Examples of groups:
  - The set of integers Z with the operation of addition (+) is an abelian group. The identity element is 0 and the inverse of a is -a.
  - The set of nonzero rational numbers Q* with the operation of multiplication (×) is an abelian group. The identity element is 1 and the inverse of a is 1/a.
  - The set of 2×2 invertible matrices with real entries M(2, R) with the operation of matrix multiplication is a group, but not abelian. The identity element is the identity matrix I and the inverse of a matrix A is A^-1.
  - The set of permutations of a finite set S with the operation of composition (◦) is a group, but not abelian. The identity element is the identity permutation id and the inverse of a permutation σ is σ^-1. This group is denoted by S_n, where n is the number of elements in S.



### Subgroups and order

- A **subgroup** of a group is a subset of the group that is also a group under the same operation.
- For example, the set of even integers is a subgroup of the group of integers under addition, since it is closed under addition and contains the identity element (0) and the inverse of every element.
- A subgroup is denoted by the symbol ⊆, which means "is a subgroup of" or "is contained in".
- To check if a subset H of a group G is a subgroup, we can use the following **subgroup test**: H is a subgroup of G if and only if
  - H is non-empty
  - For any two elements a and b in H, a * b is also in H (closure property)
  - For any element a in H, a<sup>-1</sup> is also in H (inverse property)
- The **order** of a group is the number of elements in the group, denoted by |G|.
- The order of a subgroup is the number of elements in the subgroup, denoted by |H|.
- The order of an element a in a group G is the smallest positive integer n such that a<sup>n</sup> = e, where e is the identity element of G. The order of an element is denoted by o(a) or |a|.
- If no such n exists, then the element has infinite order.
- For example, in the group of integers under addition, the order of 0 is 1, the order of 1 is infinite, and the order of 2 is infinite.



### Cyclic Groups

- A group (G, ∘) is called a cyclic group if there exists an element a∈G such that G is generated by a. In other words, every element of G can be written as a power of a .
- The element a is called a generator or a cyclic generator of G. A cyclic group may have more than one generator. For example, the group (Z, +) is cyclic and generated by both 1 and -1.
- The order of a cyclic group is the number of elements in the group. If the order of a cyclic group is finite, say n, then the order of any generator a is also n. That is, an = e, where e is the identity element of the group .
- A cyclic group of order n is denoted by Cn or Zn. For example, C4 = {e, a, a2, a3} is a cyclic group of order 4 generated by a.
- A cyclic group is always abelian, that is, it satisfies the commutative property: a ∘ b = b ∘ a for any a, b ∈ G .
- A cyclic group has exactly one subgroup of order d for each divisor d of n, where n is the order of the group. For example, C6 has subgroups of order 1, 2, 3, and 6 .
- A cyclic group is isomorphic to another cyclic group if and only if they have the same order. For example, C4 is isomorphic to Z4 .



### Cosets

- A **coset** of a subgroup H of a group (G, o) is a subset of G obtained by multiplying H with elements of G from left or right .
- Depending on the multiplication from left or right, we can classify cosets as **left cosets** or **right cosets** as follows:
  - A **left coset** of H in G is a subset of G of the form aH = {ah | h ∈ H} for some a ∈ G.
  - A **right coset** of H in G is a subset of G of the form Ha = {ha | h ∈ H} for some a ∈ G.
- For example, take H = {0, 2, 4, 6} and G = {0, 1, 2, 3, 4, 5, 6, 7} with addition modulo 8 as the operation. Then 1 + H = {1, 3, 5, 7} and H + 5 = {5, 7, 1, 3} are left and right cosets of H in G, respectively.
- Cosets are mainly used to decompose a group G into equal-sized disjoint subsets of G. It plays an important role to study many things in Group Theory; for example, normal group, Lagrange’s theorem on finite groups, etc.
- Some properties of cosets are :
  - The number of elements in a left coset of H in G is equal to the number of elements in H. Similarly, the number of elements in a right coset of H in G is equal to the number of elements in H.
  - Two left cosets of H in G are either equal or disjoint. Similarly, two right cosets of H in G are either equal or disjoint.
  - The union of all left cosets of H in G is equal to G. Similarly, the union of all right cosets of H in G is equal to G.
  - The number of left cosets of H in G is equal to the number of right cosets of H in G. This number is called the **index** of H in G and is denoted by [G : H].
  - If H is a finite subgroup of a finite group G, then [G : H] = |G| / |H|, where |G| and |H| are the orders of G and H, respectively. This is known as **Lagrange's theorem**.



### Lagrange's theorem for the notes of the Unit 2 - Algebraic Structures in the subject of Discrete Structures & Theory of Logic

- Lagrange's theorem is one of the central theorems of abstract algebra. It states that in group theory, for any finite group say G, the order of subgroup H of group G divides the order of G. The order of the group represents the number of elements .
- Lagrange's theorem can be expressed as |G| = n|H|, where n is a positive integer called the index of H in G.
- Lagrange's theorem can be proved by using the concept of cosets of a subgroup. A coset of H in G is a subset of G that is obtained by multiplying all the elements of H by a fixed element of G. There are two types of cosets: left cosets and right cosets. A left coset of H in G is denoted by gH, where g is any element of G. A right coset of H in G is denoted by Hg, where g is any element of G.
- The proof of Lagrange's theorem relies on the following facts:
  - Every element of G belongs to some coset of H, since e ∈ H and g ∈ gH for every g ∈ G.
  - Every element of G belongs to exactly one coset of H, since if gH = g'H, then g' = gh for some h ∈ H, and if g ∈ gH ∩ g'H, then g = gh = g'h' for some h, h' ∈ H, which implies gH = Hg = g'H.
  - Every coset of H has the same number of elements as H, since the map h ↦ gh is a bijection from H to gH for any g ∈ G.
  - The cosets of H partition G, since they are mutually disjoint and their union is G.
- Therefore, the number of cosets of H in G is equal to the index of H in G, and the number of elements in each coset is equal to the order of H. Hence, the order of G is equal to the product of the index and the order of H, which proves Lagrange's theorem.
- Lagrange's theorem has some important corollaries, such as:
  - The order of any element of a finite group divides the order of the group, since the order of an element is the same as the order of the cyclic subgroup generated by that element.
  - A group of prime order is cyclic and simple, since the only subgroups are the trivial subgroup and the whole group, and any non-identity element generates the whole group.
  - If G is a finite group and H and K are subgroups of G, then |HK| = |H||K|/|H ∩ K|, where HK is the set of all products hk, where h ∈ H and k ∈ K. This follows from applying Lagrange's theorem to the subgroup H ∩ K and its cosets in H and K.



### Normal Subgroups

- A normal subgroup H of a group G is a subgroup of G that is invariant under conjugation by members of the group. In other words, for every element g in G and every element h in H, we have g h g^-1 in H. The usual notation for this relation is H ≤ N G.
- Equivalently, a normal subgroup H of a group G is a subgroup of G such that every left coset and right coset corresponding to an element g are the same, that is, g H = H g.
- Normal subgroups are important because they allow us to define quotient groups, which are groups obtained by dividing a group by a normal subgroup. Quotient groups are useful for studying the structure and properties of groups.
- Some properties of normal subgroups are:

  - The trivial subgroup {e} and the whole group G are always normal subgroups of G.
  - The intersection of any collection of normal subgroups of G is a normal subgroup of G.
  - The product of any collection of normal subgroups of G is a normal subgroup of G, if the product is well-defined.
  - If H and K are normal subgroups of G, then H ∪ K is a normal subgroup of G if and only if H ⊆ K or K ⊆ H.
  - If H is a normal subgroup of G and K is a subgroup of G, then H ∩ K is a normal subgroup of K and K/H is a normal subgroup of G/H, where G/H is the quotient group of G by H.
  - If H is a normal subgroup of G and K is a normal subgroup of H, then K is a normal subgroup of G.
  - If H is a normal subgroup of G and g is an element of G, then g H g^-1 is a normal subgroup of G that is isomorphic to H.
  - If H is a subgroup of G and [G : H] = 2, that is, H has only two distinct left or right cosets in G, then H is a normal subgroup of G.
  - Every subgroup of an abelian group is normal.
  - Every subgroup of a cyclic group is normal.
  - A group that has no normal subgroups other than the trivial ones is called a simple group.



### Permutation and Symmetric Groups

- A **permutation** of a set is a bijection (one-to-one and onto function) from the set to itself. It is a way of rearranging the elements of the set in a different order.
- A **permutation group** on a set is a subset of the set of all permutations of the set that forms a group under the operation of function composition. It is a group of permutations that preserves some structure or property of the set.
- A **symmetric group** on a set is the set of all permutations of the set. It is the largest possible permutation group on the set. It is denoted by Sym(X) or S<sub>n</sub> if X = {1, 2, ..., n}.
- Every permutation group is a subgroup of a symmetric group, but not every subgroup of a symmetric group is a permutation group. For example, the group of rotations of a square is a permutation group on the set of vertices, but it is not a symmetric group because it does not contain all possible permutations of the vertices.
- The order of a permutation group is the number of permutations in the group. The order of a symmetric group is n!, where n is the size of the set. For example, the order of S<sub>4</sub> is 4! = 24.
- A permutation can be represented by a **cycle notation**, which lists the elements that are moved by the permutation in a circular order. For example, the permutation (1 2 3) means that 1 is mapped to 2, 2 is mapped to 3, and 3 is mapped to 1. The permutation (1 2)(3 4) means that 1 is mapped to 2, 2 is mapped to 1, 3 is mapped to 4, and 4 is mapped to 3. The permutation (1) means that 1 is mapped to itself, and it is called the **identity permutation**. It is denoted by e or id.
- A permutation can also be represented by a **two-row notation**, which lists the elements of the set in the first row and their images in the second row. For example, the permutation (1 2 3) can be written as

|1|2|3|
|-|-|-|
|2|3|1|

- The **inverse** of a permutation is the permutation that undoes its effect. It can be obtained by reversing the order of the cycles or swapping the rows of the two-row notation. For example, the inverse of (1 2 3) is (3 2 1) or

|1|2|3|
|-|-|-|
|3|1|2|

- The **composition** of two permutations is the permutation that results from applying the first permutation and then the second permutation. It can be obtained by multiplying the cycles from right to left or by applying the two-row notation from bottom to top. For example, the composition of (1 2 3) and (2 3 4) is (1 4 2 3) or

|1|2|3|4|
|-|-|-|-|
|2|3|4|1|
|4|1|2|3|

- The **order** of a permutation is the smallest positive integer k such that the permutation raised to the k-th power is the identity permutation. It can be obtained by finding the least common multiple of the lengths of the cycles. For example, the order of (1 2 3) is 3, and the order of (1 2)(3 4) is 2.
- A permutation is called **even** if it can be written as a product of an even number of transpositions (cycles of length 2), and **odd** if it can be written as a product of an odd number of transpositions. For example, (1 2 3) is even because it can be written as (1 2)(2 3), and (1 2)(3 4) is odd because it can be written as (1 2)(3 4). The **sign** of a permutation is +1 if it is even and -1 if it is odd. It is denoted by sgn(σ) or ε(σ).
- A **subgroup** of a group is a subset of the group that is also a group under the same operation. A subgroup is called **proper** if it is not equal to the whole group



### Group Homomorphisms

- A group homomorphism is a map between two groups that preserves the algebraic structure of both groups .
- Formally, a map $\phi: G \to H$ between two groups $(G, \cdot)$ and $(H, \circ)$ is called a group homomorphism if $\phi(g_1 \cdot g_2) = \phi(g_1) \circ \phi(g_2)$ for all $g_1, g_2 \in G$ .
- The range of $\phi$ in $H$ is called the homomorphic image of $\phi$.
- A group homomorphism that is both injective (one-to-one) and surjective (onto) is called an isomorphism of groups .
- A group homomorphism that is injective but not necessarily surjective is called a monomorphism.
- A group homomorphism that is surjective but not necessarily injective is called an epimorphism.
- A group homomorphism that is neither injective nor surjective is called an endomorphism.
- A group homomorphism from a group to itself is called an automorphism.

- Some examples of group homomorphisms are:

  - The map $f: \mathbb{Z} \to \{1, -1, i, -i\}$ defined by $f(n) = i^n$ for all $n \in \mathbb{Z}$, where $\mathbb{Z}$ is the group of integers under addition and $\{1, -1, i, -i\}$ is the group of complex numbers of unit modulus under multiplication.
  - The map $g: \mathbb{R} \to \mathbb{R}^+$ defined by $g(x) = e^x$ for all $x \in \mathbb{R}$, where $\mathbb{R}$ is the group of real numbers under addition and $\mathbb{R}^+$ is the group of positive real numbers under multiplication.
  - The map $h: S_n \to \mathbb{Z}_2$ defined by $h(\sigma) = 0$ if $\sigma$ is an even permutation and $h(\sigma) = 1$ if $\sigma$ is an odd permutation, where $S_n$ is the group of permutations of $n$ elements and $\mathbb{Z}_2$ is the group of integers modulo 2 under addition.



### Definition and elementary properties of Rings and Fields

- A **ring** is a set R with two binary operations, usually called **addition** and **multiplication**, that satisfy the following properties   :

  - (R,+) is an **abelian group**, meaning that:
    - **Closure**: For all a,b in R, a+b is also in R.
    - **Associativity**: For all a,b,c in R, (a+b)+c = a+(b+c).
    - **Commutativity**: For all a,b in R, a+b = b+a.
    - **Identity**: There exists an element 0 in R such that for all a in R, a+0 = a.
    - **Inverse**: For every a in R, there exists an element -a in R such that a+(-a) = 0.
  - (R,.) is a **semigroup**, meaning that:
    - **Closure**: For all a,b in R, a.b is also in R.
    - **Associativity**: For all a,b,c in R, (a.b).c = a.(b.c).
  - **Distributivity**: For all a,b,c in R, a.(b+c) = (a.b)+(a.c) and (a+b).c = (a.c)+(b.c).

- A ring is called **commutative** if its multiplication is also commutative, that is, for all a,b in R, a.b = b.a   .

- A ring is called **unital** or **unitary** if it has a **multiplicative identity**, that is, there exists an element 1 in R such that for all a in R, a.1 = 1.a = a   .

- A ring is called an **integral domain** if it is commutative, unital, and has no **zero divisors**, that is, for all a,b in R, if a.b = 0, then either a = 0 or b = 0   .

- A **field** is a ring that is commutative, unital, and has **multiplicative inverses**, that is, for every nonzero a in R, there exists an element a^-1 in R such that a.a^-1 = a^-1.a = 1   .

- Examples of rings are the integers Z, the rational numbers Q, the real numbers R, the complex numbers C, the polynomials R[x], and the matrices M_n(R) with n rows and columns and entries from R   .

- Examples of fields are the rational numbers Q, the real numbers R, the complex numbers C, and the finite fields F_p with p elements, where p is a prime number   .

- Some elementary properties of rings and fields are:

  - In any ring, 0.a = a.0 = 0 for all a in R   .
  - In any ring, (-a).b = a.(-b) = -(a.b) for all a,b in R   .
  - In any ring, (-a).(-b) = a.b for all a,b in R   .
  - In any ring, if 1 exists, then 1 = -1 if and only if R has exactly two elements   .
  - In any ring, if a.b = a.c and a is not a zero divisor, then b = c for all a,b,c in R   .
  - In any field, every nonzero element is a unit, and every unit is nonzero [



## Unit 3 - Lattices

- A lattice is a set of points in a space that are arranged in a regular and periodic pattern.
- A lattice can be described by a set of basis vectors that define the unit cell, which is the smallest repeating unit of the lattice.
- A lattice can also be characterized by its symmetry properties, such as the point group, the space group, and the Bravais lattice type.
- There are 14 possible Bravais lattice types in three dimensions, which are classified by the shape and size of the unit cell and the relative positions of the lattice points.
- The Bravais lattice types are: cubic (simple, body-centered, and face-centered), tetragonal (simple and body-centered), orthorhombic (simple, body-centered, base-centered, and face-centered), monoclinic (simple and base-centered), triclinic (simple), hexagonal (simple), and rhombohedral (simple).
- A crystal structure is a specific arrangement of atoms or molecules in a lattice. A crystal structure can be described by the lattice type, the basis (the type and number of atoms or molecules in the unit cell), and the lattice parameters (the lengths and angles of the unit cell edges).
- A crystal structure can also be represented by a crystallographic notation, such as the Hermann-Mauguin notation, the Schoenflies notation, or the Pearson symbol, which encode the symmetry and lattice information in a concise form.
- A crystal structure can be visualized by using a unit cell diagram, a projection diagram, or a stereographic projection, which show the relative positions of the atoms or molecules in the lattice.



### Definition for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** and a **least upper bound**.
- A **greatest lower bound** of a pair of elements x and y in a poset is an element z such that z ≤ x and z ≤ y, and there is no other element w that satisfies w ≤ x, w ≤ y and w > z.
- A **least upper bound** of a pair of elements x and y in a poset is an element z such that x ≤ z and y ≤ z, and there is no other element w that satisfies x ≤ w, y ≤ w and w < z.
- The greatest lower bound of x and y is also called the **meet** of x and y, and denoted by x ∧ y.
- The least upper bound of x and y is also called the **join** of x and y, and denoted by x ∨ y.
- A lattice can be represented by a **Hasse diagram**, which is a graphical representation of the partial order relation.
- A lattice is an **algebraic system** with two binary operations, ∨ and ∧, that satisfy certain properties.
- A lattice is denoted by [L; ∨, ∧], where L is the set of elements and ∨ and ∧ are the join and meet operations respectively.
- Some examples of lattices are the set of natural numbers with the divisibility relation and the join and meet operations defined as the least common multiple and the greatest common divisor respectively, and the set of subsets of a given set with the inclusion relation and the join and meet operations defined as the union and intersection respectively.



### Properties of lattices – Bounded

- A lattice is a partially ordered set (poset) in which every pair of elements has a least upper bound (lub) and a greatest lower bound (glb).
- A bounded lattice is a lattice that has a greatest element and a least element, denoted by 1 and 0 respectively.
- The greatest element 1 is also called the maximum, or the top element, of the lattice. It satisfies 1 ∨ a = 1 and 1 ∧ a = a for any element a in the lattice.
- The least element 0 is also called the minimum, or the bottom element, of the lattice. It satisfies 0 ∨ a = a and 0 ∧ a = 0 for any element a in the lattice.
- Every finite lattice is bounded, since the lub and glb of all the elements in the lattice are the greatest and least elements respectively.
- An example of a bounded lattice is the power set of a finite set, ordered by inclusion. The greatest element is the whole set, and the least element is the empty set.



### Complemented for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **bounded lattice** is a lattice that has a minimum element (denoted by 0) and a maximum element (denoted by 1).
- A **complemented lattice** is a bounded lattice in which every element has a **complement**, that is, an element such that their lub is 1 and their glb is 0.
- A **distributive lattice** is a lattice that satisfies the **distributive laws**, that is, for any elements x, y, and z in the lattice, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ and ∨ denote the glb and lub operations, respectively.
- A **Boolean algebra** is a complemented distributive lattice. It is also equivalent to a set of subsets of a given set, closed under the operations of union, intersection, and complement, with respect to the whole set.
- A **sublattice** of a lattice is a subset of the lattice that is also a lattice under the same glb and lub operations.
- A **homomorphism** between two lattices is a function that preserves the glb and lub operations, that is, for any elements x and y in the source lattice, f(x ∧ y) = f(x) ∧ f(y) and f(x ∨ y) = f(x) ∨ f(y) in the target lattice.
- An **isomorphism** between two lattices is a bijective homomorphism that has an inverse homomorphism. Two lattices are **isomorphic** if there exists an isomorphism between them.
- A **direct product** of two lattices is a lattice whose elements are ordered pairs of elements from the two lattices, and whose glb and lub operations are defined componentwise, that is, for any elements (x1, y1) and (x2, y2) in the direct product, (x1, y1) ∧ (x2, y2) = (x1 ∧ x2, y1 ∧ y2) and (x1, y1) ∨ (x2, y2) = (x1 ∨ x2, y1 ∨ y2).
- A **subdirect product** of two lattices is a sublattice of their direct product that projects onto both lattices, that is, for any elements x and y in the first lattice, there exists an element (x, z) in the subdirect product, and for any elements u and v in the second lattice, there exists an element (w, v) in the subdirect product.



### Modular and Complete Lattice

- A **lattice** is a partially ordered set (poset) in which every two elements have a unique least upper bound (called their **join** or **supremum**) and a unique greatest lower bound (called their **meet** or **infimum**).
- A lattice is **modular** if it satisfies the following self-dual condition: for any elements a, b, and x in the lattice, if a ≤ b, then a ∨ (b ∧ x) = (a ∨ b) ∧ x, where ∨ denotes the join operation and ∧ denotes the meet operation. This condition is also known as the **modular law**.
- A lattice is **complete** if it has a join and a meet for every subset of the lattice, not just for pairs of elements. Equivalently, a lattice is complete if it has a least element (called the **bottom** or **zero**) and a greatest element (called the **top** or **one**).
- Every finite lattice is complete, since the join and meet of any subset can be obtained by applying the join and meet operations repeatedly to the elements of the subset. However, not every infinite lattice is complete. For example, the lattice of natural numbers with the usual order is not complete, since it has no greatest element.
- Some examples of complete lattices are:

  - The lattice of all subsets of a given set, ordered by inclusion. The join of any collection of subsets is their union, and the meet of any collection of subsets is their intersection. The bottom element is the empty set, and the top element is the whole set.
  - The lattice of all partitions of a given set, ordered by refinement. The join of any collection of partitions is their coarsest common refinement, and the meet of any collection of partitions is their finest common coarsening. The bottom element is the partition that has only one block (the whole set), and the top element is the partition that has only singleton blocks (each element in a separate block).
  - The lattice of all natural numbers, ordered by divisibility. The join of any collection of natural numbers is their least common multiple, and the meet of any collection of natural numbers is their greatest common divisor. The bottom element is 1, and the top element is 0 (since every natural number divides 0).
  - The lattice of all real numbers, ordered by the usual order. The join of any collection of real numbers is their supremum, and the meet of any collection of real numbers is their infimum. The bottom element is -∞, and the top element is +∞.



### Boolean Algebra

- Boolean algebra is a branch of mathematics that deals with operations on logical values and incorporates binary variables .
- Boolean algebra traces its origins to an 1854 book by mathematician George Boole.
- The distinguishing factor of Boolean algebra is that it deals only with the study of binary variables, which can have only two possible values: 1 (true) or 0 (false) .
- The basic operations of Boolean algebra are the logical operations AND, OR and NOT, which are denoted by symbols ∧, ∨ and ¬ respectively .
- A Boolean expression is a combination of Boolean variables and operators that evaluates to a Boolean value.
- A Boolean function is a mapping from a set of Boolean variables to a Boolean value.
- A Boolean algebra is any set with binary operations ∧ and ∨ and a unary operation ¬ thereon satisfying the Boolean laws.
- The Boolean laws are a set of axioms and rules that govern the manipulation and simplification of Boolean expressions.
- Some of the common Boolean laws are:

  - Commutative laws: A ∧ B = B ∧ A and A ∨ B = B ∨ A
  - Associative laws: (A ∧ B) ∧ C = A ∧ (B ∧ C) and (A ∨ B) ∨ C = A ∨ (B ∨ C)
  - Distributive laws: A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C) and A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C)
  - Identity laws: A ∧ 1 = A and A ∨ 0 = A
  - Complement laws: A ∧ ¬A = 0 and A ∨ ¬A = 1
  - Idempotent laws: A ∧ A = A and A ∨ A = A
  - De Morgan's laws: ¬(A ∧ B) = ¬A ∨ ¬B and ¬(A ∨ B) = ¬A ∧ ¬B
  - Absorption laws: A ∧ (A ∨ B) = A and A ∨ (A ∧ B) = A
  - Involution law: ¬(¬A) = A

- Boolean algebra is widely used in digital logic, computer science, electrical engineering, cryptography, and other fields that involve binary data and logic .



### Introduction for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A lattice is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A lattice can be represented by a Hasse diagram, which is a graphical representation of the partial order relation.
- A lattice is said to be bounded if it has a minimum element (called zero or bottom) and a maximum element (called one or top).
- A lattice is said to be distributive if it satisfies the distributive laws: for any elements x, y, and z in the lattice, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ and ∨ denote the glb and lub operations, respectively.
- A lattice is said to be complemented if every element has a unique complement, that is, an element y such that x ∧ y = 0 and x ∨ y = 1, where 0 and 1 are the bottom and top elements of the lattice, respectively.
- A lattice is said to be Boolean if it is bounded, distributive, and complemented. A Boolean lattice can be seen as an algebraic structure that models the operations of Boolean logic.
- A sublattice of a lattice is a subset that is also a lattice with respect to the same partial order relation.
- A homomorphism of lattices is a function that preserves the glb and lub operations, that is, for any elements x and y in the domain lattice, f(x ∧ y) = f(x) ∧ f(y) and f(x ∨ y) = f(x) ∨ f(y) in the codomain lattice.
- An isomorphism of lattices is a bijective homomorphism that has an inverse homomorphism. Two lattices are said to be isomorphic if there exists an isomorphism between them.



### Axioms and Theorems of Boolean Algebra

- Boolean algebra is a branch of mathematics that deals with the manipulation of logical expressions and variables using the operations of AND, OR and NOT.
- A Boolean variable can have only two possible values: 0 (false) or 1 (true).
- A Boolean expression is a combination of Boolean variables and operations that evaluates to a Boolean value.
- A Boolean function is a rule that assigns a Boolean value to each possible combination of Boolean variables.
- A Boolean algebra is a set of Boolean values, variables, expressions and functions that satisfies a set of axioms or postulates that define the properties of the Boolean operations.
- The following are some of the basic axioms of Boolean algebra :

  - Commutative laws: A + B = B + A and A * B = B * A
  - Associative laws: (A + B) + C = A + (B + C) and (A * B) * C = A * (B * C)
  - Distributive laws: A * (B + C) = (A * B) + (A * C) and A + (B * C) = (A + B) * (A + C)
  - Identity laws: A + 0 = A and A * 1 = A
  - Complement laws: A + A' = 1 and A * A' = 0
  - Idempotent laws: A + A = A and A * A = A
  - Involution law: (A')' = A
  - Absorption laws: A + (A * B) = A and A * (A + B) = A
  - De Morgan's laws: (A + B)' = A' * B' and (A * B)' = A' + B'
  - Zero and one laws: A + 1 = 1 and A * 0 = 0

- The following are some of the derived theorems of Boolean algebra that can be proved using the axioms :

  - A + A * B = A + B
  - A * (A + B) = A
  - A + A' * B = A + B
  - A * (A' + B) = A * B
  - A + B * C = (A + B) * (A + C)
  - A * (B + C) = A * B + A * C
  - A' + B' = (A * B)'
  - A' * B' = (A + B)'
  - A + B = (A' * B')'
  - A * B = (A' + B')'
  - A' = (A + 1)'
  - A' = (A * 0)'
  - A + B = A + B * A'
  - A * B = A * B + A' * B
  - A + B = A + B + A * B
  - A * B = A * B * (A + B)



### Algebraic manipulation of Boolean expressions

- Boolean expressions are algebraic expressions that involve variables and operators that take only two values: true (1) or false (0).
- Boolean expressions can be used to represent logic circuits, truth tables, and sets.
- Boolean expressions can be manipulated into equivalent forms by applying the laws, rules, and theorems of Boolean algebra.
- Some of the common laws and rules of Boolean algebra are:

  - Commutative laws: A + B = B + A and A * B = B * A
  - Associative laws: (A + B) + C = A + (B + C) and (A * B) * C = A * (B * C)
  - Distributive laws: A * (B + C) = A * B + A * C and A + (B * C) = (A + B) * (A + C)
  - Identity laws: A + 0 = A and A * 1 = A
  - Complement laws: A + A' = 1 and A * A' = 0
  - Idempotent laws: A + A = A and A * A = A
  - De Morgan's laws: (A + B)' = A' * B' and (A * B)' = A' + B'
  - Absorption laws: A + A * B = A and A * (A + B) = A
  - Involution law: (A')' = A

- Some of the common theorems of Boolean algebra are:

  - Consensus theorem: A * B + A' * C + B * C = A * B + A' * C
  - Redundancy theorem: A + A * B = A
  - Simplification theorem: A * (A + B) = A
  - Adjacency theorem: A * B + A * B' = A

- Algebraic manipulation of Boolean expressions can be used to:

  - Convert a given expression to a canonical form (a standardized form) such as sum-of-products (SOP) or product-of-sums (POS).
  - Minimize the number of literals (primed or unprimed variables) or terms in an expression to reduce the complexity of the logic circuit.
  - Verify the equivalence of two expressions by showing that they have the same truth table or by simplifying them to the same expression.



### Simplification of Boolean Functions

- A boolean function is a function that takes one or more boolean variables as inputs and produces a single boolean output.
- The output of a boolean function depends on the logical operations performed on the inputs, such as AND, OR, NOT, XOR, etc.
- The algebraic expression of a boolean function can be represented using boolean variables, constants (0 or 1), and operators (+, ., ', etc.).
- The process of simplifying the algebraic expression of a boolean function is called minimization or simplification.
- Minimization is important since it reduces the cost and complexity of the associated circuit. For example, the function F = A.B + A.B + B.C can be minimized to F = A + B.C.
- There are different methods for minimizing boolean functions, such as using boolean identities, Karnaugh maps, Quine-McCluskey method, etc.
- Boolean identities are theorems or rules that can be used to manipulate and simplify boolean expressions. For example, A + A = A, A + 1 = 1, A.B + A.B' = A, etc.
- Karnaugh maps are graphical tools that can be used to simplify boolean functions with up to four variables. They are based on the principle of adjacency, which states that two minterms (terms with only one variable complemented) differ by only one variable can be combined to form a simpler term.
- Quine-McCluskey method is a tabular method that can be used to simplify boolean functions with any number of variables. It is based on the principle of prime implicants, which are the simplest terms that can cover one or more minterms of the function.



### Karnaugh maps

- A Karnaugh map (K-map) is a method of simplifying Boolean algebra expressions .
- It is a visual method that uses a grid of cells to represent all the possible combinations of input variables and their corresponding output values .
- It helps to determine the minimum expressions in the form of sum-of-products (SOP) or product-of-sums (POS), which can be implemented using a minimum number of logic gates .
- It also helps to detect and eliminate race conditions, which are situations where the output of a logic circuit depends on the order or timing of the input changes.

#### Rules for K-maps

- Select a K-map according to the number of input variables. For example, a two-variable K-map has four cells, a three-variable K-map has eight cells, and a four-variable K-map has 16 cells.
- Label the rows and columns of the K-map with the input variables and their complements in Gray code order, which means only one bit changes between adjacent cells.
- Fill the cells of the K-map with the output values (0 or 1) according to the given Boolean expression or truth table.
- Group the adjacent cells that have the same output value (1 for SOP or 0 for POS) into regions of size 1, 2, 4, 8, or 16. The regions can wrap around the edges of the K-map and overlap with each other.
- Write the simplified Boolean expression for each region by taking the common factors of the input variables. For SOP, use OR to combine the regions, and for POS, use AND to combine the regions.

#### Example Problems

- Simplify the following Boolean expression using a K-map and write the SOP form:

  F(A, B, C) = ∑(0, 1, 2, 5, 6, 7)

  Solution:

  - Draw a three-variable K-map and label the rows and columns with A, B, and C and their complements.
  - Fill the cells with 1 for the minterms (0, 1, 2, 5, 6, 7) and 0 for the rest.
  - Group the adjacent cells with 1 into regions of size 4, 2, and 2.
  - Write the simplified Boolean expression for each region and OR them together.

  K-map example 1

  F(A, B, C) = A'C + BC + AB'C'

- Simplify the following Boolean expression using a K-map and write the POS form:

  F(A, B, C, D) = ∏(0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13)

  Solution:

  - Draw a four-variable K-map and label the rows and columns with A, B, C, and D and their complements.
  - Fill the cells with 0 for the maxterms (0, 1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13) and 1 for the rest.
  - Group the adjacent cells with 0 into regions of size 4, 4, and 4.
  - Write the simplified Boolean expression for each region and AND them together.

  K-map example 2

  F(A, B, C, D) = (A + B + C + D)(A + B + C' + D')(A + B' + C + D')



### Logic gates for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- Logic gates are the basic building blocks from which most of the digital systems are built up.
- Logic gates perform logical operations on one or more binary inputs and produce a single binary output.
- The numbers 0 and 1 represent the two possible states of a logic circuit. The two states can also be referred to as 'ON and OFF' or 'HIGH and LOW' or 'TRUE and FALSE'.
- The basic logic gates are 'OR', 'AND' and 'NOT' gates. These three gates can be used to implement any other logic function.
- The OR gate produces a 1 output if at least one of its inputs is 1, otherwise it produces a 0 output.
- The AND gate produces a 1 output if both of its inputs are 1, otherwise it produces a 0 output.
- The NOT gate produces a 1 output if its input is 0, and a 0 output if its input is 1. It is also called an inverter.
- The truth table of a logic gate shows all the possible combinations of inputs and outputs for that gate.
- The symbol and truth table for each basic logic gate are shown below:

| OR gate | AND gate | NOT gate |
|:-------:|:--------:|:--------:|
| OR gate symbol | AND gate symbol | NOT gate symbol |
| | A | B | A OR B |
| | 0 | 0 | 0 |
| | 0 | 1 | 1 |
| | 1 | 0 | 1 |
| | 1 | 1 | 1 | | | A | B | A AND B |
| | 0 | 0 | 0 |
| | 0 | 1 | 0 |
| | 1 | 0 | 0 |
| | 1 | 1 | 1 | | | A | NOT A |
| | 0 | 1 |
| | 1 | 0 |

- Other logic gates that can be derived from the basic ones are 'NOR', 'NAND', 'XOR' and 'XNOR' gates.
- The NOR gate produces a 1 output if both of its inputs are 0, otherwise it produces a 0 output. It is equivalent to an OR gate followed by a NOT gate.
- The NAND gate produces a 0 output if both of its inputs are 1, otherwise it produces a 1 output. It is equivalent to an AND gate followed by a NOT gate.
- The XOR gate produces a 1 output if exactly one of its inputs is 1, otherwise it produces a 0 output. It is also called an exclusive OR gate.
- The XNOR gate produces a 0 output if exactly one of its inputs is 1, otherwise it produces a 1 output. It is also called an exclusive NOR gate.
- The symbol and truth table for each derived logic gate are shown below:

| NOR gate | NAND gate | XOR gate | XNOR gate |
|:--------:|:---------:|:--------:|:---------:|
| NOR gate symbol | NAND gate symbol | XOR gate symbol | XNOR gate symbol |
| | A | B | A NOR B |
| | 0 | 0 | 1 |
| | 0 | 1 | 0 |
| | 1 | 0 | 0 |
| | 1 | 1 | 0 | | | A | B | A NAND B |
| |



### Digital Circuits and Boolean Algebra

- A digital circuit is a system that processes binary information, which is represented by two voltage levels: high (1) and low (0).
- A logic gate is a basic building block of a digital circuit that performs a logical operation on one or more binary inputs and produces a single binary output.
- There are three basic logic gates: AND, OR, and NOT. Each gate has a symbol, a truth table, and a Boolean expression that describes its behavior.
- AND gate: outputs 1 only if both inputs are 1.
- OR gate: outputs 1 if either or both inputs are 1.
- NOT gate: outputs the opposite of the input.
- Other logic gates, such as NAND, NOR, XOR, and XNOR, can be derived from the basic gates by combining them in various ways.
- Boolean algebra is a branch of mathematics that deals with binary variables and logical operations. It was developed by George Boole in the 19th century and later refined by other mathematicians and engineers.
- Boolean algebra is helpful to analyze and simplify digital logic circuits. It allows computers to perform from simple to very complex operations.
- A Boolean variable is a symbol that can take only two values: 0 or 1. A Boolean expression is a combination of Boolean variables and operators that evaluates to a Boolean value.
- The main Boolean operators are AND (∙), OR (+), and NOT (¬). They follow certain rules and laws, such as commutativity, associativity, distributivity, identity, complement, and De Morgan's laws.
- A Boolean function is a mapping from a set of Boolean variables to a Boolean value. A Boolean function can be represented in different ways, such as a truth table, a Boolean expression, or a logic diagram.
- A truth table shows all possible combinations of input values and the corresponding output value for a Boolean function.
- A Boolean expression is an algebraic notation that uses Boolean operators and parentheses to specify the logic of a Boolean function.
- A logic diagram is a graphical representation that uses logic gate symbols and wires to show the logic of a Boolean function.
- A logic circuit is a physical implementation of a logic diagram using electronic components, such as transistors, resistors, and diodes.
- A logic circuit can be analyzed and simplified using Boolean algebra techniques, such as algebraic manipulation, Karnaugh maps, and Quine-McCluskey method.



## Unit 4 - Propositional Logic

- Propositional logic is a branch of logic that deals with propositions, which are statements that can be either true or false.
- A proposition is represented by a propositional variable, such as p, q, r, etc., or by a propositional constant, such as T (true) or F (false).
- Propositional logic uses logical connectives, such as ∧ (and), ∨ (or), ¬ (not), → (implies), and ↔ (if and only if), to form complex propositions from simpler ones.
- The truth value of a complex proposition depends on the truth values of its components and the logical connectives used.
- A truth table is a tabular representation of all possible combinations of truth values for a given set of propositions and their logical connectives.
- A tautology is a proposition that is always true, regardless of the truth values of its components. For example, p ∨ ¬p is a tautology.
- A contradiction is a proposition that is always false, regardless of the truth values of its components. For example, p ∧ ¬p is a contradiction.
- A contingency is a proposition that is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its components. For example, p ∧ q is a contingency.
- Logical equivalence is a relation between two propositions that have the same truth value in every possible situation. For example, p → q is logically equivalent to ¬p ∨ q, and p ↔ q is logically equivalent to (p → q) ∧ (q → p).
- Logical implication is a relation between two propositions that means that whenever the first proposition is true, the second proposition must also be true. For example, p → q implies that if p is true, then q is true.
- A logical argument is a sequence of propositions that ends with a conclusion, which is a proposition that is supposed to follow from the previous propositions, called premises. For example, p → q, p ∴ q is a logical argument with two premises and one conclusion.
- The validity of a logical argument is determined by whether the conclusion must be true whenever all the premises are true. For example, p → q, p ∴ q is a valid argument, but p → q, q ∴ p is not.
- A logical fallacy is a common error in reasoning that makes an argument invalid. For example, affirming the consequent is a logical fallacy that has the form p → q, q ∴ p, which is invalid.
- Some other common logical fallacies are denying the antecedent, which has the form p → q, ¬p ∴ ¬q, and circular reasoning, which has the form p ∴ p.



### Proposition for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Propositional logic is a branch of logic that studies the ways of combining and modifying statements, called propositions, using logical connectives and operators.
- A proposition is a declarative sentence that is either true or false, but not both. For example, "Sydney is an AI assistant" is a proposition, but "What is your name?" is not.
- The truth value of a proposition is the logical value assigned to it, either true (T) or false (F). The truth value of a proposition may depend on the context or the state of affairs in the world.
- A propositional variable is a symbol that can represent any proposition. Usually, propositional variables are denoted by lowercase letters such as p, q, r, etc.
- A propositional formula is a string of symbols that consists of propositional variables, logical connectives, and parentheses. For example, (p ∧ q) → r is a propositional formula.
- A logical connective is a symbol that is used to form new propositions from existing ones. The most common logical connectives are:
  - Negation (¬): It reverses the truth value of a proposition. For example, if p is true, then ¬p is false, and vice versa.
  - Conjunction (∧): It joins two propositions and is true only if both of them are true. For example, p ∧ q is true only if both p and q are true.
  - Disjunction (∨): It joins two propositions and is true if at least one of them is true. For example, p ∨ q is true if either p or q is true, or both.
  - Conditional (→): It expresses a logical implication between two propositions. For example, p → q means "if p, then q". It is false only if p is true and q is false, otherwise it is true.
  - Biconditional (↔): It expresses a logical equivalence between two propositions. For example, p ↔ q means "p if and only if q". It is true only if p and q have the same truth value, otherwise it is false.
- A truth table is a tabular representation of the truth values of a propositional formula for all possible combinations of truth values of its propositional variables. For example, the truth table for p → q is:

| p | q | p → q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | T     |
| F | F | T     |

- A tautology is a propositional formula that is always true, regardless of the truth values of its propositional variables. For example, p ∨ ¬p is a tautology.
- A contradiction is a propositional formula that is always false, regardless of the truth values of its propositional variables. For example, p ∧ ¬p is a contradiction.
- A contingency is a propositional formula that is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its propositional variables. For example, p ∧ q is a contingency.
- Logical equivalence is a relation between two propositional formulas that have the same truth value for every possible assignment of truth values to their propositional variables. For example, p → q and ¬p ∨ q are logically equivalent, denoted by p → q ≡ ¬p ∨ q.
- Logical implication is a relation between two propositional formulas that means that whenever the first formula is true, the second formula is also true. For example, p → q implies ¬p ∨ q, denoted by p → q ⇒ ¬p ∨ q.
- A logical argument is a sequence of propositions that are intended to establish the truth of a conclusion from a set of premises. For example, the following is a logical argument:

  - Premise 1: If it rains, then the grass is wet.
  - Premise 2: It rains.
  - Conclusion: The grass is wet.

- A valid argument is a logical argument that has the property that if all the premises are true, then the conclusion must also be true. For example, the above argument is valid, because the conclusion follows logically from the premises.
- A sound argument is a valid argument that has the additional property that all the premises are actually true. For example, the above argument is sound, assuming that the premises are true in the real world.
- A fallacy is a common error in reasoning that makes an argument invalid or unsound. For example, the following is a fallacious



### Well formed formula

- A well formed formula (WFF) is a finite sequence of symbols from a given alphabet that is grammatically correct according to some rules of syntax.
- The alphabet of propositional logic consists of propositional variables, logical connectives, and parentheses.
- The propositional variables are symbols that represent propositions, such as p, q, r, etc.
- The logical connectives are symbols that represent logical operations, such as negation (~), conjunction (∧), disjunction (∨), implication (→), and equivalence (↔).
- The parentheses are symbols that group symbols together and indicate the order of evaluation, such as ( and ).
- The rules of syntax for WFFs are as follows:
  - Any propositional variable is a WFF.
  - If α is a WFF, then (~α) is a WFF.
  - If α and β are WFFs, then (α ∧ β), (α ∨ β), (α → β), and (α ↔ β) are WFFs.
  - Nothing else is a WFF.
- Examples of WFFs are:
  - p
  - (~q)
  - (p ∧ q)
  - ((p ∨ q) → r)
  - ((p ↔ q) ↔ (~r))
- Examples of non-WFFs are:
  - p ∧
  - (p q)
  - (p →) q
  - p ↔ (~q
  - p ∨ q ∧ r



### Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A truth table is a mathematical table used in logic that shows the truth values of logical expressions for each possible combination of values of their variables.
- A truth table can be used to solve various problems in propositional logic, such as showing the semantics of logical operators, proving equivalences, solving satisfiability problems, etc.
- A truth table has one column for each variable and one column for the logical expression. The rows of the table correspond to all possible assignments of truth values to the variables. The truth value of the expression for each row is calculated using the rules of propositional logic.
- The following table shows the basic logical operators and their truth tables:

| Operator | Symbol | Example | Truth table |
| --- | --- | --- | --- |
| Negation | ¬ | ¬p | p ¬p<br>T F<br>F T |
| Conjunction | ∧ | p ∧ q | p q p ∧ q<br>T T T<br>T F F<br>F T F<br>F F F |
| Disjunction | ∨ | p ∨ q | p q p ∨ q<br>T T T<br>T F T<br>F T T<br>F F F |
| Implication | → | p → q | p q p → q<br>T T T<br>T F F<br>F T T<br>F F T |
| Biconditional | ↔ | p ↔ q | p q p ↔ q<br>T T T<br>T F F<br>F T F<br>F F T |

- The following table shows some common logical equivalences and their truth tables:

| Equivalence | Symbol | Example | Truth table |
| --- | --- | --- | --- |
| Commutativity | ≡ | p ∧ q ≡ q ∧ p | p q p ∧ q q ∧ p<br>T T T T<br>T F F F<br>F T F F<br>F F F F |
| Associativity | ≡ | (p ∧ q) ∧ r ≡ p ∧ (q ∧ r) | p q r (p ∧ q) ∧ r p ∧ (q ∧ r)<br>T T T T T<br>T T F F F<br>T F T F F<br>T F F F F<br>F T T F F<br>F T F F F<br>F F T F F<br>F F F F F |
| Distributivity | ≡ | p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) | p q r p ∧ (q ∨ r) (p ∧ q) ∨ (p ∧ r)<br>T T T T T<br>T T F T T<br>T F T T T<br>T F F F F<br>F T T F F<br>F T F F F<br>F F T F F<br>F F F F F |
| De Morgan's laws | ≡ | ¬(p ∧ q) ≡ ¬p ∨ ¬q | p q ¬(p ∧ q) ¬p ¬q ¬p ∨ ¬q<br>T T F F F F<br>T F T F T T<br>F T T T F T<br>F F T T T T |
| Identity laws | ≡ | p ∧ T ≡ p | p p ∧ T<br>T T<br>F F |
| Domination laws | ≡ | p ∨ T ≡ T | p p ∨ T<br>T T<br>F T |
| Double negation | ≡ | ¬¬p ≡ p | p ¬¬p<br>T T<br>F F |
| Contrapositive | ≡ | p → q ≡ ¬q → ¬p | p q p → q ¬q ¬p ¬q → ¬p<br>T T T F F T<br>T F F T F F<br>F T T F T T<br>F F T T T T |

: Truth table - Wikipedia
: Truth Tables - Propositional Logic | CodeGuage
: Propositional Logic Truth Table - Boolean Algebra - DYclassroom



### Tautology for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A tautology is a propositional formula that is true under any possible Boolean valuation of its propositional variables.
- A tautology is also called a logically valid formula, since it is always satisfied by any assignment of truth values to its variables.
- A tautology can be recognized by using a truth table, which shows all the possible combinations of truth values for the variables and the resulting truth value of the formula.
- A tautology can also be proved by using logical equivalences, which are rules that allow us to replace one propositional formula with another that has the same truth value.
- Some examples of tautologies are:

  - p ∨ ¬p (the law of excluded middle)
  - p → p (the law of identity)
  - (p → q) ∨ (q → p) (the law of material implication)
  - (p ∧ q) → p (the law of simplification)
  - (p ∧ (p ∨ q)) ↔ p (the law of idempotency of conjunction)

- A tautology can be used to show that an argument is valid, by showing that the conjunction of the premises and the negation of the conclusion is a contradiction, which is a propositional formula that is false under any possible Boolean valuation of its propositional variables.
- A tautology can also be used to simplify a complex propositional formula, by eliminating redundant terms or applying logical equivalences.



### Satisfiability for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Satisfiability is a semantic property of a propositional formula or a set of propositional formulas that indicates whether there exists a truth assignment that makes the formula or the set of formulas true .
- A propositional formula is satisfiable if there is a 1-assignment for it; a set of propositional formulas is satisfiable if there is a simultaneous 1-assignment for its elements.
- A propositional formula is unsatisfiable if there is no truth assignment that makes it true; a set of propositional formulas is unsatisfiable if there is no simultaneous truth assignment for its elements .
- A propositional formula is valid if it is true under every truth assignment; a set of propositional formulas is valid if every truth assignment makes all its elements true .
- The propositional satisfiability problem (SAT) is the problem of determining whether a given propositional formula or a set of propositional formulas is satisfiable .
- SAT is a fundamental problem in logic and computer science, as many other problems can be reduced to it, such as theorem proving, model checking, circuit design, and cryptography  .
- SAT is also a computationally hard problem, as it belongs to the class of NP-complete problems, which means that there is no known efficient algorithm that can solve it in polynomial time  .
- There are various methods and techniques to solve SAT, such as truth tables, resolution, DPLL algorithm, CDCL algorithm, and heuristic search .
- There are also various extensions and variations of SAT, such as 3-SAT, k-SAT, MAX-SAT, QSAT, and SAT modulo theories, which capture different aspects and applications of satisfiability  .



### Contradiction for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A contradiction is an assertion of propositional logic that is false in all situations; that is, it is false for all possible values of its variables .
- A contradiction can be written as a compound proposition that is logically equivalent to F (the false constant).
- A contradiction can also be written as the negation of a tautology, which is a proposition that is true in all situations.
- Examples of contradictions are:
  - A ∧ ¬A (A and not A)
  - A ∨ B ∧ ¬(A ∨ B) (A or B and not (A or B))
  - p → q ∧ p ∧ ¬q (if p then q and p and not q)
- Contradictions can be used as a tool to detect disingenuous beliefs and bias.
- Contradictions can also be used to prove propositions by contradiction, which is a form of proof that establishes the truth or the validity of a proposition, by showing that assuming the proposition to be false leads to a contradiction.
- Contraposition is a form of immediate inference in which a proposition is inferred from another and where the former has for its subject the contradictory of the original proposition's predicate.
- Example of contraposition is:
  - If p then q is equivalent to if not q then not p



### Algebra of proposition

- Algebra of proposition is the subbranch of mathematical logic that studies propositions and logical operators.
- Propositions are statements that can be either true or false, such as "It is raining" or "2 + 2 = 4".
- Logical operators are symbols that define new propositions from one or more given propositions, such as "and", "or", "not", "if...then", "if and only if".
- The most common symbols for logical operators are:

| Symbol | Name | Meaning |
| --- | --- | --- |
| $\land$ | Conjunction | And |
| $\lor$ | Disjunction | Or |
| $\lnot$ | Negation | Not |
| $\rightarrow$ | Implication | If...then |
| $\leftrightarrow$ | Equivalence | If and only if |

- The most common symbols for propositions are $p$, $q$, $r$, etc. They are called logical variables because any proposition can take their place.
- The truth value of a proposition is either true (T) or false (F). The truth value of a compound proposition (one that involves logical operators) depends on the truth values of the component propositions and the rules of the logical operators.
- A truth table is a table that shows the truth value of a compound proposition for all possible combinations of truth values of the component propositions. For example, the truth table for $p \land q$ is:

| $p$ | $q$ | $p \land q$ |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

- Two propositions are said to be equivalent if they have the same truth value for all possible truth values of their component propositions. For example, $p \rightarrow q$ is equivalent to $\lnot p \lor q$.
- An algebraic identity is a statement that expresses the equivalence of two propositions. For example, one of the algebraic identities for conjunction is:

$$p \land q \equiv q \land p$$

- This means that the order of the propositions does not matter when using the "and" operator. There are many other algebraic identities for different logical operators, such as:

$$p \lor q \equiv q \lor p$$
$$p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$$
$$\lnot (p \land q) \equiv \lnot p \lor \lnot q$$
$$p \rightarrow q \equiv \lnot p \lor q$$
$$p \leftrightarrow q \equiv (p \rightarrow q) \land (q \rightarrow p)$$

- These algebraic identities can be used to simplify or transform propositions, just like the algebraic identities for numbers can be used to simplify or transform equations.
- A proposition is said to be a tautology if it is always true, regardless of the truth values of its component propositions. For example, $p \lor \lnot p$ is a tautology, because it is true whether $p$ is true or false.
- A proposition is said to be a contradiction if it is always false, regardless of the truth values of its component propositions. For example, $p \land \lnot p$ is a contradiction, because it is false whether $p$ is true or false.
- A proposition is said to be contingent if it is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its component propositions. For example, $p \land q$ is contingent, because it is true when both $p$ and $q$ are true, and false otherwise.
- Every propositional formula is equivalent to a sum-of-products or disjunctive form, which is an OR of AND-terms, where each AND-term is an AND of variables or negations of variables. For example, the disjunctive form of $p \rightarrow q$ is:

$$(\lnot p \land \lnot q) \lor (\lnot p \land q) \lor (p \land q)$$

- The disjunctive form can be simplified by using the algebraic identities and eliminating redundant terms. For example, the simplified disjunctive form of $p \rightarrow q$ is:

$$\lnot p \lor q$$

- The algebra of proposition



### Theory of Inference for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Propositional logic is the branch of logic that studies ways of combining or altering statements or propositions to form more complicated statements or propositions.
- A proposition is a declarative sentence that is either true or false, but not both.
- Examples of propositions are: "It is raining.", "2 + 2 = 4.", "Sydney is an AI assistant."
- Examples of non-propositions are: "What time is it?", "x + y = z.", "Hello."
- Propositional logic uses symbols to represent propositions and logical connectives to join them.
- Examples of symbols and connectives are: p, q, r, ¬ (not), ∧ (and), ∨ (or), → (implies), ↔ (if and only if).
- A truth table is a table that shows the truth value of a compound proposition for every possible combination of truth values of its components.
- A tautology is a compound proposition that is always true, regardless of the truth values of its components.
- A contradiction is a compound proposition that is always false, regardless of the truth values of its components.
- A contingency is a compound proposition that is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its components.
- A logical equivalence is a relation between two propositions that have the same truth value in every possible situation.
- A logical implication is a relation between two propositions that says that whenever the first proposition is true, the second proposition must also be true.
- A logical argument is a sequence of propositions that ends with a conclusion, which is supposed to follow from the preceding propositions, called premises.
- A valid argument is a logical argument in which the conclusion is logically implied by the premises, meaning that it is impossible for the premises to be true and the conclusion to be false.
- An invalid argument is a logical argument in which the conclusion is not logically implied by the premises, meaning that it is possible for the premises to be true and the conclusion to be false.
- A sound argument is a valid argument in which the premises are also true.
- An unsound argument is an invalid argument or a valid argument with at least one false premise.
- A rule of inference is a logical rule that allows us to derive a new proposition from one or more existing propositions, based on the logical structure of the propositions.
- A popular rule of inference in propositional logic is modus ponens, which says that if p implies q and p is true, then q is also true .
- Another popular rule of inference in propositional logic is modus tollens, which says that if p implies q and q is false, then p is also false.
- A third popular rule of inference in propositional logic is contraposition, which says that if p implies q, then not q implies not p.
- Rules of inference can be used to construct logical proofs, which are sequences of propositions that use rules of inference to show that a conclusion follows from a set of premises.
- A proof is valid if it uses only valid rules of inference and the premises are true.
- A proof is invalid if it uses an invalid rule of inference or the premises are false.



## Unit 5 - Predicate Logic

- Predicate logic is a branch of logic that deals with predicates, quantifiers, and variables.
- A predicate is a statement that can be true or false depending on the values of its arguments. For example, `P(x)` is a predicate that says `x` is a prime number.
- A quantifier is a symbol that expresses how many or how much of something satisfies a predicate. For example, `∀x P(x)` is a quantified statement that says `for all x, x is a prime number`.
- A variable is a symbol that can represent any value in a given domain. For example, `x` is a variable that can represent any natural number.
- Predicate logic allows us to express more complex and general statements than propositional logic, which only deals with propositions that are true or false by themselves.
- Predicate logic has two main types of formulas: atomic formulas and complex formulas.
- An atomic formula is a formula that consists of a predicate and its arguments. For example, `P(x)` and `Q(a,b)` are atomic formulas.
- A complex formula is a formula that is formed by combining atomic formulas using logical connectives and/or quantifiers. For example, `∀x (P(x) → Q(x,a))` and `∃y (R(y) ∧ ¬S(y,b))` are complex formulas.
- The syntax and semantics of predicate logic are defined by a set of rules that specify how to construct and interpret formulas.
- The syntax rules specify how to form well-formed formulas (wffs) using symbols, parentheses, and variables.
- The semantics rules specify how to assign truth values to formulas using a structure, which consists of a domain and an interpretation.
- A domain is a set of values that the variables can take. For example, the domain of natural numbers is `{0, 1, 2, 3, ...}`.
- An interpretation is a function that assigns meanings to the predicates and constants in a formula. For example, an interpretation can define `P(x)` to mean `x is even` and `a` to mean `2`.
- A formula is true in a structure if it is true for all possible assignments of values to the variables in the formula. For example, `∀x P(x)` is true in a structure if `P(x)` is true for every value in the domain.
- A formula is valid if it is true in every possible structure. For example, `∀x (P(x) → P(x))` is valid because it is a tautology.
- A formula is satisfiable if it is true in some possible structure. For example, `∃x P(x)` is satisfiable if there is at least one value in the domain that makes `P(x)` true.
- A formula is unsatisfiable if it is false in every possible structure. For example, `∀x ¬P(x) ∧ ∃x P(x)` is unsatisfiable because it is a contradiction.



### First order predicate logic

- First order predicate logic is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- A predicate is a symbol that represents a property or relation of one or more objects. For example, `P(x)` means that `x` has the property `P`.
- A variable is a symbol that can stand for any object in a given domain. For example, `x` can represent any number, person, animal, etc.
- A quantifier is a symbol that specifies how many objects in the domain satisfy a given predicate. For example, `∀x P(x)` means that `P` is true for all `x`, and `∃x P(x)` means that there is some `x` such that `P` is true.
- First order predicate logic allows us to express more complex and precise statements than propositional logic, which lacks quantifiers. For example, we can express the statement "Every human is mortal" as `∀x (Human(x) → Mortal(x))`, where `Human` and `Mortal` are predicates, and `x` is a variable.
- First order predicate logic is the standard for the formalization of mathematics into axioms, and is studied in the foundations of mathematics. For example, Peano arithmetic and Zermelo–Fraenkel set theory are axiomatizations of number theory and set theory, respectively, into first order predicate logic.



### Well Formed Formula of Predicate Logic

- A well formed formula (WFF) of predicate logic is a string of symbols that can be interpreted as a meaningful expression in predicate logic .
- A WFF can be either a **closed formula** or an **open formula**.
  - A closed formula (also called a sentence or a proposition) is a WFF that does not contain any free variables. It can be evaluated as true or false in a given interpretation. For example: ∀x(Px ∨ Qx)
  - An open formula (also called a sentential or propositional function) is a WFF that contains at least one free variable. It cannot be evaluated as true or false by itself, but only when the free variables are assigned values. For example: Px, ∃yQxy
- The rules for constructing WFFs of predicate logic are as follows :
  - Any predicate letter followed by any constant or variable is a WFF. For example: Pq, Qx
  - The result of prefixing any WFF with ‘~’ is a WFF. For example: ~Pq, ~∃yQxy
  - The result of joining any two WFFs with ‘•’, ‘∨’, ‘⊃’, or ‘≡’ and enclosing the result in parentheses is a WFF. For example: (Pq ∨ Qx), (Px ⊃ ~Qx)
  - The result of prefixing any WFF with a quantifier ‘∀’ or ‘∃’ and a variable is a WFF. For example: ∀xPx, ∃yQxy
  - Nothing else is a WFF. For example: P, Qxy, (Px ∨) are not WFFs.



### Quantifiers

Quantifiers are symbols that are used to express how many objects in a domain satisfy a given predicate. They allow us to make statements that involve variables without assigning a specific value to them. There are two main types of quantifiers: universal and existential.

- The **universal quantifier** (∀) states that a predicate is true for every element in the domain. For example, ∀x P(x) means that P(x) is true for all x in the domain. The universal quantifier is also called the "for all" or "for every" quantifier.
- The **existential quantifier** (∃) states that there exists at least one element in the domain that makes the predicate true. For example, ∃x P(x) means that there is some x in the domain such that P(x) is true. The existential quantifier is also called the "there exists" or "there is" quantifier.

Quantifiers are usually placed before the variables that they bind, and they have a scope that determines the range of the variables. The scope of a quantifier is the part of the formula that follows it, until another quantifier with the same variable is encountered. For example, in the formula ∀x (P(x) → ∃y Q(x,y)), the scope of ∀x is (P(x) → ∃y Q(x,y)), and the scope of ∃y is Q(x,y).

Quantifiers can be used to form complex statements by combining them with logical connectives, such as negation, conjunction, disjunction, implication, and equivalence. Some rules for manipulating quantifiers are:

- The negation of a universal statement is an existential statement, and vice versa. For example, ¬∀x P(x) is equivalent to ∃x ¬P(x), and ¬∃x P(x) is equivalent to ∀x ¬P(x).
- The order of quantifiers can be changed if they are of the same type, and if the variables do not appear in the predicate. For example, ∀x ∀y P(x,y) is equivalent to ∀y ∀x P(x,y), and ∃x ∃y P(x,y) is equivalent to ∃y ∃x P(x,y).
- The order of quantifiers can also be changed if they are of different types, and if the predicate does not depend on the inner variable. For example, ∀x ∃y P(x) is equivalent to ∃y ∀x P(x), and ∃x ∀y P(y) is equivalent to ∀y ∃x P(y).

Quantifiers are useful for expressing properties and relations of sets, functions, relations, and other mathematical objects. They can also be used to define concepts such as equality, cardinality, subset, function, relation, etc. For example, x = y can be defined as ∀z (P(z,x) ↔ P(z,y)), where P is any predicate; |A| = n can be defined as ∃f (∀x (x ∈ A → f(x) ∈ {1,2,...,n}) ∧ ∀y ∀z ((y ∈ {1,2,...,n} ∧ z ∈ {1,2,...,n} ∧ f^-1(y) = f^-1(z)) → y = z)), where f is a function; A ⊆ B can be defined as ∀x (x ∈ A → x ∈ B), where A and B are sets; f : A → B can be defined as ∀x (x ∈ A → ∃y (y ∈ B ∧ f(x) = y)), where f is a function; R ⊆ A × B can be defined as ∀x ∀y (R(x,y) → (x ∈ A ∧ y ∈ B)), where R is a relation.



### Inference theory of predicate logic

- Predicate logic, also known as first-order logic or quantified logic, is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Predicates are functions that take one or more arguments and return a truth value. For example, P(x) is a predicate that takes x as an argument and returns true or false.
- Variables are symbols that can represent any object in the domain of discourse. For example, x, y, z are variables that can stand for any person, animal, thing, etc.
- Quantifiers are operators that specify the scope or range of the variables. There are two main types of quantifiers: universal and existential. For example, (x)P(x) is a universal quantifier that means "for all x, P(x) is true", and (x)P(x) is an existential quantifier that means "there exists some x such that P(x) is true".
- Inference theory of predicate logic is a set of rules that allow us to derive valid conclusions from quantified statements. There are four main rules of inference for predicate logic :
  - Universal specification (US): From (x)P(x), one can conclude P(y) for any specific y in the domain. For example, from (x)Human(x) -> Mortal(x), one can conclude Human(Socrates) -> Mortal(Socrates).
  - Universal generalization (UG): From P(y) for any specific y in the domain, one can conclude (x)P(x). For example, from Human(Socrates) -> Mortal(Socrates), one can conclude (x)Human(x) -> Mortal(x).
  - Existential specification (ES): From (x)P(x), one can conclude P(c) for some constant c in the domain. For example, from (x)Human(x) -> Mortal(x), one can conclude Human(c) -> Mortal(c) for some c.
  - Existential generalization (EG): From P(c) for some constant c in the domain, one can conclude (x)P(x). For example, from Human(c) -> Mortal(c) for some c, one can conclude (x)Human(x) -> Mortal(x).
- These rules of inference are sound and complete, meaning that they can derive all and only the valid conclusions from the premises. They can also be combined with the rules of inference for propositional logic, such as modus ponens, modus tollens, etc.



## Unit 6 - Trees

- A tree is a nonlinear data structure that consists of nodes connected by edges.
- A tree has the following properties:
  - There is one node called the root, which has no parent.
  - Every node other than the root has exactly one parent node.
  - There is a unique path from the root to every node.
  - A node with no children is called a leaf node.
  - A node with at least one child is called an internal node.
  - The height of a node is the number of edges on the longest path from the node to a leaf.
  - The depth of a node is the number of edges on the path from the node to the root.
  - The level of a node is the depth of the node plus one.
  - The height of a tree is the height of the root node.
  - The size of a tree is the number of nodes in the tree.
- A tree can be represented in different ways, such as:
  - A linked list of nodes, where each node has a data field and a pointer to its parent and children.
  - An array, where the index of a node is its level-order position and the parent-child relationship is determined by a formula.
  - A nested list, where each element is either a data value or a sublist representing a subtree.
- A tree can be traversed in different ways, such as:
  - Preorder traversal, where the root is visited first, then the left subtree, then the right subtree.
  - Inorder traversal, where the left subtree is visited first, then the root, then the right subtree.
  - Postorder traversal, where the left subtree is visited first, then the right subtree, then the root.
  - Level-order traversal, where the nodes are visited in increasing order of their levels.
- A tree can be classified into different types, such as:
  - Binary tree, where each node has at most two children.
  - Binary search tree, where each node has a key and the keys in the left subtree are smaller than the key of the node and the keys in the right subtree are larger than the key of the node.
  - Balanced binary tree, where the height of the left and right subtrees of every node differ by at most one.
  - Complete binary tree, where every level except the last is completely filled and the nodes in the last level are as far left as possible.
  - Full binary tree, where every node has either zero or two children.
  - Perfect binary tree, where every node has two children and all the leaves are at the same level.
  - General tree, where each node can have any number of children.
  - Ordered tree, where the children of a node are ordered from left to right.
  - Forest, where a set of disjoint trees are considered as a single data structure.



### Definition for the notes of the Unit 6 - Trees in the subject of Discrete Structures & Theory of Logic

- A **tree** is a discrete structure that represents hierarchical relationships between individual elements or nodes  .
- A **node** is an element of a tree that can have a label, a value, or some other information associated with it .
- A **root** is a special node in a tree that has no parent .
- A **parent** is a node that has one or more children .
- A **child** is a node that has a parent .
- A **leaf** is a node that has no children .
- A **sibling** is a node that shares the same parent with another node .
- A **subtree** is a part of a tree that contains a node and all its descendants .
- A **path** is a sequence of nodes that are connected by edges .
- A **level** is the number of edges in the path from the root to a node .
- A **height** is the maximum level of any node in a tree .
- A **degree** is the number of children of a node .
- A **binary tree** is a tree in which a parent has no more than two children .
- An **ordered tree** is a tree whose subtrees are put into a definite order and are, themselves, ordered trees.
- A **directed tree** is a tree whose edges have a direction, usually from parent to child .



### Binary tree

- A binary tree is a tree data structure where each node has at most two child nodes, creating the branches of the tree.
- The two children are usually called the left and right nodes.
- A binary tree is also a rooted tree that is also an ordered tree (a.k.a. plane tree) in which every node has at most two children.
- A rooted tree naturally imparts a notion of levels (distance from the root), thus for every node a notion of children may be defined as the nodes connected to it a level below.
- A full binary tree (sometimes referred to as a proper or plane or strict binary tree) is a tree in which every node has either 0 or 2 children.
- Another way of defining a full binary tree is a recursive definition. A full binary tree is either: A single vertex. A tree whose root node has two subtrees, both of which are full binary trees.
- A binary tree is represented by a pointer to the topmost node (commonly known as the “root”) of the tree.
- Since each element in a binary tree can have only 2 children, we typically name them the left and right child.
- A binary tree can be empty, in which case it has no nodes and no root.
- A binary tree can also be non-empty, in which case it has a root and two subtrees that are both binary trees.
- The subtrees are called the left and right subtrees of the binary tree.
- A binary tree can be traversed in different ways, such as pre-order, in-order, post-order, and level-order.
- A binary tree can have various properties and applications, such as height, depth, size, balance, search, insertion, deletion, sorting, etc.



### Binary tree traversal

- A binary tree is a non-linear data structure that stores data in the form of nodes, and nodes are connected to each other with the help of edges.
- A binary tree has one main node called the root node, and all other nodes are the children of these nodes.
- A binary tree traversal is a process of visiting each node in the binary tree exactly once in a specified order.
- There are three common types of binary tree traversal: inorder, preorder and postorder.
- Inorder traversal: visit the left subtree, then the root, then the right subtree.
- Preorder traversal: visit the root, then the left subtree, then the right subtree.
- Postorder traversal: visit the left subtree, then the right subtree, then the root.
- A binary tree traversal can be implemented using recursion or iteration.
- A binary tree traversal can be used for various purposes, such as searching, sorting, printing, copying, deleting, etc.
- A binary tree traversal can also be done in a vertical order, where nodes at the same horizontal distance from the root are clustered together and output their depth in ascending order.



### Binary search tree

- A binary search tree (BST) is a special type of binary tree that satisfies the following properties:
  - The left subtree of a node contains only nodes with keys less than the node's key.
  - The right subtree of a node contains only nodes with keys greater than the node's key.
  - The left and right subtrees of a node are also BSTs.
  - There are no duplicate keys in a BST.
- A BST supports efficient operations such as search, insert, delete, minimum, maximum, successor, and predecessor, which take O(h) time, where h is the height of the tree.
- A BST can be represented by an array, where the root node is at index 0, and the left and right children of a node at index i are at indices 2i+1 and 2i+2, respectively.
- A BST can also be represented by a linked list, where each node has a key, a data, a left pointer, and a right pointer.
- A BST can be traversed in different ways, such as preorder, inorder, postorder, and level order, which visit the nodes in different orders.
- A BST can be balanced or unbalanced, depending on how the nodes are distributed. A balanced BST has a height of O(log n), where n is the number of nodes, while an unbalanced BST can have a height of O(n) in the worst case.
- A BST can be balanced by using techniques such as rotation, splitting, joining, or using self-balancing BSTs such as AVL trees, red-black trees, or splay trees.



## Unit 7 - Graphs

- A graph is a collection of vertices (or nodes) and edges (or arcs) that connect them.
- A graph can be used to model various types of relations or networks, such as social networks, transportation networks, communication networks, etc.
- A graph can be represented in different ways, such as using an adjacency matrix, an adjacency list, or a visual diagram.
- Some basic terminology and properties of graphs are:
  - The degree of a vertex is the number of edges incident to it.
  - A loop is an edge that connects a vertex to itself.
  - A multiple edge is an edge that occurs more than once between two vertices.
  - A simple graph is a graph that has no loops or multiple edges.
  - A directed graph (or digraph) is a graph in which each edge has a direction, indicated by an arrow.
  - An undirected graph is a graph in which each edge has no direction, indicated by a line.
  - A weighted graph is a graph in which each edge has a numerical value (or weight) associated with it.
  - A subgraph of a graph is a graph that consists of some of the vertices and edges of the original graph.
  - A path in a graph is a sequence of vertices and edges that connects two vertices.
  - A cycle in a graph is a path that starts and ends at the same vertex.
  - A connected graph is a graph in which there is a path between any two vertices.
  - A disconnected graph is a graph that is not connected.
  - A component of a graph is a maximal connected subgraph of the graph.
  - A tree is a connected graph that has no cycles.
  - A forest is a graph that consists of one or more trees.
  - A spanning tree of a graph is a subgraph that is a tree and contains all the vertices of the graph.
  - A bipartite graph is a graph whose vertices can be divided into two disjoint sets such that no edge connects two vertices in the same set.
  - A complete graph is a graph in which there is an edge between every pair of vertices.
  - A planar graph is a graph that can be drawn on a plane without any edges crossing.
  - A graph isomorphism is a one-to-one correspondence between the vertices and edges of two graphs that preserves the adjacency relation.



### Definition and terminology for the notes of the Unit 7 - Graphs in the subject of Discrete Structures & Theory of Logic

- A **graph** is a mathematical structure that consists of a set of **vertices** (or nodes) and a set of **edges** (or links) that connect pairs of vertices.
- A graph can be represented by a diagram, where vertices are drawn as points or circles, and edges are drawn as lines or curves connecting the vertices.
- A graph can also be represented by an **adjacency matrix**, where each row and column corresponds to a vertex, and the entry at row i and column j is 1 if there is an edge between vertex i and vertex j, and 0 otherwise.
- A graph can be **directed** or **undirected**, depending on whether the edges have a direction or not. A directed edge is drawn as an arrow pointing from one vertex to another, and indicates that there is a relation from the first vertex to the second, but not necessarily the other way around. An undirected edge is drawn as a line or curve without arrows, and indicates that there is a relation between the two vertices in both directions.
- A graph can be **weighted** or **unweighted**, depending on whether the edges have a numerical value or not. A weighted edge is drawn with a label indicating its value, and represents the cost, distance, or strength of the relation between the two vertices. An unweighted edge has no label, and represents a binary relation (either present or absent) between the two vertices.
- A graph can be **simple** or **non-simple**, depending on whether it has multiple edges or loops. A multiple edge is an edge that connects the same pair of vertices more than once. A loop is an edge that connects a vertex to itself. A simple graph has no multiple edges or loops, while a non-simple graph may have them.
- A graph can be **connected** or **disconnected**, depending on whether there is a path between any two vertices or not. A path is a sequence of edges that starts from one vertex and ends at another, and passes through intermediate vertices without repeating any vertex or edge. A connected graph has a path between any two vertices, while a disconnected graph has at least two vertices that are not reachable from each other.
- A graph can be **cyclic** or **acyclic**, depending on whether it has a cycle or not. A cycle is a path that starts and ends at the same vertex, and has at least one edge. A cyclic graph has at least one cycle, while an acyclic graph has no cycles.
- A graph can be **complete** or **incomplete**, depending on whether it has all possible edges or not. A complete graph has an edge between every pair of vertices, while an incomplete graph has some pairs of vertices that are not connected by an edge.
- A graph can be **bipartite** or **non-bipartite**, depending on whether it can be partitioned into two sets of vertices such that no edge connects two vertices from the same set. A bipartite graph can be drawn in such a way that the vertices of one set are on one side of a line, and the vertices of the other set are on the other side of the line, and all the edges cross the line. A non-bipartite graph cannot be drawn in this way.



### Representation of graphs

A graph is a mathematical structure that consists of a set of vertices and a set of edges that connect pairs of vertices. A graph can be used to model many types of relations and processes in physical, biological, social and information systems.

There are different ways to represent a graph, depending on the purpose and the type of the graph. Some of the common representations are:

- **Adjacency matrix**: An adjacency matrix is a square matrix of size n x n, where n is the number of vertices in the graph. The entry in the i-th row and j-th column of the matrix is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For an undirected graph, the adjacency matrix is symmetric, meaning that the entry in the i-th row and j-th column is equal to the entry in the j-th row and i-th column. For a directed graph, the adjacency matrix is not necessarily symmetric, meaning that the entry in the i-th row and j-th column may not be equal to the entry in the j-th row and i-th column. For a weighted graph, the entry in the i-th row and j-th column is the weight of the edge from vertex i to vertex j, instead of 1 or 0.

  An example of an adjacency matrix for an undirected graph with 4 vertices is:

  |   | 1 | 2 | 3 | 4 |
  |---|---|---|---|---|
  | 1 | 0 | 1 | 0 | 1 |
  | 2 | 1 | 0 | 1 | 0 |
  | 3 | 0 | 1 | 0 | 1 |
  | 4 | 1 | 0 | 1 | 0 |

  An example of an adjacency matrix for a directed graph with 4 vertices is:

  |   | 1 | 2 | 3 | 4 |
  |---|---|---|---|---|
  | 1 | 0 | 1 | 0 | 0 |
  | 2 | 0 | 0 | 1 | 0 |
  | 3 | 0 | 0 | 0 | 1 |
  | 4 | 1 | 0 | 0 | 0 |

  An example of an adjacency matrix for a weighted graph with 4 vertices is:

  |   | 1 | 2 | 3 | 4 |
  |---|---|---|---|---|
  | 1 | 0 | 2 | 0 | 4 |
  | 2 | 2 | 0 | 3 | 0 |
  | 3 | 0 | 3 | 0 | 5 |
  | 4 | 4 | 0 | 5 | 0 |

  The advantages of using an adjacency matrix are:

  - It is easy to check if there is an edge between two vertices, by looking at the corresponding entry in the matrix.
  - It is easy to find the degree of a vertex, by summing up the entries in the corresponding row or column of the matrix.
  - It is easy to perform operations on graphs, such as adding or deleting edges, by changing the entries in the matrix.

  The disadvantages of using an adjacency matrix are:

  - It requires a lot of space, especially for sparse graphs, where most of the entries are 0.
  - It is not easy to visualize the structure of the graph, by looking at the matrix.

- **Adjacency list**: An adjacency list is a collection of lists, one for each vertex in the graph. Each list contains the vertices that are adjacent to the vertex, meaning that there is an edge from the vertex to the adjacent vertex. For an undirected graph, each edge appears twice in the adjacency list, once for each endpoint. For a directed graph, each edge appears once in the adjacency list, for the source vertex. For a weighted graph, each adjacent vertex is accompanied by the weight of the edge.

  An example of an adjacency list for an undirected graph with 4 vertices is:

  | Vertex | Adjacent vertices |
  |--------|-------------------|
  | 1      | 2, 4              |
  | 2      | 1, 3              |
  | 3      | 2, 4              |
  | 4      | 1, 3              |

  An example of an adjacency list for a directed graph with 4 vertices is:

  | Vertex | Adjacent vertices |
  |--------|-------------------|
  | 1      | 2



### Multigraphs

- A multigraph is a graph that allows multiple edges (also called parallel edges) between two vertices.   
- A multigraph can be represented as a pair G = (V, E), where V is a set of vertices and E is a multiset of unordered pairs of vertices. 
- A multigraph can be used to model situations where there are multiple connections or paths between two entities, such as highways, flights, or networks.  
- A multigraph can be drawn by using curves or loops to distinguish between multiple edges. 
- A multigraph can be converted into a simple graph by removing or merging multiple edges. 
- A multigraph can have loops, which are edges that connect a vertex to itself.  
- A multigraph can be directed or undirected. A directed multigraph (or multidigraph) allows multiple edges with the same source and target vertices. 
- A multigraph can have different types of edges, such as weighted, colored, or labeled edges, depending on the application.



### Bipartite Graphs

- A **bipartite graph** is a graph whose vertices can be divided into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set.
- The two sets of vertices are usually called the **parts** of the graph. They can be denoted by and .
- A bipartite graph can also be defined as a graph that has no odd cycle, that is, a cycle with an odd number of vertices.
- A bipartite graph is a special case of a **-partite graph** with .
- A bipartite graph is equivalent to a **two-colorable graph**, that is, a graph that can be colored with two colors such that no two adjacent vertices have the same color.
- All **acyclic graphs** (graphs that have no cycles) are bipartite.
- A **cyclic graph** (a graph that has at least one cycle) is bipartite if and only if all the cycles involved are of even length.
- According to **König's line coloring theorem**, all bipartite graphs are **class 1 graphs**, that is, graphs that can be edge-colored with colors, where is the maximum degree of the graph.

#### Examples of Bipartite Graphs

- The following graph is an example of a bipartite graph, with the parts and shown in different colors:

bipartite graph example

- The **complete bipartite graph** is a bipartite graph where every vertex in is adjacent to every vertex in . It is denoted by , where and are the sizes of the parts . For example, the graph is a complete bipartite graph with 3 vertices in each part:

complete bipartite graph example

- The **Heawood graph** is a bipartite graph with 14 vertices and 21 edges. It is also a **cubic graph** (a graph where every vertex has degree 3) and a **cage graph** (a graph with the smallest possible number of edges for its girth, which is the length of the shortest cycle) . It is shown below:

Heawood graph example

#### Applications of Bipartite Graphs

- Bipartite graphs can be used to model many real-world situations, such as:
  - **Matching problems**, where one set of vertices represents a set of agents and the other set represents a set of tasks, and the edges represent the possible assignments of agents to tasks .
  - **Network flow problems**, where one set of vertices represents a set of sources and the other set represents a set of sinks, and the edges represent the capacities of the channels between them .
  - **Graph coloring problems**, where one set of vertices represents a set of regions and the other set represents a set of colors, and the edges represent the constraints on the coloring of the regions .
  - **Social network analysis**, where one set of vertices represents a set of users and the other set represents a set of groups, and the edges represent the memberships of users in groups .



### Planar Graphs

- A planar graph is a graph that can be drawn on a plane without any edges crossing each other.
- A plane graph is a planar graph with a specific way of drawing it on the plane.
- A planar graph can have more than one plane graph representation.
- A planar graph divides the plane into regions called faces.
- The number of faces of a plane graph depends on how it is drawn.
- A planar graph has some properties that relate its number of vertices, edges and faces. These are:

  - Euler's formula: For any connected plane graph with n vertices, e edges and f faces, n - e + f = 2.
  - The maximum number of edges of a planar graph with n vertices is 3n - 6, if n >= 3.
  - A planar graph cannot have a subgraph that is a subdivision of K5 (the complete graph on 5 vertices) or K3,3 (the complete bipartite graph on 3 and 3 vertices).
  - A planar graph is bipartite if and only if it has no odd cycles.



### Isomorphism and Homeomorphism of graphs

- Isomorphism and homeomorphism are two concepts in graph theory that relate to the similarity and equivalence of graphs.
- A graph is a set of vertices and edges that connect some pairs of vertices. A graph can be represented by a diagram where vertices are points and edges are lines or curves.
- Two graphs are **isomorphic** if they have the same number of vertices and there is a one-to-one correspondence between the vertices of the two graphs that preserves the adjacency of the vertices. That is, two vertices are adjacent in one graph if and only if their corresponding vertices are adjacent in the other graph.
- An **isomorphism** is a bijective function that maps the vertices of one graph to the vertices of another graph in such a way that preserves the adjacency of the vertices. An isomorphism can also be seen as a relabeling of the vertices of one graph to match the vertices of another graph.
- For example, the following two graphs are isomorphic, and the function f that maps A to 1, B to 2, C to 3, D to 4, and E to 5 is an isomorphism.

isomorphic graphs

- Two graphs are **homeomorphic** if they can be obtained from each other by a sequence of subdivisions and smoothings. A **subdivision** of a graph is the operation of replacing an edge by a path of two or more edges. A **smoothing** of a graph is the inverse operation of subdivision, that is, replacing a path of two or more edges by a single edge.
- A **homeomorphism** is a graph isomorphism from some subdivision of one graph to some subdivision of another graph. A homeomorphism can also be seen as a deformation of one graph into another graph by bending, stretching, or shrinking the edges, but not breaking or crossing them.
- For example, the following two graphs are homeomorphic, and the function g that maps A to 1, B to 2, C to 3, D to 4, E to 5, F to 6, and G to 7 is a homeomorphism.

homeomorphic graphs

- Properties of isomorphisms and homeomorphisms:
  - Isomorphism and homeomorphism are equivalence relations on the set of graphs, that is, they are reflexive, symmetric, and transitive.
  - Isomorphism and homeomorphism preserve some properties of graphs, such as the number of vertices, the number of edges, the degree of vertices, the connectivity, the planarity, the Euler characteristic, etc.
  - Isomorphism is a stronger relation than homeomorphism, that is, every isomorphic pair of graphs is also homeomorphic, but not vice versa. For example, the following two graphs are homeomorphic but not isomorphic, because they have different numbers of edges.

homeomorphic but not isomorphic graphs

- Applications of isomorphism and homeomorphism:
  - Isomorphism and homeomorphism are useful for studying the structure and properties of graphs, and for classifying graphs into different types or classes.
  - Isomorphism and homeomorphism can also be used to model and compare different objects or systems that can be represented by graphs, such as molecules, networks, maps, circuits, etc.



### Euler and Hamiltonian paths

- An **Euler path** is a path in a graph that passes through every **edge** exactly once  . If it ends at the initial vertex, then it is an **Euler cycle**  .
- A **Hamiltonian path** is a path in a graph that passes through every **vertex** exactly once  . If it ends at the initial vertex, then it is a **Hamiltonian cycle**  .
- Euler paths and cycles can exist in both directed and undirected graphs, but Hamiltonian paths and cycles can only exist in undirected graphs .
- To check if a graph has an Euler path or cycle, we can use the following criteria :
  - A connected graph has an Euler cycle if and only if every vertex has an even degree.
  - A connected graph has an Euler path but not an Euler cycle if and only if it has exactly two vertices of odd degree.
- To check if a graph has a Hamiltonian path or cycle, there is no simple necessary and sufficient criteria, but we can use some sufficient conditions :
  - A graph has a Hamiltonian cycle if it is a complete graph, i.e., every pair of vertices is connected by an edge.
  - A graph has a Hamiltonian cycle if it is a cycle graph, i.e., a graph with n vertices and n edges forming a single cycle.
  - A graph has a Hamiltonian path if it is a path graph, i.e., a graph with n vertices and n-1 edges forming a single path.
- Euler and Hamiltonian paths and cycles have applications in various fields, such as network routing, DNA sequencing, traveling salesman problem, etc  .



### Graph coloring

- Graph coloring is a special case of graph labeling, where each vertex of a graph is assigned a color subject to some constraints.
- The most common constraint is that no two adjacent vertices have the same color. This is called a **proper coloring** or a **vertex coloring** .
- A graph that can be properly colored with k colors is called **k-colorable**. The minimum number of colors needed to properly color a graph is called its **chromatic number**.
- Graph coloring has many applications in various fields, such as scheduling, map coloring, register allocation, Sudoku, etc .
- Graph coloring is closely related to the concept of an **independent set**, which is a set of vertices in a graph that are not adjacent to each other . If a graph is properly colored, the vertices that are assigned a particular color form an independent set.
- Graph coloring can also be extended to other elements of a graph, such as edges, faces, or subgraphs. These are called **edge coloring**, **face coloring**, or **subgraph coloring**, respectively .
- Graph coloring is a NP-complete problem, which means that there is no efficient algorithm to find the optimal coloring of a graph in general . However, some special classes of graphs have polynomial-time algorithms or simple rules for coloring, such as trees, bipartite graphs, planar graphs, etc .



## Unit 8 - Recurrence Relation & Generating function

- A **recurrence relation** is an equation that defines a sequence recursively: each term of the sequence is defined as a function of the preceding terms.
- A **generating function** is a formal power series that encodes the information of a sequence in its coefficients.
- Recurrence relations and generating functions are useful tools for analyzing and solving problems involving discrete structures, such as combinatorics, algorithms, and cryptography.
- Some examples of recurrence relations are:

  - The Fibonacci sequence: F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1.
  - The factorial function: n! = n * (n-1)!, with 0! = 1.
  - The binomial coefficients: C(n, k) = C(n-1, k-1) + C(n-1, k), with C(n, 0) = C(n, n) = 1.

- Some examples of generating functions are:

  - The geometric series: G(x) = 1 + x + x^2 + x^3 + ... = 1 / (1 - x).
  - The exponential function: E(x) = 1 + x + x^2 / 2! + x^3 / 3! + ... = e^x.
  - The binomial theorem: B(x) = (1 + x)^n = C(n, 0) + C(n, 1) x + C(n, 2) x^2 + ... + C(n, n) x^n.

- To find the generating function of a given sequence, we can use various methods, such as:

  - The method of coefficients: equate the coefficients of the same powers of x in the generating function and the sequence, and solve for the unknowns.
  - The method of substitution: substitute a known generating function into another generating function, and simplify the result.
  - The method of partial fractions: decompose a rational generating function into simpler fractions, and use known formulas to find the corresponding sequences.

- To find the sequence of a given generating function, we can use various methods, such as:

  - The method of differentiation: differentiate the generating function with respect to x, and multiply by x^n to find the coefficient of x^n.
  - The method of integration: integrate the generating function with respect to x, and divide by x^n+1 to find the coefficient of x^n.
  - The method of expansion: expand the generating function using binomial theorem, Taylor series, or other techniques, and read off the coefficients of x^n.



### Recursive definition of functions

- A recursive definition of a function is a way of defining the value of a function for some inputs in terms of the value of the same function for other inputs, usually smaller or simpler ones.
- A recursive definition of a function consists of two parts: a base case and a recursive step.
- The base case specifies the value of the function for some inputs that do not depend on the function itself. For example, the factorial function n! is defined by the base case 0! = 1.
- The recursive step specifies the value of the function for some inputs that depend on the function itself, usually by applying some operation or relation to the function value for a smaller or simpler input. For example, the factorial function n! is defined by the recursive step (n + 1)! = (n + 1)· n !.
- A recursive definition of a function is valid if it satisfies the following conditions:
  - The base case is well-defined and covers at least one input value.
  - The recursive step is well-defined and covers all other input values.
  - The recursive step always reduces the input value to a smaller or simpler one, so that the base case is eventually reached.
  - The recursive step does not produce any contradictions or inconsistencies with the base case or itself.
- A recursive definition of a function can be used to compute the function value for any input by following the recursive step until the base case is reached, and then substituting the base case value back into the recursive step. For example, to compute 3!, we can use the recursive definition as follows:
  - 3! = (3 + 1)! / (3 + 1) = 4! / 4
  - 4! = (4 + 1)! / (4 + 1) = 5! / 5
  - 5! = (5 + 1)! / (5 + 1) = 6! / 6
  - 6! = (6 + 1)! / (6 + 1) = 7! / 7
  - 7! = (7 + 1)! / (7 + 1) = 8! / 8
  - 8! = (8 + 1)! / (8 + 1) = 9! / 9
  - 9! = (9 + 1)! / (9 + 1) = 10! / 10
  - 10! = (10 + 1)! / (10 + 1) = 11! / 11
  - 11! = (11 + 1)! / (11 + 1) = 12! / 12
  - 12! = (12 + 1)! / (12 + 1) = 13! / 13
  - 13! = (13 + 1)! / (13 + 1) = 14! / 14
  - 14! = (14 + 1)! / (14 + 1) = 15! / 15
  - 15! = (15 + 1)! / (15 + 1) = 16! / 16
  - 16! = (16 + 1)! / (16 + 1) = 17! / 17
  - 17! = (17 + 1)! / (17 + 1) = 18! / 18
  - 18! = (18 + 1)! / (18 + 1) = 19! / 19
  - 19! = (19 + 1)! / (19 + 1) = 20! / 20
  - 20! = (20 + 1)! / (20 + 1) = 21! / 21
  - 21! = (21 + 1)! / (21 + 1) = 22! / 22
  - 22! = (22 + 1)! / (22 + 1) = 23! / 23
  - 23! = (23 + 1)! / (23 + 1) = 24! / 24
  - 24! = (24 + 1)! / (24 + 1) = 25! / 25
  - 25! = (25



### Recursive algorithms

- A recursive algorithm is an algorithm that calls itself, either directly or indirectly, to solve a smaller instance of the same problem.
- A recursive algorithm must have a base case, which is a condition that terminates the recursion when it is met.
- A recursive algorithm must also have a recursive case, which is a condition that reduces the problem size and invokes the algorithm again with the smaller problem.
- A recursive algorithm can be more concise, elegant, and intuitive than an iterative algorithm, but it may also be less efficient or more difficult to analyze.
- Examples of recursive algorithms are:
  - Factorial: To compute n!, we can use the following recursive formula: n! = n * (n-1)! if n > 1, and 1 if n = 1. The base case is n = 1, and the recursive case is n > 1.
  - Fibonacci: To compute the nth Fibonacci number, we can use the following recursive formula: F(n) = F(n-1) + F(n-2) if n > 2, and 1 if n = 1 or 2. The base case is n = 1 or 2, and the recursive case is n > 2.
  - Merge sort: To sort an array, we can use the following recursive algorithm: Divide the array into two halves, sort each half recursively, and merge the two sorted halves. The base case is when the array has one or zero elements, and the recursive case is when the array has more than one element.
  - Tower of Hanoi: To move n disks from one peg to another, we can use the following recursive algorithm: Move n-1 disks from the source peg to the auxiliary peg, move the largest disk from the source peg to the destination peg, and move n-1 disks from the auxiliary peg to the destination peg. The base case is when n = 1, and the recursive case is when n > 1.



### Method of solving recurrences

- A recurrence relation is an equation that defines a sequence in terms of its previous terms. For example, T(n) = T(n-1) + n is a recurrence relation that defines the nth term of a sequence as the sum of the previous term and n.
- Recurrence relations often arise in the analysis of algorithms, especially recursive algorithms. For example, the recurrence relation T(n) = 2T(n/2) + n describes the running time of the merge sort algorithm.
- Solving a recurrence relation means finding a closed-form expression or a formula for the general term of the sequence, without referring to the previous terms. For example, the solution of the recurrence relation T(n) = T(n-1) + n is T(n) = n(n+1)/2.
- There are different methods of solving recurrences, depending on the type and complexity of the recurrence relation. Some of the common methods are:

  - **Forward substitution**: This method involves substituting the recurrence relation for n = 0, 1, 2, ... until a pattern is observed. Then, a guess is made for the general form of the solution and verified by induction. This method is simple but may not work for complex recurrences or may require a lot of computation. For example, using this method, we can solve the recurrence relation T(n) = T(n-1) + n as follows:

    - T(0) = 0 (base case)
    - T(1) = T(0) + 1 = 1
    - T(2) = T(1) + 2 = 3
    - T(3) = T(2) + 3 = 6
    - T(4) = T(3) + 4 = 10
    - ...
    - We can see that the sequence is the sum of the first n natural numbers, so we guess that T(n) = n(n+1)/2. To prove this by induction, we assume that T(k) = k(k+1)/2 for some k >= 0 and show that T(k+1) = (k+1)(k+2)/2. This is true because:

      - T(k+1) = T(k) + (k+1) by the recurrence relation
      - T(k+1) = k(k+1)/2 + (k+1) by the induction hypothesis
      - T(k+1) = (k+1)(k+2)/2 by simplifying
      - Therefore, T(n) = n(n+1)/2 for all n >= 0 by induction.

  - **Recursion tree**: This method involves drawing a tree that represents the cost of each level of recursion. The cost of each node is the amount of work done at that level, excluding the recursive calls. The total cost of the recurrence is the sum of the costs of all the nodes in the tree. This method is useful for visualizing the recurrence and estimating its asymptotic behavior. For example, using this method, we can solve the recurrence relation T(n) = 2T(n/2) + n as follows:

    - The recursion tree for this recurrence is:

      ```
      T(n) = n + 2T(n/2)
            /        \
      T(n/2) = n/2 + 2T(n/4)
              /          \
      T(n/4) = n/4 + 2T(n/8)
              /          \
             ...
            /   \
      T(1) = 1 + 2T(1/2)
            /       \
      T(1/2) = 0 + 2T(1/4)
              /         \
             ...
      ```

    - The cost of each level is n, since there are 2^i nodes at level i, each with a cost of n/2^i. The number of levels is log(n), since the recursion stops when n/2^i = 1. Therefore, the total cost of the recurrence is:

      - T(n) = n + n + n + ... + n (log(n) times)
      - T(n) = n log(n)

  - **Master theorem**: This method is a general formula for solving recurrences of the form T(n) = aT(n/b) + f(n), where a, b, and f(n) are constants or functions of n. The master theorem states that the solution of the



## Unit 9 - Combinatorics

- Combinatorics is the branch of mathematics that studies the ways of counting, arranging, and selecting objects from a given set or collection.
- Combinatorics has applications in many fields, such as cryptography, coding theory, graph theory, probability, statistics, and optimization.
- Some of the main topics in combinatorics are:

  - **Permutations**: The number of ways to order a set of objects.
  - **Combinations**: The number of ways to choose a subset of objects from a set, without regard to order.
  - **Binomial coefficients**: The coefficients of the binomial expansion, which give the number of combinations of a certain size from a set.
  - **Factorials**: The product of all positive integers up to a given number, which give the number of permutations of a set.
  - **Pascal's triangle**: A triangular array of numbers that shows the binomial coefficients and other patterns.
  - **The principle of inclusion-exclusion**: A formula that gives the number of elements in the union of several sets, by subtracting the overlaps.
  - **The pigeonhole principle**: A statement that says that if more objects are placed into fewer containers, then at least one container must contain more than one object.
  - **Partitions**: The number of ways to divide a set of objects into non-empty subsets, without regard to order.
  - **Generating functions**: A way of representing a sequence of numbers by a power series, which can be used to find formulas and properties of the sequence.
  - **Recurrence relations**: A way of defining a sequence of numbers by relating each term to previous terms, which can be used to find formulas and properties of the sequence.



### Introduction for the notes of the Unit 9 - Combinatorics in the subject of Discrete Structures & Theory of Logic

- Combinatorics is the branch of mathematics that studies the ways of counting or arranging discrete objects.
- Combinatorics has applications in many areas of computer science, such as cryptography, coding theory, graph theory, algorithm design, and artificial intelligence.
- Some of the basic concepts and techniques of combinatorics are:

  - The rule of sum and the rule of product, which allow us to count the number of possible outcomes of a compound event by adding or multiplying the number of outcomes of simpler events.
  - The principle of inclusion-exclusion, which allows us to count the number of elements in a union of sets by subtracting the number of elements in their intersections.
  - The binomial theorem, which gives us a formula for the expansion of a binomial expression raised to a power, and also allows us to compute the binomial coefficients, which count the number of ways of choosing a subset of a given size from a larger set.
  - The pigeonhole principle, which states that if we distribute more than n objects into n boxes, then at least one box must contain more than one object. This principle can be used to prove the existence of certain combinatorial patterns or properties.
  - Permutations and combinations, which count the number of ways of ordering or selecting a subset of objects from a larger set, with or without repetition, and with or without regard to order.
  - Recurrence relations, which describe the relationship between successive terms of a sequence, and can be used to model various combinatorial problems, such as the Fibonacci sequence, the Tower of Hanoi problem, and the Catalan numbers.
  - Generating functions, which are algebraic expressions that encode the information about a sequence of numbers, and can be used to manipulate, analyze, and solve recurrence relations, as well as to find closed-form formulas for combinatorial quantities.



### Counting Techniques for the notes of the Unit 9 - Combinatorics in the subject of Discrete Structures & Theory of Logic

Combinatorics is the branch of mathematics that deals with the study of finite or countable discrete structures. It includes the enumeration or counting of objects having certain properties, such as arrangements, combinations, permutations, partitions, etc. Combinatorics is useful for solving problems in computer science, cryptography, probability, and algebra.

Some of the basic counting techniques are:

- **The product rule**: This rule states that if there are $n_1$ ways to do one thing, and $n_2$ ways to do another thing, then there are $n_1 \times n_2$ ways to do both things. For example, if there are 10 different shirts and 8 different pants to choose from, then there are $10 \times 8 = 80$ ways to choose an outfit.

- **The sum rule**: This rule states that if there are $n_1$ ways to do one thing, and $n_2$ ways to do another thing, and these two things cannot be done at the same time, then there are $n_1 + n_2$ ways to do either one of them. For example, if there are 5 different books and 7 different magazines to read, and you can only read one at a time, then there are $5 + 7 = 12$ ways to choose something to read.

- **The factorial**: This is a notation that represents the product of all positive integers from 1 to a given number. It is denoted by $n!$, where $n$ is a positive integer. For example, $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$. The factorial is useful for counting the number of ways to arrange $n$ distinct objects in a row, which is $n!$.

- **The permutation**: This is a way of counting the number of ways to arrange $r$ out of $n$ distinct objects in a row, where the order matters. It is denoted by $P(n,r)$ or $_n P_r$, and it is equal to $\frac{n!}{(n-r)!}$. For example, the number of ways to arrange 3 out of 5 letters A, B, C, D, E in a row is $P(5,3) = \frac{5!}{(5-3)!} = \frac{120}{2} = 60$.

- **The combination**: This is a way of counting the number of ways to choose $r$ out of $n$ distinct objects, where the order does not matter. It is denoted by $C(n,r)$ or $_n C_r$ or ${n \choose r}$, and it is equal to $\frac{n!}{r!(n-r)!}$. For example, the number of ways to choose 3 out of 5 letters A, B, C, D, E is $C(5,3) = \frac{5!}{3!(5-3)!} = \frac{120}{6 \times 2} = 10$.

- **The binomial theorem**: This is a formula that gives the expansion of $(x+y)^n$, where $n$ is a non-negative integer. It states that $(x+y)^n = \sum_{r=0}^n {n \choose r} x^{n-r} y^r$, where ${n \choose r}$ are the binomial coefficients. For example, $(x+y)^3 = {3 \choose 0} x^3 y^0 + {3 \choose 1} x^2 y^1 + {3 \choose 2} x^1 y^2 + {3 \choose 3} x^0 y^3 = x^3 + 3x^2y + 3xy^2 + y^3$. The binomial theorem is useful for counting the number of ways to obtain a certain outcome in a repeated experiment, such as tossing a coin or rolling a die.

- **The inclusion-exclusion principle**: This is a way of counting the number of elements in a union of sets, by subtracting the number of elements in the intersections of the sets. It states that $|A \cup B| = |A| + |B| - |A \cap B|$, where $|A|$ denotes



### Pigeonhole Principle

- The pigeonhole principle is a basic principle of combinatorics that states that if there are more objects than containers, then at least one container must hold more than one object.
- Formally, the pigeonhole principle can be stated as follows: If n objects are placed into k containers, where n > k, then there exists at least one container that contains more than one object.
- The pigeonhole principle can be used to prove the existence of certain outcomes or patterns, without actually finding them. For example, using the pigeonhole principle, one can show that in any group of 13 people, there are at least two who have the same birthday month.
- The pigeonhole principle can also be generalized to account for different numbers of objects and containers, or different conditions on the containers. For example, one can show that in any group of 100 people, there are at least 50 who have the same last digit of their phone number, by using 10 containers corresponding to the 10 possible digits, and placing 100 objects (people) into them.
- The pigeonhole principle can also be applied to infinite sets, using the concept of cardinality. For example, one can show that there are infinitely many irrational numbers, by using the pigeonhole principle on the set of real numbers and the set of rational numbers, both of which have the same cardinality (aleph-one). Since there are more real numbers than rational numbers, there must be some real numbers that are not rational, and hence irrational.

