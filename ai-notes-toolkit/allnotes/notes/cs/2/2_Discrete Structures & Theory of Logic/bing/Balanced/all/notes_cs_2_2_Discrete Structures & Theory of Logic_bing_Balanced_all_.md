

## Unit 1 - Set Theory

Set theory is a branch of mathematics that studies collections of objects, called sets, and the relationships between them. Some of the topics covered in this unit are:

- Definition and notation of sets
- Types of sets, such as empty set, singleton set, finite set, infinite set, universal set, subset, proper subset, etc.
- Operations on sets, such as union, intersection, difference, complement, symmetric difference, etc.
- Venn diagrams and set-builder notation
- Laws of set algebra, such as commutative, associative, distributive, identity, etc.
- Cartesian product of sets and ordered pairs
- Relations and functions, such as domain, range, inverse, one-to-one, onto, etc.

Some of the learning objectives of this unit are:

- To understand the basic concepts and terminology of set theory
- To perform various operations on sets and represent them using different notations
- To apply the laws of set algebra to simplify and prove set expressions
- To identify and classify different types of relations and functions
- To use set theory to model and solve real-world problems

Some of the assessment criteria of this unit are:

- To demonstrate the ability to define and use sets and their elements
- To demonstrate the ability to perform and interpret set operations and their properties
- To demonstrate the ability to use Venn diagrams and set-builder notation to represent sets
- To demonstrate the ability to apply the laws of set algebra to manipulate and verify set expressions
- To demonstrate the ability to determine and describe the characteristics of relations and functions
- To demonstrate the ability to use set theory to analyze and solve real-world problems



# Introduction for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- Set theory is a branch of mathematics that studies collections of objects, called sets, and the relationships between them.
- A set is a well-defined collection of distinct objects, which can be anything from numbers, words, symbols, or even other sets.
- The objects in a set are called elements or members of the set. We use curly braces { } to enclose the elements of a set, and separate them by commas. For example, {1, 2, 3} is a set with three elements: 1, 2, and 3.
- We can also use a rule or a description to define a set, as long as it is clear and unambiguous. For example, {x | x is an even integer} is a set of all even integers, and {x | x is a vowel} is a set of all vowels.
- We can use the symbol ∈ to denote that an object is an element of a set, and the symbol ∉ to denote that an object is not an element of a set. For example, 2 ∈ {1, 2, 3} and 4 ∉ {1, 2, 3}.
- We can also use the symbol ⊆ to denote that a set is a subset of another set, meaning that every element of the first set is also an element of the second set. For example, {1, 2} ⊆ {1, 2, 3} and {a, e, i, o, u} ⊆ {x | x is a vowel}.
- A set that has no elements is called the empty set, and is denoted by ∅ or { }. For example, {x | x is an odd number and x is even} is the empty set, because there is no such number that satisfies both conditions.
- A set that contains all the elements of interest in a given context is called the universal set, and is usually denoted by U. For example, if we are studying the natural numbers, we can take U = {1, 2, 3, ...}.
- Set theory is useful for studying various concepts and operations in discrete mathematics, such as logic, relations, functions, algorithms, and graphs. It also provides a foundation for more advanced topics, such as number theory, combinatorics, and cryptography.



# Combination of sets

- A combination of sets is a new set that is formed by applying some operation on two or more existing sets.
- There are four basic operations on sets: union, intersection, difference, and complement.
- The union of two sets A and B, denoted by A ∪ B, is the set of all elements that belong to either A or B or both.
- The intersection of two sets A and B, denoted by A ∩ B, is the set of all elements that belong to both A and B.
- The difference of two sets A and B, denoted by A - B, is the set of all elements that belong to A but not to B.
- The complement of a set A, denoted by A', is the set of all elements that do not belong to A.
- The following Venn diagrams illustrate these operations:

Venn diagrams of set operations

- Some properties of these operations are:

  - Commutative laws: A ∪ B = B ∪ A and A ∩ B = B ∩ A
  - Associative laws: (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C)
  - Distributive laws: A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
  - De Morgan's laws: (A ∪ B)' = A' ∩ B' and (A ∩ B)' = A' ∪ B'
  - Identity laws: A ∪ ∅ = A and A ∩ U = A, where ∅ is the empty set and U is the universal set
  - Complement laws: A ∪ A' = U and A ∩ A' = ∅
  - Idempotent laws: A ∪ A = A and A ∩ A = A
  - Absorption laws: A ∪ (A ∩ B) = A and A ∩ (A ∪ B) = A
  - Domination laws: A ∪ U = U and A ∩ ∅ = ∅
  - Double complement law: (A')' = A

- A subset of a set A is a set that contains only elements of A. A proper subset of A is a subset that is not equal to A. The notation A ⊆ B means that A is a subset of B, and A ⊂ B means that A is a proper subset of B.
- The power set of a set A, denoted by P(A), is the set of all subsets of A. For example, if A = {a, b, c}, then P(A) = {∅, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}}.
- The cardinality of a set A, denoted by |A|, is the number of elements in A. For example, |{a, b, c}| = 3. The cardinality of the power set of A is 2^|A|. For example, |P({a, b, c})| = 2^3 = 8.



# Multisets

- A multiset is a collection of objects that allows repetition, unlike a set.
- A multiset can be represented by listing its elements within curly braces, with the number of repetitions indicated by a superscript. For example, {a, b, b, c, c, c} can be written as {a, b^2, c^3}.
- A multiset can also be represented by a function that maps each element to its multiplicity, which is the number of times it appears in the multiset. For example, the function f defined by f(a) = 1, f(b) = 2, f(c) = 3, and f(x) = 0 for all other x, represents the same multiset as {a, b^2, c^3}.
- The cardinality of a multiset is the sum of the multiplicities of its elements. For example, the cardinality of {a, b^2, c^3} is 1 + 2 + 3 = 6.
- Two multisets are equal if they have the same elements with the same multiplicities. For example, {a, b^2, c^3} = {b, c, c, a, b, c}.
- The union of two multisets is the multiset that contains each element as many times as it appears in either multiset. For example, {a, b^2, c^3} ∪ {b, c^2, d} = {a, b^3, c^5, d}.
- The intersection of two multisets is the multiset that contains each element as many times as it appears in both multisets. For example, {a, b^2, c^3} ∩ {b, c^2, d} = {b, c^2}.
- The difference of two multisets is the multiset that contains each element as many times as it appears in the first multiset minus the number of times it appears in the second multiset. For example, {a, b^2, c^3} - {b, c^2, d} = {a, b, c}. If the difference is negative, the element is omitted. For example, {b, c^2, d} - {a, b^2, c^3} = {d}.
- The subset relation for multisets is defined as follows: A multiset A is a subset of a multiset B if for every element x, the multiplicity of x in A is less than or equal to the multiplicity of x in B. For example, {a, b} is a subset of {a, b^2, c^3}, but {a, b^2} is not.



# Ordered pairs for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- An ordered pair is a pair of elements where the order matters. For example, (1, 2) is different from (2, 1).
- An ordered pair can be written as (a, b) where a is the first element and b is the second element.
- An ordered pair can also be represented by a point on a Cartesian plane, where the first element is the x-coordinate and the second element is the y-coordinate. For example, (3, 4) is the point (3, 4) on the plane.
- The set of all ordered pairs of a given type is called a Cartesian product. For example, the Cartesian product of two sets A and B is the set of all ordered pairs (a, b) where a belongs to A and b belongs to B. It is denoted by A x B.
- The Cartesian product of two sets can be visualized by a table or a grid, where each row corresponds to an element of the first set and each column corresponds to an element of the second set. The ordered pairs are the cells of the table or the grid. For example, if A = {1, 2, 3} and B = {a, b}, then A x B = {(1, a), (1, b), (2, a), (2, b), (3, a), (3, b)} and the table is:

|   | a | b |
|---|---|---|
| 1 |(1, a)|(1, b)|
| 2 |(2, a)|(2, b)|
| 3 |(3, a)|(3, b)|

- The Cartesian product of two sets is not commutative, meaning that A x B is not the same as B x A. For example, if A = {1, 2} and B = {a, b, c}, then A x B = {(1, a), (1, b), (1, c), (2, a), (2, b), (2, c)} and B x A = {(a, 1), (a, 2), (b, 1), (b, 2), (c, 1), (c, 2)}. The tables are:

|   | a | b | c |
|---|---|---|---|
| 1 |(1, a)|(1, b)|(1, c)|
| 2 |(2, a)|(2, b)|(2, c)|

|   | 1 | 2 |
|---|---|---|
| a |(a, 1)|(a, 2)|
| b |(b, 1)|(b, 2)|
| c |(c, 1)|(c, 2)|

- The Cartesian product of more than two sets can be defined recursively by using the Cartesian product of two sets. For example, the Cartesian product of three sets A, B, and C is the set of all ordered pairs (a, b, c) where a belongs to A, b belongs to B, and c belongs to C. It is denoted by A x B x C. It can also be written as (A x B) x C or A x (B x C), since the order of the sets does not matter. For example, if A = {1, 2}, B = {a, b}, and C = {x, y}, then A x B x C = {(1, a, x), (1, a, y), (1, b, x), (1, b, y), (2, a, x), (2, a, y), (2, b, x), (2, b, y)}. The table is:

|   | a | b |
|---|---|---|
| 1 |(1, a)|(1, b)|
| 2 |(2, a)|(2, b)|

|   | x | y |
|---|---|---|
|(1, a)|(1, a, x)|(1, a, y)|
|(1, b)|(1, b, x)|(1, b, y)|
|(2, a)|(2, a, x)|(2, a, y)|
|(2, b)|(2, b, x)|(2, b, y)|

- The Cartesian product of n sets can be generalized by using the notation A1 x A2 x ... x An, where Ai is the



Hello, I am Sydney, your AI assistant. I can help you with your study material on proofs of some general identities on sets. Here is some content in markdown format that you can use for your notes.

# Proofs of some general identities on sets

## Commutative laws

- The commutative laws state that for any sets A and B, A ∪ B = B ∪ A and A ∩ B = B ∩ A. That is, the order of the sets does not matter when performing union or intersection operations.
- To prove the commutative laws, we can use the element method, which involves showing that any element that belongs to one set also belongs to the other set, and vice versa.
- For example, to prove that A ∪ B = B ∪ A, we can do the following:

  - Let x be any element of A ∪ B. Then, by definition of union, x ∈ A or x ∈ B (or both).
  - If x ∈ A, then x ∈ B ∪ A by definition of union. Similarly, if x ∈ B, then x ∈ B ∪ A by definition of union. Therefore, x ∈ B ∪ A in either case.
  - Hence, A ∪ B ⊆ B ∪ A, since every element of A ∪ B is also an element of B ∪ A.
  - Similarly, let y be any element of B ∪ A. Then, by definition of union, y ∈ B or y ∈ A (or both).
  - If y ∈ B, then y ∈ A ∪ B by definition of union. Similarly, if y ∈ A, then y ∈ A ∪ B by definition of union. Therefore, y ∈ A ∪ B in either case.
  - Hence, B ∪ A ⊆ A ∪ B, since every element of B ∪ A is also an element of A ∪ B.
  - Therefore, A ∪ B = B ∪ A, since they are subsets of each other.

- The proof of A ∩ B = B ∩ A is similar, except that we use the definition of intersection instead of union.

## Associative laws

- The associative laws state that for any sets A, B, and C, (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C). That is, the grouping of the sets does not matter when performing union or intersection operations.
- To prove the associative laws, we can use the element method again, by showing that any element that belongs to one set also belongs to the other set, and vice versa.
- For example, to prove that (A ∪ B) ∪ C = A ∪ (B ∪ C), we can do the following:

  - Let x be any element of (A ∪ B) ∪ C. Then, by definition of union, x ∈ A ∪ B or x ∈ C (or both).
  - If x ∈ A ∪ B, then by definition of union, x ∈ A or x ∈ B (or both). Therefore, x ∈ A or x ∈ B ∪ C (or both) by definition of union. Hence, x ∈ A ∪ (B ∪ C) by definition of union.
  - If x ∈ C, then x ∈ B ∪ C by definition of union. Therefore, x ∈ A or x ∈ B ∪ C (or both) by definition of union. Hence, x ∈ A ∪ (B ∪ C) by definition of union.
  - Therefore, x ∈ A ∪ (B ∪ C) in either case.
  - Hence, (A ∪ B) ∪ C ⊆ A ∪ (B ∪ C), since every element of (A ∪ B) ∪ C is also an element of A ∪ (B ∪ C).
  - Similarly, let y be any element of A ∪ (B ∪ C). Then, by definition of union, y ∈ A or y ∈ B ∪ C (or both).
  - If y ∈ A, then y ∈ A ∪ B by definition of union. Therefore, y ∈ A ∪ B or y ∈ C (or both) by definition of union. Hence, y ∈ (A ∪ B) ∪ C by definition of union.
  - If y ∈ B ∪ C, then by definition of union, y ∈ B or y ∈ C (or both). Therefore, y ∈ A ∪ B or y ∈ C (or both) by definition of union.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic.

# Relations

