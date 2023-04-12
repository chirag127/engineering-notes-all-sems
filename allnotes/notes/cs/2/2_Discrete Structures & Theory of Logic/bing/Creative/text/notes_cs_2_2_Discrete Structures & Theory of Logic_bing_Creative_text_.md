

## Unit 1 - Set Theory

- Set theory is a branch of mathematics that studies collections of objects, called sets, and the relationships between them.
- A set is a well-defined collection of distinct objects, which can be anything such as numbers, letters, symbols, or even other sets.
- The objects in a set are called elements or members of the set. We use curly braces { } to enclose the elements of a set, and separate them by commas. For example, {1, 2, 3} is a set with three elements: 1, 2, and 3.
- We can also use a colon : to indicate that the elements of a set satisfy some property or rule. For example, {x : x is an even integer} is the set of all even integers.
- We can use the symbol ∈ to denote that an object is an element of a set, and the symbol ∉ to denote that an object is not an element of a set. For example, 2 ∈ {1, 2, 3} and 4 ∉ {1, 2, 3}.
- Two sets are equal if they have exactly the same elements, regardless of the order or repetition. We use the symbol = to denote equality of sets. For example, {1, 2, 3} = {3, 2, 1} = {1, 1, 2, 3}.
- A set that has no elements is called the empty set, and is denoted by ∅ or { }. For example, {x : x is an odd integer and x is divisible by 4} = ∅.
- A set that contains all the elements of interest in a given context is called the universal set, and is usually denoted by U. For example, if we are studying natural numbers, we can take U = {1, 2, 3, ...}.
- We can use Venn diagrams to represent sets and their relationships visually. A Venn diagram consists of a rectangle that represents the universal set, and circles or other shapes that represent the sets of interest. The elements of a set are usually written inside the corresponding shape, and the elements that are not in any set are written outside the shapes. For example, the following Venn diagram shows the sets A = {1, 2, 3, 4}, B = {3, 4, 5, 6}, and C = {5, 6, 7, 8}.

```markdown
+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
|                                  |
+----------------------------------+
|                                  |
|                                  |
+----------------------------------+
|                                  |
+----------------------------------+

U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {5, 6, 7, 8}

+----------------------------------+
|                                  |
|                                  |
|                                  |
|                                  |
|                                  |
|

```




### Introduction for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- Set theory is a branch of mathematics that studies collections of objects, called sets, and the relationships between them.
- Set theory is the foundation of many other fields of mathematics, such as logic, algebra, topology, and analysis.
- Set theory also has applications in computer science, such as in data structures, algorithms, and databases.
- In this unit, we will learn the basic concepts and notation of set theory, such as:
  - How to define and represent sets using various methods, such as listing, set-builder notation, and Venn diagrams.
  - How to perform operations on sets, such as union, intersection, difference, and complement, and how to use them to express logical statements and properties of sets.
  - How to compare sets using the notions of subset, superset, equality, and cardinality, and how to use them to classify sets into finite, infinite, countable, and uncountable sets.
  - How to construct new sets from existing ones using the principles of power set, Cartesian product, and function, and how to use them to model relations and functions between sets.
  - How to reason about sets using the axioms and theorems of set theory, such as the axiom of extensionality, the axiom of choice, and the Cantor's theorem.



### Combination of sets

- A combination of sets is a new set that is formed by applying some operation on two or more existing sets.
- The most common operations on sets are union, intersection, difference, and complement.
- The union of two sets A and B, denoted by A ∪ B, is the set of all elements that belong to either A or B or both. For example, if A = {1, 2, 3} and B = {3, 4, 5}, then A ∪ B = {1, 2, 3, 4, 5}.
- The intersection of two sets A and B, denoted by A ∩ B, is the set of all elements that belong to both A and B. For example, if A = {1, 2, 3} and B = {3, 4, 5}, then A ∩ B = {3}.
- The difference of two sets A and B, denoted by A - B, is the set of all elements that belong to A but not to B. For example, if A = {1, 2, 3} and B = {3, 4, 5}, then A - B = {1, 2}.
- The complement of a set A, denoted by A', is the set of all elements that belong to the universal set U but not to A. For example, if U = {1, 2, 3, 4, 5, 6} and A = {1, 2, 3}, then A' = {4, 5, 6}.
- The operations on sets can be combined using parentheses and the order of precedence. The order of precedence is: complement, intersection, difference, union. For example, if A = {1, 2, 3}, B = {3, 4, 5}, and C = {5, 6, 7}, then (A ∪ B) ∩ C = {5}, A - (B ∩ C) = {1, 2}, and (A ∩ B)' = {1, 2, 4, 6, 7}.
- The operations on sets can also be represented using Venn diagrams, which are graphical illustrations of sets and their relationships. A Venn diagram consists of a rectangle that represents the universal set U, and circles that represent the subsets of U. The regions inside the circles represent the elements of the subsets, and the regions outside the circles represent the elements of the complements. The operations on sets can be shown by shading or highlighting the regions that correspond to the resulting set. For example, the following Venn diagram shows the union of two sets A and B:

Venn diagram of A union B

- The following Venn diagram shows the intersection of two sets A and B:

Venn diagram of A intersection B

- The following Venn diagram shows the difference of two sets A and B:

Venn diagram of A difference B

- The following Venn diagram shows the complement of a set A:

Venn diagram of A complement



### Multisets

- A multiset is a collection of objects that allows for multiple occurrences of the same element.
- A multiset is also known as a bag or a list.
- A multiset can be represented by listing its elements within curly braces, with the number of repetitions indicated by a superscript. For example, {a, b, b, c, c, c} can be written as {a, b^2, c^3}.
- Alternatively, a multiset can be represented by a function that maps each element to its multiplicity, or the number of times it appears in the multiset. For example, the function f defined by f(a) = 1, f(b) = 2, f(c) = 3, and f(x) = 0 for all other x, represents the same multiset as {a, b^2, c^3}.
- The size of a multiset is the sum of the multiplicities of its elements. For example, the size of {a, b^2, c^3} is 1 + 2 + 3 = 6.
- The empty multiset is the multiset that contains no elements. It is denoted by { } or ∅.
- Two multisets are equal if they have the same elements with the same multiplicities. For example, {a, b, b, c, c, c} = {b, c, c, a, c, b}.
- A multiset A is a subset of a multiset B if every element of A has a multiplicity that is less than or equal to the multiplicity of the same element in B. For example, {a, b, c} is a subset of {a, b^2, c^3}, but {a, b^2, c} is not.
- A multiset A is a proper subset of a multiset B if A is a subset of B and A is not equal to B. For example, {a, b, c} is a proper subset of {a, b^2, c^3}, but {a, b^2, c^3} is not a proper subset of itself.
- The union of two multisets A and B is the multiset that contains every element that appears in either A or B, with the multiplicity equal to the maximum of the multiplicities in A and B. For example, the union of {a, b^2, c^3} and {a^2, b, c^2, d} is {a^2, b^2, c^3, d}.
- The intersection of two multisets A and B is the multiset that contains every element that appears in both A and B, with the multiplicity equal to the minimum of the multiplicities in A and B. For example, the intersection of {a, b^2, c^3} and {a^2, b, c^2, d} is {a, b, c^2}.
- The difference of two multisets A and B is the multiset that contains every element that appears in A but not in B, with the multiplicity equal to the difference of the multiplicities in A and B. For example, the difference of {a, b^2, c^3} and {a^2, b, c^2, d} is {b, c}. Note that the difference is not commutative, as the difference of {a^2, b, c^2, d} and {a, b^2, c^3} is {a, d}.
- The complement of a multiset A with respect to a multiset B is the difference of B and A. For example, the complement of {a, b^2, c^3} with respect to {a^2, b, c^2, d} is {a, d}.
- The Cartesian product of two multisets A and B is the multiset of all ordered pairs (a, b) where a is an element of A and b is an element of B, with the multiplicity equal to the product of the multiplicities in A and B. For example, the Cartesian product of {a, b^2, c^3} and {x, y^2} is {(a, x), (a, y^2), (b, x)^2, (b, y^4), (c, x)^3, (c, y^6)}.
- The power multiset of a multiset A is the multiset of all subsets of A, with the multiplicity equal to the number of ways to form



### Ordered pairs for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- An ordered pair is a pair of two objects that are written inside parentheses and separated by a comma, such as (a, b).
- The order of the objects in an ordered pair is important, as changing the order may result in a different ordered pair, such as (b, a), unless a = b.
- An ordered pair can be used to represent a point on a coordinate plane, where the first object is the x-coordinate and the second object is the y-coordinate, such as (3, -2).
- An ordered pair can also be used to represent an element of a relation or a cartesian product, where the first object is from one set and the second object is from another set, such as (red, circle).
- An ordered pair can be written using any notation, as long as the order and the objects are clear, such as [a, b], {a, b}, <a, b>, or a b. However, the most common notation is (a, b).
- An ordered pair can have any type of objects, such as numbers, variables, symbols, or sets, as long as they are well-defined, such as (2, 5), (x, y), (π, e), or ({1, 2}, {3, 4}).
- An ordered pair can be equal to another ordered pair if and only if both objects are equal, such as (a, b) = (a, b) and (2, 3) = (2, 3), but (a, b) ≠ (b, a) and (2, 3) ≠ (3, 2), unless a = b and 2 = 3.



### Proofs of some general identities on sets

- A set is a collection of distinct objects, such as numbers, letters, or shapes.
- An identity is a statement that is true for any sets involved, such as A ∪ B = B ∪ A, where ∪ denotes the union operation.
- To prove an identity, we need to show that the two sets on either side of the equation are equal, that is, they have the same elements.
- One way to prove an identity is to use the subset method, which involves showing that each set is a subset of the other, that is, every element of one set is also an element of the other.
- Another way to prove an identity is to use the element method, which involves showing that an arbitrary element of one set is also an element of the other, and vice versa.
- Here are some examples of proofs of general identities on sets using both methods:

#### Proof of A ∪ B = B ∪ A using the subset method

- To show that A ∪ B = B ∪ A, we need to show that A ∪ B ⊆ B ∪ A and B ∪ A ⊆ A ∪ B.
- To show that A ∪ B ⊆ B ∪ A, we need to show that for any element x, if x ∈ A ∪ B, then x ∈ B ∪ A.
- Suppose x ∈ A ∪ B. Then x ∈ A or x ∈ B, by the definition of union.
- If x ∈ A, then x ∈ B ∪ A, by the definition of union.
- If x ∈ B, then x ∈ B ∪ A, by the definition of union.
- Therefore, x ∈ B ∪ A, in either case.
- Hence, A ∪ B ⊆ B ∪ A.
- To show that B ∪ A ⊆ A ∪ B, we can use a similar argument, by swapping the roles of A and B.
- Therefore, B ∪ A ⊆ A ∪ B.
- Hence, A ∪ B = B ∪ A, by the definition of set equality.

#### Proof of A ∪ B = B ∪ A using the element method

- To show that A ∪ B = B ∪ A, we need to show that for any element x, x ∈ A ∪ B if and only if x ∈ B ∪ A.
- Suppose x ∈ A ∪ B. Then x ∈ A or x ∈ B, by the definition of union.
- If x ∈ A, then x ∈ B ∪ A, by the definition of union.
- If x ∈ B, then x ∈ B ∪ A, by the definition of union.
- Therefore, x ∈ B ∪ A, in either case.
- Hence, x ∈ A ∪ B implies x ∈ B ∪ A.
- Conversely, suppose x ∈ B ∪ A. Then x ∈ B or x ∈ A, by the definition of union.
- If x ∈ B, then x ∈ A ∪ B, by the definition of union.
- If x ∈ A, then x ∈ A ∪ B, by the definition of union.
- Therefore, x ∈ A ∪ B, in either case.
- Hence, x ∈ B ∪ A implies x ∈ A ∪ B.
- Therefore, x ∈ A ∪ B if and only if x ∈ B ∪ A, by the definition of logical equivalence.
- Hence, A ∪ B = B ∪ A, by the definition of set equality.



### Relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself.
- A relation R on a set A can be represented by a matrix M, where M[i][j] = 1 if (a_i, a_j) is in R and M[i][j] = 0 otherwise, where a_i and a_j are the i-th and j-th elements of A.
- A relation R on a set A can also be represented by a directed graph G, where the vertices are the elements of A and there is an edge from a to b if and only if (a, b) is in R.
- A relation R on a set A is called reflexive if (a, a) is in R for every a in A. A relation R is called irreflexive if (a, a) is not in R for any a in A.
- A relation R on a set A is called symmetric if (a, b) is in R implies (b, a) is in R for every a and b in A. A relation R is called antisymmetric if (a, b) and (b, a) are in R implies a = b for every a and b in A.
- A relation R on a set A is called transitive if (a, b) and (b, c) are in R implies (a, c) is in R for every a, b and c in A.
- A relation R on a set A is called an equivalence relation if it is reflexive, symmetric and transitive. An equivalence relation partitions A into disjoint subsets called equivalence classes, where two elements are in the same equivalence class if and only if they are related by R.
- A relation R on a set A is called a partial order if it is reflexive, antisymmetric and transitive. A partial order induces a hierarchy among the elements of A, where a is said to be less than or equal to b (denoted by a ≤ b) if (a, b) is in R.
- A relation R on a set A is called a total order if it is a partial order and for every a and b in A, either (a, b) or (b, a) is in R. A total order is also called a linear order, as it arranges the elements of A in a line.
- A relation R on a set A is called a function if for every a in A, there is exactly one b in A such that (a, b) is in R. A function is also denoted by f: A -> A, where f(a) = b means (a, b) is in R. A function is called one-to-one (or injective) if f(a) = f(b) implies a = b for every a and b in A. A function is called onto (or surjective) if for every b in A, there is some a in A such that f(a) = b. A function is called bijective if it is both one-to-one and onto. A bijective function is also called a permutation of A, as it rearranges the elements of A.



### Definition for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A **set** is a collection of distinct objects, called **elements** or **members** of the set.
- A set can be defined by listing its elements between curly braces, such as {1, 2, 3}, or by using a rule or a description, such as {x | x is an even positive integer less than 10}.
- Two sets are **equal** if they have exactly the same elements, regardless of the order or repetition of the elements.
- A set is a **subset** of another set if every element of the first set is also an element of the second set. The notation A ⊆ B means that A is a subset of B. Every set is a subset of itself, and the empty set {} is a subset of any set.
- A set is a **proper subset** of another set if it is a subset of the second set and not equal to it. The notation A ⊂ B means that A is a proper subset of B.
- The **union** of two sets A and B, denoted by A ∪ B, is the set of all elements that belong to either A or B or both.
- The **intersection** of two sets A and B, denoted by A ∩ B, is the set of all elements that belong to both A and B.
- The **difference** of two sets A and B, denoted by A - B, is the set of all elements that belong to A but not to B.
- The **complement** of a set A, denoted by A<sup>c</sup> or A', is the set of all elements that do not belong to A. The complement of A is relative to some universal set U, which contains all the elements under consideration.
- Two sets are **disjoint** if they have no elements in common, that is, their intersection is the empty set.
- The **cardinality** of a set A, denoted by |A|, is the number of elements in A. The cardinality of the empty set is zero.
- A set is **finite** if it has a finite number of elements, and **infinite** otherwise.
- A **power set** of a set A, denoted by P(A), is the set of all subsets of A, including the empty set and A itself. The cardinality of the power set of A is 2<sup>|A|</sup>.
- A **Cartesian product** of two sets A and B, denoted by A × B, is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B. The Cartesian product of A and B is not equal to the Cartesian product of B and A, unless A and B are equal sets. The cardinality of the Cartesian product of A and B is |A| × |B|.



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



### Properties of relations

- A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself.
- A relation R on a set A can have some properties that describe how the elements of A are related to each other. Some common properties are:
  - Reflexive: A relation R on a set A is reflexive if for every element a in A, (a, a) belongs to R. This means that every element is related to itself.
  - Symmetric: A relation R on a set A is symmetric if for every pair of elements (a, b) in R, (b, a) also belongs to R. This means that the order of the elements does not matter in the relation.
  - Transitive: A relation R on a set A is transitive if for every pair of elements (a, b) and (b, c) in R, (a, c) also belongs to R. This means that if one element is related to another, and the second element is related to a third, then the first element is also related to the third.
  - Antisymmetric: A relation R on a set A is antisymmetric if for every pair of elements (a, b) and (b, a) in R, a = b. This means that the only way two elements can be related in both directions is if they are equal.
  - Irreflexive: A relation R on a set A is irreflexive if for every element a in A, (a, a) does not belong to R. This means that no element is related to itself.
  - Asymmetric: A relation R on a set A is asymmetric if for every pair of elements (a, b) in R, (b, a) does not belong to R. This means that the order of the elements matters in the relation, and no element can be related to itself.
  - Equivalence: A relation R on a set A is an equivalence relation if it is reflexive, symmetric, and transitive. This means that the relation partitions A into disjoint subsets, called equivalence classes, such that every element in a class is related to every other element in the same class, and no element in a class is related to any element in a different class.
  - Partial order: A relation R on a set A is a partial order if it is reflexive, antisymmetric, and transitive. This means that the relation imposes a hierarchy on A, such that some elements are comparable and some are not, and there is no circularity in the relation. A partial order can be represented by a Hasse diagram, which is a graph that shows the elements of A as nodes and the relation R as edges, omitting the reflexive and transitive edges.
  - Total order: A relation R on a set A is a total order if it is a partial order and for every pair of elements a and b in A, either (a, b) or (b, a) belongs to R. This means that the relation imposes a linear order on A, such that every element is comparable to every other element, and there is no ambiguity in the relation. A total order can be represented by a line, where the elements of A are arranged from left to right according to the relation R.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of composite relations:

### Composite Relations

- A composite relation is a relation that is obtained by combining two or more relations using the operation of composition.
- The composition of two relations R and S is denoted by R ∘ S and is defined as follows:

  - R ∘ S = {(a, c) | ∃b such that (a, b) ∈ R and (b, c) ∈ S}

  - In other words, R ∘ S is the set of ordered pairs (a, c) such that there exists an element b that is related to both a and c by R and S, respectively.

- For example, if R = {(1, 2), (2, 3), (3, 4)} and S = {(2, 5), (3, 6), (4, 7)}, then R ∘ S = {(1, 5), (1, 6), (2, 6), (2, 7), (3, 7)}.

- The composition of relations is not commutative, that is, R ∘ S ≠ S ∘ R in general.
- The composition of relations is associative, that is, (R ∘ S) ∘ T = R ∘ (S ∘ T) for any three relations R, S, and T.
- The composition of relations can be used to model various scenarios, such as:

  - The transitive closure of a relation R, denoted by R+, is the smallest relation that contains R and is transitive. It can be obtained by taking the union of R, R ∘ R, R ∘ R ∘ R, and so on.

  - The equivalence relation generated by a relation R, denoted by R*, is the smallest relation that contains R and is reflexive, symmetric, and transitive. It can be obtained by taking the union of R, R ∘ R, R ∘ R ∘ R, R ∘ R ∘ R ∘ R, and so on, along with the identity relation I.

  - The functional dependency of a relation R, denoted by R → S, is a relation that indicates that for any two tuples x and y in R, if x and y agree on the attributes in S, then they also agree on the attributes in R. It can be obtained by taking the intersection of R and S ∘ R.



### Equality of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself.
- Two relations R and S on a set A are equal if and only if they have the same elements, that is, R = S if and only if R ⊆ S and S ⊆ R.
- The equality of relations is reflexive, symmetric and transitive, meaning that for any relations R, S and T on a set A, the following properties hold:
  - R = R (reflexivity)
  - If R = S, then S = R (symmetry)
  - If R = S and S = T, then R = T (transitivity)
- The equality of relations is also an equivalence relation, meaning that it partitions the set of all relations on A into equivalence classes, where each class contains all the relations that are equal to each other.
- An example of an equivalence class of relations on a set A = {1, 2, 3} is the class of all reflexive relations on A, which contains the following four relations:
  - R1 = {(1, 1), (2, 2), (3, 3)}
  - R2 = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1)}
  - R3 = {(1, 1), (2, 2), (3, 3), (1, 3), (3, 1)}
  - R4 = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (1, 3), (3, 1)}
- All these relations are equal to each other because they have the same reflexive pairs, and any other relation on A that has the same reflexive pairs will also belong to this class.



### Recursive definition of relation

- A relation is a set of ordered pairs that satisfies some property or condition.
- A recursive definition of a relation consists of two parts: a base case and a recursive step.
- A base case specifies one or more ordered pairs that belong to the relation.
- A recursive step specifies a rule that generates new ordered pairs from the existing ones.
- A recursive definition of a relation is complete if every ordered pair in the relation can be obtained by applying the base case and the recursive step finitely many times.

#### Example 1: The relation "is a multiple of" on the set of natural numbers

- Base case: (0, n) belongs to the relation for any natural number n.
- Recursive step: If (a, b) belongs to the relation, then (a + b, b) also belongs to the relation.
- This means that a is a multiple of b if and only if a can be obtained by adding b to itself zero or more times.

#### Example 2: The relation "is an ancestor of" on the set of people

- Base case: (p, q) belongs to the relation if p is a parent of q.
- Recursive step: If (p, q) and (q, r) belong to the relation, then (p, r) also belongs to the relation.
- This means that p is an ancestor of r if and only if p is a parent of q and q is an ancestor of r.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of order of relations for the notes of the unit 1 - set theory in the subject of discrete structures and theory of logic.

### Order of relations

- A relation R on a set A is called an **order relation** or a **partial order** if it satisfies the following properties for all x, y, and z in A:
  - **Reflexivity**: xRx
  - **Antisymmetry**: if xRy and yRx, then x = y
  - **Transitivity**: if xRy and yRz, then xRz
- An order relation is also called a **partial order** because it may not compare every pair of elements in A. For example, the relation of "divides" on the set of positive integers is a partial order, but it does not compare 2 and 3, since neither 2 divides 3 nor 3 divides 2.
- A set A with a partial order R is called a **partially ordered set** or a **poset**, denoted by (A, R).
- A partial order R on a set A is called a **total order** or a **linear order** if it also satisfies the following property for all x and y in A:
  - **Comparability**: either xRy or yRx
- A total order is also called a **linear order** because it arranges the elements of A in a linear sequence, such as the usual order of numbers or alphabets. For example, the relation of "less than or equal to" on the set of real numbers is a total order.
- A set A with a total order R is called a **totally ordered set** or a **chain**, denoted by (A, R).
- A subset B of a poset (A, R) is called a **chain** if (B, R) is a totally ordered set. For example, the set {1, 2, 4, 8} is a chain in the poset of positive integers with the relation of "divides".
- A subset B of a poset (A, R) is called an **antichain** if no two distinct elements of B are comparable by R. For example, the set {2, 3, 5, 7} is an antichain in the poset of positive integers with the relation of "divides".
- A relation R on a set A is called a **strict partial order** if it satisfies the following properties for all x, y, and z in A:
  - **Irreflexivity**: not xRx
  - **Asymmetry**: if xRy, then not yRx
  - **Transitivity**: if xRy and yRz, then xRz
- A strict partial order is a partial order without reflexivity and antisymmetry. For example, the relation of "less than" on the set of real numbers is a strict partial order.
- A relation R on a set A is called a **strict total order** or a **linear order** if it is a strict partial order and it also satisfies the following property for all x and y in A:
  - **Comparability**: either xRy or yRx
- A strict total order is a total order without reflexivity and antisymmetry. For example, the relation of "less than" on the set of real numbers is a strict total order.



### Functions

- A function is a special kind of relation that assigns a unique output to each input.
- A function can be represented by a set of ordered pairs, a table, a graph, or a formula.
- A function in set theory is simply a mapping of some (or all) elements from one set, called the domain, to some (or all) elements in another set, called the codomain  .
- The set of all possible outputs of a function is called the range, which is a subset of the codomain.
- A function can be written as f: A -> B, where f is the name of the function, A is the domain, and B is the codomain.
- The notation f(a) = b means that the function f maps the element a in the domain to the element b in the codomain.
- A function is said to be well-defined if it assigns a unique output to each input, that is, if f(a) = b and f(a) = c, then b = c.
- A function is said to be one-to-one (or injective) if it maps different inputs to different outputs, that is, if f(a) = f(b), then a = b.
- A function is said to be onto (or surjective) if it maps every element in the codomain to some element in the domain, that is, for every b in B, there exists some a in A such that f(a) = b.
- A function is said to be bijective (or invertible) if it is both one-to-one and onto, that is, it establishes a one-to-one correspondence between the elements of the domain and the codomain.
- A function that is bijective has an inverse function, denoted by f^-1, that reverses the mapping of f, that is, f^-1(f(a)) = a and f(f^-1(b)) = b for all a in A and b in B.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Discrete Structures & Theory of Logic. Here are some definitions for the notes of Unit 1 - Set Theory.

### Definition for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A **set** is a collection of distinct objects, called **elements** or **members** of the set. A set can be represented by listing its elements between braces, such as {1, 2, 3}, or by using a rule or a description, such as {x | x is an even positive integer less than 10}.
- A set is said to be **well-defined** if there is a clear criterion to determine whether an object belongs to the set or not. For example, the set of all prime numbers is well-defined, but the set of all interesting numbers is not well-defined.
- Two sets are **equal** if they have exactly the same elements. For example, {1, 2, 3} = {3, 2, 1}, but {1, 2, 3} ≠ {1, 2, 4}.
- A set is a **subset** of another set if every element of the first set is also an element of the second set. For example, {1, 2} is a subset of {1, 2, 3}, but {1, 4} is not a subset of {1, 2, 3}. We use the symbol ⊆ to denote subset, and ⊂ to denote proper subset (a subset that is not equal to the original set).
- A set is **empty** if it has no elements. The empty set is denoted by ∅ or {}. The empty set is a subset of every set.
- The **union** of two sets is the set of all elements that belong to either set or both. For example, {1, 2, 3} ∪ {3, 4, 5} = {1, 2, 3, 4, 5}. The union of a set and the empty set is the original set.
- The **intersection** of two sets is the set of all elements that belong to both sets. For example, {1, 2, 3} ∩ {3, 4, 5} = {3}. The intersection of a set and the empty set is the empty set.
- The **difference** of two sets is the set of all elements that belong to the first set but not to the second set. For example, {1, 2, 3} - {3, 4, 5} = {1, 2}. The difference of a set and the empty set is the original set.
- The **complement** of a set is the set of all elements that do not belong to the set. The complement of a set is relative to a **universal set**, which is the set of all possible elements under consideration. For example, if the universal set is {1, 2, 3, 4, 5}, then the complement of {1, 2, 3} is {4, 5}. The complement of a set is denoted by a bar over the set, such as Ā.
- Two sets are **disjoint** if they have no elements in common. For example, {1, 2, 3} and {4, 5, 6} are disjoint, but {1, 2, 3} and {3, 4, 5} are not disjoint. The empty set is disjoint from every set.
- The **cardinality** of a set is the number of elements in the set. For example, the cardinality of {1, 2, 3} is 3, and the cardinality of the empty set is 0. The cardinality of a set is denoted by |A| or #A.
- A set is **finite** if it has a finite number of elements, and **infinite** otherwise. For example, {1, 2, 3} is finite, but the set of all natural numbers is infinite. An infinite set can be **countable** or **uncountable**, depending on whether its elements can be listed in a sequence or not. For example, the set of all natural numbers is countable, but the set of all real numbers is uncountable.



### Classification of functions for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A function is a relation between two sets that assigns exactly one element of the second set to each element of the first set.
- The first set is called the domain of the function and the second set is called the codomain of the function.
- The set of all elements of the codomain that are assigned by the function is called the range of the function.
- A function can be represented by a set of ordered pairs, a table, a graph, or a formula.
- Functions can be classified into different types based on their properties, such as:

  - Injective functions: A function is injective (or one-to-one) if it assigns different elements of the codomain to different elements of the domain. That is, no two distinct elements of the domain have the same image in the codomain.
  - Surjective functions: A function is surjective (or onto) if it assigns every element of the codomain to some element of the domain. That is, the range of the function is equal to the codomain.
  - Bijective functions: A function is bijective (or one-to-one and onto) if it is both injective and surjective. That is, it assigns every element of the codomain to a unique element of the domain.
  - Inverse functions: A function has an inverse function if there exists another function that reverses the effect of the original function. That is, for every pair of elements (x, y) in the original function, there is a pair of elements (y, x) in the inverse function. An inverse function exists if and only if the original function is bijective.
  - Identity functions: An identity function is a function that assigns every element of a set to itself. That is, for every element x in the set, the function maps x to x. An identity function is bijective and its own inverse.
  - Constant functions: A constant function is a function that assigns the same element of the codomain to every element of the domain. That is, for every element x in the domain, the function maps x to a fixed element c in the codomain. A constant function is neither injective nor surjective, unless the domain and the codomain are both singleton sets.
  - Linear functions: A linear function is a function that can be expressed by the formula f(x) = ax + b, where a and b are constants. A linear function is injective if and only if a is not zero, and surjective if and only if the codomain is the set of all real numbers.
  - Quadratic functions: A quadratic function is a function that can be expressed by the formula f(x) = ax^2 + bx + c, where a, b, and c are constants. A quadratic function is neither injective nor surjective, unless the domain and the codomain are both singleton sets.



### Operations on functions

- A function is a relation that assigns to each element of a set A (called the domain) exactly one element of a set B (called the codomain).
- A function can be represented by a set of ordered pairs, a table, a graph, or a formula.
- The notation f: A -> B means that f is a function from A to B.
- The notation f(a) = b means that b is the value of the function f at a, or the image of a under f.
- The notation f(A) = {f(a) | a in A} means the image of the set A under f, or the set of all values of f at elements of A.
- The notation f^-1(b) = {a in A | f(a) = b} means the preimage of b under f, or the set of all elements of A that map to b under f.
- The notation f^-1(B) = {a in A | f(a) in B} means the preimage of the set B under f, or the set of all elements of A that map to elements of B under f.

Some common operations on functions are:

- Composition: The composition of two functions f and g, denoted by f o g, is the function that maps x to f(g(x)). That is, f o g(x) = f(g(x)) for all x in the domain of g. The domain of f o g is the set of all x in the domain of g such that g(x) is in the domain of f.
- Inverse: The inverse of a function f, denoted by f^-1, is the function that maps y to x if and only if f(x) = y. That is, f^-1(y) = x if and only if f(x) = y for all x in the domain of f and y in the codomain of f. The inverse of f exists if and only if f is one-to-one and onto, meaning that f maps each element of A to a unique element of B and covers all elements of B. The domain of f^-1 is the codomain of f, and the codomain of f^-1 is the domain of f. The inverse of f satisfies the property that f o f^-1 = f^-1 o f = I, where I is the identity function that maps x to x.
- Restriction: The restriction of a function f to a subset A of its domain, denoted by f|A, is the function that maps x to f(x) for all x in A. That is, f|A(x) = f(x) for all x in A. The domain of f|A is A, and the codomain of f|A is the same as the codomain of f. The restriction of f to A is a function from A to B.
- Extension: The extension of a function f from a subset A of a set X to the whole set X, denoted by f^X, is the function that maps x to f(x) for all x in A, and to some arbitrary value for all x in X - A. That is, f^X(x) = f(x) for all x in A, and f^X(x) = c for some constant c for all x in X - A. The domain of f^X is X, and the codomain of f^X is the same as the codomain of f. The extension of f from A to X is a function from X to B.



### Recursively defined functions for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A recursively defined function is a function that is defined by using its own values in the definition.
- A recursively defined function has two parts: a base case and a recursive step.
- The base case specifies the value of the function for one or more initial inputs, usually the smallest or simplest ones.
- The recursive step specifies how to compute the value of the function for any other input, using the values of the function for smaller or simpler inputs.
- A recursively defined function must have a well-defined domain, which is the set of all possible inputs for which the function is defined.
- A recursively defined function must also satisfy the principle of mathematical induction, which states that if the base case is true and the recursive step is true for any input, then the function is true for all inputs in the domain.
- An example of a recursively defined function is the factorial function, which is defined as follows:

  - Base case: `n! = 1` for `n = 0`
  - Recursive step: `n! = n * (n-1)!` for `n > 0`
  - Domain: `n` is a non-negative integer
  - Induction: The base case is true, and the recursive step is true for any `n > 0`, since `(n-1)!` is already defined by the function. Therefore, the function is true for all non-negative integers.

- Another example of a recursively defined function is the Fibonacci sequence, which is defined as follows:

  - Base case: `F(0) = 0` and `F(1) = 1`
  - Recursive step: `F(n) = F(n-1) + F(n-2)` for `n > 1`
  - Domain: `n` is a non-negative integer
  - Induction: The base case is true, and the recursive step is true for any `n > 1`, since `F(n-1)` and `F(n-2)` are already defined by the function. Therefore, the function is true for all non-negative integers.



### Growth of Functions

- The growth of a function is a measure of how fast its output value increases as its input value becomes larger.
- The growth of a function is determined by the highest order term: if you add a bunch of terms, the function grows about as fast as the largest term (for large enough input values).
- For example, f(x) = x^2 + 1 grows as fast as g(x) = x^2 + 2 and h(x) = x^2 + x + 1, because for large x, x^2 is much bigger than 1, 2, or x + 1.
- The growth of functions is often described using a special notation – the Big-O Notation, Big-Omega Notation, and Big-Theta Notation. Theses special notations estimate the growth of the function by comparing it to another simpler function.
- Big-O Notation: We say f(x) is O(g(x)) if there are constants C and k such that |f(x)| <= C|g(x)| whenever x > k. In other words, Big-O is the upper bound for the growth of the function.
- Big-Omega Notation: We say f(x) is Omega(g(x)) if there are constants C and k such that |f(x)| >= C|g(x)| whenever x > k. In other words, Big-Omega is the lower bound for the growth of the function.
- Big-Theta Notation: We say f(x) is Theta(g(x)) if there are constants C1, C2 and k such that C1|g(x)| <= |f(x)| <= C2|g(x)| whenever x > k. In other words, Big-Theta is the tight bound for the growth of the function.
- For example, f(x) = 3x^2 + 5x + 2 is O(x^2), Omega(x^2), and Theta(x^2), because we can choose appropriate constants C, C1, C2 and k to satisfy the inequalities.
- The growth of functions is important for analyzing the efficiency and complexity of algorithms, as it gives an estimate of how the running time or space requirement of an algorithm changes with the size of the input.



### Natural Numbers

- Natural numbers are the counting numbers, such as 1, 2, 3, 4, 5, etc.
- Natural numbers are denoted by the symbol **N**.
- Natural numbers are a subset of the integers, which are a subset of the rational numbers, which are a subset of the real numbers.
- Natural numbers have the following properties:
  - They are **ordered**, meaning that there is a first natural number (1), a second natural number (2), and so on, and that any two natural numbers can be compared using the symbols <, >, or =.
  - They are **closed** under addition and multiplication, meaning that the sum or product of any two natural numbers is also a natural number.
  - They have an **identity element** for both addition and multiplication, meaning that there is a natural number (0) that when added or multiplied to any natural number gives the same natural number as the result.
  - They have an **associative property** for both addition and multiplication, meaning that the order of grouping natural numbers does not affect the result of adding or multiplying them.
  - They have a **commutative property** for both addition and multiplication, meaning that the order of natural numbers does not affect the result of adding or multiplying them.
  - They have a **distributive property** of multiplication over addition, meaning that multiplying a natural number by the sum of two natural numbers is the same as multiplying the natural number by each of the two natural numbers and then adding the results.
- Natural numbers do not have the following properties:
  - They are not **closed** under subtraction and division, meaning that the difference or quotient of any two natural numbers may not be a natural number.
  - They do not have an **inverse element** for either subtraction or division, meaning that there is no natural number that when subtracted or divided from any natural number gives the identity element (0) as the result.
  - They do not have a **subtraction property** of equality, meaning that subtracting the same natural number from both sides of an equation may not preserve the truth value of the equation.
  - They do not have a **division property** of equality, meaning that dividing both sides of an equation by the same nonzero natural number may not preserve the truth value of the equation.



### Introduction for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- Set theory is a branch of mathematics that studies collections of objects, called sets, and the relationships between them.
- A set is a well-defined collection of distinct objects, which can be anything such as numbers, letters, symbols, or even other sets.
- The objects in a set are called elements or members of the set. We use curly braces { } to enclose the elements of a set, and separate them by commas. For example, {1, 2, 3} is a set with three elements: 1, 2, and 3.
- We can also use a rule or a description to define a set, as long as it is clear and unambiguous. For example, {x | x is a positive integer less than 10} is a set with nine elements: 1, 2, 3, 4, 5, 6, 7, 8, and 9.
- We can use the symbol ∈ to denote that an object is an element of a set, and the symbol ∉ to denote that an object is not an element of a set. For example, 4 ∈ {1, 2, 3, 4} and 5 ∉ {1, 2, 3, 4}.
- We can use the symbol = to denote that two sets have exactly the same elements, and the symbol ≠ to denote that two sets have at least one different element. For example, {1, 2, 3} = {3, 2, 1} and {1, 2, 3} ≠ {1, 2, 4}.
- There are some special sets that are commonly used in mathematics, such as the empty set, the universal set, and the sets of natural numbers, integers, rational numbers, real numbers, and complex numbers. We will learn more about these sets in the following sections.
- Set theory is the foundation of many other branches of mathematics, such as logic, algebra, geometry, topology, and analysis. It also has applications in computer science, such as data structures, algorithms, databases, and cryptography.



### Mathematical Induction

- Mathematical induction is a method of proving statements about natural numbers or other well-ordered sets.
- The basic principle of mathematical induction is that if a statement is true for some initial value and if it remains true when the value is increased by one, then it is true for all values in the set.
- The steps of mathematical induction are as follows:
  - **Base case**: Show that the statement is true for the smallest or first value in the set, usually denoted by n = 1 or n = 0.
  - **Inductive hypothesis**: Assume that the statement is true for some arbitrary value n = k, where k is a natural number or an element of the set.
  - **Inductive step**: Show that the statement is true for the next value n = k + 1, using the inductive hypothesis and logical reasoning.
  - **Conclusion**: By the principle of mathematical induction, the statement is true for all values of n in the set.
- An example of mathematical induction is to prove that the sum of the first n natural numbers is n(n + 1) / 2 for all n ≥ 1.
  - **Base case**: When n = 1, the sum of the first natural number is 1, which is equal to 1(1 + 1) / 2. Hence, the statement is true for n = 1.
  - **Inductive hypothesis**: Assume that the statement is true for some arbitrary value n = k, that is, the sum of the first k natural numbers is k(k + 1) / 2.
  - **Inductive step**: We need to show that the statement is true for n = k + 1, that is, the sum of the first k + 1 natural numbers is (k + 1)((k + 1) + 1) / 2. Using the inductive hypothesis, we can write the sum of the first k + 1 natural numbers as follows:

    ```
    1 + 2 + ... + k + (k + 1) = (k(k + 1) / 2) + (k + 1)
                             = (k + 1)(k / 2 + 1)
                             = (k + 1)((k + 1) + 1) / 2
    ```

    Hence, the statement is true for n = k + 1.
  - **Conclusion**: By the principle of mathematical induction, the statement is true for all n ≥ 1.