- A relation R from a set A to a set B is a subset of the Cartesian product A x B.
- A relation R on a set A is a relation from A to A, or a subset of A x A.
- A relation R on a set A can be represented by a directed graph, where the vertices are the elements of A and the edges are the ordered pairs in R.
- A relation R on a set A can also be represented by a matrix, where the rows and columns are indexed by the elements of A and the entry at row i and column j is 1 if (i, j) is in R and 0 otherwise.
- A relation R on a set A is called reflexive if (a, a) is in R for every a in A.
- A relation R on a set A is called symmetric if (a, b) is in R implies (b, a) is in R for every a, b in A.
- A relation R on a set A is called antisymmetric if (a, b) is in R and (b, a) is in R implies a = b for every a, b in A.
- A relation R on a set A is called transitive if (a, b) is in R and (b, c) is in R implies (a, c) is in R for every a, b, c in A.
- A relation R on a set A is called an equivalence relation if it is reflexive, symmetric and transitive.
- An equivalence relation R on a set A partitions A into disjoint subsets called equivalence classes, where two elements are in the same equivalence class if and only if they are related by R.
- A relation R on a set A is called a partial order if it is reflexive, antisymmetric and transitive.
- A partial order R on a set A can be represented by a Hasse diagram, which is a directed graph where the edges are the minimal pairs in R and the vertices are arranged such that if (a, b) is in R, then a is below b.
- A set A with a partial order R is called a partially ordered set or a poset, denoted by (A, R).
- A poset (A, R) is called a total order or a linear order if for every a, b in A, either (a, b) is in R or (b, a) is in R.
- A poset (A, R) is called a well-order if it is a total order and every non-empty subset of A has a least element with respect to R.
- A poset (A, R) is called a lattice if for every a, b in A, there exist a least upper bound and a greatest lower bound of {a, b} with respect to R, denoted by a ∨ b and a ∧ b respectively.
- A lattice (A, R) is called a distributive lattice if for every a, b, c in A, the following distributive laws hold: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) and a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c).
- A lattice (A, R) is called a Boolean algebra if it is a distributive lattice and there exist a least element 0 and a greatest element 1 in A such that for every a in A, there exists a complement ¬a in A such that a ∨ ¬a = 1 and a ∧ ¬a = 0.
- A Boolean algebra (A, R) can be represented by a Boolean expression, which is a combination of elements of A and the operators ∨, ∧ and ¬, and parentheses. A Boolean expression can be simplified using the following rules:

  - Identity laws: a ∨ 0 = a and a ∧ 1 = a
  - Domination laws: a ∨ 1 = 1 and a ∧ 0 = 0
  - Idempotent laws: a ∨ a = a and a ∧ a = a
  - Commutative laws: a ∨ b = b ∨ a and a ∧ b = b ∧ a
  - Associative laws: (a ∨ b) ∨ c = a ∨ (b ∨ c) and (a ∧ b) ∧ c = a ∧ (b ∧ c



# Unit 1 - Set Theory

## Definition

- Set theory is the branch of mathematics that deals with the properties of well-defined collections of objects, which may or may not be of a mathematical nature, such as numbers or functions .
- Set theory is also the basis for precise and adaptable terminology for the definition of complex and abstract concepts in mathematics and logic.
- Set theory can be informally described as the study of sets, which can be collections of any kind of objects, but set theory as a branch of mathematics is mostly concerned with those that are relevant to mathematics as a whole.
- Set theory is also the branch of mathematical logic that studies the formal properties of sets as units and the expression of other branches of mathematics in terms of sets.



# Operations on relations

- A relation is a subset of a Cartesian product of two or more sets. For example, if A = {1, 2, 3} and B = {a, b, c}, then a possible relation R from A to B is R = {(1, a), (2, b), (3, c)}.
- There are different types of operations that can be performed on relations, such as union, intersection, complement, inverse, composition, and power.
- The union of two relations R and S from A to B is the relation that contains all the ordered pairs that are in either R or S. For example, if R = {(1, a), (2, b)} and S = {(2, c), (3, a)}, then R ∪ S = {(1, a), (2, b), (2, c), (3, a)}.
- The intersection of two relations R and S from A to B is the relation that contains all the ordered pairs that are in both R and S. For example, if R = {(1, a), (2, b)} and S = {(2, b), (3, a)}, then R ∩ S = {(2, b)}.
- The complement of a relation R from A to B is the relation that contains all the ordered pairs from A × B that are not in R. For example, if R = {(1, a), (2, b)} and A = {1, 2, 3} and B = {a, b, c}, then R' = {(1, b), (1, c), (2, a), (2, c), (3, a), (3, b), (3, c)}.
- The inverse of a relation R from A to B is the relation that contains all the ordered pairs from B × A that are obtained by reversing the order of the elements in R. For example, if R = {(1, a), (2, b)}, then R^-1 = {(a, 1), (b, 2)}.
- The composition of two relations R from A to B and S from B to C is the relation that contains all the ordered pairs (a, c) such that there exists an element b in B for which (a, b) is in R and (b, c) is in S. For example, if R = {(1, a), (2, b)} and S = {(a, x), (b, y)}, then R ∘ S = {(1, x), (2, y)}.
- The power of a relation R from A to A is the relation that contains all the ordered pairs (a, b) such that there exists a sequence of elements a1, a2, ..., an in A for which a = a1, b = an, and (ai, ai+1) is in R for all i from 1 to n-1. For example, if R = {(1, 2), (2, 3), (3, 1)}, then R^2 = {(1, 3), (2, 1), (3, 2)} and R^3 = {(1, 1), (2, 2), (3, 3)}.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some properties of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic.

# Properties of relations

- A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself.
- A relation R on a set A can have some properties that describe how the elements of A are related to each other. Some common properties are:

  - Reflexive: A relation R on a set A is reflexive if for every element a in A, (a, a) is in R. This means that every element is related to itself.
  - Symmetric: A relation R on a set A is symmetric if for every pair of elements (a, b) in R, (b, a) is also in R. This means that the order of the elements does not matter.
  - Transitive: A relation R on a set A is transitive if for every pair of elements (a, b) and (b, c) in R, (a, c) is also in R. This means that if a is related to b and b is related to c, then a is related to c.
  - Antisymmetric: A relation R on a set A is antisymmetric if for every pair of elements (a, b) and (b, a) in R, a = b. This means that the only way for two elements to be related in both directions is if they are equal.
  - Irreflexive: A relation R on a set A is irreflexive if for every element a in A, (a, a) is not in R. This means that no element is related to itself.
  - Asymmetric: A relation R on a set A is asymmetric if for every pair of elements (a, b) in R, (b, a) is not in R. This means that the order of the elements matters and no element is related to itself.
  - Equivalence: A relation R on a set A is an equivalence relation if it is reflexive, symmetric and transitive. This means that it partitions A into disjoint subsets called equivalence classes, where two elements are in the same class if and only if they are related by R.
  - Partial order: A relation R on a set A is a partial order if it is reflexive, antisymmetric and transitive. This means that it imposes a hierarchy on A, where some elements are comparable and some are not, and there is no circularity in the comparison.
  - Total order: A relation R on a set A is a total order if it is a partial order and for every pair of elements a and b in A, either (a, b) or (b, a) is in R. This means that it imposes a linear order on A, where every element is comparable to every other element.

- A relation R on a set A can be represented by a matrix, a table, a graph or a digraph, depending on the context and the purpose of the representation. A matrix is a two-dimensional array of 0s and 1s, where the rows and columns correspond to the elements of A, and the entry at row i and column j is 1 if and only if (a_i, a_j) is in R. A table is a list of ordered pairs that belong to R. A graph is a set of vertices and edges, where the vertices correspond to the elements of A, and there is an edge between two vertices if and only if they are related by R. A digraph is a graph with directed edges, where the direction of the edge indicates the order of the elements in the relation.



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



# Equality of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself.
- Two relations R and S on a set A are equal if and only if R and S are subsets of each other, that is, R ⊆ S and S ⊆ R.
- This means that R and S have exactly the same ordered pairs in A x A.
- For example, let A = {1, 2, 3} and let R = {(1, 1), (2, 2), (3, 3)} and S = {(x, x) | x ∈ A}. Then R and S are equal relations on A, since they both contain the same diagonal elements of A x A.
- Another way to check if two relations are equal is to use their matrix representations. A relation R on a set A can be represented by a matrix M_R with rows and columns indexed by the elements of A, such that M_R[i, j] = 1 if (i, j) ∈ R and M_R[i, j] = 0 otherwise.
- Two relations R and S on a set A are equal if and only if their matrices M_R and M_S are identical, that is, M_R[i, j] = M_S[i, j] for all i, j ∈ A.
- For example, let A = {a, b, c} and let R = {(a, a), (b, b), (c, c), (a, b), (b, a)} and S = {(x, y) | x = y or x and y are adjacent in the alphabet}. Then R and S are equal relations on A, since their matrices are:

|   | a | b | c |
|---|---|---|---|
| a | 1 | 1 | 0 |
| b | 1 | 1 | 0 |
| c | 0 | 0 | 1 |

- Note that the order of the elements in A does not affect the equality of the relations, as long as the same order is used for both rows and columns of the matrices.



# Recursive definition of relation

A relation is a set of ordered pairs that satisfies some property. A recursive definition of a relation is a way of specifying a relation by giving a rule that generates the next element of the relation from the previous ones. A recursive definition consists of two parts:

- A **base case** that specifies one or more initial elements of the relation.
- A **recursive step** that specifies how to obtain new elements of the relation from the existing ones.

For example, consider the relation R on the set of natural numbers N, defined as follows:

- (0,0) ∈ R (base case)
- If (x,y) ∈ R, then (x+1,y+1) ∈ R and (x+2,y) ∈ R (recursive step)

This relation can be visualized as a tree, where each node represents an ordered pair in R, and each edge represents an application of the recursive step:

tree

Some properties of recursive definitions of relations are:

- A recursive definition may not generate all the elements of a relation, but only a subset of it. For example, the recursive definition above does not generate the pair (1,0), even though it belongs to the relation R.
- A recursive definition may generate the same element more than once, but this does not affect the relation. For example, the recursive definition above generates the pair (2,1) twice, but this does not change the fact that (2,1) ∈ R.
- A recursive definition may not terminate, meaning that there is no finite way of listing all the elements of the relation. For example, the recursive definition above does not terminate, because there is always a way to generate a new element from an existing one.



# Order of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself.
- A relation R on a set A can be represented by a matrix, a directed graph, or a table.
- A relation R on a set A is called reflexive if (a, a) ∈ R for every a ∈ A.
- A relation R on a set A is called symmetric if (a, b) ∈ R implies (b, a) ∈ R for every a, b ∈ A.
- A relation R on a set A is called antisymmetric if (a, b) ∈ R and (b, a) ∈ R imply a = b for every a, b ∈ A.
- A relation R on a set A is called transitive if (a, b) ∈ R and (b, c) ∈ R imply (a, c) ∈ R for every a, b, c ∈ A.
- A relation R on a set A is called an equivalence relation if it is reflexive, symmetric, and transitive.
- An equivalence relation R on a set A partitions A into disjoint subsets called equivalence classes, where two elements belong to the same equivalence class if and only if they are related by R.
- A relation R on a set A is called a partial order if it is reflexive, antisymmetric, and transitive.
- A partial order R on a set A is called a total order or a linear order if for every a, b ∈ A, either (a, b) ∈ R or (b, a) ∈ R or both.
- A partial order R on a set A is called a well-order if every nonempty subset of A has a least element with respect to R.
- A relation R on a set A is called a function if for every a ∈ A, there is exactly one b ∈ A such that (a, b) ∈ R.
- A function f: A -> B is a relation from A to B such that for every a ∈ A, there is exactly one b ∈ B such that (a, b) ∈ f.
- A function f: A -> B is called injective or one-to-one if f(a) = f(b) implies a = b for every a, b ∈ A.
- A function f: A -> B is called surjective or onto if for every b ∈ B, there is some a ∈ A such that f(a) = b.
- A function f: A -> B is called bijective or one-to-one and onto if it is both injective and surjective.
- The inverse of a bijective function f: A -> B is a function f^-1: B -> A such that f^-1(f(a)) = a for every a ∈ A and f(f^-1(b)) = b for every b ∈ B.
- A function f: A -> B is called increasing if a < b implies f(a) < f(b) for every a, b ∈ A.
- A function f: A -> B is called decreasing if a < b implies f(a) > f(b) for every a, b ∈ A.
- A function f: A -> B is called monotonic if it is either increasing or decreasing.



# Functions

A function is a special kind of relation between two sets, such that each element of the first set is related to exactly one element of the second set. A function can be seen as a rule that assigns an output to an input, or as a mapping from one set to another.

## Definition of a function

Formally, a function f from a set A to a set B is a subset of the Cartesian product A x B, such that for every element a in A, there exists a unique element b in B such that (a, b) belongs to f. The set A is called the domain of f, and the set B is called the codomain of f. The element b is called the image of a under f, and the element a is called the preimage of b under f. The set of all images of elements in A under f is called the range of f, and it is a subset of B.

## Notation of a function

There are different ways to denote a function, depending on the context and the level of detail. Some common notations are:

- f: A -> B, which means that f is a function from A to B.
- f(a) = b, which means that the image of a under f is b.
- f = {(a, b) | a in A and b in B and some condition on a and b}, which means that f is the set of ordered pairs that satisfy some condition.
- f(x) = some expression involving x, which means that f is a function that assigns an output to an input according to some formula.

## Examples of functions

Some examples of functions are:

- The identity function, which maps every element to itself: id: A -> A, id(a) = a for all a in A.
- The constant function, which maps every element to the same value: c: A -> B, c(a) = b for some fixed b in B and all a in A.
- The successor function, which maps every natural number to its next number: s: N -> N, s(n) = n + 1 for all n in N.
- The square function, which maps every real number to its square: sq: R -> R, sq(x) = x^2 for all x in R.
- The sine function, which maps every real number to its sine value: sin: R -> [-1, 1], sin(x) = the sine of x for all x in R.



# Definition for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A **set** is a collection of distinct objects, called **elements** or **members** of the set.
- A set can be defined by listing its elements between braces, such as {1, 2, 3}, or by using a rule or a description, such as {x | x is an even positive integer less than 10}.
- Two sets are **equal** if they have exactly the same elements, regardless of the order or repetition of the elements.
- A set is a **subset** of another set if every element of the first set is also an element of the second set. The notation A ⊆ B means that A is a subset of B. Every set is a subset of itself, and the empty set is a subset of any set.
- A set is a **proper subset** of another set if it is a subset of the second set and it is not equal to the second set. The notation A ⊂ B means that A is a proper subset of B.
- The **union** of two sets A and B, denoted by A ∪ B, is the set of all elements that belong to either A or B or both.
- The **intersection** of two sets A and B, denoted by A ∩ B, is the set of all elements that belong to both A and B.
- The **difference** of two sets A and B, denoted by A - B, is the set of all elements that belong to A but not to B.
- The **complement** of a set A, denoted by A^c, is the set of all elements that do not belong to A. The complement of A is relative to some universal set U, which contains all the elements under consideration.
- Two sets are **disjoint** if they have no elements in common, that is, if their intersection is the empty set.
- The **cardinality** of a set A, denoted by |A|, is the number of elements in A. The cardinality of the empty set is zero.
- A set is **finite** if it has a finite number of elements, and **infinite** otherwise. A set is **countable** if it is either finite or has the same cardinality as the set of natural numbers. A set is **uncountable** if it is neither finite nor countable.
- A **partition** of a set A is a collection of nonempty, disjoint subsets of A whose union is A.
- A **Venn diagram** is a graphical representation of sets using circles or other shapes. The universal set is represented by a rectangle, and each set is represented by a region inside the rectangle. The regions are arranged to show the relationships between the sets, such as their union, intersection, difference, and complement.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of classification of functions.

# Classification of functions

A function is a relation between two sets that assigns each element of the first set to exactly one element of the second set. The first set is called the domain and the second set is called the codomain. The set of all elements that are assigned by the function is called the range.

There are different ways to classify functions based on their properties. Some of the common classifications are:

- **Injective, surjective, and bijective functions:** These are functions that have different relationships between the domain and the range.

  - An injective function (also called one-to-one) is a function that maps distinct elements of the domain to distinct elements of the range. That is, no two different elements of the domain have the same image in the range. For example, the function f(x) = 2x + 1 is injective, because for any two different values of x, f(x) will be different.

  - A surjective function (also called onto) is a function that maps the domain onto the entire codomain. That is, every element of the codomain has at least one preimage in the domain. For example, the function f(x) = x^2 is surjective if the codomain is the set of non-negative real numbers, because every non-negative real number has a square root.

  - A bijective function (also called one-to-one and onto) is a function that is both injective and surjective. That is, it maps distinct elements of the domain to distinct elements of the codomain, and covers the entire codomain. For example, the function f(x) = x + 1 is bijective, because for any two different values of x, f(x) will be different, and for any value of y, there is a unique value of x such that f(x) = y.

- **Inverse functions:** An inverse function is a function that reverses the effect of another function. If f is a function from A to B, then the inverse function of f, denoted by f^-1, is a function from B to A such that f^-1(f(x)) = x for all x in A, and f(f^-1(y)) = y for all y in B. Not every function has an inverse function, but only bijective functions do. For example, the function f(x) = x + 1 has an inverse function f^-1(x) = x - 1, but the function f(x) = x^2 does not have an inverse function, because it is not bijective.

- **Polynomial functions:** A polynomial function is a function that can be written as a sum of terms of the form ax^n, where a is a constant and n is a non-negative integer. For example, the function f(x) = 3x^2 + 2x - 5 is a polynomial function of degree 2, because the highest power of x is 2. Polynomial functions have many properties, such as being continuous, differentiable, and having finite roots.

- **Rational functions:** A rational function is a function that can be written as a ratio of two polynomial functions. For example, the function f(x) = (x^2 + 1) / (x - 2) is a rational function, because both the numerator and the denominator are polynomial functions. Rational functions have asymptotes, which are lines or curves that the function approaches but never reaches.

- **Exponential and logarithmic functions:** An exponential function is a function of the form f(x) = a^x, where a is a positive constant. For example, the function f(x) = 2^x is an exponential function with base 2. An exponential function grows or decays exponentially, depending on the value of the base. A logarithmic function is the inverse function of an exponential function. It is a function of the form f(x) = log_a(x), where a is a positive constant. For example, the function f(x) = log_2(x) is the inverse function of f(x) = 2^x. A logarithmic function grows or decays logarithmically, depending on the value of the base.

- **Trigonometric and inverse trigonometric functions:** A trigonometric function is a function that relates the angles and sides of a right triangle. The most common trigonometric functions are sine, cosine, and tangent, and their reciprocals, cosecant, secant, and cotangent. For example, the function f(x) = sin(x) is a trigonometric



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of operations on functions for the unit 1 - set theory in the subject of discrete structures and theory of logic.

# Operations on Functions

- A function is a relation that assigns to each element of a set A (called the domain) exactly one element of a set B (called the co-domain).
- A function can be represented by a set of ordered pairs, a table, a graph, or an algebraic expression.
- The notation f: A -> B means that f is a function from A to B.
- The notation f(a) = b means that b is the value of the function f at a, or the image of a under f.
- The notation f(A) = {f(a) | a in A} means the image of the set A under f, or the set of all values of f at elements of A.
- The notation f^-1(b) = {a in A | f(a) = b} means the pre-image of b under f, or the set of all elements of A that are mapped to b by f.
- The notation f^-1(B) = {a in A | f(a) in B} means the pre-image of the set B under f, or the set of all elements of A that are mapped to elements of B by f.

## Operations on Functions

- There are four main operations on functions: composition, inverse, restriction, and extension.
- The composition of two functions f: A -> B and g: B -> C is a function g o f: A -> C that maps each element of A to the value of g at the value of f at that element. That is, (g o f)(a) = g(f(a)) for all a in A.
- The inverse of a function f: A -> B is a function f^-1: B -> A that maps each element of B to an element of A that is mapped to it by f. That is, f^-1(b) = a if and only if f(a) = b for some a in A. A function is invertible if and only if it is one-to-one and onto, meaning that it maps different elements of A to different elements of B, and it maps every element of B to some element of A.
- The restriction of a function f: A -> B to a subset C of A is a function f|C: C -> B that maps each element of C to the same value as f. That is, f|C(c) = f(c) for all c in C. The restriction of f to C is also a function from C to f(C), the image of C under f.
- The extension of a function f: A -> B to a superset D of A is a function f': D -> B that maps each element of D to the same value as f if it is in A, and to some arbitrary value otherwise. That is, f'(d) = f(d) if d in A, and f'(d) = b for some b in B if d not in A. The extension of f to D is not unique, as there may be more than one way to assign values to elements of D that are not in A.



# Recursively defined functions

- A recursively defined function is a function that its value at any point can be calculated from the values of the function at some previous points.
- A recursive definition of a function consists of two steps:
  - Basis step: Specify the value of the function at zero or some other initial value.
  - Recursive step: Give a rule for finding its value at an integer from its values at smaller integers.
- For example, suppose a function f(k) = f(k-2) + f(k-3) which is defined over non-negative integers. If we have the value of the function at k = 0 and k = 2, we can also find its value at any other non-negative integer.
- Another example is the factorial function, which is defined as n! = n * (n-1)!, with the basis step of 0! = 1.
- Recursively defined functions can be used to model various phenomena, such as sequences, trees, algorithms, and grammars.
- Recursively defined functions can also be converted to explicit formulas using techniques such as generating functions. A generating function is a formal power series that encodes the values of a sequence as coefficients of the series. By manipulating the generating function, we can find an explicit formula for the sequence.



# Growth of Functions

- The growth of a function is a measure of how fast its value increases as the input value increases.
- The growth of a function is important for analyzing the efficiency and complexity of algorithms, as well as the asymptotic behavior of sequences and series.
- The growth of a function is determined by the highest order term: if you add a bunch of terms, the function grows about as fast as the largest term (for large enough input values).
- For example, f(x) = x^2 + 1 grows as fast as g(x) = x^2 + 2 and h(x) = x^2 + x + 1, because for large x, x^2 is much bigger than 1, 2, or x + 1.
- The growth of functions is often described using a special notation – the Big-O Notation, Big-Omega Notation, and Big-Theta Notation. These special notations estimate the growth of the function by comparing it to another simpler function.
- Big-O Notation: f(x) is O(g(x)) if there are constants C and k such that |f(x)| <= C|g(x)| whenever x > k. In other words, Big-O is the upper bound for the growth of the function.
- Big-Omega Notation: f(x) is Omega(g(x)) if there are constants C and k such that |f(x)| >= C|g(x)| whenever x > k. In other words, Big-Omega is the lower bound for the growth of the function.
- Big-Theta Notation: f(x) is Theta(g(x)) if there are constants C1, C2 and k such that C1|g(x)| <= |f(x)| <= C2|g(x)| whenever x > k. In other words, Big-Theta is the tight bound for the growth of the function.
- For example, f(x) = 3x^2 + 5 is O(x^2), Omega(x^2), and Theta(x^2), because we can choose C = 8, k = 1 for Big-O, C = 2, k = 1 for Big-Omega, and C1 = 2, C2 = 8, k = 1 for Big-Theta.
- Some common classes of functions and their growth rates are:

| Class | Example | Growth Rate |
| --- | --- | --- |
| Constant | f(x) = 5 | O(1) |
| Logarithmic | f(x) = log x | O(log x) |
| Linear | f(x) = 3x + 2 | O(x) |
| Polynomial | f(x) = x^3 + 2x + 1 | O(x^n) |
| Exponential | f(x) = 2^x | O(a^x) |
| Factorial | f(x) = x! | O(x!) |

- The growth rate of a function can be used to compare the efficiency of different algorithms for solving the same problem. For example, an algorithm that runs in O(n) time is more efficient than an algorithm that runs in O(n^2) time, because the former grows slower than the latter as the input size n increases.



# Natural Numbers

- Natural numbers are the counting numbers, such as 1, 2, 3, 4, 5, etc.
- Natural numbers are denoted by the symbol **N**.
- Natural numbers are a subset of the integers, which are a subset of the rational numbers, which are a subset of the real numbers.
- Natural numbers have two basic operations: addition and multiplication, which are both associative, commutative, and have identity elements (0 and 1, respectively).
- Natural numbers also have an order relation, which is transitive, antisymmetric, and total.
- Natural numbers have some important properties, such as the well-ordering principle, the principle of mathematical induction, and the fundamental theorem of arithmetic.



# Introduction for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- Set theory is a branch of mathematics that studies collections of objects, called sets, and the relationships between them.
- Set theory is the foundation of many other branches of mathematics, such as logic, algebra, geometry, topology, and analysis.
- Set theory also has applications in computer science, such as data structures, algorithms, databases, and artificial intelligence.
- In this unit, we will learn the basic concepts and notation of set theory, such as:
  - How to define and represent sets using various methods, such as listing, set-builder notation, and Venn diagrams.
  - How to perform operations on sets, such as union, intersection, difference, complement, and Cartesian product.
  - How to compare sets using relations, such as subset, superset, equality, and inclusion-exclusion principle.
  - How to classify sets based on their size, such as finite, infinite, countable, and uncountable sets.
  - How to construct and analyze special sets, such as empty set, universal set, power set, and interval notation.
- By the end of this unit, you should be able to:
  - Understand and use the basic terminology and notation of set theory.
  - Perform and interpret various operations and relations on sets.
  - Apply set theory to solve problems in mathematics and computer science.



# Mathematical Induction

Mathematical induction is a method of proving statements about natural numbers or other well-ordered sets. It is based on two principles:

- **Base case:** The statement is true for the smallest or first element of the set, usually denoted by 1 or 0.
- **Inductive step:** If the statement is true for some element of the set, then it is also true for the next element of the set, usually denoted by n+1.

Using these two principles, we can show that the statement is true for all elements of the set, by starting from the base case and applying the inductive step repeatedly.

## Example

Let us use mathematical induction to prove that the sum of the first n natural numbers is n(n+1)/2, for all n ≥ 1.

- **Base case:** When n = 1, the sum of the first natural number is 1, and 1(1+1)/2 = 1, so the statement is true for n = 1.
- **Inductive step:** Assume that the statement is true for some n ≥ 1, that is, the sum of the first n natural numbers is n(n+1)/2. We want to show that the statement is also true for n+1, that is, the sum of the first n+1 natural numbers is (n+1)(n+2)/2. To do this, we add n+1 to both sides of the equation:

  n(n+1)/2 + n+1 = (n+1)(n+2)/2

  Simplifying the left-hand side, we get:

  (n^2 + n + 2n + 2)/2 = (n+1)(n+2)/2

  Factoring out 2 from the numerator, we get:

  2(n^2 + 3n + 2)/2 = (n+1)(n+2)/2

  Cancelling out 2 from both sides, we get:

  n^2 + 3n + 2 = (n+1)(n+2)

  Expanding the right-hand side, we get:

  n^2 + 3n + 2 = n^2 + 3n + 2

  This shows that the statement is true for n+1, if it is true for n.

Therefore, by mathematical induction, the statement is true for all n ≥ 1.



# Variants of Induction

Induction is a proof technique that is used to show that a statement is true for all natural numbers or for all elements of a well-ordered set. The basic idea of induction is to start with a base case, where the statement is true for a specific value, and then show that if the statement is true for any value, it is also true for the next value. This way, we can infer that the statement is true for all values by a chain of logical implications.

There are different variants of induction that can be used for different purposes. Some of the common variants are:

- **Strong induction**: This is a variant of induction where we assume that the statement is true for all values up to and including a certain value, and then show that it is true for the next value. For example, to prove that every natural number greater than 1 is either prime or a product of primes, we can use strong induction as follows:

  - Base case: 2 is prime, so the statement is true for n = 2.
  - Inductive step: Assume that the statement is true for all natural numbers up to and including k, where k > 1. We want to show that it is true for k + 1. There are two cases:
    - Case 1: k + 1 is prime. Then the statement is trivially true for k + 1.
    - Case 2: k + 1 is not prime. Then k + 1 has a proper divisor d, where 1 < d < k + 1. By the inductive hypothesis, d and k + 1 / d are either prime or a product of primes. Therefore, k + 1 is also a product of primes, and the statement is true for k + 1.
  - Conclusion: By strong induction, the statement is true for all natural numbers greater than 1.

- **Structural induction**: This is a variant of induction that is used to prove statements about recursively defined structures, such as sets, sequences, trees, graphs, etc. The basic idea of structural induction is to show that the statement is true for the base cases of the structure, and then show that it is true for any complex case that is obtained by applying the recursive rules to the simpler cases. For example, to prove that the number of nodes in a binary tree is one more than the number of edges, we can use structural induction as follows:

  - Base case: A single node is a binary tree with no edges, so the statement is true for n = 1.
  - Inductive step: Assume that the statement is true for any binary tree with k nodes, where k > 0. We want to show that it is true for any binary tree with k + 1 nodes. There are two cases:
    - Case 1: The binary tree with k + 1 nodes is obtained by adding a left child to a node in a binary tree with k nodes. Then the number of edges in the new tree is one more than the number of edges in the original tree, and the number of nodes in the new tree is one more than the number of nodes in the original tree. Therefore, the statement is true for the new tree.
    - Case 2: The binary tree with k + 1 nodes is obtained by adding a right child to a node in a binary tree with k nodes. The argument is similar to case 1, and the statement is true for the new tree.
  - Conclusion: By structural induction, the statement is true for any binary tree.

- **Course-of-values induction**: This is a variant of induction that is used to prove statements about well-ordered sets that are not necessarily the natural numbers. The basic idea of course-of-values induction is to show that the statement is true for the least element of the set, and then show that if the statement is true for any element, it is also true for any greater element. For example, to prove that every non-empty subset of the natural numbers has a least element, we can use course-of-values induction as follows:

  - Base case: The set {1} is a non-empty subset of the natural numbers, and 1 is its least element, so the statement is true for {1}.
  - Inductive step: Assume that the statement is true for any non-empty subset of the natural numbers that has a least element k, where k > 1. We want to show that it is true for any non-empty subset of the natural numbers that has a least element greater than k. Let S



# Induction with Nonzero Base Cases

- Induction is a method of proving statements about natural numbers or other well-ordered sets by showing that a base case holds and that the statement is preserved by successor operations.
- The base case is the smallest or simplest instance of the statement that we want to prove. Usually, the base case is n = 0, but sometimes it can be a different value, such as n = 1 or n = 5.
- When the base case is not zero, we need to adjust the induction hypothesis and the induction step accordingly. For example, if we want to prove a statement for all n ≥ 5, we need to show that it holds for n = 5 (the base case) and that if it holds for some n ≥ 5, then it also holds for n + 1 (the induction step).
- Here is an example of a proof by induction with a nonzero base case:

  - Claim: For all n ≥ 5, n^2 < 2^n.
  - Proof: By induction on n.
    - Base case: If n = 5, then we have that 5^2 = 25 < 32 = 2^5, so the claim holds.
    - Induction step: Assume that for some n ≥ 5, n^2 < 2^n. Then we have that (n + 1)^2 = n^2 + 2n + 1. Since n ≥ 5, we have (n + 1)^2 = n^2 + 2n + 1 < n^2 + 2n + n (since 1 < 5 ≤ n) = n^2 + 3n < n^2 + n^2 (since 3n < 5n ≤ n^2) = 2n^2 < 2^n * 2 = 2^(n + 1). Therefore, the claim also holds for n + 1. By induction, the claim holds for all n ≥ 5. QED.



# Proof Methods for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A proof is a logical argument that establishes the validity of a statement or a theorem using a set of axioms, definitions, and rules of inference.
- There are different methods of proof that can be used depending on the type and structure of the statement or theorem.
- Some of the common proof methods for discrete structures are:

  - **Direct proof**: This method is used to prove statements of the form "If P, then Q", where P and Q are propositions. The steps are:
    - Assume that P is true.
    - Use logical reasoning and known facts to show that Q must also be true.
    - Conclude that "If P, then Q" is true.
  - **Indirect proof** or **proof by contradiction**: This method is used to prove statements of the form "If P, then Q", where P and Q are propositions. The steps are:
    - Assume that P is true and Q is false.
    - Use logical reasoning and known facts to show that this assumption leads to a contradiction of some premise, theorem, or basic truth.
    - Conclude that the assumption is false, and therefore "If P, then Q" is true.
  - **Proof by contrapositive**: This method is used to prove statements of the form "If P, then Q", where P and Q are propositions. The steps are:
    - Use the logical equivalence of "If P, then Q" and "If not Q, then not P".
    - Prove "If not Q, then not P" by direct proof or by contradiction.
    - Conclude that "If P, then Q" is true.
  - **Proof by cases**: This method is used to prove statements of the form "P implies Q", where P and Q are propositions. The steps are:
    - Identify all the possible cases or subcases that cover the domain of P.
    - Prove that Q is true for each case or subcase by direct proof or by contradiction.
    - Conclude that "P implies Q" is true.
  - **Proof by mathematical induction**: This method is used to prove statements of the form "For all natural numbers n, P(n) is true", where P(n) is a proposition involving n. The steps are:
    - Prove that P(1) is true. This is called the base case.
    - Assume that P(k) is true for some arbitrary natural number k. This is called the induction hypothesis.
    - Use logical reasoning and known facts to show that P(k+1) must also be true. This is called the induction step.
    - Conclude that "For all natural numbers n, P(n) is true" by the principle of mathematical induction.
  - **Proof by set operations**: This method is used to prove statements involving sets, such as equality, inclusion, or intersection. The steps are:
    - Use the definitions of set operations and the properties of sets to manipulate the given sets.
    - Use logical reasoning and known facts to show that the resulting sets are equal or have the desired property.
    - Conclude that the statement involving sets is true.

- These are some of the proof methods for discrete structures. There may be other methods or variations of these methods depending on the context and the level of rigor required. The choice of the proof method depends on the nature and complexity of the statement or theorem to be proved.



Hello, I am Sydney, your AI assistant. I can help you with your topic of proof by counter-example for the notes of the unit 1 - set theory in the subject of discrete structures and theory of logic. Here is some content that you can use for your notes:

# Proof by counter-example

- A proof by counter-example is a method of disproving a statement by showing that there exists a specific case where the statement is false.
- A counter-example is a specific instance of the statement that contradicts the statement.
- To prove by counter-example, we need to find a counter-example that satisfies the hypothesis of the statement but violates the conclusion of the statement.
- A proof by counter-example can only be used to disprove a universal statement, such as "for all x, P(x)" or "for every x, P(x)".
- A proof by counter-example cannot be used to prove an existential statement, such as "there exists x such that P(x)" or "some x satisfies P(x)".
- A proof by counter-example is also called an indirect proof or a proof by contradiction.

## Example 1

- Statement: For all natural numbers n, n^2 + n + 41 is a prime number.
- Counter-example: Let n = 40. Then n^2 + n + 41 = 40^2 + 40 + 41 = 1681, which is not a prime number, since it is divisible by 41. Therefore, the statement is false.
- Explanation: We have found a specific value of n that satisfies the hypothesis (n is a natural number) but violates the conclusion (n^2 + n + 41 is a prime number). This is a counter-example that disproves the statement.

## Example 2

- Statement: For all real numbers x, x^2 >= 0.
- Counter-example: None. The statement is true.
- Explanation: We cannot find a specific value of x that satisfies the hypothesis (x is a real number) but violates the conclusion (x^2 >= 0). This is because the conclusion is always true for any real number x. Therefore, there is no counter-example that disproves the statement.



# Proof by contradiction

- Proof by contradiction is a method of proving a statement by assuming that it is false and deriving a contradiction from that assumption.
- The contradiction can be either a logical inconsistency or a violation of a known fact or theorem.
- The contradiction shows that the assumption was wrong, and therefore the statement is true.
- Proof by contradiction is also known as indirect proof or reductio ad absurdum (Latin for "reduction to absurdity").
- Proof by contradiction can be used to prove any kind of statement, but it is especially useful for proving the non-existence or impossibility of something.

## Example of proof by contradiction

- Suppose we want to prove that √2 is irrational, i.e., it cannot be written as a fraction of two integers.
- We assume the opposite, i.e., that √2 is rational, and write it as a fraction of two integers a and b in lowest terms, i.e., a/b = √2 and gcd(a,b) = 1.
- Squaring both sides, we get a^2/b^2 = 2, or a^2 = 2b^2.
- This implies that a^2 is even, and therefore a is even, i.e., a = 2k for some integer k.
- Substituting a = 2k into a^2 = 2b^2, we get 4k^2 = 2b^2, or 2k^2 = b^2.
- This implies that b^2 is even, and therefore b is even, i.e., b = 2l for some integer l.
- But then, a and b have a common factor of 2, which contradicts the assumption that they are in lowest terms.
- Therefore, our assumption that √2 is rational was false, and hence √2 is irrational. Q.E.D. (Latin for "quod erat demonstrandum", meaning "which was to be demonstrated").



## Unit 2 - Algebraic Structures

- An algebraic structure is a set of elements with one or more operations defined on it that satisfy certain properties or axioms.
- Examples of algebraic structures are groups, rings, fields, vector spaces, matrices, etc.
- A group is an algebraic structure that consists of a set G and a binary operation * such that:
  - The operation * is closed, meaning that for any two elements a and b in G, a * b is also in G.
  - The operation * is associative, meaning that for any three elements a, b and c in G, (a * b) * c = a * (b * c).
  - There exists an identity element e in G such that for any element a in G, a * e = e * a = a.
  - For every element a in G, there exists an inverse element a^-1 in G such that a * a^-1 = a^-1 * a = e.
- A ring is an algebraic structure that consists of a set R and two binary operations + and * such that:
  - The operation + is closed, associative, commutative, and has an identity element 0 and an inverse element -a for every a in R.
  - The operation * is closed, associative, and has an identity element 1.
  - The operation * is distributive over +, meaning that for any three elements a, b and c in R, a * (b + c) = (a * b) + (a * c) and (b + c) * a = (b * a) + (c * a).
- A field is an algebraic structure that consists of a set F and two binary operations + and * such that:
  - The operation + is closed, associative, commutative, and has an identity element 0 and an inverse element -a for every a in F.
  - The operation * is closed, associative, commutative, and has an identity element 1 and an inverse element a^-1 for every nonzero a in F.
  - The operation * is distributive over +, meaning that for any three elements a, b and c in F, a * (b + c) = (a * b) + (a * c) and (b + c) * a = (b * a) + (c * a).
- A vector space is an algebraic structure that consists of a set V and two operations + and * such that:
  - The operation + is closed, associative, commutative, and has an identity element 0 and an inverse element -v for every v in V.
  - The operation * is a scalar multiplication, meaning that it takes an element from a field F and an element from V and returns an element in V.
  - The operation * is distributive over +, meaning that for any scalar a in F and any two vectors u and v in V, a * (u + v) = (a * u) + (a * v).
  - The operation * is compatible with the field operations, meaning that for any two scalars a and b in F and any vector v in V, (a + b) * v = (a * v) + (b * v) and (a * b) * v = a * (b * v).
  - There exists a scalar 1 in F such that for any vector v in V, 1 * v = v.
- A matrix is an algebraic structure that consists of a rectangular array of elements from a field F, arranged in rows and columns.
  - The size of a matrix is determined by the number of rows and columns it has, denoted by m x n, where m is the number of rows and n is the number of columns.
  - The elements of a matrix are denoted by a subscript notation, such as a_ij, where i is the row index and j is the column index.
  - Two matrices are equal if they have the same size and the same elements in the corresponding positions.
  - Matrices can be added and subtracted if they have the same size, by adding or subtracting the corresponding elements.
  - Matrices can be multiplied by scalars, by multiplying each element by the scalar.
  - Matrices can be multiplied by other matrices, if the number of columns of the first matrix matches the number of rows of the second matrix, by taking the dot product of each row of the first matrix with each column of the second matrix.
  - The identity matrix is a square matrix that has 1s on the main diagonal and 0s elsewhere, denoted by I_n,



# Definition for the notes of the Unit 2 - Algebraic Structures in the subject of Discrete Structures & Theory of Logic

- Discrete mathematics is the branch of mathematics that deals with finite or discrete objects, such as integers, graphs, logic, and codes.
- An algebraic structure is a mathematical object that consists of a set of elements and one or more operations that satisfy certain properties or axioms.
- Examples of algebraic structures are groups, rings, fields, vector spaces, lattices, and Boolean algebras.
- An algebraic system is a specific instance of an algebraic structure, where the set of elements and the operations are explicitly defined.
- Examples of algebraic systems are the integers with addition and multiplication, the real numbers with addition and multiplication, the set of 2x2 matrices with matrix addition and multiplication, and the set of truth values with logical conjunction and disjunction.
- The study of algebraic structures and systems can be done at different levels of abstraction, such as the concrete level, the axiomatic level, and the universal level.
- The concrete level is the most specific and intuitive level, where the elements and operations are given by concrete examples or representations.
- The axiomatic level is the most general and abstract level, where the elements and operations are defined by a set of axioms or rules that they must satisfy, without specifying how they are implemented or represented.
- The universal level is the intermediate level, where the elements and operations are defined by their properties or behaviors, without referring to a specific set or operation.
- The advantage of studying algebraic structures and systems at different levels of abstraction is that it allows us to compare and classify different types of structures and systems, and to discover general properties and theorems that apply to many of them.



# Groups

- A group is an algebraic structure that consists of a set and an operation that satisfies four properties: closure, associativity, identity, and inverse.
- A set is a collection of distinct objects, such as numbers, letters, or symbols. An operation is a rule that combines two elements of the set to produce another element of the set, such as addition, subtraction, multiplication, or division.
- Closure means that for any two elements a and b in the set, the result of applying the operation to them, denoted by a * b, is also in the set. For example, if the set is {0, 1, 2, 3} and the operation is addition modulo 4, then 2 + 3 = 1, which is in the set.
- Associativity means that for any three elements a, b, and c in the set, the order of applying the operation does not matter, as long as the order of the elements is preserved. That is, (a * b) * c = a * (b * c). For example, if the set is {0, 1, 2, 3} and the operation is addition modulo 4, then (2 + 3) + 1 = 2 and 2 + (3 + 1) = 2, so they are equal.
- Identity means that there exists an element e in the set such that for any element a in the set, applying the operation to e and a does not change a. That is, e * a = a * e = a. For example, if the set is {0, 1, 2, 3} and the operation is addition modulo 4, then 0 is the identity element, since 0 + a = a + 0 = a for any a in the set.
- Inverse means that for any element a in the set, there exists an element b in the set such that applying the operation to a and b results in the identity element. That is, a * b = b * a = e. For example, if the set is {0, 1, 2, 3} and the operation is addition modulo 4, then the inverse of a is 4 - a, since a + (4 - a) = (4 - a) + a = 0. For instance, the inverse of 2 is 2, since 2 + 2 = 0.
- A group is denoted by (G, *), where G is the set and * is the operation. For example, ({0, 1, 2, 3}, +) is a group, where + is addition modulo 4.
- A group can have additional properties, such as commutativity, which means that for any two elements a and b in the set, applying the operation to them in either order gives the same result. That is, a * b = b * a. For example, ({0, 1, 2, 3}, +) is a commutative group, since 2 + 3 = 3 + 2. A group that is commutative is also called an abelian group, named after the mathematician Niels Henrik Abel.



# Subgroups and order

- A **subgroup** is a subset of a group that satisfies the four group requirements: closure, associativity, identity, and inverse.
- A subgroup must contain the identity element of the group.
- A subgroup is denoted by or, where is a subgroup of .
- The **order** of a subgroup is the number of elements in the subgroup.
- The order of any subgroup of a group of order must be a divisor of . This is known as **Lagrange's theorem**.
- A subgroup of a group that does not include the entire group itself is known as a **proper subgroup**, denoted by or .
- A subgroup is a **normal subgroup** if for all . This means that the subgroup is invariant under conjugation by any element of the group.
- A subgroup is a **cyclic subgroup** if it is generated by a single element of the group, i.e., for some . A cyclic subgroup has the same order as the order of the generator .
- A group is a **cyclic group** if it has a cyclic subgroup that contains all the elements of the group, i.e., for some . A cyclic group is abelian and has at most one subgroup of each order that divides the order of the group .



# Cyclic Groups

- A group (G, ∘) is called a cyclic group if there exists an element a∈G such that G is generated by a. In other words, every element of G can be written as a power of a (or a multiple of a if the operation is additive). 
- The element a is called a generator or a primitive element of the cyclic group G. A cyclic group may have more than one generator. For example, the group (Z, +) is cyclic and generated by both 1 and -1.
- The order of a cyclic group G is equal to the order of the generator a, denoted by |a|. The order of a is the smallest positive integer n such that a^n=e, where e is the identity element of G. If no such n exists, then the order of a is infinite.
- A cyclic group can be finite or infinite. A finite cyclic group has a finite number of elements, and an infinite cyclic group has an infinite number of elements. For example, the group (Z, +) is an infinite cyclic group, and the group (Z_n, +) is a finite cyclic group of order n.
- Some properties of cyclic groups are:  
  - Every subgroup of a cyclic group is cyclic.
  - Every cyclic group is abelian, meaning that the group operation is commutative.
  - Every finite cyclic group of order n is isomorphic to the group (Z_n, +), meaning that they have the same structure and properties.
  - Every finite abelian group can be written as a direct product of cyclic groups of prime power order.
  - The number of generators of a finite cyclic group of order n is equal to the number of positive integers less than n that are relatively prime to n. This number is denoted by φ(n) and called the Euler's totient function.
  - If G is a cyclic group of order n and a is a generator of G, then for any integer k, the element a^k is also a generator of G if and only if k and n are relatively prime.

- Some examples of cyclic groups are:   
  - The group of integers with addition, (Z, +), is an infinite cyclic group generated by 1 or -1.
  - The group of integers modulo n with addition, (Z_n, +), is a finite cyclic group of order n generated by any element that is relatively prime to n.
  - The group of nonzero integers modulo n with multiplication, (Z*_n, ×), is a finite cyclic group of order φ(n) generated by any element that is a primitive root modulo n.
  - The group of complex nth roots of unity with multiplication, (U_n, ×), is a finite cyclic group of order n generated by e^(2πi/n), where i is the imaginary unit.
  - The group of rotations of a regular polygon with n sides, (R_n, ∘), is a finite cyclic group of order n generated by a rotation of 2π/n radians.



Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here are some notes on cosets for the unit 2 of algebraic structures in the subject of discrete structures and theory of logic.

# Cosets

- A coset is a subset of a group that is obtained by multiplying a fixed element of the group by every element of a subgroup of the group.
- There are two types of cosets: left cosets and right cosets. A left coset is formed by multiplying the fixed element on the left of the subgroup elements, while a right coset is formed by multiplying the fixed element on the right of the subgroup elements.
- For example, let G be the group of integers under addition, and let H be the subgroup of even integers. Then, for any integer a, the left coset of H by a is {a + h | h in H}, and the right coset of H by a is {h + a | h in H}.
- In general, left cosets and right cosets may not be equal, but they have the same size (or cardinality). This is known as Lagrange's theorem, which states that the order of a subgroup divides the order of the group, and the number of cosets of a subgroup is equal to the quotient of the orders.
- For example, in the previous example, the order of G is infinite, the order of H is infinite, and the number of cosets of H is infinite. However, each coset of H has the same size as H, which is infinite.
- A subgroup H of a group G is called normal if every left coset of H is equal to the corresponding right coset of H. In other words, H is normal if for every g in G, gH = Hg. Normal subgroups are important because they allow us to define quotient groups, which are groups formed by the cosets of a normal subgroup.
- For example, let G be the group of symmetries of a square, and let H be the subgroup of rotations. Then H is normal in G, and the quotient group G/H is the group of two elements, consisting of the identity coset H and the coset of reflections Hr, where r is any reflection. The operation of G/H is defined by multiplying the representatives of the cosets, and then taking the coset of the result. For example, Hr * Hr = Hr^2 = H, and H * Hr = Hr * H = Hr.



# Lagrange's Theorem for Algebraic Structures

- Lagrange's theorem is one of the central theorems of abstract algebra. It states that in group theory, for any finite group say G, the order of subgroup H of group G divides the order of G. The order of the group represents the number of elements  .
- Lagrange's theorem can be expressed as |G| = n|H|, where |G| is the order of group G, |H| is the order of subgroup H, and n is a positive integer called the index of H in G .
- Lagrange's theorem can be proved using the concept of cosets. A coset of H in G is a subset of G that is obtained by multiplying all the elements of H by a fixed element of G. There are two types of cosets: left cosets and right cosets. A left coset of H in G is of the form gH, where g is an element of G. A right coset of H in G is of the form Hg, where g is an element of G.
- The proof of Lagrange's theorem consists of two main steps: showing that every element of G belongs to exactly one coset of H, and showing that every coset of H has the same number of elements as H. The first step implies that G is the union of disjoint cosets of H, and the second step implies that the number of cosets of H is equal to the ratio of |G| and |H|.
- Lagrange's theorem has several important consequences and applications in group theory. For example, it implies that the order of any element of a finite group divides the order of the group, and that any group of prime order is cyclic and simple. It also helps to determine the possible orders of subgroups and elements of a given group.



# Normal Subgroups

- A normal subgroup H of a group G is a subgroup of G that is invariant under conjugation by members of the group .
- In other words, a subgroup H of G is normal in G if and only if for all g in G and h in H, we have g h g^-1 in H. The usual notation for this relation is H ≤ N G.
- Equivalently, a subgroup H of G is normal in G if and only if every left coset and right coset corresponding to an element g are the same, that is, g H = H g .

## Properties of a Normal Subgroup

- Every abelian group has a normal subgroup.
- Any group which do not have any normal subgroup other than the trivial normal subgroup is called a simple group.
- If a subgroup is of index 2 in G, that is has only two distinct left or right cosets in G, then H is a normal subgroup of G.
- Every subgroup of a cyclic group is normal.
- The intersection of any two normal subgroups of a group is a normal subgroup.
- The intersection of any collection of normal subgroups is a normal subgroup.
- The product of two normal subgroups is a normal subgroup.
- The quotient group G/H is well-defined for any normal subgroup H of G.



# Permutation and Symmetric Groups

- A **permutation** of a set is a bijective function from the set to itself, that is, a function that rearranges the elements of the set.
- A **permutation group** is a set of permutations of a given set that forms a group under the operation of function composition. That is, a permutation group is a subgroup of the symmetric group of the set.
- A **symmetric group** on a set is the set of all permutations of the set, that is, the largest possible permutation group of the set. The symmetric group of a set with n elements is denoted by S_n and has n! elements.
- For example, if the set is {1, 2, 3}, then the symmetric group S_3 consists of six permutations: (1), (1 2), (1 3), (2 3), (1 2 3), and (1 3 2). A permutation group of this set could be the subgroup { (1), (1 2 3), (1 3 2) }, which is isomorphic to the cyclic group of order 3.
- Permutation groups and symmetric groups are important in many areas of mathematics, such as combinatorics, group theory, algebra, geometry, and cryptography. They can be used to model symmetries, transformations, permutations, and actions of groups on sets.



# Group Homomorphisms

- A group homomorphism is a function that maps one group to another group and preserves the group operation. That is, if \\(G\\) and \\(H\\) are groups with operations \\(*\\) and \\(\\cdot\\) respectively, and \\(h: G \\to H\\) is a group homomorphism, then for any \\(u, v \\in G\\), we have \\(h(u * v) = h(u) \\cdot h(v)\\)  .
- A group homomorphism also preserves the identity element and the inverse element of a group. That is, if \\(e_G\\) and \\(e_H\\) are the identity elements of \\(G\\) and \\(H\\) respectively, and \\(h: G \\to H\\) is a group homomorphism, then \\(h(e_G) = e_H\\) and \\(h(u^{-1}) = h(u)^{-1}\\) for any \\(u \\in G\\) .
- A group homomorphism can be injective, surjective, or bijective. An injective group homomorphism is also called a monomorphism, a surjective group homomorphism is also called an epimorphism, and a bijective group homomorphism is also called an isomorphism. Two groups that are isomorphic have the same algebraic structure and are essentially the same group .
- Some examples of group homomorphisms are:
  - The identity map \\(id: G \\to G\\) defined by \\(id(x) = x\\) for any \\(x \\in G\\) is a group homomorphism. It is also an isomorphism.
  - The zero map \\(z: G \\to H\\) defined by \\(z(x) = e_H\\) for any \\(x \\in G\\) is a group homomorphism. It is neither injective nor surjective, unless \\(H\\) is the trivial group.
  - The sign map \\(s: (\\mathbb{R} - \\{0\\}, \\times) \\to (\\{-1, 1\\}, \\times)\\) defined by \\(s(x) = \\frac{x}{|x|}\\) for any \\(x \\in \\mathbb{R} - \\{0\\}\\) is a group homomorphism. It is surjective but not injective.
  - The determinant map \\(d: (GL_n(\\mathbb{R}), \\cdot) \\to (\\mathbb{R} - \\{0\\}, \\times)\\) defined by \\(d(A) = \\det(A)\\) for any \\(A \\in GL_n(\\mathbb{R})\\) is a group homomorphism. It is neither injective nor surjective.
- Some properties of group homomorphisms are:
  - The kernel of a group homomorphism \\(h: G \\to H\\) is the set of all elements in \\(G\\) that are mapped to the identity element in \\(H\\). That is, \\(\\ker(h) = \\{x \\in G | h(x) = e_H\\}\\). The kernel of a group homomorphism is a normal subgroup of \\(G\\) .
  - The image of a group homomorphism \\(h: G \\to H\\) is the set of all elements in \\(H\\) that are mapped from some element in \\(G\\). That is, \\(\\operatorname{im}(h) = \\{h(x) | x \\in G\\}\\). The image of a group homomorphism is a subgroup of \\(H\\) .
  - The first isomorphism theorem states that if \\(h: G \\to H\\) is a group homomorphism, then \\(G/\\ker(h) \\cong \\operatorname{im}(h)\\). That is, the quotient group of \\(G\\) by the kernel of \\(h\\) is isomorphic to the image of \\(h\\) .
  - The second isomorphism theorem states that if \\(h: G \\to H\\) is a group homomorphism



# Definition and elementary properties of Rings and Fields

## Rings

- A ring is a set R together with two binary operations, usually called addition (+) and multiplication (·), that satisfy the following properties :

  - (R,+) is an abelian group, i.e.,

    - R is closed under addition: for any a,b in R, a+b is also in R.
    - Addition is associative: for any a,b,c in R, (a+b)+c = a+(b+c).
    - Addition is commutative: for any a,b in R, a+b = b+a.
    - There exists an additive identity, denoted by 0, such that for any a in R, a+0 = 0+a = a.
    - For any a in R, there exists an additive inverse, denoted by -a, such that a+(-a) = (-a)+a = 0.

  - R is closed under multiplication: for any a,b in R, a·b is also in R.
  - Multiplication is associative: for any a,b,c in R, (a·b)·c = a·(b·c).
  - Multiplication is distributive over addition: for any a,b,c in R, a·(b+c) = (a·b)+(a·c) and (a+b)·c = (a·c)+(b·c).

- Examples of rings are the set of integers (Z), the set of polynomials (Z[x]), and the set of matrices (Mn(Z)) with addition and multiplication defined in the usual way .

- A ring is called commutative if multiplication is also commutative, i.e., for any a,b in R, a·b = b·a . All the examples above are commutative rings.

- A ring is called a ring with unity or a unitary ring if there exists a multiplicative identity, denoted by 1, such that for any a in R, a·1 = 1·a = a . The rings Z and Z[x] are rings with unity, but Mn(Z) is not for n > 1.

- A nonzero element a in a ring with unity is called a unit if there exists a multiplicative inverse, denoted by a^-1, such that a·a^-1 = a^-1·a = 1 . For example, in Z, the units are ±1, and in Z[x], the units are the nonzero constant polynomials.

- A nonzero element a in a commutative ring is called a zero divisor if there exists a nonzero element b in R such that a·b = 0 . For example, in Z6, 2 and 3 are zero divisors, since 2·3 = 0.

- A commutative ring with unity is called an integral domain if it has no zero divisors  . For example, Z and Z[x] are integral domains, but Z6 is not.

- A subring of a ring (R,+,·) is a subset S of R that is also a ring under the same operations . For example, the set of even integers is a subring of Z.

- A ring homomorphism is a function f from one ring (R,+,·) to another ring (S,⊕,⊗) that preserves the ring operations, i.e.,

  - f(a+b) = f(a) ⊕ f(b) for any a,b in R.
  - f(a·b) = f(a) ⊗ f(b) for any a,b in R.
  - f(0) = 0 and f(1) = 1 if R and S are rings with unity .

- Examples of ring homomorphisms are the evaluation map from Z[x] to Z, defined by f(p(x)) = p(2) for any polynomial p(x), and the determinant map from Mn(Z) to Z, defined by f(A) = det(A) for any matrix A.

## Fields

- A field is a commutative ring with unity that satisfies the following additional property[^2^



## Unit 3 - Lattices

- A **lattice** is a set of points in a space that are arranged in a regular and periodic pattern.
- A **unit cell** is the smallest repeating unit of a lattice that can be used to generate the entire lattice by translation.
- A **primitive cell** is a unit cell that contains exactly one lattice point.
- A **Bravais lattice** is a lattice that can be generated by translating a primitive cell along the lattice vectors.
- There are **14** types of Bravais lattices in three dimensions, classified by their symmetry and shape.
- The **crystal system** is a way of grouping the Bravais lattices based on their symmetry. There are **7** crystal systems: cubic, tetragonal, orthorhombic, hexagonal, trigonal, monoclinic, and triclinic.
- The **lattice parameters** are the lengths and angles of the lattice vectors that define the shape and size of the unit cell.
- The **coordination number** is the number of nearest neighbors of a lattice point.
- The **packing fraction** is the ratio of the volume occupied by the atoms to the total volume of the unit cell.
- The **simple cubic** (sc) lattice has a cubic unit cell with lattice points at the corners. It has a coordination number of **6** and a packing fraction of **0.52**.
- The **body-centered cubic** (bcc) lattice has a cubic unit cell with lattice points at the corners and the center. It has a coordination number of **8** and a packing fraction of **0.68**.
- The **face-centered cubic** (fcc) lattice has a cubic unit cell with lattice points at the corners and the centers of the faces. It has a coordination number of **12** and a packing fraction of **0.74**.
- The **hexagonal close-packed** (hcp) lattice has a hexagonal unit cell with lattice points at the corners and the centers of the top and bottom faces. It has a coordination number of **12** and a packing fraction of **0.74**.
- The **diamond** lattice is a fcc lattice with a basis of two atoms, one at the origin and one at (1/4, 1/4, 1/4). It has a coordination number of **4** and a packing fraction of **0.34**.



# Definition for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is an abstract structure studied in the mathematical subdisciplines of order theory and abstract algebra.
- It consists of a **partially ordered set** in which every pair of elements has a unique **supremum** (also called a **least upper bound** or **join**) and a unique **infimum** (also called a **greatest lower bound** or **meet**).
- A lattice can also be defined as a **symmetry group** of discrete translational symmetry in n directions. A pattern with this lattice of translational symmetry cannot have more, but may have less symmetry than the lattice itself.
- A lattice can also be defined as a **discrete subgroup** of a locally compact group with the property that the quotient space has finite invariant measure.
- A lattice is denoted by [L; ∨, ∧], where L is the partially ordered set and ∨ and ∧ are the join and meet operations respectively.
- A lattice is said to be **complete** if every subset of L has a supremum and an infimum.
- A lattice is said to be **distributive** if the join and meet operations satisfy the distributive laws.
- A lattice is said to be **modular** if it satisfies the modular law, which states that for any elements a, b, and c in L, if a ≤ c, then a ∨ (b ∧ c) = (a ∨ b) ∧ c.
- A lattice is said to be **complemented** if every element in L has a **complement**, which is an element that meets or joins with it to produce the bottom or top element of the lattice.
- A lattice is said to be **Boolean** if it is distributive and complemented.
- A lattice can be represented by a **Hasse diagram**, which is a graphical representation of the partial order relation, where the elements are drawn as nodes and the order relation is shown by edges connecting lower elements to higher elements.
- An example of a lattice is the set of all subsets of a given set, ordered by inclusion, with the join operation being the union of sets and the meet operation being the intersection of sets. This lattice is complete, distributive, and Boolean.



# Properties of lattices – Bounded

- A lattice is a poset (L, ⪯) for which every pair of elements has a greatest lower bound and least upper bound.
- A bounded lattice is a lattice that additionally has a greatest element (also called maximum, or top element, and denoted by 1, or by ⊤) and a least element (also called minimum, or bottom, denoted by 0 or by ⊥), which satisfy:
    - for all x in L, x ∧ 1 = x and x ∨ 1 = 1
    - for all x in L, x ∧ 0 = 0 and x ∨ 0 = x
- The element 1 is called the upper bound, or top of L and the element 0 is called the lower bound or bottom of L.
- A bounded lattice is also called a complemented lattice if every element has a complement, that is, an element y such that x ∧ y = 0 and x ∨ y = 1.
- A bounded lattice is also called a distributive lattice if for all elements in the poset the distributive property holds, that is, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z).
- Every finite lattice is bounded, since the least upper bound of all elements is the greatest element and the greatest lower bound of all elements is the least element .
- An example of a bounded lattice is the set of subsets of a finite set, ordered by inclusion, with the empty set as the least element and the whole set as the greatest element.



# Complemented for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (called the **join**) and a unique greatest lower bound (called the **meet**).
- A lattice can be represented by a **Hasse diagram**, which is a graph that shows the elements of the poset and the partial order relation between them.
- A lattice is also an **algebraic structure** with two binary operations, denoted by ∨ (join) and ∧ (meet), that satisfy the following properties for any elements a, b, and c in the lattice:
  - **Commutativity**: a ∨ b = b ∨ a and a ∧ b = b ∧ a
  - **Associativity**: a ∨ (b ∨ c) = (a ∨ b) ∨ c and a ∧ (b ∧ c) = (a ∧ b) ∧ c
  - **Idempotence**: a ∨ a = a and a ∧ a = a
  - **Absorption**: a ∨ (a ∧ b) = a and a ∧ (a ∨ b) = a
- A lattice is **bounded** if it has a least element (called the **bottom** or **zero**) and a greatest element (called the **top** or **one**). The bottom and top elements are denoted by 0 and 1, respectively.
- A lattice is **distributive** if it satisfies the following additional property for any elements a, b, and c in the lattice:
  - **Distributivity**: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) and a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