### Variants of Induction for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- Induction is a method of proving statements about sets that are well-ordered, meaning that every non-empty subset has a least element.
- There are different variants of induction, depending on the type of set and the relation that orders it.
- Some common variants of induction are:

  - **Ordinary induction**: This is the induction on the set of natural numbers, ordered by the usual less than relation. The principle of ordinary induction states that if a statement P(n) is true for n = 0 (base case) and for n = k implies P(k+1) (inductive step), then P(n) is true for all natural numbers n.
  - **Transfinite induction**: This is the induction on the set of ordinal numbers, ordered by the usual less than relation. The principle of transfinite induction states that if a statement P(α) is true for α = 0 (base case) and for all ordinals β < α implies P(β) (inductive step), then P(α) is true for all ordinals α.
  - **Structural induction**: This is the induction on the set of terms or expressions that are built from some basic symbols and some rules of formation. The principle of structural induction states that if a statement P(t) is true for all basic terms t (base case) and for all terms t that are formed by applying a rule to some terms s1, ..., sn implies P(t) (inductive step), then P(t) is true for all terms t.
  - **Well-founded induction**: This is the induction on any set that is well-ordered by some relation R. The principle of well-founded induction states that if a statement P(x) is true for all x that have no R-predecessors (base case) and for all x that have R-predecessors y1, ..., yn implies P(y1), ..., P(yn) and P(x) (inductive step), then P(x) is true for all x in the set.

- All variants of induction are special cases of well-founded induction, which is the most general form of induction.



### Induction with Nonzero Base cases

- Induction is a method of mathematical proof that can be used to show that a statement is true for all natural numbers, or for all elements of a well-ordered set.
- The basic idea of induction is to start with a base case, where the statement is true for some initial value, and then show that if the statement is true for any value, it is also true for the next value. This is called the inductive step.
- By applying the inductive step repeatedly, we can conclude that the statement is true for all values that come after the base case.
- Sometimes, the base case is not zero, but some other value. For example, we may want to prove a statement for all natural numbers greater than or equal to 10, or for all positive integers that are multiples of 3.
- In such cases, we can still use induction, but we need to adjust the base case and the inductive step accordingly.
- The general form of induction with nonzero base cases is as follows:

  - Let P(n) be a statement involving a natural number n.
  - Let k be a fixed natural number, such that P(k) is true. This is the base case.
  - Assume that P(n) is true for some arbitrary natural number n ≥ k. This is the induction hypothesis.
  - Show that P(n+1) is true, using the induction hypothesis. This is the inductive step.
  - Conclude that P(n) is true for all natural numbers n ≥ k, by the principle of mathematical induction.

- Here is an example of induction with nonzero base cases:

  - Let P(n) be the statement that 2^n > n + 10, for any natural number n.
  - We want to prove that P(n) is true for all natural numbers n ≥ 4.
  - The base case is n = 4. We can check that P(4) is true, since 2^4 = 16 > 4 + 10 = 14.
  - The inductive step is to assume that P(n) is true for some arbitrary natural number n ≥ 4, and show that P(n+1) is true.
  - We have P(n) : 2^n > n + 10, by the induction hypothesis.
  - We want to show P(n+1) : 2^(n+1) > (n+1) + 10.
  - We can start from the left-hand side of P(n+1) and manipulate it as follows:

    - 2^(n+1) = 2 * 2^n > 2 * (n + 10), by P(n)
    - 2 * (n + 10) = 2n + 20 > n + 11, by simple algebra
    - n + 11 = (n + 1) + 10, by simple algebra

  - Therefore, 2^(n+1) > (n + 1) + 10, which is P(n+1).
  - We have shown the inductive step, so we can conclude that P(n) is true for all natural numbers n ≥ 4, by the principle of mathematical induction.



### Proof Methods

A proof is a logical argument that establishes the validity of a mathematical statement. There are different methods of proof, depending on the type and structure of the statement. Some of the common proof methods are:

- **Direct proof**: A direct proof shows that a statement of the form "if p, then q" is true by assuming that p is true and then using logical rules and definitions to show that q must also be true. For example, to prove that if n is an even integer, then n^2 is also even, we can assume that n is even and write n = 2k for some integer k. Then, n^2 = (2k)^2 = 4k^2 = 2(2k^2), which is also even by definition.

- **Indirect proof**: An indirect proof shows that a statement of the form "if p, then q" is true by assuming that q is false and then using logical rules and definitions to show that p must also be false. This is also known as proof by contrapositive, since it proves the contrapositive statement "if not q, then not p". For example, to prove that if n^2 is odd, then n is odd, we can assume that n is even and write n = 2k for some integer k. Then, n^2 = (2k)^2 = 4k^2, which is even, contradicting the assumption that n^2 is odd. Therefore, if n^2 is odd, then n must be odd.

- **Proof by contradiction**: A proof by contradiction shows that a statement p is true by assuming that p is false and then using logical rules and definitions to show that this leads to a contradiction, which means that the assumption was wrong and p must be true. For example, to prove that √2 is irrational, we can assume that √2 is rational and write √2 = a/b for some integers a and b with no common factors. Then, squaring both sides and rearranging, we get 2b^2 = a^2, which implies that a^2 is even. By the previous direct proof, this means that a is even, and we can write a = 2k for some integer k. Substituting this into the equation, we get 2b^2 = (2k)^2, which simplifies to b^2 = 2k^2, which implies that b^2 is even. By the same direct proof, this means that b is even, which contradicts the assumption that a and b have no common factors. Therefore, √2 cannot be rational and must be irrational.

- **Proof by cases**: A proof by cases shows that a statement p is true by dividing the possible cases of p into mutually exclusive and exhaustive subcases and then proving each subcase separately. For example, to prove that for any integer n, n^3 + 5 is divisible by 6, we can consider the two possible cases of n: n is even or n is odd. If n is even, then n^3 is also even, and n^3 + 5 is odd. By the division algorithm, we can write n^3 + 5 = 6q + r for some integers q and r, where 0 ≤ r < 6. Since n^3 + 5 is odd, r must be odd as well, and the only possible values of r are 1, 3, or 5. However, none of these values satisfy the equation n^3 + 5 = 6q + r, since n^3 is a multiple of 4 and 6q is a multiple of 6. Therefore, there is no remainder and n^3 + 5 is divisible by 6. If n is odd, then n^3 is also odd, and n^3 + 5 is even. By the same division algorithm, we can write n^3 + 5 = 6q + r for some integers q and r, where 0 ≤ r < 6. Since n^3 + 5 is even, r must be even as well, and the only possible values of r are 0, 2, or 4. However, none of these values satisfy the equation n^3 + 5 = 6q + r, since n^3 is one more than a multiple of 8 and 6q is a multiple of 6. Therefore, there is no remainder and n^3 + 5 is divisible by 6. Since we have covered all possible cases of n, we have proved that for any integer n, n^3 +



### Proof by counter – example for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A proof by counter-example is a method of disproving a universal statement by providing a specific instance that contradicts it.
- A universal statement is a statement that claims something is true for all elements of a certain set or domain, such as "all natural numbers are even" or "all dogs are mammals".
- A counter-example is an element of the set or domain that does not satisfy the statement, such as 3 for the first statement or a platypus for the second statement.
- To prove a statement by counter-example, one must show that the statement is false for at least one element of the set or domain, and that the element is indeed a member of the set or domain.
- A proof by counter-example can only be used to disprove a universal statement, not to prove an existential statement (a statement that claims something is true for at least one element of a set or domain).
- A proof by counter-example is usually easier and shorter than a direct proof or a proof by contradiction, but it may not always be possible to find a counter-example for a false statement.
- A proof by counter-example is also known as a refutation or a falsification.



### Proof by contradiction

- A proof by contradiction is a method of proving a statement by assuming that it is false and deriving a contradiction from that assumption.
- The contradiction can be a logical inconsistency, a violation of a known fact, or a self-contradictory statement.
- The contradiction shows that the initial assumption was wrong, and therefore the statement that was assumed to be false must be true.
- A proof by contradiction can be written in the following form:

  - Suppose that statement P is false, that is, ¬P is true.
  - Show that ¬P implies Q, where Q is a contradiction.
  - Conclude that ¬P is false, and therefore P is true.

- For example, to prove that √2 is irrational, we can use a proof by contradiction as follows:

  - Suppose that √2 is rational, that is, √2 = a/b, where a and b are integers with no common factors.
  - Squaring both sides, we get 2 = a^2 / b^2, or 2b^2 = a^2.
  - This implies that a^2 is even, and therefore a is even, that is, a = 2k for some integer k.
  - Substituting a = 2k into 2b^2 = a^2, we get 2b^2 = 4k^2, or b^2 = 2k^2.
  - This implies that b^2 is even, and therefore b is even, that is, b = 2l for some integer l.
  - But then a and b have a common factor of 2, which contradicts the assumption that they have no common factors.
  - Therefore, the assumption that √2 is rational is false, and √2 is irrational.



## Unit 2 - Algebraic Structures

- An algebraic structure is a set of elements with one or more operations defined on it that satisfy certain properties or axioms.
- Examples of algebraic structures are groups, rings, fields, vector spaces, matrices, etc.
- The most basic algebraic structure is a group, which is a set with a binary operation that is associative, has an identity element, and has an inverse for every element.
- A ring is a set with two binary operations, usually called addition and multiplication, that satisfy the properties of a group under addition, and are associative and distributive under both operations.
- A field is a ring with the additional property that every nonzero element has a multiplicative inverse, i.e., it is a group under both addition and multiplication.
- A vector space is a set of elements, called vectors, with two operations, usually called addition and scalar multiplication, that satisfy the properties of a group under addition, and are associative, distributive, and commutative under both operations.
- A matrix is a rectangular array of numbers or symbols that can be added and multiplied according to certain rules. A matrix can represent a linear transformation, a system of equations, or a vector space.



### Definition for the notes of the Unit 2 - Algebraic Structures in the subject of Discrete Structures & Theory of Logic

- An **algebraic structure** is a mathematical object that consists of a set of elements and one or more operations that satisfy certain properties or axioms.
- **Discrete mathematics** is the branch of mathematics that deals with finite or discrete structures, such as sets, graphs, logic, and cryptography.
- An **algebraic system** is an algebraic structure that has a single underlying set and one or more operations defined on it.
- Some examples of algebraic systems are:
  - **Groups**: A set with a single operation that is associative, has an identity element, and has an inverse for every element.
  - **Rings**: A set with two operations, usually called addition and multiplication, that are both associative, have identity elements, and are commutative, and where addition has inverses for every element and multiplication distributes over addition.
  - **Fields**: A ring where both operations have inverses for every nonzero element.
  - **Lattices**: A set with two operations, usually called meet and join, that are both associative, commutative, and idempotent, and where both operations satisfy the absorption law.
- Algebraic structures can be studied at different levels of abstraction, such as the **concrete level**, where the elements and operations are explicitly given, the **axiomatic level**, where the properties or axioms of the operations are specified, and the **universal level**, where the relations between different algebraic structures are explored.
- Algebraic structures are useful for modeling various phenomena in mathematics, computer science, and other fields, such as symmetry, cryptography, coding theory, logic, and algebraic geometry.



### Groups

- A group is a set G with a binary operation * that satisfies the following properties:
  - Closure: For all a, b in G, a * b is also in G.
  - Associativity: For all a, b, c in G, (a * b) * c = a * (b * c).
  - Identity: There exists an element e in G such that for all a in G, e * a = a * e = a. This element is called the identity element of G.
  - Inverse: For every element a in G, there exists an element b in G such that a * b = b * a = e. This element is called the inverse of a and is denoted by a^-1.
- A group is called abelian or commutative if it also satisfies the following property:
  - Commutativity: For all a, b in G, a * b = b * a.
- Some examples of groups are:
  - The set of integers Z with the operation of addition (+).
  - The set of nonzero rational numbers Q* with the operation of multiplication (×).
  - The set of invertible n × n matrices M_n with the operation of matrix multiplication (·).
  - The set of permutations of a finite set S with the operation of composition (◦).
  - The set of symmetries of a regular polygon with the operation of combining symmetries.



### Subgroups and order

- A **subgroup** is a subset of a group that satisfies the four group requirements: closure, associativity, identity, and inverse.
- A subgroup must contain the identity element of the group and must be closed under the group operation.
- A subgroup is denoted by or , where is the group and is the subgroup.
- The **order** of a subgroup is the number of elements in the subgroup.
- The order of any subgroup of a group of order must be a divisor of , by Lagrange's theorem.
- A subgroup of a group that does not include the entire group itself is known as a **proper subgroup**, denoted by or .
- A subgroup is called a **cyclic subgroup** if it is generated by a single element, i.e., if there exists an element such that .
- A subgroup is called a **normal subgroup** if it is invariant under conjugation by any element of the group, i.e., if for all .
- A subgroup is called a **discrete subgroup** if it has no limit points in the underlying topological space, i.e., if for each element in , there is a neighborhood that only contains that element.



### Cyclic Groups

- A group (G, ∘) is called a cyclic group if there exists an element a∈G such that G is generated by a. In other words, every element of G can be written as a power of a .
- The element a is called a generator or a cyclic generator of G. A cyclic group may have more than one generator .
- The order of a cyclic group is the number of elements in the group. It is denoted by |G| .
- The order of a generator a of a cyclic group G is the smallest positive integer n such that a^n = e, where e is the identity element of G. It is denoted by |a| .
- The order of a generator a of a cyclic group G is equal to the order of the group G, i.e., |a| = |G| .
- A cyclic group is always abelian, i.e., it satisfies the commutative property: a ∘ b = b ∘ a for all a, b ∈ G .
- A cyclic group of order n is isomorphic to the additive group of integers modulo n, i.e., G ≅ Z_n .
- Every subgroup of a cyclic group is cyclic .
- A cyclic group of order n has exactly one subgroup of order d for each divisor d of n .
- A cyclic group of order n has exactly φ(d) generators, where φ is the Euler's totient function, for each divisor d of n .
- A finite group is cyclic if and only if it has at most one subgroup of each order dividing the order of the group .
- A group of prime order is cyclic and has exactly two generators .



### Cosets

- A **coset** of a subgroup H of a group (G, o) is a subset of G obtained by multiplying H with elements of G from left or right .
- Depending on the multiplication from left or right, we can classify cosets as **left cosets** or **right cosets** as follows:
  - A **left coset** of H in G is a subset of G of the form aH = {a * h | h ∈ H}, where a is any element of G.
  - A **right coset** of H in G is a subset of G of the form Ha = {h * a | h ∈ H}, where a is any element of G.
- For example, take H = {0, 2, 4, 6} and G = {0, 1, 2, 3, 4, 5, 6, 7}, both with addition modulo 8 as the operation. Then 1 + H = {1, 3, 5, 7} and H + 5 = {5, 7, 1, 3} are left and right cosets of H in G, respectively.
- Cosets are mainly used to decompose a group G into equal-sized disjoint subsets of G. It plays an important role to study many things in Group Theory; for example, normal group, Lagrange’s theorem on finite groups, etc.



### Lagrange's theorem for the notes of the Unit 2 - Algebraic Structures in the subject of Discrete Structures & Theory of Logic

- Lagrange's theorem is one of the central theorems of abstract algebra. It states that in group theory, for any finite group say G, the order of subgroup H of group G divides the order of G. The order of the group represents the number of elements .
- Lagrange's theorem can be expressed as |G| = n|H|, where n is a positive integer called the index of H in G.
- Lagrange's theorem can be proved by using the concept of cosets of a subgroup. A coset of H in G is a subset of G that is obtained by multiplying all the elements of H by a fixed element of G. There are two types of cosets: left cosets and right cosets. A left coset of H in G is of the form gH, where g is an element of G. A right coset of H in G is of the form Hg, where g is an element of G.
- The key properties of cosets are:

  - Every element of G belongs to exactly one left coset of H and exactly one right coset of H.
  - Every left coset of H has the same number of elements as H, and every right coset of H has the same number of elements as H.
  - Two left cosets of H are either equal or disjoint, and two right cosets of H are either equal or disjoint.
  - The number of left cosets of H in G is equal to the number of right cosets of H in G, and this number is the index of H in G.

- Using these properties, we can prove Lagrange's theorem as follows:

  - Let G be a finite group and H be a subgroup of G. Let n be the index of H in G, and let g1, g2, ..., gn be the distinct elements of G that form the left cosets of H. That is, G = g1H ∪ g2H ∪ ... ∪ gnH, where the union is disjoint.
  - Since every left coset of H has the same number of elements as H, we have |giH| = |H| for every i = 1, 2, ..., n.
  - Therefore, by the principle of counting, we have |G| = |g1H| + |g2H| + ... + |gnH| = n|H|.
  - Hence, |H| divides |G|, which proves Lagrange's theorem.

- Lagrange's theorem has some important consequences, such as:

  - The order of any element of a finite group divides the order of the group.
  - If G is a finite group and H is a subgroup of G such that |H| = |G|/2, then H is a normal subgroup of G.
  - If G is a finite group of prime order, then G is cyclic and has no proper subgroups.
  - If G is a finite group and K is a normal subgroup of G, then the order of the quotient group G/K divides the order of G.



### Normal Subgroups

- A normal subgroup H of a group G is a subgroup of G that is invariant under conjugation by members of the group. In other words, for every element g in G and every element h in H, we have g h g^-1 in H .
- Equivalently, a normal subgroup H of a group G is a subgroup of G such that every left coset and right coset corresponding to an element g are the same, that is, g H = H g .
- The usual notation for this relation is H ≤ G, or H ⊲ G if H is normal in G.
- Normal subgroups are important because they allow us to define quotient groups, which are groups obtained by dividing a group by a normal subgroup. Quotient groups are useful for studying the structure and properties of groups.
- Some properties of normal subgroups are :
  - Every abelian group has a normal subgroup.
  - Any group which do not have any normal subgroup other than the trivial normal subgroup is called a simple group.
  - If a subgroup is of index 2 in G, that is has only two distinct left or right cosets in G, then H is a normal subgroup of G.
  - Every subgroup of a cyclic group is normal.
  - The intersection of any two normal subgroups of a group is a normal subgroup.
  - The intersection of any collection of normal subgroups is a normal subgroup.
  - The product of two normal subgroups of a group is a normal subgroup.
  - The product of any collection of normal subgroups is a normal subgroup.
  - The center of a group is a normal subgroup.
  - The commutator subgroup of a group is a normal subgroup.
  - The kernel of a homomorphism is a normal subgroup.
  - The image of a homomorphism is a normal subgroup.



### Permutation and Symmetric Groups

- A **permutation** of a set is a bijective function from the set to itself, that is, a function that rearranges the elements of the set .
- A **permutation group** is a subgroup of the symmetric group, that is, a set of permutations that is closed under function composition and inverse, and contains the identity permutation .
- A **symmetric group** on a set is the set of all permutations on the set, under the operation of function composition .
- The symmetric group on a set of n elements is denoted by S_n and has n! elements  .
- The symmetric group S_n is non-abelian for n > 2, and has a simple subgroup A_n, called the alternating group, consisting of all even permutations .
- The symmetric group S_n acts on the set of n elements by permutation, and the orbits of this action are the singletons. The stabilizer of any element is the subgroup S_(n-1) of permutations that fix that element .
- The symmetric group S_n also acts on the set of k-subsets of the n elements, by permuting the elements of each subset. The orbits of this action are the k-element subsets, and the stabilizer of any subset is the subgroup S_k x S_(n-k) of permutations that permute the elements within the subset and outside the subset separately .
- The symmetric group S_n has many other interesting subgroups and actions, such as the dihedral group D_n, the cycle group C_n, the symmetric group S_(n-1), the wreath product S_k wr S_n, and the Young subgroup S_\lambda for any partition \lambda of n .



### Group Homomorphisms