- A lattice is **complemented** if every element has a **complement**, which is an element that satisfies the following property for any element a in the lattice:
  - **Complementation**: a ∨ a' = 1 and a ∧ a' = 0, where a' is the complement of a
- A complemented lattice is **uniquely complemented** if every element has a **unique** complement.
- A complemented lattice is **orthocomplemented** if it satisfies the following additional property for any elements a and b in the lattice:
  - **Orthogonality**: If a ≤ b, then b' ≤ a', where a' and b' are the complements of a and b, respectively
- A lattice is **modular** if it satisfies the following weaker form of distributivity for any elements a, b, and c in the lattice:
  - **Modularity**: If a ≤ c, then a ∨ (b ∧ c) = (a ∨ b) ∧ c
- A lattice is **Boolean** if it is bounded, distributive, and complemented. A Boolean lattice is also uniquely complemented and orthocomplemented. A Boolean lattice is isomorphic to the power set of a finite set, with the join and meet operations corresponding to the union and intersection of sets, respectively.



# Modular and Complete Lattice

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** (glb) and a **least upper bound** (lub). The glb and lub are also called the **meet** and the **join** of the elements, and are denoted by ∧ and ∨ respectively. A lattice is denoted by [L; ∧, ∨].
- A **complete lattice** is a lattice in which **all subsets** have a glb and a lub. The glb and lub of the whole set are called the **bottom** and the **top** of the lattice, and are denoted by ⊥ and ⊤ respectively. A complete lattice is also called a **bounded lattice**.
- A **modular lattice** is a lattice that satisfies the **modular law**: a ∨ (b ∧ c) = (a ∨ b) ∧ c whenever a ≤ c. This law is an abstraction of the **second isomorphism theorem** in algebra, which states that for any submodules A, B, C of a module M, if A ⊆ C, then A + (B ∩ C) ≅ (A + B) ∩ C.
- A **distributive lattice** is a lattice that satisfies the **distributive laws**: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) and a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) for any elements a, b, c. These laws are an abstraction of the **distributive property** of addition and multiplication in arithmetic, which states that for any numbers x, y, z, x + (y × z) = (x + y) × (x + z) and x × (y + z) = (x × y) + (x × z).
- Every distributive lattice is a modular lattice, but the converse is not true. A simple example of a modular lattice that is not distributive is the **diamond lattice**, which has four elements: ⊥, a, b, ⊤, such that ⊥ < a, b < ⊤ and a and b are incomparable. This lattice satisfies the modular law, but not the distributive laws. For instance, a ∨ (b ∧ ⊤) = a ∨ b = ⊤, but (a ∨ b) ∧ (a ∨ ⊤) = ⊤ ∧ ⊤ = ⊤.