- A group homomorphism is a function that maps one group to another group in such a way that the group operation is preserved. That is, if $G$ and $H$ are groups with operations $\ast$ and $\cdot$, respectively, then a function $h:G\to H$ is a group homomorphism if for all $u,v\in G$, we have $h(u\ast v)=h(u)\cdot h(v)$.
- A group homomorphism preserves the identity element and the inverse element of a group. That is, if $h:G\to H$ is a group homomorphism, then $h(e_G)=e_H$, where $e_G$ and $e_H$ are the identity elements of $G$ and $H$, respectively, and $h(u^{-1})=h(u)^{-1}$ for all $u\in G$.
- The kernel of a group homomorphism is the set of all elements in the domain that are mapped to the identity element in the codomain. That is, if $h:G\to H$ is a group homomorphism, then $\ker h=\{u\in G\mid h(u)=e_H\}$.
- The image of a group homomorphism is the set of all elements in the codomain that are mapped from some element in the domain. That is, if $h:G\to H$ is a group homomorphism, then $\operatorname{im} h=\{h(u)\mid u\in G\}$.
- A group homomorphism is injective if and only if its kernel is trivial, that is, $\ker h=\{e_G\}$. A group homomorphism is surjective if and only if its image is the whole codomain, that is, $\operatorname{im} h=H$.
- A group homomorphism that is both injective and surjective is called an isomorphism. Two groups that are isomorphic have the same algebraic structure and are essentially the same group, except for the names of the elements. If there exists an isomorphism between $G$ and $H$, we write $G\cong H$ and say that $G$ and $H$ are isomorphic groups.



### Definition and elementary properties of Rings and Fields

- A **ring** is a set \\(R\\) equipped with two binary operations, usually called **addition** and **multiplication**, such that the following properties hold for all \\(a, b, c \in R\\):

  - \\(R\\) is an **abelian group** under addition, i.e., \\(a + b = b + a\\), \\(a + (b + c) = (a + b) + c\\), there exists a **zero element** \\(0\\) such that \\(a + 0 = a\\), and there exists an **additive inverse** \\(-a\\) such that \\(a + (-a) = 0\\).
  - Multiplication is **associative**, i.e., \\(a \cdot (b \cdot c) = (a \cdot b) \cdot c\\).
  - Multiplication is **distributive** over addition, i.e., \\(a \cdot (b + c) = a \cdot b + a \cdot c\\) and \\((a + b) \cdot c = a \cdot c + b \cdot c\\).

- A ring is called **commutative** if multiplication is also commutative, i.e., \\(a \cdot b = b \cdot a\\) for all \\(a, b \in R\\).
- A ring is called **unital** or **unitary** if it has a **multiplicative identity** \\(1\\) such that \\(a \cdot 1 = 1 \cdot a = a\\) for all \\(a \in R\\).
- A ring is called an **integral domain** if it is commutative, unital, and has **no zero divisors**, i.e., if \\(a \cdot b = 0\\) then either \\(a = 0\\) or \\(b = 0\\).
- A **field** is a ring that is commutative, unital, and has **multiplicative inverses** for all nonzero elements, i.e., for every \\(a \neq 0\\) there exists \\(a^{-1}\\) such that \\(a \cdot a^{-1} = a^{-1} \cdot a = 1\\).

- Some examples of rings are:

  - The set of integers \\(\mathbb{Z}\\) with the usual addition and multiplication is a commutative, unital ring, but not a field, since not every nonzero integer has a multiplicative inverse in \\(\mathbb{Z}\\).
  - The set of polynomials \\(R[x]\\) with coefficients in a ring \\(R\\) and the usual polynomial addition and multiplication is a ring. It is commutative and unital if \\(R\\) is commutative and unital. It is an integral domain if \\(R\\) is an integral domain.
  - The set of \\(n \times n\\) square matrices with entries in a ring \\(R\\) and the usual matrix addition and multiplication is a ring. It is commutative and unital if \\(R\\) is commutative and unital and \\(n = 1\\). It is never an integral domain if \\(n > 1\\), since there are nonzero matrices that multiply to zero.

- Some examples of fields are:

  - The set of rational numbers \\(\mathbb{Q}\\), the set of real numbers \\(\mathbb{R}\\), and the set of complex numbers \\(\mathbb{C}\\) with the usual addition and multiplication are fields.
  - The set of integers modulo a prime number \\(p\\), denoted by \\(\mathbb{Z}_p\\) or \\(\mathbb{F}_p\\), with addition and multiplication defined by taking the remainder after dividing by \\(p\\), is a field. For example, \\(\mathbb{Z}_2\\) is the field with two elements \\(0\\) and \\(1\\), where \\(1 + 1 = 0\\) and \\(1 \cdot 1 = 1\\).
  - The set of polynomials \\(\mathbb{F}_p[x]\\) with coefficients in \\(\mathbb{F}_p\\) and the usual polynomial addition and multiplication is not a field, but it contains some subfields of



## Unit 3 - Lattices

- A lattice is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A lattice can also be defined as an algebraic structure with two binary, commutative and associative operations, usually denoted by ∧ (meet) and ∨ (join), that satisfy the absorption laws: a ∧ (a ∨ b) = a and a ∨ (a ∧ b) = a for all elements a and b.
- A lattice can be represented by a Hasse diagram, which is a graph that shows the elements and their order relation by using nodes and edges. The nodes represent the elements and the edges represent the order relation. An edge from a node x to a node y means that x ≤ y and there is no element z such that x ≤ z ≤ y. The bottom node is the minimum element and the top node is the maximum element of the lattice, if they exist.
- A lattice is called bounded if it has a minimum element (called bottom or zero) and a maximum element (called top or one). A bounded lattice can be denoted by (L, ≤, 0, 1).
- A lattice is called distributive if it satisfies the distributive laws: a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) and a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) for all elements a, b and c. A distributive lattice can be characterized by the absence of sublattices isomorphic to M3 (a diamond with a node inside) or N5 (a pentagon with a node above and below).
- A lattice is called complemented if every element has a complement, that is, an element x such that x ∧ y = 0 and x ∨ y = 1 for some element y. A complemented lattice is called uniquely complemented if every element has a unique complement. A complemented distributive lattice is always uniquely complemented.
- A lattice is called modular if it satisfies the modular law: a ≤ c implies a ∨ (b ∧ c) = (a ∨ b) ∧ c for all elements a, b and c. A modular lattice can be characterized by the absence of sublattices isomorphic to N5. A distributive lattice is always modular, but the converse is not true.
- A lattice is called complete if every subset of elements has a lub and a glb. A complete lattice is always bounded, since the lub of the empty set is the bottom element and the glb of the empty set is the top element. A complete lattice can be denoted by (L, ≤, ⊥, ⊤).
- A lattice is called a Boolean algebra if it is a bounded, distributive and complemented lattice. A Boolean algebra can be denoted by (B, ≤, ∨, ∧, ¬, 0, 1), where ¬ is the complement operation. A Boolean algebra can also be defined as an algebraic structure with two binary operations ∨ and ∧, a unary operation ¬, and two constants 0 and 1, that satisfy the following axioms for all elements a, b and c:

  - Commutative laws: a ∨ b = b ∨ a and a ∧ b = b ∧ a
  - Associative laws: a ∨ (b ∨ c) = (a ∨ b) ∨ c and a ∧ (b ∧ c) = (a ∧ b) ∧ c
  - Distributive laws: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) and a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
  - Identity laws: a ∨ 0 = a and a ∧ 1 = a
  - Complement laws: a ∨ ¬a = 1 and a ∧ ¬a = 0
  - Idempotent laws: a ∨ a = a and a ∧ a = a
  - Absorption laws: a ∨ (a ∧ b) = a and a ∧ (a ∨ b) = a
  - De Morgan's laws: ¬(a ∨ b) = ¬a ∧ ¬b and ¬(a ∧ b) = ¬a ∨ ¬b

- A Boolean algebra can be represented by a power set, that



### Definition for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** and a **least upper bound** .
- A greatest lower bound of two elements a and b in a poset is an element c such that c ≤ a and c ≤ b, and there is no other element d that satisfies these conditions and is greater than c. It is also called the **meet** or the **infimum** of a and b, and denoted by a ∧ b .
- A least upper bound of two elements a and b in a poset is an element c such that a ≤ c and b ≤ c, and there is no other element d that satisfies these conditions and is less than c. It is also called the **join** or the **supremum** of a and b, and denoted by a ∨ b .
- A lattice can be represented by a **Hasse diagram**, which is a graphical representation of the partial order relation. In a Hasse diagram, each element of the poset is represented by a point, and a line segment is drawn between two points if and only if they are comparable and there is no other element between them. The lower elements are placed below the higher elements .
- A lattice can also be defined as an algebraic structure with two binary operations, called meet and join, that satisfy certain properties. These properties are: commutativity, associativity, idempotence, absorption, and the existence of a least element and a greatest element .
- A lattice is a special case of a **semilattice**, which is a poset that has either a meet or a join operation for every pair of elements, but not necessarily both.
- A lattice is also a special case of a **distributive lattice**, which is a lattice that satisfies the **distributive law**: a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) and a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) for all elements a, b, and c in the lattice .
- A lattice is also a special case of a **modular lattice**, which is a lattice that satisfies the **modular law**: a ∧ (b ∨ (a ∧ c)) = (a ∧ b) ∨ (a ∧ c) and a ∨ (b ∧ (a ∨ c)) = (a ∨ b) ∧ (a ∨ c) for all elements a, b, and c in the lattice .
- A lattice is also a special case of a **complete lattice**, which is a lattice that has a meet and a join operation for every subset of the lattice, not just for pairs of elements .
- A lattice is also a special case of a **bounded lattice**, which is a lattice that has a least element and a greatest element, denoted by 0 and 1 respectively .
- A lattice is also a special case of a **complemented lattice**, which is a bounded lattice that has a **complement** for every element, that is, an element a' such that a ∧ a' = 0 and a ∨ a' = 1 .
- A lattice is also a special case of a **Boolean algebra**, which is a complemented distributive lattice that satisfies the **duality principle**: for any statement involving the lattice operations and elements, the statement remains true if we interchange ∧ and ∨, and 0 and 1 .



### Properties of lattices – Bounded

- A lattice is a poset (L, ⪯) for which every pair of elements has a greatest lower bound and least upper bound.
- A bounded lattice is a lattice that additionally has a greatest element (also called maximum, or top element, and denoted by 1, or by ⊤) and a least element (also called minimum, or bottom, and denoted by 0, or by ⊥), which satisfy:
  - for all x in L, x ∧ 1 = x and x ∨ 1 = 1
  - for all x in L, x ∧ 0 = 0 and x ∨ 0 = x
- The element 1 is called the upper bound, or top of L and the element 0 is called the lower bound or bottom of L.
- A complemented lattice is a bounded lattice in which every element is complemented. Namely, the complement of 1 is 0, and the complement of 0 is 1.
- A distributive lattice is a lattice in which for all elements in the poset the distributive property holds:
  - x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z)
  - x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)
- Every finite lattice L = {a 1,a 2,a 3....a n} is bounded. Proof:
  - Let L = {a 1,a 2,a 3....a n} be a finite lattice.
  - Consider the element a 1 ∨ a 2 ∨ a 3....∨ a n. This element belongs to L, since L is closed under ∨.
  - For any element a i in L, we have a i ∨ (a 1 ∨ a 2 ∨ a 3....∨ a n) = a 1 ∨ a 2 ∨ a 3....∨ a n, by the idempotent law of ∨.
  - Therefore, a 1 ∨ a 2 ∨ a 3....∨ a n is the greatest element of L, and we denote it by 1.
  - Similarly, consider the element a 1 ∧ a 2 ∧ a 3....∧ a n. This element belongs to L, since L is closed under ∧.
  - For any element a i in L, we have a i ∧ (a 1 ∧ a 2 ∧ a 3....∧ a n) = a 1 ∧ a 2 ∧ a 3....∧ a n, by the idempotent law of ∧.
  - Therefore, a 1 ∧ a 2 ∧ a 3....∧ a n is the least element of L, and we denote it by 0.
  - Hence, L is a bounded lattice.



### Complemented for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **bounded lattice** is a lattice that has a minimum element (denoted by 0) and a maximum element (denoted by 1).
- A **complemented lattice** is a bounded lattice in which every element has a complement, that is, an element such that their lub is 1 and their glb is 0.
- A **distributive lattice** is a lattice that satisfies the distributive laws: for all x, y, z in the lattice, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ denotes the glb and ∨ denotes the lub.
- A **Boolean algebra** is a distributive complemented lattice. It is also a Boolean ring, that is, a ring with two operations (+ and ·) such that for all x, y, z in the ring, x + y = y + x, x · y = y · x, x + (y + z) = (x + y) + z, x · (y · z) = (x · y) · z, x · (y + z) = (x · y) + (x · z), x + (y · z) = (x + y) · (x + z), x + x = 0, and x · x = x. The operations + and · correspond to the symmetric difference and the intersection of sets, respectively.
- A **Boolean function** is a function from a set of n Boolean variables to a single Boolean value. It can be represented by a truth table, a Boolean expression, or a Boolean circuit.
- A **Boolean expression** is a combination of Boolean variables, constants (0 and 1), and operators (∧, ∨, ¬, →, ↔, ⊕, etc.). It can be simplified using Boolean algebra laws and rules, such as De Morgan's laws, absorption, idempotence, etc.
- A **Boolean circuit** is a directed acyclic graph (DAG) with nodes labeled by Boolean variables, constants, or operators, and edges representing the flow of information. The output of the circuit is the value of the node with no outgoing edges. The size of the circuit is the number of nodes, and the depth of the circuit is the length of the longest path from an input node to the output node.



### Modular and Complete Lattice

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** (glb) and a **least upper bound** (lub). The glb and lub are also called the **meet** and the **join** of the elements, and are denoted by ∧ and ∨ respectively. A lattice is denoted by [L; ∧, ∨].
- A **complete lattice** is a lattice in which **all subsets** have a glb and a lub. The glb and lub of the whole set are called the **minimum** and the **maximum** of the lattice, and are denoted by 0 and 1 respectively. A complete lattice is also called a **bounded lattice**.
- A **modular lattice** is a lattice that satisfies the **modular law**: a ∨ (b ∧ c) = (a ∨ b) ∧ c whenever a ≤ c. This law is an abstraction of the **second isomorphism theorem** in algebra, which states that for any submodules A, B, C of a module M, if A ⊆ C, then A + (B ∩ C) ≅ (A + B) ∩ C.
- A modular lattice has a **composition sequence**, which is a finite sequence of elements x1, x2, ..., xn such that x1 = 0, xn = 1, and xi ∧ xi+1 = 0 for all i. The length of the composition sequence is called the **dimension** of the modular lattice, and is denoted by d(L).
- A modular lattice has a **dimension function**, which is an integer-valued function d such that d(x ∨ y) + d(x ∧ y) = d(x) + d(y) and such that if the interval [a, b] is prime, it follows that d(b) = d(a) + 1. A prime interval is an interval that contains no other elements except its endpoints.
- Examples of modular lattices are:
  - The **subspaces** of a vector space (or more generally the **submodules** of a module over a ring).
  - The **ideals** of a principal ideal domain (or more generally a Dedekind domain).
  - The **subgroups** of a finite abelian group (or more generally a finite solvable group).
  - The **faces** of a convex polytope (or more generally a matroid).
  - The **subsets** of a finite set (or more generally a distributive lattice).



### Boolean Algebra

- Boolean algebra is a branch of mathematics that deals with operations on logical values with binary variables  .
- The Boolean variables are represented as binary numbers to represent truths: 1 = true and 0 = false .
- The basic operations in Boolean algebra are the logical operations AND, OR and NOT .
- AND is denoted by ∧, OR by ∨ and NOT by ¬.
- AND returns 1 if both operands are 1, otherwise 0.
- OR returns 1 if either operand is 1, otherwise 0.
- NOT returns 1 if the operand is 0, and 0 if the operand is 1.
- For example, 1 ∧ 0 = 0, 1 ∨ 0 = 1, ¬1 = 0, ¬0 = 1.
- Boolean algebra can be used to manipulate and simplify logical expressions, such as those used in digital circuits .
- Boolean algebra can also be defined abstractly as any set with binary operations ∧ and ∨ and a unary operation ¬ satisfying the Boolean laws.
- The Boolean laws are a set of axioms and rules that govern the behavior of Boolean operations.
- Some of the Boolean laws are:

  - Commutative laws: A ∧ B = B ∧ A, A ∨ B = B ∨ A.
  - Associative laws: (A ∧ B) ∧ C = A ∧ (B ∧ C), (A ∨ B) ∨ C = A ∨ (B ∨ C).
  - Distributive laws: A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C), A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C).
  - Identity laws: A ∧ 1 = A, A ∨ 0 = A.
  - Complement laws: A ∧ ¬A = 0, A ∨ ¬A = 1.
  - Idempotent laws: A ∧ A = A, A ∨ A = A.
  - De Morgan's laws: ¬(A ∧ B) = ¬A ∨ ¬B, ¬(A ∨ B) = ¬A ∧ ¬B.
  - Absorption laws: A ∧ (A ∨ B) = A, A ∨ (A ∧ B) = A.
  - Involution law: ¬(¬A) = A.

- A Boolean function is a function that takes one or more Boolean variables as inputs and returns a Boolean value as output.
- A Boolean function can be represented in various ways, such as a truth table, an algebraic expression, a logic diagram or a Boolean circuit.
- A truth table is a table that lists all possible combinations of inputs and their corresponding outputs.
- An algebraic expression is a formula that uses Boolean variables and operations to describe the output.
- A logic diagram is a graphical representation that uses symbols for Boolean variables and operations to show the logic of the function.
- A Boolean circuit is a physical implementation of a logic diagram using electronic components such as switches, gates and wires.
- For example, the Boolean function F(A, B) = A ∧ ¬B can be represented as:

  - Truth table:

    | A | B | F(A, B) |
    |---|---|---------|
    | 0 | 0 | 0       |
    | 0 | 1 | 0       |
    | 1 | 0 | 1       |
    | 1 | 1 | 0       |

  - Algebraic expression: F(A, B) = A ∧ ¬B
  - Logic diagram:

    Logic diagram of F(A, B) = A ∧ ¬B

  - Boolean circuit:

    ![Boolean circuit of F(A, B) = A ∧ ¬B](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/AND_NOT_c



### Introduction for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **poset** is a set with a binary relation that is reflexive, antisymmetric, and transitive.
- A **least upper bound** of a subset S of a poset P is an element x in P such that x is greater than or equal to every element in S and there is no element y in P that is smaller than x and greater than or equal to every element in S.
- A **greatest lower bound** of a subset S of a poset P is an element x in P such that x is less than or equal to every element in S and there is no element y in P that is greater than x and less than or equal to every element in S.
- A **bounded lattice** is a lattice that has a minimum element (called **zero**) and a maximum element (called **one**).
- A **complemented lattice** is a bounded lattice in which every element has a unique complement, that is, an element x such that x and its complement have zero as their glb and one as their lub.
- A **Boolean algebra** is a complemented lattice that satisfies the distributive law, that is, for any elements x, y, and z, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ denotes the glb and ∨ denotes the lub.
- A **sublattice** of a lattice L is a subset of L that is also a lattice with respect to the same partial order.
- A **homomorphism** of lattices is a function f from one lattice L to another lattice M that preserves the glb and lub operations, that is, for any elements x and y in L, f(x ∧ y) = f(x) ∧ f(y) and f(x ∨ y) = f(x) ∨ f(y).
- An **isomorphism** of lattices is a bijective homomorphism that has an inverse that is also a homomorphism. Two lattices are **isomorphic** if there exists an isomorphism between them.



### Axioms and Theorems of Boolean Algebra

Boolean algebra is a branch of mathematics that deals with the manipulation of logical expressions involving two values: true (1) and false (0). It is widely used in digital electronics and computer science to design and analyze circuits, algorithms, and programs.

The basic operations of Boolean algebra are:

- AND (∧): The output is true only if both inputs are true.
- OR (∨): The output is true if at least one input is true.
- NOT (¬): The output is the opposite of the input.

There are some set of logical expressions that we accept as true and upon which we can build a set of useful theorems. These sets of logical expressions are known as axioms or postulates of Boolean algebra. An axiom is nothing more than the definition of the three basic logic operations.

The following are the axioms of Boolean algebra :

- Commutative laws: The order of the operands does not affect the result of the operation.
  - A ∧ B = B ∧ A
  - A ∨ B = B ∨ A
- Associative laws: The grouping of the operands does not affect the result of the operation.
  - (A ∧ B) ∧ C = A ∧ (B ∧ C)
  - (A ∨ B) ∨ C = A ∨ (B ∨ C)
- Distributive laws: The AND operation distributes over the OR operation, and vice versa.
  - A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C)
  - A ∨ (B ∧ C) = (A ∨ B) ∧ (A ∨ C)
- Identity laws: The identity element for the AND operation is 1, and for the OR operation is 0.
  - A ∧ 1 = A
  - A ∨ 0 = A
- Complement laws: The complement of an element is the element that gives 0 when ANDed with it, and 1 when ORed with it.
  - A ∧ ¬A = 0
  - A ∨ ¬A = 1
- Idempotent laws: An element ANDed or ORed with itself gives the same element.
  - A ∧ A = A
  - A ∨ A = A
- Absorption laws: An element ANDed with the OR of itself and another element gives the same element, and vice versa.
  - A ∧ (A ∨ B) = A
  - A ∨ (A ∧ B) = A
- De Morgan's laws: The complement of the AND of two elements is the same as the OR of their complements, and vice versa.
  - ¬(A ∧ B) = ¬A ∨ ¬B
  - ¬(A ∨ B) = ¬A ∧ ¬B
- Involution law: The complement of the complement of an element is the same element.
  - ¬(¬A) = A

The theorems of Boolean algebra are derived from the axioms using logical reasoning. They can be used to simplify and manipulate Boolean expressions. Some examples of theorems are:

- Zero and one laws: An element ANDed with 0 gives 0, and ORed with 1 gives 1.
  - A ∧ 0 = 0
  - A ∨ 1 = 1
- Domination laws: An element ORed with 0 gives the same element, and ANDed with 1 gives the same element.
  - A ∨ 0 = A
  - A ∧ 1 = A
- Double negation law: The complement of the complement of an element is the same element.
  - ¬(¬A) = A
- Redundancy laws: An element ANDed with the OR of itself and another element gives the same element, and vice versa.
  - A ∧ (A ∨ B) = A
  - A ∨ (A ∧ B) = A
- Consensus law: The OR of two elements ANDed with the complement of the third element is the same as the OR of the two elements.
  - (A ∧ ¬B) ∨ (B ∧ ¬C) ∨ (C ∧ ¬A) = (A ∧ ¬B) ∨ (B ∧ ¬C)



### Algebraic manipulation of Boolean expressions

- Boolean expressions are algebraic expressions that involve variables and operators that take only two values: true (1) or false (0).
- The main operators in Boolean algebra are AND (`*`), OR (`+`), and NOT (`'`).
- AND operator returns true only if both operands are true, OR operator returns true if at least one operand is true, and NOT operator returns the opposite of the operand.
- Boolean algebra has some basic laws and rules that can be used to simplify and manipulate Boolean expressions, such as:
  - Commutative laws: `A + B = B + A` and `A * B = B * A`
  - Associative laws: `(A + B) + C = A + (B + C)` and `(A * B) * C = A * (B * C)`
  - Distributive laws: `A * (B + C) = (A * B) + (A * C)` and `A + (B * C) = (A + B) * (A + C)`
  - Identity laws: `A + 0 = A` and `A * 1 = A`
  - Complement laws: `A + A' = 1` and `A * A' = 0`
  - Idempotent laws: `A + A = A` and `A * A = A`
  - Involution law: `(A')' = A`
  - De Morgan's laws: `(A + B)' = A' * B'` and `(A * B)' = A' + B'`
  - Absorption laws: `A + (A * B) = A` and `A * (A + B) = A`
  - Consensus law: `A * B + A' * C + B * C = A * B + A' * C`
- Algebraic manipulation of Boolean expressions is the process of applying these laws and rules to transform one expression into an equivalent one that is simpler, more standardized, or more suitable for a specific purpose.
- Some common forms of Boolean expressions are:
  - Sum-of-products (SOP): A Boolean expression that is a sum (OR) of one or more product (AND) terms, such as `A * B + A' * C`.
  - Product-of-sums (POS): A Boolean expression that is a product (AND) of one or more sum (OR) terms, such as `(A + B) * (A' + C)`.
  - Canonical form: A Boolean expression that is either a SOP or a POS form that contains all the variables in each term, such as `A * B + A' * B' * C`.
  - Minterm: A product term that contains all the variables in the expression, either complemented or uncomplemented, such as `A * B' * C`.
  - Maxterm: A sum term that contains all the variables in the expression, either complemented or uncomplemented, such as `A' + B + C'`.
- Algebraic manipulation of Boolean expressions can be useful for simplifying complex expressions, minimizing the number of literals (variables) or terms, converting between different forms, and designing digital circuits.



### Simplification of Boolean Functions

- A boolean function is a function that takes one or more boolean variables as inputs and produces a single boolean output.
- The algebraic expression of a boolean function can be written using boolean operators such as AND, OR, NOT, XOR, etc.
- The simplification of a boolean function is the process of finding an equivalent expression that uses fewer operators, variables, or terms.
- The simplification of a boolean function is important because it reduces the cost and complexity of the associated circuit that implements the function.
- There are different methods for simplifying boolean functions, such as using boolean algebra, Karnaugh maps, Quine-McCluskey method, etc.

#### Using Boolean Algebra

- Boolean algebra is a set of rules and theorems that can be used to manipulate and simplify boolean expressions.
- Some of the basic rules and theorems of boolean algebra are:

  - Commutative laws: A + B = B + A, A.B = B.A
  - Associative laws: (A + B) + C = A + (B + C), (A.B).C = A.(B.C)
  - Distributive laws: A + (B.C) = (A + B).(A + C), A.(B + C) = (A.B) + (A.C)
  - Identity laws: A + 0 = A, A.1 = A
  - Complement laws: A + A' = 1, A.A' = 0
  - Idempotent laws: A + A = A, A.A = A
  - Involution law: (A')' = A
  - De Morgan's laws: (A + B)' = A'.B', (A.B)' = A' + B'
  - Absorption laws: A + (A.B) = A, A.(A + B) = A
  - Consensus law: A.B + A'.C + B.C = A.B + A'.C

- To simplify a boolean function using boolean algebra, we can apply these rules and theorems in a systematic way until we reach the simplest form possible.
- For example, to simplify the function F = A.B + A.B + B.C, we can use the following steps:

  - F = A.B + A.B + B.C (given)
  - F = A.(B + B) + B.C (distributive law)
  - F = A.1 + B.C (idempotent law)
  - F = A + B.C (identity law)



### Karnaugh maps

- A Karnaugh map (K-map) is a method of simplifying Boolean algebra expressions .
- It is a visual method that uses a grid of cells to represent all the possible combinations of input variables and their corresponding output values .
- It helps to determine the minimum expressions in the form of sum-of-products (SOP) or product-of-sums (POS), which can be implemented using a minimum number of logic gates .
- It also helps to detect and eliminate race conditions, which are situations where the output depends on the order or timing of the input changes.

#### Working of K-maps

- To use a K-map, the following steps are followed :
  - Select a K-map according to the number of input variables. For example, a 2-variable K-map has 4 cells, a 3-variable K-map has 8 cells, and a 4-variable K-map has 16 cells.
  - Label the rows and columns of the K-map with the input variables and their complements, using the Gray code order. The Gray code order ensures that adjacent cells differ by only one bit.
  - Fill the cells of the K-map with the output values (0 or 1) for each input combination, either from a given truth table or a Boolean expression.
  - Group the adjacent cells that have the same output value (1 for SOP or 0 for POS) into regions, following these rules:
    - Each region must contain a power of 2 number of cells (1, 2, 4, 8, etc.).
    - Each region must be as large as possible, without including cells with different output values.
    - Each region must be rectangular or square in shape, and can wrap around the edges of the K-map if needed.
    - Each cell can belong to more than one region, as long as it does not create any redundant terms.
  - Write the simplified Boolean expression for each region by identifying the input variables that remain constant within the region. For example, a region that covers the cells AB' and AB has the expression A, since A is 1 in both cells and B changes from 0 to 1.
  - Combine the expressions for all the regions using the OR operator for SOP or the AND operator for POS. This is the final simplified Boolean expression.

#### Example Problems

- Example 1: Simplify the following Boolean expression using a K-map and write the SOP form:

  F(A,B,C) = A'BC + AB'C + ABC

  Solution:

  - Step 1: Select a 3-variable K-map with 8 cells and label the rows and columns with A, B, C and their complements.

  |   | 00 | 01 | 11 | 10 |
  |---|----|----|----|----|
  | 0 |    |    |    |    |
  | 1 |    |    |    |    |

  - Step 2: Fill the cells with the output values from the given expression. For example, A'BC corresponds to the cell 011, which has the output value 1.

  |   | 00 | 01 | 11 | 10 |
  |---|----|----|----|----|
  | 0 | 0  | 0  | 1  | 0  |
  | 1 | 0  | 1  | 1  | 1  |

  - Step 3: Group the adjacent cells that have the same output value 1 into regions, following the rules.

  |   | 00 | 01 | 11 | 10 |
  |---|----|----|----|----|
  | 0 | 0  | 0  | 1  | 0  |
  | 1 | 0  | 1  | 1  | 1  |

  The regions are shown in different colors:

  |   | 00 | 01 | 11 | 10 |
  |---|----|----|----|----|
  | 0 | 0  | 0  |<span style="color:red">1</span>| 0  |
  | 1 | 0  |<span style="color:blue">1</span>|<span style="color:red">1</span>|



### Logic gates

- A logic gate is an idealized or physical device that performs a Boolean function, a logical operation performed on one or more binary inputs that produces a single binary output.
- Logic gates can be made using various types of devices, such as pneumatic, mechanical, molecular, optical, or electronic.
- There are seven basic types of logic gates: AND, OR, NOT, NAND, NOR, XOR, and XNOR.
- Each logic gate has a symbol, a truth table, and a Boolean expression that represents its function.
- A logic gate can be combined with other logic gates to form a logic circuit, which can perform more complex operations than a single gate .
- A logic circuit can be simplified using Boolean algebra or Karnaugh maps to reduce the number of gates and inputs required.
- Logic gates and circuits are the building blocks of digital systems, such as computers, calculators, and microcontrollers.



### Digital circuits and Boolean algebra

- Digital circuits are electronic devices that process binary information, which is represented by two voltage levels: high (1) and low (0).
- Boolean algebra is a branch of mathematics that deals with binary variables and logical operations, such as AND, OR, and NOT.
- Boolean algebra can be used to model the behavior of digital circuits, and to simplify and analyze them.
- The basic elements of digital circuits are logic gates, which perform Boolean operations on one or more inputs and produce one output.
- The most common logic gates are AND, OR, and NOT gates, which have the following truth tables:

| A | B | A AND B |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    1    |

| A | B | A OR B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   1    |

| A | NOT A |
|---|-------|
| 0 |   1   |
| 1 |   0   |

- Other logic gates, such as NAND, NOR, XOR, and XNOR, can be derived from the basic gates by combining them in different ways.
- Boolean algebra has some basic laws and rules that can be used to manipulate and simplify Boolean expressions, such as:

  - Commutative law: A AND B = B AND A, A OR B = B OR A
  - Associative law: (A AND B) AND C = A AND (B AND C), (A OR B) OR C = A OR (B OR C)
  - Distributive law: A AND (B OR C) = (A AND B) OR (A AND C), A OR (B AND C) = (A OR B) AND (A OR C)
  - Identity law: A AND 1 = A, A OR 0 = A
  - Complement law: A AND NOT A = 0, A OR NOT A = 1
  - De Morgan's law: NOT (A AND B) = NOT A OR NOT B, NOT (A OR B) = NOT A AND NOT B

- Boolean algebra can be used to design and optimize digital circuits by finding the simplest and most efficient way to implement a given Boolean function, which is a mapping from a set of inputs to a single output.
- A Boolean function can be represented in different ways, such as:

  - Truth table: A table that shows the output value for every possible combination of input values.
  - Boolean expression: An algebraic expression that uses Boolean variables and operators to describe the output value in terms of the input values.
  - Logic diagram: A graphical representation that uses symbols for logic gates and wires to show how the output value is computed from the input values.
  - Karnaugh map: A visual method that uses a grid of cells to group and simplify the terms of a Boolean expression.

- A Boolean function can have more than one equivalent representation, and some representations may be more concise and easier to implement than others.
- The goal of Boolean algebra is to find the minimal representation of a Boolean function, which is the one that uses the least number of logic gates and wires.



## Unit 4 - Propositional Logic

- Propositional logic is a branch of logic that deals with propositions, which are statements that can be either true or false.
- Propositional logic uses symbols and connectives to represent propositions and their logical relations.
- The basic symbols of propositional logic are:
  - **Propositional variables**: lowercase letters such as p, q, r, etc. that stand for arbitrary propositions.
  - **Logical constants**: uppercase letters such as T and F that stand for the truth values true and false, respectively.
  - **Logical connectives**: symbols such as ¬ (negation), ∧ (conjunction), ∨ (disjunction), → (implication), and ↔ (equivalence) that combine propositions to form more complex propositions.
- The basic rules of propositional logic are:
  - **Syntax**: the rules that define how to form well-formed formulas (wffs) from symbols and connectives. A wff is a string of symbols that is syntactically correct and meaningful in propositional logic.
  - **Semantics**: the rules that define how to assign truth values to wffs based on the truth values of their components. A truth assignment is a function that maps each propositional variable to either T or F. A truth table is a table that shows the truth values of a wff for all possible truth assignments of its propositional variables.
  - **Validity**: the property of a wff that is true for all possible truth assignments of its propositional variables. A valid wff is also called a tautology.
  - **Satisfiability**: the property of a wff that is true for at least one truth assignment of its propositional variables. A satisfiable wff is also called a contingent wff. An unsatisfiable wff is also called a contradiction.
  - **Equivalence**: the relation between two wffs that have the same truth value for all possible truth assignments of their propositional variables. Two equivalent wffs are also called logically equivalent or logically identical.
  - **Implication**: the relation between two wffs such that the truth of the first wff implies the truth of the second wff for all possible truth assignments of their propositional variables. The first wff is also called the antecedent or the premise, and the second wff is also called the consequent or the conclusion. An implication is also called a logical consequence or a logical entailment.
  - **Inference**: the process of deriving a new wff from one or more given wffs using logical rules. An inference is also called a logical deduction or a logical argument. An inference is valid if the conclusion follows from the premises by the rules of propositional logic. An inference is sound if it is valid and the premises are true.



### Proposition for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Propositional logic is a branch of logic that studies the ways of combining and modifying statements, called propositions, using logical connectives and operators.
- A proposition is a declarative sentence that is either true or false, but not both. For example, "Sydney is an AI assistant" is a proposition, but "What is your name?" is not.
- Logical connectives are symbols that are used to form compound propositions from simpler ones. The main logical connectives are:
  - Negation (¬): It reverses the truth value of a proposition. For example, if p is "It is raining", then ¬p is "It is not raining".
  - Conjunction (∧): It joins two propositions and is true only when both of them are true. For example, if p is "It is raining" and q is "It is cold", then p ∧ q is "It is raining and it is cold".
  - Disjunction (∨): It joins two propositions and is true when at least one of them is true. For example, if p is "It is raining" and q is "It is cold", then p ∨ q is "It is raining or it is cold".
  - Conditional (→): It represents an implication or a cause-effect relationship between two propositions. It is true when the antecedent (the proposition before the arrow) is false or the consequent (the proposition after the arrow) is true. For example, if p is "It is raining" and q is "The ground is wet", then p → q is "If it is raining, then the ground is wet".
  - Biconditional (↔): It represents an equivalence or a necessary and sufficient condition between two propositions. It is true when both propositions have the same truth value. For example, if p is "It is raining" and q is "The ground is wet", then p ↔ q is "It is raining if and only if the ground is wet".
- Logical operators are symbols that are used to modify propositions or perform operations on them. The main logical operators are:
  - Parentheses ( ): They are used to group propositions and indicate the order of evaluation. For example, (p ∧ q) ∨ r is different from p ∧ (q ∨ r).
  - Truth tables: They are tables that show the truth value of a compound proposition for every possible combination of truth values of its components. For example, the truth table for p ∧ q is:

| p | q | p ∧ q |
|---|---|-------|
| T | T | T     |
| T | F | F     |
| F | T | F     |
| F | F | F     |

  - Logical equivalence: Two propositions are logically equivalent if they have the same truth value for every possible assignment of truth values to their components. For example, p ∧ q is logically equivalent to q ∧ p, and ¬(p ∧ q) is logically equivalent to ¬p ∨ ¬q. Logical equivalence can be proved using truth tables or logical laws.
  - Logical laws: They are rules or principles that can be used to simplify or manipulate propositions. For example, some of the logical laws are:
    - Commutative laws: p ∧ q ≡ q ∧ p and p ∨ q ≡ q ∨ p
    - Associative laws: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r) and (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)
    - Distributive laws: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) and p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
    - Identity laws: p ∧ T ≡ p and p ∨ F ≡ p
    - Negation laws: ¬(¬p) ≡ p and p ∧ ¬p ≡ F and p ∨ ¬p ≡ T
    - Double negation law: ¬(¬p) ≡ p
    - De Morgan's laws: ¬(p ∧ q) ≡ ¬p ∨ ¬q and ¬(p ∨ q) ≡ ¬p ∧ ¬q
    - Implication law: p → q ≡ ¬p ∨ q
    - Contrapositive law: p → q ≡ ¬q → ¬p
    - Biconditional law: p ↔ q ≡ (p → q) ∧ (q → p)
- Propositional



### Well formed formula

- A well formed formula (wff) is a finite sequence of symbols from a given alphabet that is grammatically correct according to some rules of syntax.
- The alphabet of propositional logic consists of the following symbols:
  - Propositional variables: p, q, r, ...
  - Logical connectives: ¬ (negation), ∧ (conjunction), ∨ (disjunction), → (implication), ↔ (equivalence)
  - Parentheses: (, )
- The rules of syntax for propositional logic are as follows:
  - Every propositional variable is a wff.
  - If α is a wff, then ¬α is a wff.
  - If α and β are wffs, then (α ∧ β), (α ∨ β), (α → β), and (α ↔ β) are wffs.
  - Nothing else is a wff.
- Examples of wffs are:
  - p
  - ¬q
  - (p ∧ q)
  - (¬p ∨ (q → r))
  - ((p ↔ q) ↔ r)
- Examples of non-wffs are:
  - p ∧
  - ¬(p q)
  - (p →) ∨ q
  - p ↔ (q r)
  - (p ∨ q ∧ r)



### Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A truth table is a mathematical table used in logic that shows the truth values of logical expressions for each possible combination of values of their variables.
- A truth table can be used to show the semantics of logical operators, prove logical equivalences, solve satisfiability problems, and other applications in propositional logic.
- A truth table has one column for each variable and one column for the logical expression. The rows of the table correspond to all possible assignments of truth values to the variables. The truth value of the expression is calculated for each row and written in the last column.
- The following table shows the basic logical operators and their truth tables:

| Operator | Symbol | Example | Truth table |
|:--------:|:------:|:-------:|:-----------:|
| Negation | ¬, ~, ! | ¬p | p | ¬p |
| | | | T | F |
| | | | F | T |
| Conjunction | ∧, &, and | p ∧ q | p | q | p ∧ q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | F |
| | | | F | F | F |
| Disjunction | ∨, \|\|, or | p ∨ q | p | q | p ∨ q |
| | | | T | T | T |
| | | | T | F | T |
| | | | F | T | T |
| | | | F | F | F |
| Conditional | →, =>, implies | p → q | p | q | p → q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | T |
| | | | F | F | T |
| Biconditional | ↔, <=>, iff | p ↔ q | p | q | p ↔ q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | F |
| | | | F | F | T |
| Exclusive or | ⊕, ^, xor | p ⊕ q | p | q | p ⊕ q |
| | | | T | T | F |
| | | | T | F | T |
| | | | F | T | T |
| | | | F | F | F |