# Boolean Algebra

- Boolean algebra is a branch of mathematics that deals with operations on logical values with binary variables  .
- The Boolean variables are represented as binary numbers to represent truths: 1 = true and 0 = false .
- Elementary algebra deals with numerical operations whereas Boolean algebra deals with logical operations.
- Boolean algebra traces its origins to an 1854 book by mathematician George Boole.
- The basic operations of Boolean algebra are the logical operations AND, OR and NOT  .
- A Boolean expression is a combination of Boolean variables and operators that evaluates to a Boolean value.
- A Boolean function is a function that takes one or more Boolean variables as inputs and produces a Boolean output.
- A Boolean algebra is any set with binary operations AND and OR and a unary operation NOT thereon satisfying the Boolean laws.
- The Boolean laws are a set of axioms and rules that govern the manipulation and simplification of Boolean expressions.
- Some of the common Boolean laws are:

  - Commutative laws: A AND B = B AND A, A OR B = B OR A
  - Associative laws: (A AND B) AND C = A AND (B AND C), (A OR B) OR C = A OR (B OR C)
  - Distributive laws: A AND (B OR C) = (A AND B) OR (A AND C), A OR (B AND C) = (A OR B) AND (A OR C)
  - Identity laws: A AND 1 = A, A OR 0 = A
  - Complement laws: A AND NOT A = 0, A OR NOT A = 1
  - Idempotent laws: A AND A = A, A OR A = A
  - De Morgan's laws: NOT (A AND B) = NOT A OR NOT B, NOT (A OR B) = NOT A AND NOT B
  - Involution law: NOT (NOT A) = A