- To construct a truth table for a complex expression, we can use the following steps:
  - Identify all the variables and operators in the expression and assign a column for each of them.
  - Write all possible combinations of truth values for the variables in the rows of the table. A common method is to use binary counting, starting from all F's and ending with all T's.
  - Fill in the columns for the operators by applying the corresponding truth tables to the values of the variables or subexpressions. Start from the innermost parentheses and work outwards.
  - The last column will contain the truth values of the whole expression.
- For example, to construct a truth table for the expression (p ∧ q) → (p ∨ q), we can follow these steps:

| Step | Expression | Column |
|:----:|:----------:|:------:|
| 1 | (p ∧ q) → (p ∨ q) | p | q | p ∧ q | p ∨ q | (p ∧ q) → (p ∨ q) |
| 2 | (p ∧ q) → (p ∨ q) | p | q | p ∧ q | p ∨ q | (p ∧ q) → (p ∨ q) |
| | | F | F | | | |
| | | F | T | | | |
| | | T | F | | | |
| | | T | T | | | |
| 3 | (p ∧ q) → (p ∨ q) | p | q | p ∧ q | p ∨ q | (p ∧ q) → (p ∨ q) |
| | | F | F | F | F | |
| | | F | T | F | T | |
| | | T | F | F | T | |
| | | T | T | T | T | |
| 4



### Tautology

- A tautology is a statement of propositional logic that is always true, regardless of the truth values of the propositional variables involved .
- A tautology can be recognized by using a truth table, which shows all the possible combinations of truth values for the propositional variables and the resulting truth value of the statement. If the statement is true for every row of the truth table, then it is a tautology .
- A tautology can also be recognized by using logical equivalences, which are rules that allow us to replace one statement with another that has the same truth value. If a statement can be reduced to a single propositional variable or a constant (such as T or F), then it is a tautology.
- Some examples of tautologies are :

  - p ∨ ¬p (either p or not p)
  - p → p (if p then p)
  - (p ∧ q) → (p ∨ q) (if p and q then p or q)
  - (p ↔ q) ↔ ((p → q) ∧ (q → p)) (p is equivalent to q if and only if p implies q and q implies p)
  - T (true)

- A tautology is a rule of replacement in propositional logic, which means that it can be used to replace a statement with another that has the same truth value without changing the validity of an argument.
- The rules of replacement that are based on tautologies are:

  - Idempotency of disjunction: p ∨ p ≡ p (p or p is equivalent to p)
  - Idempotency of conjunction: p ∧ p ≡ p (p and p is equivalent to p)
  - Commutativity of disjunction: p ∨ q ≡ q ∨ p (p or q is equivalent to q or p)
  - Commutativity of conjunction: p ∧ q ≡ q ∧ p (p and q is equivalent to q and p)
  - Associativity of disjunction: (p ∨ q) ∨ r ≡ p ∨ (q ∨ r) (p or q or r is equivalent to p or q or r)
  - Associativity of conjunction: (p ∧ q) ∧ r ≡ p ∧ (q ∧ r) (p and q and r is equivalent to p and q and r)
  - Distributivity of disjunction over conjunction: p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r) (p or q and r is equivalent to p or q and p or r)
  - Distributivity of conjunction over disjunction: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) (p and q or r is equivalent to p and q or p and r)
  - Double negation: ¬¬p ≡ p (not not p is equivalent to p)
  - De Morgan's laws: ¬(p ∨ q) ≡ ¬p ∧ ¬q (not p or q is equivalent to not p and not q)
  - De Morgan's laws: ¬(p ∧ q) ≡ ¬p ∨ ¬q (not p and q is equivalent to not p or not q)
  - Implication: p → q ≡ ¬p ∨ q (p implies q is equivalent to not p or q)
  - Contrapositive: p → q ≡ ¬q → ¬p (p implies q is equivalent to not q implies not p)
  - Equivalence: p ↔ q ≡ (p → q) ∧ (q → p) (p is equivalent to q is equivalent to p implies q and q implies p)
  - Negation of equivalence: ¬(p ↔ q) ≡ p ↔ ¬q (not p is equivalent to q is equivalent to p is equivalent to not q)
  - Excluded middle: p ∨ ¬p ≡ T (p or not p is equivalent to true)
  - Contradiction: p ∧ ¬p ≡ F (p and not p is equivalent to false)
  - Simplification: p ∧ q ⊢ p (p and q implies p)
  - Addition: p ⊢ p ∨ q (p implies p or q)
  - Modus ponens: p



### Satisfiability for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Satisfiability is a semantic property of a propositional formula or a set of propositional formulas that indicates whether there exists a truth assignment that makes the formula or the set true .
- A propositional formula is satisfiable if there is a 1-assignment for it; a set of propositional formulas is satisfiable if there is a simultaneous 1-assignment for its elements.
- A propositional formula is unsatisfiable if there is no truth assignment that makes it true; a set of propositional formulas is unsatisfiable if there is no simultaneous truth assignment for its elements .
- A propositional formula is valid if it is true under every truth assignment; a set of propositional formulas is valid if every truth assignment makes all its elements true .
- The propositional satisfiability problem (SAT) is the problem of determining whether a given propositional formula or set is satisfiable or not .
- SAT is a fundamental problem in logic and computer science, as many other problems can be reduced to it or solved by it  .
- SAT is also a computationally hard problem, as it belongs to the class of NP-complete problems, which means that there is no known efficient algorithm that can solve it in polynomial time  .
- There are various methods and techniques to solve SAT, such as truth tables, resolution, DPLL algorithm, heuristics, and SAT solvers  .
- There are also various extensions and variations of SAT, such as 3-SAT, k-SAT, Horn-SAT, XOR-SAT, QBF, and CSP  .



### Contradiction for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A contradiction is an assertion of propositional logic that is false in all situations; that is, it is false for all possible values of its variables .
- A contradiction can be written as a compound proposition that is logically equivalent to the constant false proposition, denoted by ⊥.
- A contradiction can also be written as a negation of a tautology, which is a proposition that is true in all situations.
- Examples of contradictions are:
  - A ∧ ¬A (A and not A)
  - A ∨ B ∧ ¬(A ∨ B) (A or B and not (A or B))
  - p → q ∧ p ∧ ¬q (if p then q and p and not q)
- A contradiction can be used as a tool to detect disingenuous beliefs and bias.
- A contradiction can also be used as a form of proof by showing that assuming the proposition to be false leads to a contradiction.
- A contradiction can also be used as a form of contraposition, which is a form of immediate inference in which a proposition is inferred from another and where the former has for its subject the contradictory of the original proposition's predicate.



### Algebra of proposition

- Algebra of proposition is the subbranch of mathematical logic that studies propositions and logical operators.
- Propositions are statements that can be either true or false, such as "It is raining" or "2 + 2 = 4".
- Logical operators are symbols that define new propositions from one or more given propositions, such as "and", "or", "not", "if...then", and "if and only if".
- The most common symbols for logical operators are:

| Symbol | Name | Meaning |
|:------:|:----:|:-------:|
| $\land$ | Conjunction | And |
| $\lor$ | Disjunction | Or |
| $\lnot$ | Negation | Not |
| $\rightarrow$ | Implication | If...then |
| $\leftrightarrow$ | Equivalence | If and only if |

- The most common symbols for propositions are $p$, $q$, $r$, etc. They are also called logical variables, because any proposition can take their place.
- The truth value of a proposition is either true (T) or false (F), depending on whether the proposition is true or false in reality.
- The truth value of a compound proposition, formed by applying logical operators to one or more propositions, depends on the truth values of the component propositions and the rules of the logical operators.
- A truth table is a table that shows the truth value of a compound proposition for all possible combinations of truth values of the component propositions.
- For example, the truth table for $p \land q$ is:

| $p$ | $q$ | $p \land q$ |
|:---:|:---:|:-----------:|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

- This means that $p \land q$ is true only when both $p$ and $q$ are true, and false otherwise.
- Similarly, the truth table for $p \lor q$ is:

| $p$ | $q$ | $p \lor q$ |
|:---:|:---:|:----------:|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

- This means that $p \lor q$ is true when either $p$ or $q$ is true, or both, and false only when both $p$ and $q$ are false.
- The truth tables for the other logical operators can be found in the references  .
- Two propositions are said to be equivalent if they have the same truth value for all possible truth values of their component propositions.
- For example, $p \rightarrow q$ is equivalent to $\lnot p \lor q$, as shown by their truth tables:

| $p$ | $q$ | $p \rightarrow q$ | $\lnot p \lor q$ |
|:---:|:---:|:-----------------:|:----------------:|
| T | T | T | T |
| T | F | F | F |
| F | T | T | T |
| F | F | T | T |

- Equivalence can be shown by using the symbol $\equiv$, such as $p \rightarrow q \equiv \lnot p \lor q$.
- Equivalence can also be proven by using logical laws, such as commutative, associative, distributive, identity, negation, double negation, De Morgan's, implication, and equivalence laws  .
- For example, to prove that $p \rightarrow q \equiv \lnot p \lor q$, we can use the implication law, which states that $p \rightarrow q \equiv \lnot (p \land \lnot q)$, and then use De Morgan's law, which states that $\lnot (p \land \lnot q) \equiv \lnot p \lor \lnot (\lnot q)$, and then use the double negation law, which states that $\lnot (\lnot q) \equiv q$.
- Therefore, we have:

$$
\begin{align*}
p \rightarrow q &\equiv \lnot (p \land \lnot q) && \text{(by implication law)} \\
&\equiv \lnot p \lor



### Theory of Inference

- Theory of inference is the study of how to derive valid conclusions from given premises using rules of logic.
- In propositional logic, the premises and conclusions are statements or propositions that can be true or false.
- Rules of inference are the logical principles that allow us to infer new propositions from existing ones.
- Some popular rules of inference in propositional logic are  :
  - Modus ponens: If p implies q and p is true, then q is true.
  - Modus tollens: If p implies q and q is false, then p is false.
  - Contraposition: If p implies q, then not q implies not p.
  - Conjunction: If p and q are true, then p and q is true.
  - Simplification: If p and q is true, then p is true.
  - Addition: If p is true, then p or q is true.
  - Disjunctive syllogism: If p or q is true and p is false, then q is true.
  - Hypothetical syllogism: If p implies q and q implies r, then p implies r.
- An argument is a sequence of propositions that ends with a conclusion.
- An argument is valid if the conclusion follows logically from the premises, i.e., if the premises are true, then the conclusion must be true.
- An argument is sound if it is valid and the premises are true.
- To prove the validity of an argument, we can use a truth table, a proof by contradiction, or a natural deduction.
- A truth table is a table that lists all the possible combinations of truth values for the propositions involved and shows the truth value of the argument for each case.
- A proof by contradiction is a method that assumes the opposite of the conclusion and shows that it leads to a contradiction with the premises or a logical absurdity.
- A natural deduction is a method that uses rules of inference to derive the conclusion from the premises in a step-by-step manner.



## Unit 5 - Predicate Logic

Predicate logic is a branch of logic that deals with predicates, quantifiers, and variables. Predicate logic is more expressive than propositional logic, as it can represent the structure and relations of objects and properties in a domain of discourse.

### 5.1 Predicates and Quantifiers

- A predicate is a sentence that contains a subject and a verb, and expresses a statement about the subject. For example, "x is red" is a predicate, where x is the subject and "is red" is the verb.
- A quantifier is a word or symbol that specifies how many or how much of something is being referred to. For example, "all", "some", "none", "there exists", and "for all" are quantifiers.
- A variable is a symbol that can stand for any object or value in a domain of discourse. For example, x, y, z, and n are variables.
- A predicate logic formula is a combination of predicates, quantifiers, variables, logical connectives, and parentheses. For example, ∀x (P(x) → Q(x)) is a predicate logic formula, where ∀ is the universal quantifier, P and Q are predicates, and x is a variable.

### 5.2 Interpretations and Models

- An interpretation of a predicate logic formula is a way of assigning meanings to the predicates, variables, and quantifiers in the formula. For example, an interpretation of ∀x (P(x) → Q(x)) could be: the domain of discourse is the set of natural numbers, P(x) means "x is even", Q(x) means "x is divisible by 4", and ∀ means "for all".
- A model of a predicate logic formula is an interpretation that makes the formula true. For example, the interpretation above is a model of ∀x (P(x) → Q(x)), since it is true that for all natural numbers x, if x is even, then x is divisible by 4.
- A predicate logic formula is valid if it is true in every interpretation, and satisfiable if it is true in at least one interpretation. For example, ∀x (P(x) → Q(x)) is valid if P(x) implies Q(x) for any possible meaning of P and Q, and satisfiable if there is at least one interpretation where P(x) implies Q(x).

### 5.3 Rules of Inference

- A rule of inference is a logical principle that allows us to derive a new formula from one or more existing formulas. For example, modus ponens is a rule of inference that says: if P and P → Q are true, then Q is true.
- A proof is a sequence of formulas, each of which is either an assumption or derived from previous formulas by a rule of inference. For example, a proof of Q from P and P → Q is:

1. P (assumption)
2. P → Q (assumption)
3. Q (modus ponens from 1 and 2)

- A formula is provable from a set of assumptions if there is a proof of the formula from the assumptions. For example, Q is provable from {P, P → Q}.
- A formula is a logical consequence of a set of formulas if it is true in every interpretation that makes the set of formulas true. For example, Q is a logical consequence of {P, P → Q}.
- A sound rule of inference is one that preserves logical consequence, i.e., if the premises are true, then the conclusion is true. For example, modus ponens is a sound rule of inference.
- A complete set of rules of inference is one that can prove any logical consequence from any set of formulas. For example, the following rules of inference are a complete set for predicate logic:

- Universal instantiation: from ∀x P(x), infer P(t), where t is any term
- Existential generalization: from P(t), infer ∃x P(x), where t is any term
- Universal generalization: from P(x), infer ∀x P(x), where x is not free in any assumption
- Existential instantiation: from ∃x P(x), infer P(c), where c is a new constant not occurring in any formula
- Modus ponens: from P and P → Q, infer Q
- Modus tollens: from ¬Q and P → Q, infer ¬P
- Hypothetical syllogism: from P → Q and Q → R, infer P → R
- Disjunctive syllogism: from P ∨ Q and ¬P, infer Q
- Addition: from P, infer P ∨ Q, where Q is



### First order predicate for the notes of the Unit 5 - Predicate Logic in the subject of Discrete Structures & Theory of Logic

- First order predicate logic is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Predicates are symbols that represent properties or relations of objects in a domain of discourse.
- Variables are symbols that can take any value from a domain of discourse.
- Quantifiers are symbols that express how many objects in a domain of discourse satisfy a predicate.
- The two most common quantifiers are the universal quantifier (∀) and the existential quantifier (∃).
- The universal quantifier (∀) means "for all" or "every". For example, ∀x P(x) means "P(x) is true for every x in the domain of discourse".
- The existential quantifier (∃) means "there exists" or "some". For example, ∃x P(x) means "there is some x in the domain of discourse such that P(x) is true".
- First order predicate logic can express more complex and nuanced statements than propositional logic, which lacks quantifiers.
- For example, propositional logic cannot express the statement "every human is mortal", but first order predicate logic can, using the predicate H(x) for "x is human" and M(x) for "x is mortal". The statement can be written as ∀x (H(x) → M(x)).
- First order predicate logic is the standard for the formalization of mathematics into axioms, and is studied in the foundations of mathematics.
- Some examples of axiomatizations of number theory and set theory using first order predicate logic are Peano arithmetic and Zermelo–Fraenkel set theory.



### Well Formed Formula of Predicate Logic

- A well formed formula (WFF) of predicate logic is a string of symbols that can be interpreted as a meaningful expression in predicate logic.
- A WFF can be either a **closed formula** or an **open formula**.
- A closed formula (also called a **sentence** or a **proposition**) is a WFF that does not contain any free variables. It can be evaluated as true or false in a given interpretation.
- An open formula (also called a **sentential function** or a **propositional function**) is a WFF that contains at least one free variable. It can be evaluated as true or false only when the free variables are assigned values from a given domain.
- The rules for constructing WFFs of predicate logic are as follows :
  - Any predicate letter followed by any constant or variable is a WFF. For example: `Pq`, `Qx`, `Rab`.
  - The result of prefixing any WFF with `~` (negation) is a WFF. For example: `~Pq`, `~(Qx ∨ Ry)`.
  - The result of joining any two WFFs with `•` (conjunction), `∨` (disjunction), `⊃` (implication), or `≡` (equivalence) and enclosing the result in parentheses is a WFF. For example: `(Pq • Qx)`, `(Qx ⊃ Ry)`, `(Pq ≡ ~Qx)`.
  - The result of prefixing any WFF with `∀` (universal quantifier) or `∃` (existential quantifier) and a variable is a WFF. For example: `∀x Pq`, `∃y Qx`, `∀x (Qx ⊃ Ry)`.
  - Nothing else is a WFF of predicate logic.



### Quantifiers

- Quantifiers are symbols that express the quantity or scope of a statement in predicate logic.
- There are two main types of quantifiers: universal and existential.
- The universal quantifier, denoted by ∀ (for all), means that the statement is true for every element in the domain of discourse.
- The existential quantifier, denoted by ∃ (there exists), means that the statement is true for at least one element in the domain of discourse.
- Quantifiers can be combined with logical connectives and parentheses to form complex statements.
- The order and placement of quantifiers matter, as they can change the meaning of a statement.
- For example, ∀x∃yP(x,y) means that for every x, there is some y such that P(x,y) is true, while ∃y∀xP(x,y) means that there is some y, such that for every x, P(x,y) is true.
- Quantifiers can also be negated, using the rules of De Morgan's laws. For example, ¬∀xP(x) is equivalent to ∃x¬P(x), and ¬∃xP(x) is equivalent to ∀x¬P(x).
- Quantifiers can be used to express statements that involve properties, relations, functions, sets, and other mathematical concepts.



### Inference theory of predicate logic

- Predicate logic, also known as first-order logic or quantified logic, is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Predicates are functions that take one or more arguments and return a truth value. For example, P(x) is a predicate that takes x as an argument and returns true or false.
- Variables are symbols that can represent any object in the domain of discourse. For example, x, y, z are variables that can stand for any person, animal, thing, etc.
- Quantifiers are operators that specify the scope or range of variables. There are two main types of quantifiers: universal and existential. For example, (x)P(x) is a universal quantifier that means "for all x, P(x) is true", and (Ex)P(x) is an existential quantifier that means "there exists some x such that P(x) is true".
- Inference theory of predicate logic is a set of rules that allow us to derive valid conclusions from quantified statements. There are four main rules of inference for predicate logic :
  - Universal specification (US): From (x)P(x), one can conclude P(y) for any y in the domain. For example, from (x)Human(x) -> Mortal(x), one can conclude Human(Socrates) -> Mortal(Socrates).
  - Universal generalization (UG): From P(y) for any y in the domain, one can conclude (x)P(x). For example, from Even(2) and Even(4), one can conclude (x)Even(x) -> x mod 2 = 0.
  - Existential specification (ES): From (Ex)P(x), one can conclude P(c) for some constant c in the domain. For example, from (Ex)Prime(x), one can conclude Prime(2) or Prime(3) or Prime(5), etc.
  - Existential generalization (EG): From P(c) for some constant c in the domain, one can conclude (Ex)P(x). For example, from Odd(3), one can conclude (Ex)Odd(x).
- These rules of inference can be used to construct valid arguments in predicate logic. For example, given the premises (x)Human(x) -> Mortal(x) and Human(Socrates), we can use US to derive Human(Socrates) -> Mortal(Socrates), and then use modus ponens to derive Mortal(Socrates).
- Inference theory of predicate logic is also useful for proving the validity or invalidity of arguments in predicate logic. For example, to prove that the argument (x)P(x) -> Q(x), (Ex)P(x) |- (Ex)Q(x) is valid, we can use the following steps:
  - Assume the premises (x)P(x) -> Q(x) and (Ex)P(x).
  - Use ES to derive P(c) for some constant c.
  - Use US to derive P(c) -> Q(c).
  - Use modus ponens to derive Q(c).
  - Use EG to derive (Ex)Q(x).
  - Therefore, the conclusion (Ex)Q(x) follows from the premises by the rules of inference.
- Inference theory of predicate logic is based on the assumption that the domain of discourse is non-empty, meaning that there is at least one object in the domain. If the domain is empty, then some of the rules of inference may not hold. For example, if the domain is empty, then (x)P(x) is vacuously true for any predicate P, but P(y) may not be true for any y. Therefore, US may not be valid in an empty domain. Similarly, if the domain is empty, then (Ex)P(x) is vacuously false for any predicate P, but P(c) may be true for some constant c. Therefore, EG may not be valid in an empty domain. To avoid these problems, we usually assume that the domain is non-empty when using inference theory of predicate logic.



## Unit 6 - Trees

- A tree is a nonlinear data structure that consists of nodes connected by edges.
- A tree has the following properties:
  - There is one node called the root, which has no parent.
  - Every node except the root has exactly one parent node.
  - A node can have zero or more child nodes.
  - There is a unique path from the root to every node.
  - A node with no children is called a leaf node.
- Some common types of trees are:
  - Binary tree: A tree where each node has at most two children.
  - Binary search tree: A binary tree where the left subtree of a node contains only nodes with values less than the node's value, and the right subtree contains only nodes with values greater than or equal to the node's value.
  - Balanced binary tree: A binary tree where the height of the left and right subtrees of every node differ by at most one.
  - AVL tree: A balanced binary search tree where the balance factor of every node is either -1, 0, or 1. The balance factor is the difference between the heights of the left and right subtrees.
  - Red-black tree: A balanced binary search tree where every node is either red or black, and the following properties hold:
    - The root is black.
    - Every leaf is black.
    - If a node is red, then both its children are black.
    - Every simple path from a node to a descendant leaf has the same number of black nodes.
  - B-tree: A tree where each node has a variable number of children, and the following properties hold:
    - The root has at least two children, unless it is the only node.
    - Every node except the root and the leaves has at least t children and at most 2t children, where t is a fixed positive integer.
    - Every leaf has the same depth, which is the height of the tree.
    - Every node contains at most 2t-1 keys, which are stored in sorted order.
    - The keys of a node divide the range of keys in its subtrees. For example, if a node has three keys a, b, and c, and four children x, y, z, and w, then all the keys in x are less than a, all the keys in y are between a and b, all the keys in z are between b and c, and all the keys in w are greater than c.
- Some common operations on trees are:
  - Traversal: Visiting every node in the tree in a specific order. There are three types of traversal for binary trees:
    - Preorder: Visit the root, then the left subtree, then the right subtree.
    - Inorder: Visit the left subtree, then the root, then the right subtree.
    - Postorder: Visit the left subtree, then the right subtree, then the root.
  - Search: Finding a node with a given value or key in the tree. The search algorithm depends on the type of the tree. For example, for a binary search tree, we can compare the value with the root, and then recursively search in the left or right subtree depending on the result of the comparison.
  - Insertion: Adding a new node with a given value or key to the tree. The insertion algorithm depends on the type of the tree. For example, for a binary search tree, we can search for the position where the new node should be inserted, and then link it to its parent. For a B-tree, we may need to split a node if it is full, and then adjust the keys and links accordingly.
  - Deletion: Removing a node with a given value or key from the tree. The deletion algorithm depends on the type of the tree. For example, for a binary search tree, we can find the node to be deleted, and then replace it with its successor or predecessor, or remove it if it is a leaf. For a B-tree, we may need to merge or redistribute nodes if they become too small, and then adjust the keys and links accordingly.



### Definition for the notes of the Unit 6 - Trees in the subject of Discrete Structures & Theory of Logic

- A **tree** is a connected, undirected graph that has no cycles.
- A **rooted tree** is a tree in which one vertex is designated as the **root** and every edge is directed away from the root.
- A **leaf** is a vertex of degree one in a tree, or a vertex with no children in a rooted tree.
- A **subtree** of a tree is a tree that consists of a vertex in the tree and all its descendants, along with the edges connecting them.
- A **binary tree** is a rooted tree in which every vertex has at most two children, called the **left child** and the **right child**.
- A **full binary tree** is a binary tree in which every vertex has either zero or two children.
- A **complete binary tree** is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
- A **height-balanced binary tree** is a binary tree in which the height of the left and right subtrees of every vertex differ by at most one.
- A **binary search tree** is a binary tree in which the key of each vertex is greater than or equal to the keys of all vertices in its left subtree and less than or equal to the keys of all vertices in its right subtree.
- A **spanning tree** of a graph is a subgraph that is a tree and contains all the vertices of the graph.
- A **minimum spanning tree** of a weighted graph is a spanning tree that has the smallest possible sum of weights of its edges.



### Binary tree

- A binary tree is a tree data structure where each node has at most two child nodes, creating the branches of the tree  .
- The two children are usually called the left and right nodes .
- A binary tree is also an ordered tree (a.k.a. plane tree) in which every node has a fixed position relative to its parent.
- A binary tree can be empty (no nodes) or non-empty (at least one node).
- A binary tree can be classified into different types based on the number and structure of its nodes, such as:
  - A full binary tree (sometimes referred to as a proper or plane or strict binary tree) is a tree in which every node has either 0 or 2 children .
  - A complete binary tree is a tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
  - A balanced binary tree is a tree in which the height of the left and right subtrees of every node differ by at most 1.
  - A perfect binary tree is a full binary tree in which all leaves are at the same level.
- A binary tree can be represented by a pointer to the topmost node (commonly known as the “root”) of the tree.
- A binary tree can be traversed in different ways, such as:
  - Preorder traversal: visit the root node, then the left subtree, then the right subtree.
  - Inorder traversal: visit the left subtree, then the root node, then the right subtree.
  - Postorder traversal: visit the left subtree, then the right subtree, then the root node.
  - Level order traversal: visit the nodes level by level, from left to right.
- A binary tree can be used to implement various data structures and algorithms, such as:
  - Binary search tree: a binary tree where the left subtree of a node contains only nodes with keys less than the node's key, and the right subtree of a node contains only nodes with keys greater than the node's key.
  - Heap: a binary tree where the key of a node is greater than or equal to (max-heap) or less than or equal to (min-heap) the keys of its children.
  - Huffman coding: a binary tree where the leaves represent symbols and their frequencies, and the internal nodes represent the prefix codes for the symbols.
  - Expression tree: a binary tree where the leaves represent operands and the internal nodes represent operators.
  - Decision tree: a binary tree where the nodes represent questions or tests, and the branches represent possible outcomes or actions.



### Binary tree traversal

Binary tree traversal is a process of visiting each node in a binary tree exactly once in a predefined order. A binary tree is a non-linear data structure that consists of nodes connected by edges. Each node has at most two children, called the left child and the right child. The node without any child is called a leaf node. The node at the top of the tree is called the root node.

There are three common types of binary tree traversal: inorder, preorder and postorder. Each type of traversal defines a different order of visiting the nodes. The order of traversal can be represented by a recursive algorithm or an iterative algorithm using a stack.

#### Inorder traversal

Inorder traversal visits the nodes in the following order:

- Traverse the left subtree in inorder
- Visit the root node
- Traverse the right subtree in inorder

Inorder traversal is useful for binary search trees, as it gives the nodes in sorted order. For example, the inorder traversal of the following binary tree is 4, 2, 5, 1, 3.

```
    1
   / \
  2   3
 / \
4   5
```

The recursive algorithm for inorder traversal is:

```
void inorder(node *root) {
  if (root == NULL) return; // base case
  inorder(root->left); // traverse left subtree
  print(root->data); // visit root node
  inorder(root->right); // traverse right subtree
}
```

The iterative algorithm for inorder traversal using a stack is:

```
void inorder(node *root) {
  stack<node*> s; // create an empty stack
  node *current = root; // start from the root node
  while (current != NULL || !s.empty()) { // while there are nodes to visit
    while (current != NULL) { // while the current node is not null
      s.push(current); // push the current node to the stack
      current = current->left; // move to the left child
    }
    current = s.top(); // pop the top node from the stack
    s.pop();
    print(current->data); // visit the node
    current = current->right; // move to the right child
  }
}
```

#### Preorder traversal

Preorder traversal visits the nodes in the following order:

- Visit the root node
- Traverse the left subtree in preorder
- Traverse the right subtree in preorder

Preorder traversal is useful for creating a copy of the tree or printing the tree structure. For example, the preorder traversal of the following binary tree is 1, 2, 4, 5, 3.

```
    1
   / \
  2   3
 / \
4   5
```

The recursive algorithm for preorder traversal is:

```
void preorder(node *root) {
  if (root == NULL) return; // base case
  print(root->data); // visit root node
  preorder(root->left); // traverse left subtree
  preorder(root->right); // traverse right subtree
}
```

The iterative algorithm for preorder traversal using a stack is:

```
void preorder(node *root) {
  stack<node*> s; // create an empty stack
  s.push(root); // push the root node to the stack
  while (!s.empty()) { // while the stack is not empty
    node *current = s.top(); // pop the top node from the stack
    s.pop();
    print(current->data); // visit the node
    if (current->right != NULL) s.push(current->right); // push the right child to the stack if not null
    if (current->left != NULL) s.push(current->left); // push the left child to the stack if not null
  }
}
```

#### Postorder traversal

Postorder traversal visits the nodes in the following order:

- Traverse the left subtree in postorder
- Traverse the right subtree in postorder
- Visit the root node

Postorder traversal is useful for deleting the tree or evaluating an expression tree. For example, the postorder traversal of the following binary tree is 4, 5, 2, 3, 1.

```
    1
   / \
  2   3
 / \
4   5
```

The recursive algorithm for postorder traversal is:

```
void postorder(node *root) {
  if (root == NULL) return; // base case
  postorder(root->left); //

```




### Binary search tree

- A binary search tree (BST) is a rooted binary tree data structure with the following properties :
  - The key of each node is greater than all the keys in its left subtree and less than all the keys in its right subtree.
  - The left and right subtrees of each node are also binary search trees.
  - There are no duplicate keys in the tree.
- A binary search tree supports the following operations in logarithmic time on average :
  - Search: find a node with a given key in the tree, or return null if not found.
  - Insert: add a new node with a given key and value to the tree, maintaining the BST property.
  - Delete: remove a node with a given key from the tree, maintaining the BST property.
  - Min: find the node with the smallest key in the tree.
  - Max: find the node with the largest key in the tree.
  - Predecessor: find the node with the largest key that is smaller than a given key.
  - Successor: find the node with the smallest key that is larger than a given key.
  - Inorder: traverse the nodes in the tree in ascending order of their keys.
- A binary search tree can be represented by an array, where the root node is at index 1, and the left and right children of a node at index i are at indices 2i and 2i+1, respectively.
- A binary search tree can also be represented by a linked list, where each node has a pointer to its left and right child, and optionally a pointer to its parent.
- A binary search tree can be balanced or unbalanced, depending on the shape of the tree. A balanced BST has a height that is logarithmic in the number of nodes, while an unbalanced BST can have a height that is linear in the number of nodes. A balanced BST can be achieved by using self-balancing algorithms, such as AVL trees, red-black trees, or splay trees .

: Binary search tree - Wikipedia
: Binary Search Tree - GeeksforGeeks
: Binary Search Trees - Princeton University



## Unit 7 - Graphs

- A graph is a collection of vertices (or nodes) and edges (or arcs) that connect them.
- A graph can be represented by an adjacency matrix, an adjacency list, or an edge list.
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



### Definition and terminology for the notes of the Unit 7 - Graphs in the subject of Discrete Structures & Theory of Logic

- A **graph** is a mathematical structure that consists of a set of **vertices** and a set of **edges** that connect pairs of vertices.
- A graph can be represented by a diagram where vertices are drawn as dots or circles and edges are drawn as lines or curves between them.
- A graph can also be represented by an **adjacency matrix**, a square matrix where the entry in row i and column j is 1 if there is an edge between vertex i and vertex j, and 0 otherwise.
- A graph can be **directed** or **undirected**. A directed graph has edges that are ordered pairs of vertices, indicating a direction from one vertex to another. An undirected graph has edges that are unordered pairs of vertices, indicating no direction.
- A graph can be **simple** or **multigraph**. A simple graph has no **loops** (edges that connect a vertex to itself) and no **multiple edges** (more than one edge between the same pair of vertices). A multigraph can have loops and multiple edges.
- A graph can be **weighted** or **unweighted**. A weighted graph has a **weight** (a numerical value) assigned to each edge, indicating some measure of cost, distance, or importance. An unweighted graph has no weights on the edges.
- A graph can be **connected** or **disconnected**. A connected graph has a **path** (a sequence of edges) between any two vertices. A disconnected graph has at least two vertices that are not connected by a path.
- A graph can be **cyclic** or **acyclic**. A cyclic graph has a **cycle** (a path that starts and ends at the same vertex). An acyclic graph has no cycles.
- A graph can be **complete** or **incomplete**. A complete graph has an edge between every pair of vertices. An incomplete graph has at least one pair of vertices that are not adjacent.
- A graph can be **bipartite** or **non-bipartite**. A bipartite graph has a **partition** (a division) of the vertices into two sets, such that every edge connects a vertex from one set to a vertex from the other set. A non-bipartite graph has no such partition.



### Representation of graphs

A graph is a mathematical structure that consists of a set of vertices and a set of edges that connect pairs of vertices. A graph can be used to model many types of relations and processes in physical, biological, social and information systems.

There are different ways to represent a graph, depending on the purpose and the type of the graph. Some of the common representations are:

- **Adjacency matrix**: An adjacency matrix is a square matrix of size n x n, where n is the number of vertices in the graph. The entry in the i-th row and j-th column of the matrix is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For an undirected graph, the adjacency matrix is symmetric, meaning that the entry in the i-th row and j-th column is equal to the entry in the j-th row and i-th column. For a directed graph, the adjacency matrix is not necessarily symmetric, meaning that the entry in the i-th row and j-th column may not be equal to the entry in the j-th row and i-th column. For a weighted graph, the entry in the i-th row and j-th column is the weight of the edge from vertex i to vertex j, instead of 1 or 0.

  An example of an adjacency matrix for an undirected graph with 5 vertices is:

  |   | 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|
  | 1 | 0 | 1 | 0 | 0 | 1 |
  | 2 | 1 | 0 | 1 | 1 | 0 |
  | 3 | 0 | 1 | 0 | 1 | 0 |
  | 4 | 0 | 1 | 1 | 0 | 1 |
  | 5 | 1 | 0 | 0 | 1 | 0 |

  An example of an adjacency matrix for a directed graph with 5 vertices is:

  |   | 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|
  | 1 | 0 | 1 | 0 | 0 | 0 |
  | 2 | 0 | 0 | 1 | 0 | 0 |
  | 3 | 0 | 0 | 0 | 1 | 0 |
  | 4 | 0 | 0 | 0 | 0 | 1 |
  | 5 | 1 | 0 | 0 | 0 | 0 |

  An example of an adjacency matrix for a weighted graph with 5 vertices is:

  |   | 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|
  | 1 | 0 | 2 | 0 | 0 | 5 |
  | 2 | 2 | 0 | 3 | 4 | 0 |
  | 3 | 0 | 3 | 0 | 1 | 0 |
  | 4 | 0 | 4 | 1 | 0 | 2 |
  | 5 | 5 | 0 | 0 | 2 | 0 |

  The advantages of using an adjacency matrix are:

  - It is easy to check if there is an edge between two vertices, by looking at the corresponding entry in the matrix.
  - It is easy to add or remove an edge, by changing the corresponding entry in the matrix.
  - It is easy to compute the degree of a vertex, by summing up the entries in the corresponding row or column of the matrix.

  The disadvantages of using an adjacency matrix are:

  - It requires O(n^2) space, where n is the number of vertices, which can be wasteful if the graph is sparse (has few edges).
  - It requires O(n) time to find all the neighbors of a vertex, by scanning the corresponding row or column of the matrix.

- **Adjacency list**: An adjacency list is a collection of lists, one for each vertex in the graph. The list for a vertex contains all the vertices that are adjacent to it, i.e., have an edge from or to it. For an undirected graph, the list for a vertex contains all the vertices that share an edge with it. For a directed graph, the list for a vertex contains all the vertices that have an edge to it, i.e., the successors of the vertex. For a weighted graph



### Multigraphs

- A **multigraph** is a graph that allows multiple edges (also called parallel edges) between the same pair of vertices. A multigraph may or may not have loops, which are edges that connect a vertex to itself .
- A **simple graph** is a graph that has no loops and no multiple edges, i.e., each edge connects two distinct vertices and no two edges connect the same pair of vertices.
- A **pseudograph** is a graph that allows both loops and multiple edges.
- A **multidigraph** (or **directed multigraph**) is a directed graph that allows multiple arcs (also called parallel arcs) between the same pair of vertices, i.e., arcs that have the same source and target nodes. A multidigraph may or may not have loops.
- A **digraph** (or **directed graph**) is a graph that has a direction associated with each edge, i.e., each edge is an ordered pair of vertices. A digraph may or may not have loops and multiple edges.
- The **degree** of a vertex in a multigraph is the number of edges incident to it, counting each loop twice and each multiple edge according to its multiplicity.
- The **in-degree** of a vertex in a multidigraph is the number of arcs directed to it, counting each loop once and each multiple arc according to its multiplicity. The **out-degree** of a vertex in a multidigraph is the number of arcs directed from it, counting each loop once and each multiple arc according to its multiplicity.
- A multigraph is **connected** if there is a path between any two vertices. A multidigraph is **strongly connected** if there is a directed path between any two vertices. A multidigraph is **weakly connected** if it is connected when ignoring the directions of the arcs.
- A **subgraph** of a multigraph is a multigraph whose vertex set is a subset of the original multigraph and whose edge set is a subset of the original edge set. A **subgraph** of a multidigraph is a multidigraph whose vertex set is a subset of the original multidigraph and whose arc set is a subset of the original arc set.
- A **spanning subgraph** of a multigraph is a subgraph that contains all the vertices of the original multigraph. A **spanning subgraph** of a multidigraph is a subgraph that contains all the vertices of the original multidigraph.
- A **walk** in a multigraph is a sequence of vertices and edges that starts and ends at a vertex, such that each edge is incident to the vertices before and after it in the sequence. A **walk** in a multidigraph is a sequence of vertices and arcs that starts and ends at a vertex, such that each arc is directed from the vertex before it to the vertex after it in the sequence.
- A **trail** is a walk that does not repeat any edge. A **path** is a walk that does not repeat any vertex. A **circuit** is a trail that starts and ends at the same vertex. A **cycle** is a path that starts and ends at the same vertex.
- A **Eulerian trail** is a trail that contains every edge of the multigraph exactly once. A **Eulerian circuit** is a circuit that contains every edge of the multigraph exactly once. A **Eulerian path** is a path that contains every edge of the multidigraph exactly once. A **Eulerian cycle** is a cycle that contains every edge of the multidigraph exactly once.
- A **Hamiltonian path** is a path that contains every vertex of the multigraph exactly once. A **Hamiltonian cycle** is a cycle that contains every vertex of the multigraph exactly once.
- A **tree** is a connected simple graph that has no cycles. A **forest** is a simple graph that has no cycles, i.e., a disjoint union of trees. A **rooted tree** is a tree in which one vertex is designated as the root and every edge is directed away from the root. A **rooted forest** is a forest in which each component is a rooted tree.
- A **spanning tree** of a connected multigraph is a spanning subgraph that is a tree. A **spanning forest** of a multigraph is



### Bipartite graphs