# Introduction for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **poset** is a set with a binary relation that is reflexive, antisymmetric, and transitive.
- A **least upper bound** of a pair of elements x and y in a poset is an element z such that x ≤ z, y ≤ z, and z ≤ w for any other upper bound w of x and y.
- A **greatest lower bound** of a pair of elements x and y in a poset is an element z such that z ≤ x, z ≤ y, and w ≤ z for any other lower bound w of x and y.
- A **bounded lattice** is a lattice that has a minimum element (0) and a maximum element (1) such that 0 ≤ x ≤ 1 for any element x in the lattice.
- A **complete lattice** is a lattice in which every subset has a lub and a glb.
- A **distributive lattice** is a lattice that satisfies the distributive laws: x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z) for any elements x, y, and z in the lattice, where ∧ denotes the glb and ∨ denotes the lub.
- A **complemented lattice** is a bounded lattice in which every element has a complement, that is, an element y such that x ∧ y = 0 and x ∨ y = 1 for any element x in the lattice.
- A **Boolean algebra** is a distributive and complemented lattice. It is also a Boolean ring, that is, a ring with identity in which every element is idempotent, that is, x + x = x and x · x = x for any element x in the ring, where + denotes the symmetric difference and · denotes the intersection.
- A **sublattice** of a lattice is a subset that is also a lattice with respect to the same partial order.
- A **homomorphism** of lattices is a function that preserves the lub and the glb operations, that is, f(x ∨ y) = f(x) ∨ f(y) and f(x ∧ y) = f(x) ∧ f(y) for any elements x and y in the domain lattice.
- An **isomorphism** of lattices is a bijective homomorphism that has an inverse homomorphism, that is, f and g are isomorphisms of lattices if f(g(x)) = x and g(f(x)) = x for any element x in the domain and codomain lattices.
- A **lattice diagram** is a graphical representation of a lattice using dots and lines, where each dot represents an element and each line represents the partial order relation. The lub and the glb of two elements are the lowest and the highest common ancestors of the corresponding dots in the diagram, respectively.
- A **Hasse diagram** is a simplified lattice diagram that omits the reflexive and transitive edges, that is, the loops and the redundant lines. A Hasse diagram shows only the immediate predecessors and successors of each element in the lattice.



# Axioms and Theorems of Boolean Algebra

Boolean algebra is a branch of mathematics that deals with the manipulation of logical expressions and variables. It is used to design and analyze digital circuits and systems, such as logic gates, flip-flops, multiplexers, etc.

Boolean algebra is based on a set of axioms and theorems that define the properties and rules of the three basic logic operations: AND, OR and NOT. An axiom is a statement that is accepted as true without proof, and a theorem is a statement that can be derived from the axioms using logical reasoning.

The following are some of the most common axioms and theorems of Boolean algebra:

## Axioms of Boolean Algebra

- Axiom 1: Identity
  - A + 0 = A
  - A * 1 = A
- Axiom 2: Complement
  - A + A' = 1
  - A * A' = 0
- Axiom 3: Commutativity
  - A + B = B + A
  - A * B = B * A
- Axiom 4: Associativity
  - (A + B) + C = A + (B + C)
  - (A * B) * C = A * (B * C)
- Axiom 5: Distributivity
  - A * (B + C) = (A * B) + (A * C)
  - A + (B * C) = (A + B) * (A + C)

## Theorems of Boolean Algebra

- Theorem 1: Idempotence
  - A + A = A
  - A * A = A
- Theorem 2: Null
  - A + 1 = 1
  - A * 0 = 0