- A bipartite graph is a graph in which the set of vertices can be partitioned into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set .
- A bipartite graph can also be defined as a graph that is two-colorable, meaning that the vertices can be colored with two colors such that no two adjacent vertices have the same color .
- The two sets of vertices in a bipartite graph are usually called the parts of the graph, and are denoted by and . A bipartite graph can be written as .
- A complete bipartite graph is a bipartite graph in which every vertex in is adjacent to every vertex in . A complete bipartite graph with vertices in and vertices in can be denoted by .
- Bipartite graphs are mostly used in modeling relationships, especially between two separate classes of objects, such as customers and products, students and courses, etc.
- Some properties of bipartite graphs are:
  - A bipartite graph has no odd cycles, that is, cycles of odd length .
  - The chromatic number of a bipartite graph is 2, that is, it can be colored with two colors .
  - The maximum number of edges in a bipartite graph with vertices is , where and are the sizes of the parts .
  - The bipartite graphs are precisely the graphs that have no induced subgraphs isomorphic to , , or  .



### Planar Graphs

- A planar graph is a graph that can be drawn on a plane without any edges crossing.
- A plane graph is a planar graph with a specific way of drawing it on a plane, such that the edges are represented by curves that do not intersect except at their endpoints.
- A planar graph can have different plane graphs, depending on how it is drawn. For example, the following graph is planar and has two different plane graphs:

```
    A-----B
   / \   / \
  /   \ /   \
 C-----D-----E
```

```
    A-----B
   / \   / \
  /   \ /   \
 C     D     E
  \   / \   /
   \ /   \ /
    F-----G
```

- A planar graph divides the plane into regions called faces. The number of faces depends on the plane graph. For example, the first plane graph above has four faces, while the second one has six faces.
- A planar graph has some properties that relate the number of vertices, edges, and faces. For example, Euler's formula states that for any connected plane graph, the following equation holds:

```
V - E + F = 2
```

where V is the number of vertices, E is the number of edges, and F is the number of faces.
- A planar graph also has some limitations on the number and degree of its vertices and edges. For example, Kuratowski's theorem states that a graph is planar if and only if it does not contain a subgraph that is homeomorphic to K5 (the complete graph on five vertices) or K3,3 (the complete bipartite graph on six vertices).



### Isomorphism and Homeomorphism of graphs

- Isomorphism and homeomorphism are two concepts in graph theory that deal with the similarity and equivalence of graphs.
- A graph is a set of vertices and edges that connect some pairs of vertices. A graph can be represented by a diagram where vertices are shown as dots and edges are shown as lines or curves.
- Two graphs are **isomorphic** if they have the same number of vertices and edges, and there is a one-to-one correspondence between their vertices that preserves the adjacency of vertices. That is, two vertices are adjacent in one graph if and only if their corresponding vertices are adjacent in the other graph.
- An **isomorphism** is a bijective function that maps the vertices of one graph to the vertices of another graph, such that the edge relation is preserved. For example, the following two graphs are isomorphic, and the function f is an isomorphism:

isomorphic graphs

- Two graphs are **homeomorphic** if they can be obtained from each other by a sequence of subdivisions and contractions of edges. A **subdivision** of an edge is the operation of replacing an edge by a path of two or more edges, with a new vertex on each internal edge. A **contraction** of an edge is the inverse operation of removing an edge and identifying its endpoints as a single vertex. For example, the following two graphs are homeomorphic, and the sequence of operations shows how to transform one graph into the other:

homeomorphic graphs

- A **homeomorphism** is a graph isomorphism from some subdivision of one graph to some subdivision of another graph. For example, the function g is a homeomorphism from the first graph to the second graph in the above example:

homeomorphism

- Properties of isomorphisms and homeomorphisms:
  - Isomorphism is an equivalence relation on graphs, that is, it is reflexive, symmetric and transitive. Homeomorphism is also an equivalence relation on graphs.
  - Isomorphism preserves the degree of vertices, that is, the number of edges incident to a vertex. Homeomorphism does not preserve the degree of vertices, as subdivision and contraction can change the degree of vertices.
  - Isomorphism preserves the number of cycles, that is, the closed paths in a graph. Homeomorphism does not preserve the number of cycles, as subdivision and contraction can create or destroy cycles.
  - Isomorphism preserves the planarity of graphs, that is, the property of being drawable on a plane without crossing edges. Homeomorphism also preserves the planarity of graphs, as subdivision and contraction do not affect the planarity of graphs.



### Euler and Hamiltonian paths

- An **Euler path** is a path that passes through every **edge** exactly once  . If it ends at the initial vertex then it is an **Euler cycle**  .
- A **Hamiltonian path** is a path that passes through every **vertex** exactly once  . If it ends at the initial vertex then it is a **Hamiltonian cycle**  .
- Euler paths and cycles can be found using **Euler's theorem**, which states that a connected graph has an Euler path if and only if it has exactly **zero or two vertices of odd degree** . A connected graph has an Euler cycle if and only if it has **no vertices of odd degree** .
- Hamiltonian paths and cycles are harder to find, as there is no simple necessary and sufficient criteria to determine if they exist in a graph. However, some **sufficient conditions** are:
  - **Dirac's theorem**: A simple graph with n vertices (n ≥ 3) is Hamiltonian if every vertex has degree n/2 or greater .
  - **Ore's theorem**: A simple graph with n vertices (n ≥ 3) is Hamiltonian if for every pair of non-adjacent vertices, their degrees sum to n or more .
  - **Bondy and Chvátal's theorem**: A simple graph with n vertices (n ≥ 3) is Hamiltonian if for every pair of non-adjacent vertices with degrees summing to less than n, adding an edge between them results in a Hamiltonian graph .
- Some **necessary conditions** for a graph to be Hamiltonian are:
  - The graph must be **connected** .
  - The graph must have at least **three vertices** .
  - The graph must not contain any **vertex cut** (a set of vertices whose removal disconnects the graph) .
- Some examples of graphs that have Euler paths, Euler cycles, Hamiltonian paths, and Hamiltonian cycles are shown below:

Euler and Hamiltonian paths and cycles

- The graph on the left has an Euler path (a-b-c-d-e-f-g-h-i-j-k-l) but not an Euler cycle, as it has two vertices of odd degree (a and l) . It also has a Hamiltonian path (a-b-c-d-e-f-g-h-i-j-k-l) but not a Hamiltonian cycle, as a and l are not adjacent .
- The graph on the right has an Euler cycle (a-b-c-d-e-f-g-h-i-j-k-l-a) and an Euler path (any subset of the cycle), as it has no vertices of odd degree . It also has a Hamiltonian cycle (a-b-c-d-e-f-g-h-i-j-k-l-a) and a Hamiltonian path (any subset of the cycle), as it satisfies Dirac's theorem .



### Graph coloring

- Graph coloring is a special case of graph labeling, where each vertex of a graph is assigned a color, subject to some constraints.
- One of the most common constraints is that no two adjacent vertices (vertices that are connected by an edge) have the same color. This is called a **proper coloring** or a **vertex coloring** .
- Graph coloring is closely related to the concept of an **independent set**, which is a set of vertices in a graph that are not adjacent to each other. If a graph is properly colored, the vertices that have the same color form an independent set .
- Graph coloring has many applications in computer science, such as scheduling, register allocation, map coloring, Sudoku, and cryptography .
- The minimum number of colors needed to properly color a graph is called the **chromatic number** of the graph, denoted by χ(G). Finding the chromatic number of a graph is an NP-hard problem, meaning that there is no efficient algorithm to solve it in general .
- Some special classes of graphs have known chromatic numbers, such as bipartite graphs (χ(G) = 2), complete graphs (χ(G) = n, where n is the number of vertices), and trees (χ(G) = 2, unless the graph has only one vertex, then χ(G) = 1) .
- There are different types of graph coloring, such as **edge coloring** (assigning colors to the edges of a graph, such that no two adjacent edges have the same color), **face coloring** (assigning colors to the faces of a planar graph, such that no two adjacent faces have the same color), and **list coloring** (assigning colors to the vertices of a graph, such that each vertex has a list of available colors to choose from) .



## Unit 8 - Recurrence Relation & Generating function

- A recurrence relation is an equation that defines a sequence recursively, that is, each term of the sequence is expressed as a function of the preceding terms.
- A generating function is a formal power series that encodes the information of a sequence in its coefficients.
- Recurrence relations and generating functions are useful tools for analyzing and solving many problems in discrete mathematics, such as counting, combinatorics, recurrence, and algorithms.

### Examples of recurrence relations

- The Fibonacci sequence is defined by the recurrence relation F(n) = F(n-1) + F(n-2), with initial conditions F(0) = 0 and F(1) = 1.
- The factorial function is defined by the recurrence relation n! = n * (n-1)!, with initial condition 0! = 1.
- The binomial coefficients are defined by the recurrence relation C(n,k) = C(n-1,k-1) + C(n-1,k), with initial conditions C(n,0) = C(n,n) = 1.

### Examples of generating functions

- The generating function of the Fibonacci sequence is F(x) = x / (1 - x - x^2), which can be obtained by multiplying both sides of the recurrence relation by x^n and summing over n.
- The generating function of the factorial function is F(x) = e^x, which can be obtained by using the Taylor series expansion of e^x.
- The generating function of the binomial coefficients is F(x) = (1 + x)^n, which can be obtained by using the binomial theorem.



### Recursive definition of functions

- A recursive definition of a function is a way of defining a function by using its own previous values as inputs for the next values.
- A recursive function is a function that calls itself as part of its computation.
- A recursive function has two parts: a base case and a recursive case.
- The base case is the simplest or smallest input for which the function can be defined directly.
- The recursive case is the general or larger input for which the function can be defined in terms of the function applied to a smaller input.
- A recursive function must have at least one base case and at least one recursive case.
- A recursive function must always move towards the base case, otherwise it will never terminate.
- A recursive function can be represented by a recurrence relation, which is an equation that expresses the value of the function in terms of its previous values.
- A recursive function can also be represented by a generating function, which is a formal power series that encodes the sequence of values generated by the function.
- Examples of recursive functions are the factorial function, the Fibonacci sequence, the Ackermann function, etc .



### Recursive algorithms

- A recursive algorithm is an algorithm that calls itself, either directly or indirectly, to solve a smaller instance of the same problem.
- A recursive algorithm must have a base case, which is a condition that terminates the recursion when it is satisfied.
- A recursive algorithm must also have a recursive case, which is a condition that reduces the problem size and invokes the algorithm again with the smaller problem.
- A recursive algorithm can be more elegant and concise than an iterative algorithm, but it may also be less efficient or more difficult to understand.
- Examples of recursive algorithms are:
  - Merge sort, which sorts an array by recursively dividing it into two halves, sorting each half, and merging them together.
  - Quick sort, which sorts an array by recursively partitioning it around a pivot element, and sorting the left and right subarrays.
  - Tower of Hanoi, which moves a stack of disks from one peg to another, by recursively moving the top n-1 disks to a spare peg, moving the bottom disk to the destination peg, and moving the n-1 disks from the spare peg to the destination peg.
  - Fibonacci series, which generates the nth term of the sequence by recursively adding the previous two terms.
  - Factorial, which computes the product of all positive integers up to n by recursively multiplying n by the factorial of n-1.



### Method of solving recurrences

A recurrence relation is an equation that defines a sequence in terms of its previous terms. Recurrence relations are often used to model the time complexity of recursive algorithms. There are several methods to solve recurrence relations, such as:

- **Forward substitution**: This method involves solving the recurrence relation for small values of n until a pattern emerges, and then making a guess for the general solution. The guess can be verified by mathematical induction.
- **Recursion tree**: This method involves converting the recurrence relation into a tree, where each node represents the cost of a recursive call. The total cost of the algorithm is the sum of the costs of all the nodes in the tree. The tree can be simplified by using asymptotic notation and bounding the costs of each level .
- **Master theorem**: This method is applicable for recurrence relations of the form T(n) = aT(n/b) + f(n), where a, b, and f(n) are constants or functions of n. The master theorem provides a formula to find the asymptotic solution of T(n) based on the comparison of f(n) and n^(log_b a).
- **Akra-Bazzi method**: This method is a generalization of the master theorem that can handle recurrence relations of the form T(n) = g(n) + \sum_{i=1}^k a_i T(b_i n + h_i(n)), where g(n), a_i, b_i, and h_i(n) are constants or functions of n. The Akra-Bazzi method provides a formula to find the asymptotic solution of T(n) based on the solution of a certain integral.



## Unit 9 - Combinatorics

- Combinatorics is the branch of mathematics that studies the ways of counting, arranging, and selecting objects from a given set or collection.
- Combinatorics has applications in many areas of mathematics, such as probability, graph theory, cryptography, coding theory, and algebra.
- Some of the basic concepts and techniques of combinatorics are:

  - **Factorial**: The factorial of a positive integer n, denoted by n!, is the product of all positive integers from 1 to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. The factorial of 0 is defined to be 1, that is, 0! = 1.
  - **Permutation**: A permutation of a set of n distinct objects is an ordered arrangement of those objects. For example, the permutations of the set {a, b, c} are abc, acb, bac, bca, cab, and cba. The number of permutations of n distinct objects is n!. For example, the number of permutations of 3 distinct objects is 3! = 6.
  - **Combination**: A combination of a set of n distinct objects is an unordered selection of k objects from that set, where k is a nonnegative integer less than or equal to n. For example, the combinations of the set {a, b, c} taken 2 at a time are ab, ac, and bc. The number of combinations of n distinct objects taken k at a time is denoted by C(n, k) or (n k), and is given by the formula C(n, k) = n! / (k! (n - k)!). For example, the number of combinations of 3 distinct objects taken 2 at a time is C(3, 2) = 3! / (2! 1!) = 3.
  - **Binomial Coefficient**: The binomial coefficient (n k) is another notation for C(n, k), the number of combinations of n distinct objects taken k at a time. The binomial coefficient has many properties and applications, such as the binomial theorem, which states that (x + y)^n = sum_(k=0)^n (n k) x^(n-k) y^k, where sum_(k=0)^n means the sum of the terms from k = 0 to k = n.
  - **The Rule of Sum**: The rule of sum states that if a task can be done in m ways or in n ways, where the two sets of ways are mutually exclusive (that is, they do not overlap), then the task can be done in m + n ways. For example, if a person can choose a shirt from 5 different colors and a pair of pants from 4 different styles, then the person can choose an outfit in 5 + 4 = 9 ways.
  - **The Rule of Product**: The rule of product states that if a task can be done in m ways and another task can be done in n ways, where the two tasks are independent (that is, the choice of one does not affect the choice of the other), then the two tasks can be done together in m x n ways. For example, if a person can choose a shirt from 5 different colors and a pair of pants from 4 different styles, then the person can choose an outfit in 5 x 4 = 20 ways.



### Introduction for the notes of the Unit 9 - Combinatorics in the subject of Discrete Structures & Theory of Logic

- Combinatorics is the branch of mathematics that deals with counting, arranging, and selecting discrete objects.
- Combinatorics has applications in many areas of computer science, such as cryptography, coding theory, algorithm design, graph theory, and artificial intelligence.
- Some of the basic concepts and techniques of combinatorics are:

  - The rule of sum and the rule of product, which allow us to count the number of possible outcomes of a compound event by adding or multiplying the number of outcomes of simpler events.
  - The principle of inclusion-exclusion, which allows us to count the number of elements in a union of sets by subtracting the number of elements in their intersections.
  - The binomial theorem, which gives us a formula for expanding a power of a binomial expression, and also allows us to compute binomial coefficients, which count the number of ways to choose a subset of a given size from a set.
  - Permutations and combinations, which count the number of ways to order or select a subset of objects from a set, with or without repetition, and with or without regard to order.
  - The pigeonhole principle, which states that if more than n objects are placed into n boxes, then some box must contain more than one object, and which can be used to prove the existence of certain patterns or properties.
  - Recurrence relations, which describe how a sequence of numbers or functions is defined in terms of its previous terms, and which can be used to model various phenomena, such as the Fibonacci sequence, the Tower of Hanoi problem, and the Catalan numbers.
  - Generating functions, which are formal power series that encode the information about a sequence of numbers or functions, and which can be used to manipulate, solve, and analyze recurrence relations, as well as to count various combinatorial objects.



### Counting Techniques

- Counting techniques are methods to determine the number of possible outcomes of a given situation without actually listing or counting them.
- Counting techniques are useful for solving problems in combinatorics, probability, and cryptography.
- Some common counting techniques are:

  - **The product rule**: If there are n ways to perform the first task and m ways to perform the second task, then there are n × m ways to perform both tasks in sequence.
  - **The sum rule**: If there are n ways to perform the first task and m ways to perform the second task, and the tasks are mutually exclusive, then there are n + m ways to perform either task.
  - **The inclusion-exclusion principle**: If there are n ways to perform the first task and m ways to perform the second task, and the tasks are not mutually exclusive, then there are n + m - k ways to perform either task, where k is the number of ways to perform both tasks.
  - **The permutation rule**: If there are n distinct objects and we want to arrange r of them in a specific order, then there are n! / (n - r)! ways to do so, where n! is the factorial of n.
  - **The combination rule**: If there are n distinct objects and we want to choose r of them without regard to order, then there are n! / (r! (n - r)!) ways to do so, where n! is the factorial of n and r! is the factorial of r.
  - **The binomial coefficient**: The binomial coefficient (n choose r) is the number of ways to choose r objects from n distinct objects without regard to order. It is equal to n! / (r! (n - r)!).
  - **The multinomial coefficient**: The multinomial coefficient (n choose r1, r2, ..., rk) is the number of ways to divide n distinct objects into k groups of sizes r1, r2, ..., rk, without regard to order. It is equal to n! / (r1! r2! ... rk!).
  - **The pigeonhole principle**: If there are n objects and k boxes, and n > k, then at least one box must contain more than one object. This principle can be used to prove the existence of certain outcomes or patterns.



### Pigeonhole Principle

- The pigeonhole principle is a basic but powerful idea in combinatorics that states that if more objects are placed into fewer containers, then at least one container must hold more than one object.
- The principle can be used to prove the existence of certain outcomes without explicitly finding them, or to show that some outcomes are impossible.
- The principle is also known as the Dirichlet principle, after the German mathematician Peter Gustav Lejeune Dirichlet, who popularized it in the 19th century.
- The principle can be illustrated by a simple example: if there are 10 pigeons and 9 pigeonholes, then at least one pigeonhole must contain more than one pigeon, since 10 is greater than 9.
- The principle can be generalized to different situations, such as:
  - If there are n+1 pigeons and n pigeonholes, then at least one pigeonhole must contain more than one pigeon, or at least two pigeonholes must contain the same number of pigeons.
  - If there are N pigeons and K pigeonholes, and N/K is not an integer, then at least one pigeonhole must contain more than N/K pigeons, or at least K+1 pigeonholes must contain the same number of pigeons.
  - If there are N pigeons and K pigeonholes, and N > K, then the maximum number of pigeons that can be placed in the pigeonholes such that no pigeonhole contains more than one pigeon is K, and the minimum number of pigeons that must be placed in the pigeonholes such that every pigeonhole contains at least one pigeon is K.
- The principle can be applied to various problems in mathematics, such as:
  - Proving that there are infinitely many prime numbers, by assuming that there are finitely many and placing them into pigeonholes according to their remainders when divided by a larger prime number.
  - Proving that there are irrational numbers, by assuming that there are only rational numbers and placing them into pigeonholes according to their denominators when written in lowest terms.
  - Proving that there are two people in the world with the same number of hairs on their head, by assuming that there are 7 billion people and 150,000 hairs on average, and placing them into pigeonholes according to their hair count.
  - Proving that there are two points in a unit square with distance less than 1/2, by dividing the square into four equal quarters and placing the points into pigeonholes according to their quarter.
  - Proving that there are two people in a group of 23 who have the same birthday, by assuming that there are 365 days in a year and placing the people into pigeonholes according to their birthday.