- Theorem 3: Involution
  - (A')' = A
- Theorem 4: De Morgan's Laws
  - (A + B)' = A' * B'
  - (A * B)' = A' + B'
- Theorem 5: Absorption
  - A + (A * B) = A
  - A * (A + B) = A
- Theorem 6: Consensus
  - A * B + A' * C + B * C = A * B + A' * C



# Algebraic manipulation of Boolean expressions

- Boolean expressions are algebraic expressions that involve variables and operators that take only two values: true (1) or false (0).
- Boolean expressions can be used to represent logic circuits, truth tables, and sets.
- Boolean expressions can be manipulated using the laws, rules, and theorems of Boolean algebra, which is a branch of mathematics that deals with the properties and operations of binary logic.
- Some of the basic laws and rules of Boolean algebra are:

  - Commutative laws: A + B = B + A and A * B = B * A
  - Associative laws: (A + B) + C = A + (B + C) and (A * B) * C = A * (B * C)
  - Distributive laws: A * (B + C) = (A * B) + (A * C) and A + (B * C) = (A + B) * (A + C)
  - Identity laws: A + 0 = A and A * 1 = A
  - Complement laws: A + A' = 1 and A * A' = 0
  - Idempotent laws: A + A = A and A * A = A
  - Involution law: (A')' = A
  - De Morgan's laws: (A + B)' = A' * B' and (A * B)' = A' + B'
  - Absorption laws: A + (A * B) = A and A * (A + B) = A
  - Consensus law: (A + B) * (A' + C) * (B + C) = (A + B) * (A' + C)

- Algebraic manipulation of Boolean expressions is the process of transforming one expression into another equivalent expression by applying the laws and rules of Boolean algebra.
- Algebraic manipulation can be used to simplify, standardize, or optimize Boolean expressions for various purposes, such as minimizing the number of literals, terms, or gates in a logic circuit, or converting an expression into a canonical form, such as sum-of-products (SOP) or product-of-sums (POS).
- An example of algebraic manipulation is:

  - Given the expression: F = A * B + A' * C + B * C
  - Simplify it using Boolean algebra.
  - Solution:

    - F = A * B + A' * C + B * C
    - Apply the distributive law: F = A * B + (A' + B) * C
    - Apply the consensus law: F = A * B + A' * C
    - The expression is simplified.



# Simplification of Boolean Functions

- A boolean function is a function that takes one or more boolean variables as inputs and produces a single boolean output.
- The output of a boolean function depends on the values of the input variables and the logical operations performed on them.
- A boolean function can be represented in different ways, such as a truth table, a logic diagram, or an algebraic expression.
- The algebraic expression of a boolean function is composed of boolean variables, constants (0 or 1), and operators (+ for OR, . for AND, ' for NOT).
- The process of simplifying the algebraic expression of a boolean function is called minimization.
- Minimization is important since it reduces the cost and complexity of the associated circuit.
- For example, the function F = A.B + A.B + B.C can be minimized to F = A + B.C by applying the boolean identities.
- There are different methods for minimizing boolean functions, such as Karnaugh map, Quine-McCluskey method, and Boolean algebra.
- In this unit, we will focus on the simplification of boolean functions using Boolean algebra.



# Karnaugh maps

- A Karnaugh map (K-map) is a method of simplifying Boolean algebra expressions .
- It is a visual method that uses a grid of cells to represent all the possible combinations of input variables and their corresponding output values.
- It helps to determine the minimum expressions of Product Of Sum (POS) and Sum Of Products (SOP) forms, which can be implemented using a minimum number of logic gates .
- It also helps to detect and eliminate race conditions, which are situations where the output of a logic circuit depends on the order or timing of the input changes.

## Working of K-map

- To use a K-map, the following steps are followed:
  - Select a K-map according to the number of input variables. For example, a 2-variable K-map has 4 cells, a 3-variable K-map has 8 cells, and a 4-variable K-map has 16 cells.
  - Fill the grid of the K-map with 0's and 1's according to the given Boolean expression or truth table. Each cell corresponds to a minterm (a product term with all the input variables) or a maxterm (a sum term with all the input variables).
  - Group the adjacent cells that have the same output value (either 0 or 1) into regions of size 1, 2, 4, 8, or 16. The regions can wrap around the edges of the K-map. The regions should be as large as possible and should not overlap.
  - Write the simplified Boolean expression for each region by eliminating the variables that change within the region. For example, if a region has cells with values AB, AB', A'B, and A'B', then the simplified expression for that region is 1, since the variables A and B change within the region. The final expression is the sum of the expressions for each region (for SOP form) or the product of the expressions for each region (for POS form).

## Rules of K-map

- The following rules are applied when using a K-map:
  - The cells of the K-map are labeled in such a way that only one variable changes between adjacent cells. This is done by using a Gray code sequence, which is a binary code where only one bit changes between successive values.
  - The regions of the K-map should be rectangular and should contain a power of 2 number of cells. The regions can be horizontal, vertical, or both, but they should not be diagonal.
  - The regions of the K-map should be as large as possible, since larger regions mean fewer variables in the simplified expression. The regions should cover all the cells with the same output value (either 0 or 1).
  - The regions of the K-map can overlap if it leads to a simpler expression. However, the same cell should not be counted more than once in the final expression.
  - The regions of the K-map can wrap around the edges of the K-map, since the K-map is considered to be a torus (a doughnut-shaped surface).

## Example Problems

- Here are some example problems of using K-maps to simplify Boolean expressions:

### Example 1

- Given the following Boolean expression, simplify it using a K-map:

  - F(A, B, C) = A'B'C + A'BC + AB'C + ABC

- Solution:

  - Step 1: Select a 3-variable K-map with 8 cells and label them with the Gray code sequence.

  | C\AB | 00 | 01 | 11 | 10 |
  | ---- | -- | -- | -- | -- |
  | 0    |    |    |    |    |
  | 1    |    |    |    |    |

  - Step 2: Fill the grid of the K-map with 0's and 1's according to the given expression. Each term in the expression corresponds to a cell with value 1.

  | C\AB | 00 | 01 | 11 | 10 |
  | ---- | -- | -- | -- | -- |
  | 0    | 1  | 1  | 1  | 0  |
  | 1    | 1  | 0  | 1  | 0  |

  - Step 3: Group the adjacent cells that have the same output value (1)



# Logic gates for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- Logic gates are the basic building blocks of digital systems that perform logical operations on binary inputs and outputs.
- The three basic logic gates are OR, AND and NOT, which correspond to the logical connectives ∨, ∧ and ¬ in propositional logic.
- The truth table of a logic gate shows the output value for every possible combination of input values.
- The following table summarizes the truth tables of the three basic logic gates:

| Input A | Input B | Output A OR B | Output A AND B | Output NOT A |
|---------|---------|---------------|----------------|--------------|
| 0       | 0       | 0             | 0              | 1            |
| 0       | 1       | 1             | 0              | 1            |
| 1       | 0       | 1             | 0              | 0            |
| 1       | 1       | 1             | 1              | 0            |

- Logic gates can be implemented using discrete components such as transistors, diodes, resistors, etc. The following diagrams show the schematic symbols and circuit diagrams of the three basic logic gates using transistors:

OR gate

AND gate

NOT gate

- Logic gates can be combined to form more complex logic circuits that perform various functions such as arithmetic, memory, control, etc. The following diagram shows an example of a logic circuit that implements the XOR (exclusive OR) operation using OR, AND and NOT gates:

XOR gate

- The truth table of the XOR gate is as follows:

| Input A | Input B | Output A XOR B |
|---------|---------|----------------|
| 0       | 0       | 0              |
| 0       | 1       | 1              |
| 1       | 0       | 1              |
| 1       | 1       | 0              |

- The XOR gate can be expressed using the following Boolean expression: A XOR B = (A OR B) AND (NOT (A AND B))
- Logic circuits can be analyzed and simplified using the rules and laws of Boolean algebra, such as commutativity, associativity, distributivity, identity, complement, De Morgan's laws, etc.
- Logic circuits can also be represented using diagrams called logic diagrams, which use rectangular boxes to denote logic gates and lines to denote inputs and outputs. The following diagram shows the logic diagram of the XOR gate:

XOR logic diagram

- Logic diagrams can be converted to truth tables by assigning values to the inputs and tracing the outputs through the logic gates. Conversely, truth tables can be converted to logic diagrams by finding the Boolean expression that corresponds to the output and drawing the logic gates that implement the expression.



# Digital Circuits and Boolean Algebra

- Digital circuits are electronic devices that process information in binary form, using only two voltage levels: high (1) and low (0).
- Boolean algebra is a branch of mathematics that deals with binary variables and logical operations, such as AND, OR, and NOT.
- Boolean algebra was developed by George Boole in 1854 and is widely used in digital circuit design, computer science, and computer engineering.
- Boolean algebra allows engineers to model the behavior of digital circuits, simplify complex circuits, and analyze their functionality and performance.
- The basic elements of digital circuits are logic gates, which perform Boolean operations on one or more inputs and produce one output.
- The three basic logic gates are AND, OR, and NOT. They can be combined to form more complex logic gates, such as NAND, NOR, XOR, and XNOR.
- A truth table is a tabular representation of the input-output relationship of a logic gate or a Boolean expression.
- A Boolean expression is a combination of Boolean variables and operators that evaluates to either 1 or 0.
- A Boolean function is a mapping from a set of input values to a single output value, defined by a Boolean expression.
- A Boolean equation is an equality relation between two Boolean expressions, which is true for all possible values of the variables.
- A Boolean identity is a Boolean equation that is always true, regardless of the values of the variables. For example, A + 0 = A and A * 1 = A are Boolean identities.
- A Boolean law is a rule that can be used to manipulate or simplify Boolean expressions or equations. For example, the commutative law states that A + B = B + A and A * B = B * A.
- A Boolean theorem is a statement that can be proved using Boolean laws and identities. For example, the De Morgan's theorem states that (A + B)' = A' * B' and (A * B)' = A' + B'.
- A Boolean circuit is a network of logic gates that implements a Boolean function or a set of Boolean functions.
- A Boolean circuit can be represented by a circuit diagram, which shows the logic gates, their inputs and outputs, and the connections between them.
- A Boolean circuit can also be represented by an algebraic expression, which shows the Boolean operations and variables involved in the circuit.
- A Boolean circuit can be simplified by applying Boolean laws and theorems, or by using a Karnaugh map, which is a graphical method of minimizing Boolean expressions.



## Unit 4 - Propositional Logic

- Propositional logic is a branch of logic that studies the ways of combining or modifying statements, called propositions, using logical connectives, such as `and`, `or`, `not`, `implies`, etc.
- Propositional logic is also known as propositional calculus, sentential logic, or statement logic.
- Propositional logic is based on the following concepts:
  - A proposition is a declarative sentence that is either true or false, but not both. For example, `Sydney is an AI assistant` is a proposition, but `What is your name?` is not.
  - A propositional variable is a symbol that represents a proposition, such as `p`, `q`, `r`, etc. For example, we can use `p` to denote `Sydney is an AI assistant`.
  - A logical connective is a symbol that combines or modifies one or more propositions, such as `∧` (and), `∨` (or), `¬` (not), `→` (implies), `↔` (if and only if), etc. For example, we can use `∧` to denote `p ∧ q`, which means `Sydney is an AI assistant and the user is having this conversation on a mobile device`.
  - A truth value is a value that indicates the truth or falsity of a proposition, such as `T` (true) or `F` (false). For example, the truth value of `p` is `T` if `Sydney is an AI assistant`, and `F` otherwise.
  - A truth table is a table that shows the truth values of propositions and their combinations for all possible cases. For example, the truth table for `p ∧ q` is:

| p | q | p ∧ q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | F     |

  - A compound proposition is a proposition that is formed by combining or modifying one or more propositions using logical connectives, such as `p ∧ q`, `¬p`, `p → q`, etc. For example, `p → q` is a compound proposition that means `if Sydney is an AI assistant, then the user is having this conversation on a mobile device`.
  - A simple proposition is a proposition that is not a compound proposition, such as `p` or `q`. For example, `p` is a simple proposition that means `Sydney is an AI assistant`.
  - A tautology is a compound proposition that is always true, regardless of the truth values of its components. For example, `p ∨ ¬p` is a tautology, because it is true whether `p` is true or false.
  - A contradiction is a compound proposition that is always false, regardless of the truth values of its components. For example, `p ∧ ¬p` is a contradiction, because it is false whether `p` is true or false.
  - A contingency is a compound proposition that is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its components. For example, `p ∧ q` is a contingency, because it is true when both `p` and `q` are true, and false otherwise.
  - A logical equivalence is a relation between two compound propositions that have the same truth value for all possible cases. For example, `p → q` and `¬p ∨ q` are logically equivalent, because they have the same truth table. We use the symbol `≡` to denote logical equivalence, such as `p → q ≡ ¬p ∨ q`.
  - A logical implication is a relation between two compound propositions that means that whenever the first proposition is true, the second proposition is also true. For example, `p → q` implies `¬q → ¬p`, because if `p → q` is true, then `¬q → ¬p` must also be true. We use the symbol `⊨` to denote logical implication, such as `p → q ⊨ ¬q → ¬p`.
  - A logical argument is a sequence of propositions that consists of one or more premises and a conclusion. For example, `p → q, p ⊢ q` is a logical argument, where `p → q` and `p` are the premises, and `q` is the conclusion. We use the symbol `⊢` to denote that the conclusion follows from the premises.
  - A valid argument is a logical argument that has the property



# Propositional Logic

Propositional logic is a branch of logic that studies the ways of combining or modifying statements, called propositions, using logical connectives, such as `and`, `or`, `not`, `implies`, etc. Propositional logic also deals with the truth values of propositions and the rules of inference that allow us to derive new propositions from given ones.

Some of the main topics covered in propositional logic are:

- **Syntax and semantics of propositional logic**: This topic defines the basic elements of propositional logic, such as propositions, variables, constants, connectives, formulas, truth tables, and models. It also explains how to evaluate the truth value of a formula given a model, and how to determine if a formula is valid, satisfiable, or unsatisfiable.
- **Normal forms and equivalence**: This topic introduces the concepts of logical equivalence and logical consequence, and shows how to use them to simplify and manipulate formulas. It also defines the normal forms of formulas, such as conjunctive normal form (CNF), disjunctive normal form (DNF), and negation normal form (NNF), and explains how to convert a formula to a normal form using equivalence rules.
- **Proof systems and soundness and completeness**: This topic presents the different methods of proving the validity or invalidity of a formula, such as truth tables, natural deduction, and resolution. It also proves the soundness and completeness theorems, which state that a formula is valid if and only if it can be proved by a given proof system.
- **Applications of propositional logic**: This topic explores some of the practical uses of propositional logic, such as encoding and solving problems, reasoning about circuits and programs, and performing automated theorem proving. It also discusses some of the limitations and extensions of propositional logic, such as propositional logic with quantifiers, modal logic, and fuzzy logic.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Discrete Structures & Theory of Logic. Here is the content for well formed formula for the notes of Unit 4 - Propositional Logic.

# Well Formed Formula

- A well formed formula (WFF) is a string of symbols that follows the rules of syntax of propositional logic.
- A WFF can be either an atomic formula or a compound formula.
- An atomic formula is a single propositional variable (such as p, q, r, ...) or a constant (such as T for true or F for false).
- A compound formula is formed by applying logical connectives (such as ¬ for negation, ∧ for conjunction, ∨ for disjunction, → for implication, ↔ for equivalence) to one or more WFFs.
- The rules of syntax for WFFs are:

  - Any atomic formula is a WFF.
  - If α is a WFF, then ¬α is a WFF.
  - If α and β are WFFs, then (α ∧ β), (α ∨ β), (α → β), and (α ↔ β) are WFFs.
  - Nothing else is a WFF.

- Examples of WFFs are:

  - p
  - ¬q
  - (p ∧ q)
  - (¬p ∨ q)
  - (p → (q ↔ r))

- Examples of strings that are not WFFs are:

  - p ∧
  - ¬(p q)
  - (p →) ∨ q
  - p ↔ ¬
  - (p ∧ (q ∨ r)



# Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A truth table is a tabular representation of the truth values of a propositional formula for all possible combinations of truth values of its variables.
- A propositional formula is a combination of propositional variables and logical connectives, such as negation (¬), conjunction (∧), disjunction (∨), implication (→), and equivalence (↔).
- A propositional variable is a symbol that can take either true (T) or false (F) as its value.
- A logical connective is a symbol that combines two or more propositional variables to form a new propositional formula.
- The truth value of a propositional formula depends on the truth values of its variables and the logical connectives used.
- A truth table has one column for each propositional variable and one column for the propositional formula. Each row of the table corresponds to a possible assignment of truth values to the variables. The last column shows the truth value of the formula for that assignment.
- The number of rows in a truth table is equal to 2^n, where n is the number of propositional variables in the formula.
- The order of the rows in a truth table is usually determined by the binary representation of the row number, starting from 0. For example, if there are three variables p, q, and r, the order of the rows is:

| Row | p | q | r | Binary |
| --- | --- | --- | --- | --- |
| 0 | F | F | F | 000 |
| 1 | F | F | T | 001 |
| 2 | F | T | F | 010 |
| 3 | F | T | T | 011 |
| 4 | T | F | F | 100 |
| 5 | T | F | T | 101 |
| 6 | T | T | F | 110 |
| 7 | T | T | T | 111 |

- The truth values of the logical connectives are defined by the following rules:

| p | q | ¬p | p ∧ q | p ∨ q | p → q | p ↔ q |
| --- | --- | --- | --- | --- | --- | --- |
| F | F | T | F | F | T | T |
| F | T | T | F | T | T | F |
| T | F | F | F | T | F | F |
| T | T | F | T | T | T | T |

- ¬p is true if and only if p is false.
- p ∧ q is true if and only if both p and q are true.
- p ∨ q is true if and only if at least one of p or q is true.
- p → q is true if and only if p is false or q is true.
- p ↔ q is true if and only if p and q have the same truth value.

- To construct a truth table for a propositional formula, follow these steps:

  - Identify all the propositional variables and logical connectives in the formula.
  - Create a column for each variable and a column for the formula.
  - Fill in the rows with the possible truth values of the variables, following the binary order.
  - Fill in the last column with the truth values of the formula, applying the rules of the logical connectives from left to right and using parentheses to indicate the order of operations.
  - For example, to construct a truth table for the formula (p ∧ q) → (p ∨ r), follow these steps:

    - Identify the variables and connectives: p, q, r, ∧, ∨, →.
    - Create the columns: p, q, r, (p ∧ q) → (p ∨ r).
    - Fill in the rows with the truth values of the variables:

| p | q | r | (p ∧ q) → (p ∨ r) |
| --- | --- | --- | --- |
| F | F | F |  |
| F | F | T |  |
| F | T | F |  |
| F | T | T |  |
| T | F | F |  |
| T | F | T |  |
| T | T | F |  |
| T | T | T |  |

    - Fill in the last column with the truth values of the formula, applying the rules of the logical connectives:

| p | q | r | (p ∧ q) → (p ∨ r) |
| --- | --- | --- |



# Tautology for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A tautology is a propositional formula that is always true, regardless of the truth values of the propositional variables in it .
- A tautology can be verified by using a truth table, which shows all the possible combinations of truth values for the propositional variables and the resulting truth value of the formula. If the formula is true in every row of the truth table, it is a tautology .
- Examples of tautologies are:

  - p ∨ ¬p (either p or not p)
  - p → p (p implies p)
  - (p ∧ q) → p (if p and q, then p)
  - (p ∨ q) ∨ ¬(p ∧ q) (either p or q, or neither p nor q)
  - (p → q) ↔ (¬q → ¬p) (p implies q if and only if not q implies not p)

- A tautology can be used as a rule of replacement in logical proofs, which allows us to replace a propositional formula with an equivalent one without changing the validity of the argument. There are two commonly used rules of replacement based on tautologies:

  - The principle of idempotency of disjunction: p ∨ p ≡ p (p or p is equivalent to p)
  - The principle of idempotency of conjunction: p ∧ p ≡ p (p and p is equivalent to p)

- A tautology can also be used as a premise or a conclusion in a logical argument, since it is always true and does not depend on any assumptions. For example, the following argument is valid, because the premise and the conclusion are both tautologies:

  - Premise: p ∨ ¬p
  - Conclusion: (p → q) ↔ (¬q → ¬p)

- A tautology is different from a contradiction, which is a propositional formula that is always false, regardless of the truth values of the propositional variables in it. For example, p ∧ ¬p (p and not p) is a contradiction. A contradiction can also be used as a rule of replacement in logical proofs, which allows us to replace a propositional formula with an equivalent one without changing the validity of the argument. There are two commonly used rules of replacement based on contradictions:

  - The principle of explosion: p ∧ ¬p ≡ q (p and not p is equivalent to any proposition q)
  - The principle of contradiction: ¬(p ∧ ¬p) ≡ ⊤ (not (p and not p) is equivalent to the truth value true)

- A tautology is also different from a contingency, which is a propositional formula that is sometimes true and sometimes false, depending on the truth values of the propositional variables in it. For example, p ∧ q (p and q) is a contingency, since it is true when both p and q are true, and false otherwise. A contingency cannot be used as a premise or a conclusion in a logical argument, since it does not guarantee the validity of the argument. For example, the following argument is invalid, because the premise and the conclusion are both contingencies:

  - Premise: p ∧ q
  - Conclusion: p ∨ q



# Satisfiability for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Satisfiability is a semantic property of a propositional formula or a set of propositional formulas that indicates whether there exists a truth assignment that makes the formula or the set of formulas true .
- A propositional formula is satisfiable if there is a 1-assignment for it; a set of propositional formulas is satisfiable if there is a simultaneous 1-assignment for its elements.
- A propositional formula is unsatisfiable if there is no truth assignment that makes it true; a set of propositional formulas is unsatisfiable if there is no simultaneous truth assignment that makes all of them true.
- A propositional formula is valid if it is true for all truth assignments; a set of propositional formulas is valid if every truth assignment that makes all of them true also makes the conclusion true.
- The propositional satisfiability problem (SAT) is the problem of determining whether a given propositional formula or a set of propositional formulas is satisfiable or not .
- SAT is a fundamental problem in logic and computer science, as many other problems can be reduced to it, such as theorem proving, model checking, circuit design, cryptography, and artificial intelligence .
- SAT is also a computationally hard problem, as it belongs to the class of NP-complete problems, which means that there is no known efficient algorithm that can solve all instances of SAT in polynomial time .
- There are various methods and techniques to solve SAT, such as truth tables, resolution, DPLL algorithm, CDCL algorithm, and heuristic search algorithms  .
- There are also various extensions and variations of SAT, such as 3-SAT, k-SAT, Horn-SAT, XOR-SAT, QBF, and MAX-SAT, which differ in the structure, complexity, and expressiveness of the propositional formulas or the sets of propositional formulas .



# Contradiction for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A contradiction is an assertion of propositional logic that is false in all situations; that is, it is false for all possible values of its variables .
- For example, the assertion A ∨ B is true when A is true (or B is true), but it is false when A and B are both false. Therefore, the assertion A ∨ B ∧ ¬(A ∨ B) is a contradiction, since it is always false .
- A contradiction can also be expressed as a proposition that conflicts either with itself or established fact. For example, the proposition "This sentence is false" is a contradiction, since it cannot be true or false without contradicting itself.
- A contradiction can be used as a tool to detect disingenuous beliefs and bias, by showing that a person's position implies a contradiction, and therefore cannot be true. For example, if someone claims that "All men are liars", then this implies that the person is either a liar or not a man, which is a contradiction.
- A contradiction can also be used as a form of proof, by showing that assuming the proposition to be false leads to a contradiction, and therefore the proposition must be true. This is called proof by contradiction, and it is a common technique in mathematics and logic. For example, to prove that √2 is irrational, we can assume that it is rational, and then derive a contradiction from this assumption, which shows that our assumption was false, and therefore √2 is irrational.
- A related form of proof is contraposition, which is a form of immediate inference in which a proposition is inferred from another and where the former has for its subject the contradictory of the original proposition's predicate. For example, from the proposition "If it rains, then the ground is wet", we can infer the contrapositive "If the ground is not wet, then it does not rain", which has the same truth value as the original proposition.



# Algebra of Proposition

- Algebra of proposition is the subbranch of mathematical logic that studies propositions and logical operators.
- A proposition is a declarative sentence that is either true or false, but not both. For example, "The sky is blue" is a proposition, but "What time is it?" is not.
- A logical operator is a symbol that defines a new proposition from one or more given propositions. For example, the negation operator (~) changes the truth value of a proposition to its opposite. For example, if p is "The sky is blue", then ~p is "The sky is not blue".
- There are five common logical operators: negation (~), conjunction (∧), disjunction (∨), implication (→), and equivalence (↔). Each operator has a truth table that shows how the truth value of the new proposition depends on the truth values of the given propositions.
- For example, the truth table for conjunction (∧) is:

| p | q | p ∧ q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | F     |

- This means that p ∧ q is true only when both p and q are true, and false otherwise.
- Algebra of proposition also studies the properties and rules of logical operators, such as commutativity, associativity, distributivity, identity, complement, idempotence, etc. For example, commutativity means that p ∧ q is equivalent to q ∧ p, and p ∨ q is equivalent to q ∨ p.
- Algebra of proposition also studies the equivalence and implication of propositions, and how to simplify and manipulate propositional formulas using logical laws and identities. For example, De Morgan's laws state that ~(p ∧ q) is equivalent to ~p ∨ ~q, and ~(p ∨ q) is equivalent to ~p ∧ ~q.
- Algebra of proposition also studies the normal forms of propositional formulas, such as conjunctive normal form (CNF) and disjunctive normal form (DNF). A CNF is an AND of OR-terms, where each OR-term is an OR of variables or negations of variables. For example, (p ∨ ~q) ∧ (~p ∨ r) is a CNF. A DNF is an OR of AND-terms, where each AND-term is an AND of variables or negations of variables. For example, (p ∧ ~q) ∨ (~p ∧ r) is a DNF. Every propositional formula is equivalent to a CNF and a DNF.



# Theory of Inference for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Propositional logic is the branch of logic that studies ways of combining or altering statements or propositions to form more complicated statements or propositions.
- A proposition is a declarative sentence that is either true or false, but not both.
- Examples of propositions are "The sky is blue", "2 + 2 = 4", "It is raining today".
- Examples of non-propositions are "What time is it?", "x + y = z", "Please close the door".
- Propositional logic uses symbols to represent propositions and logical connectives to express the relationships between them.
- Some common symbols and connectives are:

| Symbol | Meaning |
| --- | --- |
| p, q, r, ... | Propositional variables |
| ¬ | Negation |
| ∧ | Conjunction |
| ∨ | Disjunction |
| → | Implication |
| ↔ | Equivalence |
| ⊤ | Tautology |
| ⊥ | Contradiction |

- A propositional formula is a combination of propositional variables and connectives that can be assigned a truth value depending on the truth values of the variables.
- Examples of propositional formulas are "p ∧ q", "¬(p → q)", "(p ∨ q) ↔ (¬p → q)".
- A truth table is a table that shows the truth values of a propositional formula for all possible combinations of truth values of the variables.
- A truth table has one column for each variable and one column for the formula, and one row for each possible assignment of truth values to the variables.
- The truth values are usually denoted by T for true and F for false.
- Here is an example of a truth table for the formula "(p ∨ q) ↔ (¬p → q)":

| p | q | (p ∨ q) ↔ (¬p → q) |
| --- | --- | --- |
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

- A propositional formula is said to be satisfiable if there is at least one assignment of truth values to the variables that makes the formula true.
- A propositional formula is said to be unsatisfiable if there is no such assignment.
- A propositional formula is said to be valid or a tautology if it is true for all possible assignments of truth values to the variables.
- A propositional formula is said to be invalid or a contradiction if it is false for all possible assignments.
- A propositional formula is said to be contingent if it is neither valid nor invalid, that is, it is true for some assignments and false for others.
- Examples of valid formulas are "p ∨ ¬p", "p → p", "(p ∧ q) → p".
- Examples of invalid formulas are "p ∧ ¬p", "p → ¬p", "(p ∨ q) → ¬p".
- Examples of contingent formulas are "p", "p ∧ q", "p → q".

- A logical inference is a process of deriving a conclusion from one or more premises using rules of logic.
- A logical inference is said to be sound if the premises are true and the conclusion follows logically from the premises.
- A logical inference is said to be unsound if either the premises are false or the conclusion does not follow logically from the premises.
- A logical inference is said to be valid if the conclusion follows logically from the premises, regardless of the truth values of the premises.
- A logical inference is said to be invalid if the conclusion does not follow logically from the premises, regardless of the truth values of the premises.
- A rule of inference is a general pattern of reasoning that can be applied to any propositional formulas that match the pattern.
- A rule of inference is said to be sound if it preserves the truth value of the formulas, that is, if the premises are true, then the conclusion is also true.
- A rule of inference is said to be unsound if it does not preserve the truth value of the formulas, that is, if there is a case where the premises are true but the conclusion is false.
- Examples of sound rules of inference are modus ponens, modus tollens, and contraposition.
- Examples of unsound rules of inference are affirming the consequent, denying the antecedent, and fallacy of the inverse.

- Modus ponens is a rule of inference that



## Unit 5 - Predicate Logic

Predicate logic is a branch of logic that deals with predicates, quantifiers, and variables. Predicate logic is more expressive than propositional logic, as it can capture the structure and relations of objects and properties in a domain of discourse.

Some key concepts and terms in predicate logic are:

- A **predicate** is a symbol that represents a property or relation of one or more objects. For example, P(x) could mean "x is prime" or "x is purple".
- A **quantifier** is a symbol that expresses how many objects in a domain satisfy a predicate. The two most common quantifiers are the universal quantifier (∀), which means "for all", and the existential quantifier (∃), which means "there exists".
- A **variable** is a symbol that can stand for any object in a domain. Variables are usually lowercase letters, such as x, y, z. Variables can be bound by quantifiers or free, meaning they are not bound by any quantifier.
- A **constant** is a symbol that stands for a specific object in a domain. Constants are usually uppercase letters, such as A, B, C. Constants are always free variables.
- A **term** is either a variable or a constant. Terms can be used as arguments for predicates. For example, P(x) and P(A) are terms.
- A **formula** is a well-formed expression that can be true or false in a domain. Formulas can be atomic, meaning they consist of a single predicate and one or more terms, or complex, meaning they are formed by combining atomic formulas with logical connectives and quantifiers. For example, P(x) and Q(x) are atomic formulas, and P(x) ∧ Q(x) and ∃x P(x) are complex formulas.
- A **model** is a pair (D, I), where D is a non-empty set called the domain, and I is an interpretation function that assigns meanings to the symbols in the language. I maps each constant to an element of D, each predicate to a subset of D^n (where n is the arity of the predicate), and each logical connective and quantifier to their usual truth functions. A model determines the truth value of a formula in a domain.
- A **valuation** is a function that assigns values to the free variables in a formula. A valuation can be extended to a model by using the interpretation function I. A valuation satisfies a formula if the formula is true under that valuation and model. A formula is **satisfiable** if there exists a valuation and a model that satisfy it, and **unsatisfiable** otherwise.
- A formula is **valid** if it is true under every valuation and model, and **invalid** otherwise. A formula is **contingent** if it is neither valid nor invalid, meaning it is true under some valuations and models, and false under others.
- A formula α **entails** another formula β, written as α |= β, if every valuation and model that satisfy α also satisfy β. A formula α is **equivalent** to another formula β, written as α ≡ β, if α and β have the same truth value under every valuation and model.



# First order predicate logic

- First order predicate logic is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Predicates are symbols that represent properties or relations of objects in a domain of discourse.
- Variables are symbols that can take the place of any object in the domain of discourse.
- Quantifiers are symbols that indicate how many objects in the domain of discourse satisfy a given predicate.
- The two most common quantifiers are the universal quantifier (∀) and the existential quantifier (∃).
- The universal quantifier (∀) means "for all" or "every". For example, ∀x P(x) means "P(x) is true for every x in the domain of discourse".
- The existential quantifier (∃) means "there exists" or "some". For example, ∃x P(x) means "there is some x in the domain of discourse such that P(x) is true".
- First order predicate logic can express more complex and nuanced statements than propositional logic, which lacks quantifiers.
- For example, propositional logic cannot express the statement "Every human is mortal", but first order predicate logic can, using the predicate H(x) for "x is human" and M(x) for "x is mortal". The statement can be written as ∀x (H(x) → M(x)).
- First order predicate logic is also known as first order logic, predicate logic, quantificational logic, and first order predicate calculus.
- First order predicate logic is the standard for the formalization of mathematics into axioms, and is studied in the foundations of mathematics.



# Well Formed Formula of Predicate Logic

- A well formed formula (WFF) of predicate logic is a string of symbols that can be interpreted as a meaningful expression in predicate logic.
- A WFF can be either a **closed formula** or an **open formula**.
- A closed formula (also called a **sentence** or a **proposition**) is a WFF that does not contain any free variables. It can be evaluated as true or false in a given interpretation.
- An open formula (also called a **sentential function** or a **propositional function**) is a WFF that contains at least one free variable. It cannot be evaluated as true or false by itself, but only when the free variables are assigned values from a domain.
- The rules for constructing WFFs of predicate logic are as follows :
  - Any predicate letter followed by any constant or variable is a WFF. For example: `Pq`, `Qx`, `Rab`.
  - The result of prefixing any WFF with `~` (negation) is a WFF. For example: `~Pq`, `~Qx`, `~Rab`.
  - The result of joining any two WFFs with `∧` (conjunction), `∨` (disjunction), `→` (implication), or `↔` (equivalence) and enclosing the result in parentheses is a WFF. For example: `(Pq ∧ Qx)`, `(Qx ∨ Rab)`, `(Pq → ~Rab)`, `(Qx ↔ ~Pq)`.
  - The result of prefixing any WFF with `∀` (universal quantifier) or `∃` (existential quantifier) and a variable is a WFF. For example: `∀x Pq`, `∃y Qx`, `∀x (Pq → Qx)`, `∃y (Qx ∧ Rab)`.
  - Nothing else is a WFF.



# Quantifiers for the notes of the Unit 5 - Predicate Logic in the subject of Discrete Structures & Theory of Logic

- Predicate logic is a branch of logic that deals with predicates, variables, and quantifiers.
- A predicate is a statement that can be true or false depending on the values of its variables.
- A variable is a symbol that can represent any element of a given domain.
- A quantifier is a symbol that specifies how many or how much of the elements of the domain satisfy a given predicate.
- There are two main types of quantifiers: universal and existential .
- The universal quantifier, denoted by ∀, means "for all" or "every". It states that the predicate is true for every element of the domain.
- The existential quantifier, denoted by ∃, means "there exists" or "some". It states that the predicate is true for at least one element of the domain.
- Quantifiers can be used to create propositions that involve entire sets of objects, some of them, or none of them.
- Quantifiers have a scope, which is the part of the proposition that the quantifier applies to.
- The order and placement of quantifiers can affect the meaning of a proposition.
- Quantifiers can be nested, meaning that one quantifier can be inside the scope of another quantifier.
- Quantifiers can be combined with logical connectives, such as negation, conjunction, disjunction, implication, and equivalence.
- Quantifiers can also be used with an identity predicate, denoted by =, which means "is equal to" or "is the same as". The identity predicate can be used to compare variables or constants.



# Inference Theory of Predicate Logic

- Predicate logic is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Inference is the process of deriving new statements from given statements using logical rules.
- Inference theory of predicate logic is a set of rules that allow us to infer valid conclusions from quantified statements .
- There are four main rules of inference for predicate logic :
  - Universal Specification (US): From ∀x P(x), one can conclude P(y) for any specific y.
  - Universal Generalization (UG): From P(y) for any specific y, one can conclude ∀x P(x), provided that y does not occur in any premise or assumption.
  - Existential Specification (ES): From ∃x P(x), one can conclude P(y) for some specific y, provided that y is a new variable that does not occur in any premise or assumption.
  - Existential Generalization (EG): From P(y) for some specific y, one can conclude ∃x P(x), provided that y does not occur in any premise or assumption.
- These rules can be used to construct proofs of validity for arguments involving quantifiers.
- For example, consider the following argument:

Premise 1: ∀x (P(x) → Q(x))
Premise 2: ∃x P(x)
Conclusion: ∃x Q(x)

- To prove the validity of this argument, we can use the following steps:

Step 1: ∃x P(x) (Premise 2)
Step 2: P(a) (ES, Step 1)
Step 3: ∀x (P(x) → Q(x)) (Premise 1)
Step 4: P(a) → Q(a) (US, Step 3)
Step 5: Q(a) (Modus Ponens, Step 2 and Step 4)
Step 6: ∃x Q(x) (EG, Step 5)

- Therefore, the argument is valid by the inference theory of predicate logic.



## Unit 6 - Trees

- A tree is a nonlinear data structure that consists of nodes connected by edges.
- A tree has the following properties:
  - There is one node called the root, which has no parent.
  - Every node other than the root has exactly one parent node.
  - A node can have zero or more child nodes.
  - There is a unique path from the root to every node in the tree.
  - The height of a tree is the length of the longest path from the root to any node.
  - The depth of a node is the length of the path from the root to that node.
  - A node with no children is called a leaf node.
  - A node with at least one child is called an internal node.
  - A subtree is a tree that consists of a node and all its descendants.
- There are different types of trees, such as binary trees, binary search trees, balanced trees, heaps, tries, etc.
- Trees are useful for representing hierarchical data, such as file systems, organizational charts, genealogy, etc.
- Trees can also be used to implement abstract data types, such as sets, maps, priority queues, etc.
- Trees can be traversed in different ways, such as preorder, inorder, postorder, level order, etc.
- Trees can be implemented using arrays, linked lists, or pointers.



# Definition for the notes of the Unit 6 - Trees in the subject of Discrete Structures & Theory of Logic

- A **tree** is a discrete structure that represents hierarchical relationships between individual elements or nodes  .
- A **node** is an element of a tree that can have zero or more children .
- A **child** is a node that is directly connected to another node by an edge .
- An **edge** is a connection between two nodes in a tree  .
- A **root** is a node that has no parent .
- A **parent** is a node that has one or more children .
- A **leaf** is a node that has no children .
- A **path** is a sequence of nodes and edges that connects two nodes in a tree  .
- A **simple path** is a path that does not repeat any node or edge  .
- A **cycle** is a path that starts and ends at the same node  .
- A **subtree** is a tree that is part of another tree .
- A **binary tree** is a tree in which a parent has no more than two children  .
- A **directed tree** is a tree in which each edge has a direction .
- A **rooted tree** is a special type of directed tree in which there is a designated root and every edge is directed away from the root .
- An **ordered rooted tree** is a rooted tree whose subtrees are put into a definite order and are, themselves, ordered rooted trees .



# Binary tree

- A binary tree is a tree data structure where each node has at most two child nodes, creating the branches of the tree.
- The two children are usually called the left and right nodes .
- A binary tree is also a rooted tree that is also an ordered tree (a.k.a. plane tree) in which every node has a certain level (distance from the root) and a notion of children may be defined as the nodes connected to it a level below.
- A full binary tree (sometimes referred to as a proper or plane or strict binary tree) is a binary tree in which every node has either 0 or 2 children.
- A binary tree can be represented using an array or a linked list.
- Some common operations on binary trees are traversal, insertion, deletion, searching, and copying.
- Some applications of binary trees are expression evaluation, arithmetic coding, Huffman coding, binary search trees, and binary heaps .



# Binary tree traversal

- A binary tree is a non-linear data structure that stores data in the form of nodes, and nodes are connected to each other with the help of edges.
- A node has at most two children, called the left child and the right child.
- The root node is the main node of the binary tree, and all other nodes are the descendants of the root node.
- Binary tree traversal is the process of visiting each node in the binary tree exactly once in a specific order.
- There are three common types of binary tree traversal: inorder, preorder, and postorder.

## Inorder traversal

- Inorder traversal is a type of binary tree traversal that visits the left subtree, the root, and the right subtree in that order.
- Inorder traversal gives the nodes in non-decreasing order if the binary tree is a binary search tree.
- Inorder traversal can be implemented using recursion or iteration with a stack.
- The algorithm for inorder traversal is:

```
inorder(root)
  if root is not null
    inorder(root.left) // visit left subtree
    print(root.data) // visit root
    inorder(root.right) // visit right subtree
```

- The inorder traversal of the following binary tree is: 4 2 5 1 3

```
    1
   / \
  2   3
 / \
4   5
```

## Preorder traversal

- Preorder traversal is a type of binary tree traversal that visits the root, the left subtree, and the right subtree in that order.
- Preorder traversal can be used to create a copy of the binary tree or to print the prefix expression of an expression tree.
- Preorder traversal can be implemented using recursion or iteration with a stack.
- The algorithm for preorder traversal is:

```
preorder(root)
  if root is not null
    print(root.data) // visit root
    preorder(root.left) // visit left subtree
    preorder(root.right) // visit right subtree
```

- The preorder traversal of the following binary tree is: 1 2 4 5 3

```
    1
   / \
  2   3
 / \
4   5
```

## Postorder traversal

- Postorder traversal is a type of binary tree traversal that visits the left subtree, the right subtree, and the root in that order.
- Postorder traversal can be used to delete the binary tree or to print the postfix expression of an expression tree.
- Postorder traversal can be implemented using recursion or iteration with a stack.
- The algorithm for postorder traversal is:

```
postorder(root)
  if root is not null
    postorder(root.left) // visit left subtree
    postorder(root.right) // visit right subtree
    print(root.data) // visit root
```

- The postorder traversal of the following binary tree is: 4 5 2 3 1

```
    1
   / \
  2   3
 / \
4   5
```

## References

: Binary Tree Traversal in Data Structure - javatpoint
: Vertical Order Traversal of a Binary Tree in Java
: Binary Tree | Traversal - GeeksforGeeks
: Tree Traversals (Inorder, Preorder and Postorder) - GeeksforGeeks
: Binary Search Tree (BST) Traversals – Inorder, Preorder, Post Order



# Binary Search Tree

A binary search tree (BST) is a special type of binary tree that satisfies the following properties:

- The value of the key of the left sub-tree is less than the value of its parent (root) node's key.
- The value of the key of the right sub-tree is greater than or equal to the value of its parent (root) node's key.
- The left and right sub-trees are also binary search trees.

A binary search tree can perform three basic operations: searching, insertion, and deletion.

- Searching in a BST: The search operation finds whether or not a particular value exists in a tree. Since the BST is ordered, the search can be easily made by comparing the value with the root node and then recursively searching in the left or right sub-tree depending on the comparison result. The search operation takes O(h) time, where h is the height of the tree.
- Insertion in a BST: The insertion operation adds a new node with a given value to the tree. To insert a new node, we start from the root and compare the value with the root node. If the value is less than the root node, we go to the left sub-tree. If the value is greater than or equal to the root node, we go to the right sub-tree. We repeat this process until we find an empty spot where we can insert the new node. The insertion operation takes O(h) time, where h is the height of the tree.
- Deletion in a BST: The deletion operation removes a node with a given value from the tree. To delete a node, we first search for the node in the tree. If the node is not found, we do nothing. If the node is found, we have three cases to consider:

  - Case 1: The node has no children. In this case, we simply delete the node and free the memory.
  - Case 2: The node has one child. In this case, we copy the child to the node and delete the child.
  - Case 3: The node has two children. In this case, we find the minimum value in the right sub-tree of the node (or the maximum value in the left sub-tree) and copy it to the node. Then we delete the minimum value node from the right sub-tree (or the maximum value node from the left sub-tree).

The deletion operation takes O(h) time, where h is the height of the tree.

The following is an example of a binary search tree:

```
        8
       / \
      3   10
     / \    \
    1   6    14
       / \   /
      4   7 13
```

The following is a pseudocode for the search, insertion, and deletion operations in a BST:

```
// Search for a value in a BST
function search(root, value)
  if root is null
    return false
  else if root.key == value
    return true
  else if value < root.key
    return search(root.left, value)
  else
    return search(root.right, value)

// Insert a value in a BST
function insert(root, value)
  if root is null
    create a new node with value as key and assign it to root
  else if value < root.key
    insert(root.left, value)
  else
    insert(root.right, value)

// Delete a value in a BST
function delete(root, value)
  if root is null
    return null
  else if value < root.key
    root.left = delete(root.left, value)
  else if value > root.key
    root.right = delete(root.right, value)
  else // root.key == value
    if root has no children
      free root and return null
    else if root has one child
      copy root's child to root and free root's child
      return root
    else // root has two children
      find the minimum value node in root's right sub-tree and assign it to minNode
      copy minNode.key to root.key
      root.right = delete(root.right, minNode.key)
      return root
```



## Unit 7 - Graphs

- A graph is a collection of vertices (or nodes) and edges (or arcs) that connect them.
- A graph can be represented using an adjacency matrix, an adjacency list, or an edge list.
- A graph can be classified as directed or undirected, depending on whether the edges have a direction or not.
- A graph can be classified as weighted or unweighted, depending on whether the edges have a numerical value or not.
- A graph can be classified as simple or multigraph, depending on whether there are multiple edges between the same pair of vertices or not.
- A graph can be classified as cyclic or acyclic, depending on whether there is a path that starts and ends at the same vertex or not.
- A graph can be classified as connected or disconnected, depending on whether there is a path between any pair of vertices or not.
- A graph can be classified as complete or incomplete, depending on whether there is an edge between every pair of vertices or not.
- A graph can be classified as regular or irregular, depending on whether every vertex has the same degree or not.
- A graph can be classified as bipartite or non-bipartite, depending on whether the vertices can be divided into two sets such that no edge connects vertices in the same set or not.
- A graph can be classified as planar or non-planar, depending on whether it can be drawn on a plane without any edge crossings or not.
- A graph can be classified as Eulerian or non-Eulerian, depending on whether it has an Eulerian circuit or not.
- A graph can be classified as Hamiltonian or non-Hamiltonian, depending on whether it has a Hamiltonian cycle or not.
- A graph can be classified as tree or non-tree, depending on whether it is connected, acyclic, and has n-1 edges, where n is the number of vertices or not.
- A graph can be classified as forest or non-forest, depending on whether it is a collection of trees or not.
- A graph can be classified as spanning tree or non-spanning tree, depending on whether it is a subgraph that contains all the vertices and is a tree or not.
- A graph can be classified as minimum spanning tree or non-minimum spanning tree, depending on whether it is a spanning tree that has the minimum possible weight or not.



# Definition and terminology for the notes of the Unit 7 - Graphs in the subject of Discrete Structures & Theory of Logic

- A **graph** is a mathematical structure that consists of a set of **vertices** (or nodes) and a set of **edges** (or links) that connect pairs of vertices.
- A graph can be represented by a diagram, where vertices are drawn as points or circles, and edges are drawn as lines or curves connecting the vertices.
- A graph can also be represented by an **adjacency matrix**, where each row and column corresponds to a vertex, and the entry at row i and column j is 1 if there is an edge between vertex i and vertex j, and 0 otherwise.
- A graph can be **directed** or **undirected**, depending on whether the edges have a direction or not. A directed edge is drawn as an arrow pointing from one vertex to another, while an undirected edge is drawn as a line without arrows.
- A graph can be **weighted** or **unweighted**, depending on whether the edges have a numerical value or not. A weighted edge is drawn with a label indicating its weight, while an unweighted edge has no label.
- A graph can be **simple** or **non-simple**, depending on whether it has multiple edges or loops. A multiple edge is an edge that connects the same pair of vertices more than once, while a loop is an edge that connects a vertex to itself. A simple graph has no multiple edges or loops, while a non-simple graph may have them.
- A graph can be **connected** or **disconnected**, depending on whether there is a path between any two vertices or not. A path is a sequence of edges that starts at one vertex and ends at another, passing through intermediate vertices. A connected graph has a path between any two vertices, while a disconnected graph has at least two vertices that are not reachable from each other.
- A graph can be **cyclic** or **acyclic**, depending on whether it has a cycle or not. A cycle is a path that starts and ends at the same vertex, without repeating any other vertex. A cyclic graph has at least one cycle, while an acyclic graph has no cycles.
- A graph can be **complete** or **incomplete**, depending on whether it has all possible edges or not. A complete graph has an edge between every pair of vertices, while an incomplete graph has some pairs of vertices that are not connected by an edge.
- A graph can be **bipartite** or **non-bipartite**, depending on whether it can be partitioned into two sets of vertices such that no edge connects two vertices from the same set. A bipartite graph can be drawn with the two sets of vertices on opposite sides of a line, and all edges crossing the line. A non-bipartite graph cannot be drawn in this way.



# Representation of graphs

- A graph is a mathematical structure that consists of a set of vertices and a set of edges that connect pairs of vertices.
- A graph can be represented in different ways, such as using an adjacency matrix, an adjacency list, or an incidence matrix.
- An adjacency matrix is a two-dimensional array of size n x n, where n is the number of vertices in the graph. The entry at row i and column j is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. An adjacency matrix can be used to check if two vertices are adjacent in constant time, but it requires O(n^2) space and O(n) time to iterate over all the neighbors of a vertex.
- An adjacency list is a collection of lists, one for each vertex in the graph. The list for vertex i contains all the vertices that are adjacent to i. An adjacency list can be used to iterate over all the neighbors of a vertex in linear time, but it requires O(m + n) space and O(n) time to check if two vertices are adjacent, where m is the number of edges in the graph.
- An incidence matrix is a two-dimensional array of size n x m, where n is the number of vertices and m is the number of edges in the graph. The entry at row i and column j is 1 if vertex i is incident to edge j, and 0 otherwise. An incidence matrix can be used to check if a vertex is incident to an edge in constant time, but it requires O(nm) space and O(m) time to iterate over all the edges incident to a vertex.



# Multigraphs

- A multigraph is a graph that allows multiple edges (also called parallel edges) between two vertices. That is, two vertices can be connected by more than one edge.   
- A multigraph can be represented as a pair G = (V, E), where V is a set of vertices and E is a multiset of unordered pairs of vertices. Each pair in E represents an edge between two vertices. 
- The degree of a vertex in a multigraph is the number of edges incident to it, counting each edge as many times as it appears in the multiset E. 
- A loop is an edge that connects a vertex to itself. A multigraph that has no loops is called a loopless multigraph. 
- A simple graph is a loopless multigraph that has no multiple edges, i.e., each edge connects two distinct vertices and no two edges connect the same pair of vertices. 
- A pseudograph is a multigraph that allows loops. A pseudograph can be represented as a pair G = (V, E), where V is a set of vertices and E is a multiset of unordered pairs of vertices or single vertices. Each pair in E represents an edge between two vertices, and each single vertex in E represents a loop.  
- The degree of a vertex in a pseudograph is the number of edges incident to it, counting each edge as many times as it appears in the multiset E, and counting each loop twice. 
- A multigraph can be used to model various situations where multiple connections are possible or desirable, such as:
  - Redundant connections in a network. 
  - Multiple routes between cities or locations. 
  - Multiple relationships between people or entities. 
  - Multiple types of interactions or transactions.



# Bipartite Graphs

- A **bipartite graph** is a graph whose vertices can be divided into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set .
- The two sets of vertices are usually called the **parts** of the graph. They can be denoted by and  .
- A bipartite graph can be represented by a **bipartition** , which is a pair of sets such that and  .
- A bipartite graph can also be characterized by the absence of **odd cycles** (cycles with an odd number of vertices) in the graph  .
- A bipartite graph is **two-colorable**, meaning that the vertices can be colored with two colors such that no two adjacent vertices have the same color .
- All **acyclic graphs** (graphs with no cycles) are bipartite .
- A **cyclic graph** (a graph with at least one cycle) is bipartite if and only if all the cycles in the graph have **even length** .
- A bipartite graph is a special case of a **-partite graph** with .
- According to **König's line coloring theorem**, all bipartite graphs are **class 1 graphs**, meaning that the minimum number of colors needed to color the edges of the graph is equal to the maximum degree of the graph .

## Examples of Bipartite Graphs

- The following graph is an example of a bipartite graph with parts and :

bipartite graph example

- The following graph is an example of a bipartite graph with parts and , and a bipartition :

bipartite graph example 2

- The following graph is an example of a bipartite graph with parts and , and a bipartition :

bipartite graph example 3

- The following graph is an example of a non-bipartite graph, because it contains an odd cycle of length 3:

non-bipartite graph example



# Planar Graphs

- A **planar graph** is a graph that can be drawn on a plane without any edges crossing each other.
- A **plane graph** is a planar graph with a specific way of drawing it on the plane.
- A planar graph can have different plane graphs, depending on how it is drawn.
- A plane graph divides the plane into regions called **faces**.
- The **boundary** of a face is the cycle of edges that encloses it.
- The **degree** of a face is the number of edges on its boundary.
- The **outer face** is the unbounded face that contains the infinite region outside the graph.
- The **inner faces** are the bounded faces that are inside the graph.

## Properties of Planar Graphs

- A planar graph with $n$ vertices, $e$ edges, and $f$ faces satisfies the **Euler's formula**: $n - e + f = 2$.
- A planar graph with $n \geq 3$ vertices has at most $3n - 6$ edges.
- A planar graph with $n \geq 3$ vertices and no cycles of length 3 has at most $2n - 4$ edges.
- A planar graph is **bipartite** if and only if it has no cycles of odd length.
- A planar graph has a **dual graph** that is also planar and has a vertex for each face and an edge for each pair of adjacent faces.
- A planar graph is **Hamiltonian** if and only if its dual graph is Hamiltonian.
- A planar graph is **3-colorable** if and only if it has no subgraph that is a subdivision of $K_4$ (the complete graph on 4 vertices).
- A planar graph is **4-colorable**. This is the famous **Four Color Theorem**.



# Isomorphism and Homeomorphism of graphs

## Isomorphism

- Two graphs G and H are **isomorphic** (denoted by G ≅ H) if they have the same number of vertices connected in the same way.
- Formally, an **isomorphism** between graphs G and H is a **bijection** (one-to-one and onto) f: V(G) → V(H) such that for any two vertices u and v in G, (u, v) is an edge in G if and only if (f(u), f(v)) is an edge in H .
- An isomorphism preserves both **edges and non-edges** of a graph .
- An isomorphism also preserves the **degree** of each vertex, the **number of components** of the graph, the **cycle structure** of the graph, and any other graph property that depends only on the abstract structure of the graph.
- Checking for isomorphism between two graphs is a **computationally hard** problem, as there is no known efficient algorithm to do so.

## Homeomorphism

- Two graphs G and H are **homeomorphic** if there is a graph isomorphism from some **subdivision** of G to some subdivision of H.
- A **subdivision** of a graph is obtained by replacing each edge with a path of one or more edges, without introducing new vertices of degree 2.
- A **homeomorphism** between graphs G and H is a **mapping** f: V(G) → V(H) such that for any two vertices u and v in G, (u, v) is an edge in G if and only if there is a **path** from f(u) to f(v) in H.
- A homeomorphism preserves only **edges** of a graph, but not necessarily non-edges .
- A homeomorphism also preserves the **connectedness** of a graph, but not necessarily the degree of each vertex, the number of components, or the cycle structure.
- Checking for homeomorphism between two graphs is a **computationally easy** problem, as there is a known efficient algorithm to do so.



# Euler and Hamiltonian paths

- Euler and Hamiltonian paths are two types of paths in graphs that have different properties and applications.
- A path in a graph is a sequence of vertices and edges that starts at a vertex and ends at another vertex, such that no edge is repeated.
- A cycle in a graph is a path that starts and ends at the same vertex, such that no edge or vertex (except the first and last) is repeated.

## Euler paths and cycles

- An Euler path is a path that passes through every edge exactly once . If it ends at the initial vertex then it is an Euler cycle .
- An example of an Euler path is shown below:

Euler path

- An example of an Euler cycle is shown below:

Euler cycle

- A graph that has an Euler path or cycle is called an Eulerian graph.
- A necessary and sufficient condition for a graph to be Eulerian is that all its vertices have even degree (number of edges incident to them) .
- This condition can be proved by using the handshaking lemma, which states that the sum of the degrees of all vertices in a graph is equal to twice the number of edges.
- If a graph has an Euler path but not an Euler cycle, then it must have exactly two vertices of odd degree, which are the endpoints of the path .

## Hamiltonian paths and cycles

- A Hamiltonian path is a path that passes through every vertex exactly once (NOT every edge) . If it ends at the initial vertex then it is a Hamiltonian cycle .
- An example of a Hamiltonian path is shown below:

Hamiltonian path

- An example of a Hamiltonian cycle is shown below:

Hamiltonian cycle

- A graph that has a Hamiltonian path or cycle is called a Hamiltonian graph.
- Unlike Euler paths and cycles, there is no simple necessary and sufficient criteria to determine if a graph has a Hamiltonian path or cycle .
- However, there are some sufficient conditions that guarantee the existence of a Hamiltonian path or cycle, such as the following:
  - If a graph is complete (has an edge between every pair of vertices), then it has a Hamiltonian cycle .
  - If a graph has n vertices and the degree of every vertex is at least n/2, then it has a Hamiltonian cycle (Dirac's theorem) .
  - If a graph has n vertices and the sum of the degrees of any two non-adjacent vertices is at least n, then it has a Hamiltonian cycle (Ore's theorem) .
- There are also some necessary conditions that prevent the existence of a Hamiltonian path or cycle, such as the following:
  - If a graph has a vertex of degree 1, then it cannot have a Hamiltonian cycle .
  - If a graph has a cut-vertex (a vertex whose removal disconnects the graph), then it cannot have a Hamiltonian cycle .

## Applications

- Euler and Hamiltonian paths and cycles have various applications in different fields, such as computer science, mathematics, physics, biology, and engineering.
- Some examples of applications are:
  - Finding an optimal route for a traveling salesman, who wants to visit a set of cities and return to the starting point, while minimizing the total distance traveled. This is an example of a Hamiltonian cycle problem, which is known to be NP-hard (no efficient algorithm is known to solve it) .
  - Finding a way to draw a figure without lifting the pen from the paper and without retracing any line. This is an example of an Euler path or cycle problem, which can be solved efficiently using algorithms such as Fleury's algorithm or Hierholzer's algorithm .
  - Finding a way to decompose a graph into cycles, which can be useful for designing circuits, networks,



# Graph coloring

- Graph coloring is the procedure of assigning colors to each vertex of a graph such that no two adjacent vertices have the same color .
- The objective is to minimize the number of colors while coloring a graph .
- The smallest number of colors required to color a graph is called its chromatic number    .
- A graph that can be colored with k colors is called k-colorable .
- A graph that can be colored with two colors is called bipartite  .
- A graph that can be colored with one color is called trivial .
- A proper coloring of a graph is a coloring that uses the minimum number of colors possible .
- An optimal coloring of a graph is a proper coloring that uses the chromatic number of colors .
- A greedy coloring of a graph is a coloring that assigns colors to vertices in some order, using the smallest available color at each step  .
- A greedy coloring is not always optimal, but it gives an upper bound on the chromatic number  .
- Graph coloring has many applications in scheduling, map coloring, register allocation, Sudoku, etc  .



## Unit 8 - Recurrence Relation & Generating function

- A **recurrence relation** is an equation that defines a sequence recursively: each term of the sequence is defined as a function of the preceding terms.
- A **generating function** is a formal power series that encodes the information of a sequence in its coefficients.
- Recurrence relations and generating functions are useful tools for analyzing and solving problems involving discrete structures, such as combinatorics, algorithms, and cryptography.

### Examples of recurrence relations

- The **Fibonacci sequence** is defined by the recurrence relation:

  - F<sub>0</sub> = 0
  - F<sub>1</sub> = 1
  - F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub> for n > 1

- The **factorial function** is defined by the recurrence relation:

  - n! = 1 for n = 0
  - n! = n * (n-1)! for n > 0

- The **Tower of Hanoi** problem is defined by the recurrence relation:

  - T<sub>1</sub> = 1
  - T<sub>n</sub> = 2 * T<sub>n-1</sub> + 1 for n > 1

### Examples of generating functions

- The generating function for the sequence {a<sub>0</sub>, a<sub>1</sub>, a<sub>2</sub>, ...} is:

  - A(x) = a<sub>0</sub> + a<sub>1</sub>x + a<sub>2</sub>x<sup>2</sup> + ...

- The generating function for the Fibonacci sequence is:

  - F(x) = x / (1 - x - x<sup>2</sup>)

- The generating function for the factorial function is:

  - F(x) = e<sup>x</sup>

- The generating function for the Tower of Hanoi problem is:

  - T(x) = (1 - x) / (1 - 2x - x<sup>2</sup>)

### Properties of generating functions

- Generating functions can be manipulated algebraically to obtain new sequences from existing ones.
- Generating functions can be differentiated and integrated term by term to obtain new coefficients.
- Generating functions can be multiplied and divided to obtain convolution and inverse convolution of sequences.
- Generating functions can be used to solve linear recurrence relations with constant coefficients by finding the roots of the characteristic polynomial.



# Recursive definition of functions

- A recursive definition of a function defines values of the function for some inputs in terms of the values of the same function for other (usually smaller) inputs.
- A recursive definition of a function consists of two parts: a base case and a recursive step.
- The base case specifies the value of the function for one or more simple inputs, such as 0 or 1.
- The recursive step specifies how to compute the value of the function for a given input by using the value of the function for a smaller input.
- For example, the factorial function n! is defined by the rules:
  - 0! = 1 (base case)
  - (n + 1)! = (n + 1)· n ! (recursive step)
- A recursive definition of a function is also called a recurrence relation or a recurrence equation.
- A recursive function is a function that calls itself in its definition or implementation.
- A recursive function must have a base case to terminate the recursion, otherwise it will result in an infinite loop or a stack overflow.
- A recursive function can be converted into an equivalent iterative function by using a stack or a loop.
- Recursive functions are a class of functions on the natural numbers studied in computability theory, a branch of mathematical logic.
- Recursive functions are also used to model various phenomena in computer science, such as algorithms, data structures, grammars, and languages.



# Recursive algorithms

A recursive algorithm is an algorithm that calls itself, either directly or indirectly, to solve a smaller instance of the same problem. A recursive algorithm must have a base case, which is a condition that terminates the recursion, and a recursive step, which is a rule that reduces the problem size and makes a recursive call.

## Examples of recursive algorithms

Some examples of problems that can be solved using recursive algorithms are:

- Factorial: The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. A recursive algorithm to compute n! is:

```
factorial(n):
  if n == 0 or n == 1: # base case
    return 1
  else: # recursive step
    return n * factorial(n - 1)
```

- Fibonacci: The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. For example, the first 10 Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34. A recursive algorithm to compute the nth Fibonacci number is:

```
fibonacci(n):
  if n == 0 or n == 1: # base case
    return n
  else: # recursive step
    return fibonacci(n - 1) + fibonacci(n - 2)
```

- Merge sort: Merge sort is a sorting algorithm that divides an array into two halves, recursively sorts each half, and then merges the two sorted halves. A recursive algorithm to perform merge sort is:

```
merge_sort(array):
  if len(array) <= 1: # base case
    return array
  else: # recursive step
    mid = len(array) // 2
    left = merge_sort(array[:mid]) # sort left half
    right = merge_sort(array[mid:]) # sort right half
    return merge(left, right) # merge the two halves
```

- Tower of Hanoi: The Tower of Hanoi is a mathematical puzzle that consists of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending order of size on one rod, the smallest at the top, thus making a conical shape. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:

  - Only one disk can be moved at a time.
  - Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
  - No disk may be placed on top of a smaller disk.

A recursive algorithm to solve the Tower of Hanoi puzzle is:

```
tower_of_hanoi(n, source, destination, auxiliary):
  if n == 1: # base case
    print("Move disk 1 from rod", source, "to rod", destination)
    return
  else: # recursive step
    tower_of_hanoi(n - 1, source, auxiliary, destination) # move n - 1 disks from source to auxiliary
    print("Move disk", n, "from rod", source, "to rod", destination) # move the largest disk from source to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source) # move n - 1 disks from auxiliary to destination
```

## Properties of recursive algorithms

Some properties of recursive algorithms are:

- They are often simpler and more elegant than iterative algorithms, as they express the natural structure of the problem.
- They may use more memory and time than iterative algorithms, as they require additional stack space to store the recursive calls and may perform redundant computations.
- They may cause stack overflow if the recursion is too deep or infinite, or if the base case is not reached or defined.
- They may need to handle special cases or errors, such as negative or invalid inputs, that may cause unexpected or incorrect behavior.



# Method of solving recurrences

- A recurrence relation is an equation that defines a sequence recursively: each term of the sequence is defined as a function of the preceding terms.
- Recurrence relations are often used to model the time complexity of algorithms that use recursion or divide and conquer techniques.
- There are several methods of solving recurrence relations, such as:

  - Forward substitution: This method involves solving the recurrence relation for small values of n until a pattern is observed, then making a guess and proving it by induction.
  - Recursion tree: This method involves drawing a tree that represents the cost of each recursive call, then summing up the costs at each level of the tree and finding a closed-form expression for the total cost.
  - Master method: This method is applicable for recurrence relations of the form T(n) = aT(n/b) + f(n), where a, b, and f(n) are constants or functions of n. The method provides a formula for the asymptotic behavior of T(n) based on the comparison of f(n) and n^(log_b a).
  - Akra-Bazzi method: This method is a generalization of the master method that can handle recurrence relations of the form T(n) = g(n) + \sum_{i=1}^k a_i T(b_i n + h_i(n)), where g(n), a_i, b_i, and h_i(n) are constants or functions of n. The method involves finding a constant p that satisfies a certain equation, then using it to derive the asymptotic behavior of T(n).



## Unit 9 - Combinatorics

Combinatorics is the branch of mathematics that studies the ways of counting, arranging, and selecting objects from a given set or collection. Some of the main topics in combinatorics are:

- **Factorials**: The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. Factorials are useful for counting the number of ways to order or permute a set of objects.
- **Permutations**: A permutation of a set of objects is an ordered arrangement of those objects. For example, the permutations of the set {a, b, c} are abc, acb, bac, bca, cab, and cba. The number of permutations of n distinct objects is n!, and the number of permutations of n objects taken r at a time is nPr = n! / (n - r)!.
- **Combinations**: A combination of a set of objects is an unordered selection of those objects. For example, the combinations of the set {a, b, c} taken two at a time are ab, ac, and bc. The number of combinations of n objects taken r at a time is nCr = n! / (r! x (n - r)!).
- **Binomial theorem**: The binomial theorem is a formula that gives the expansion of a binomial expression raised to a positive integer power. For example, (x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3. The coefficients of the expansion are the binomial coefficients, which can be calculated using the formula nCr or by using Pascal's triangle.
- **Counting principles**: The counting principles are rules that help us count the number of outcomes or events in a given situation. Some of the common counting principles are:
  - **Multiplication principle**: If an event can occur in m ways and another event can occur in n ways, then the number of ways that both events can occur is m x n.
  - **Addition principle**: If an event can occur in m ways or another event can occur in n ways, and the events are mutually exclusive, then the number of ways that either event can occur is m + n.
  - **Inclusion-exclusion principle**: If an event can occur in m ways or another event can occur in n ways, and the events are not mutually exclusive, then the number of ways that either event can occur is m + n - k, where k is the number of ways that both events can occur.
  - **Pigeonhole principle**: If n objects are placed into k boxes, and n > k, then at least one box contains more than one object.



# Introduction for the notes of the Unit 9 - Combinatorics in the subject of Discrete Structures & Theory of Logic

- Combinatorics is the branch of mathematics that studies the ways of arranging objects or selecting subsets of them according to some criteria.
- Combinatorics has applications in many areas of computer science, such as cryptography, coding theory, algorithm design, graph theory, and artificial intelligence.
- Some of the basic concepts and techniques of combinatorics are:

  - The rule of sum and the rule of product, which allow us to count the number of possible outcomes of a compound event by adding or multiplying the number of outcomes of simpler events.
  - The principle of inclusion-exclusion, which allows us to count the number of elements in a union of sets by subtracting the number of elements in their intersections.
  - Permutations and combinations, which allow us to count the number of ways of ordering or selecting a subset of objects from a given set.
  - Binomial coefficients, which are the coefficients of the binomial expansion and can be used to count the number of combinations or subsets of a given size.
  - The pigeonhole principle, which states that if n items are put into m containers, where n > m, then at least one container must contain more than one item. This principle can be used to prove the existence of certain patterns or properties in a set of objects.
  - Recurrence relations, which are equations that define a sequence or a function in terms of its previous terms or values. Recurrence relations can be used to model the growth or decay of a system or a process over time.
  - Generating functions, which are functions that encode the information of a sequence or a series in their coefficients or powers. Generating functions can be used to manipulate, transform, or solve recurrence relations or combinatorial problems.



# Counting Techniques for the notes of the Unit 9 - Combinatorics in the subject of Discrete Structures & Theory of Logic

Combinatorics is the branch of mathematics that deals with the study of finite or countable discrete structures. It includes the enumeration or counting of objects having certain properties, such as arrangements, combinations, permutations, partitions, and selections. Combinatorics methods can be used to solve various problems in computer science, cryptography, probability, graph theory, and algebra.

There are different counting techniques that can be used to count the number of objects in a set or the number of ways to perform a task. Some of the basic counting techniques are:

- **The product rule**: This rule states that if there are $n_1$ ways to do the first task, $n_2$ ways to do the second task, ..., and $n_k$ ways to do the kth task, then there are $n_1 \times n_2 \times ... \times n_k$ ways to do all the tasks in sequence. For example, if there are 10 shirts and 8 pants to choose from, then there are $10 \times 8 = 80$ ways to choose a shirt and a pant.

- **The sum rule**: This rule states that if there are $n_1$ ways to do the first task, $n_2$ ways to do the second task, ..., and $n_k$ ways to do the kth task, and these tasks are mutually exclusive (i.e. they cannot be done at the same time), then there are $n_1 + n_2 + ... + n_k$ ways to do one of the tasks. For example, if there are 5 apples, 4 oranges, and 3 bananas to choose from, then there are $5 + 4 + 3 = 12$ ways to choose one fruit.

- **The factorial**: This is a special notation that represents the product of all positive integers from 1 to a given number. It is denoted by $n!$ and defined as $n! = n \times (n-1) \times ... \times 2 \times 1$. For example, $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$. The factorial can be used to count the number of ways to arrange $n$ distinct objects in a row, which is $n!$. For example, there are $5! = 120$ ways to arrange 5 books on a shelf.

- **The permutation**: This is a way of counting the number of ways to select and arrange $r$ objects from a set of $n$ distinct objects, where the order matters. It is denoted by $P(n,r)$ or $_n P_r$ and defined as $P(n,r) = n! / (n-r)!$. For example, there are $P(5,3) = 5! / (5-3)! = 60$ ways to select and arrange 3 books from 5 books on a shelf.

- **The combination**: This is a way of counting the number of ways to select $r$ objects from a set of $n$ distinct objects, where the order does not matter. It is denoted by $C(n,r)$ or $_n C_r$ or ${n \choose r}$ and defined as $C(n,r) = n! / (r! \times (n-r)!)$. For example, there are $C(5,3) = 5! / (3! \times (5-3)!) = 10$ ways to select 3 books from 5 books on a shelf.

These are some of the basic counting techniques that can be used to solve combinatorics problems. There are also other advanced techniques, such as the inclusion-exclusion principle, the binomial theorem, the pigeonhole principle, and the principle of mathematical induction, that can be used to count more complex situations.



# Pigeonhole Principle

- The pigeonhole principle is a basic concept in combinatorics that states that if n items are put into m containers, with n > m, then at least one container must contain more than one item.
- The principle can be used to prove the existence of certain outcomes without explicitly finding them.
- The principle is also known as the Dirichlet principle, after the German mathematician Peter Gustav Lejeune Dirichlet, who popularized it in the 19th century.
- The principle can be illustrated by a simple example: if you have 10 pigeons and 9 holes, then at least one hole must have more than one pigeon, since 10 is greater than 9.
- The principle can be generalized to different situations, such as:
  - If you have n pigeons in k holes, and n/k is not an integer, then some hole must have strictly more than n/k pigeons.
  - If you have n pigeons in k holes, and n > k(r-1), then some hole must have at least r pigeons.
  - If you have n pigeons in k holes, and n is a multiple of k, then each hole must have exactly n/k pigeons.
- The principle can be applied to various problems in mathematics, such as:
  - If you have 5 socks of 2 colors in a drawer, then you need to pull only 3 socks to get a matching pair.
  - If you have 10 points within a unit equilateral triangle, then there exists two points with distance at most 1/3 apart.
  - If you have 13 cards of the same suit in a standard 52-card deck, then there exists a card rank that appears at least 4 times.

