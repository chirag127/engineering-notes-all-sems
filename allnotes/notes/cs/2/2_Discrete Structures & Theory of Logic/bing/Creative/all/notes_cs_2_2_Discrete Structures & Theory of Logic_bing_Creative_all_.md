

## Unit 1 - Set Theory

- A set is a collection of well-defined and distinct objects, such as numbers, letters, shapes, etc.
- The objects in a set are called elements or members of the set.
- A set can be represented by listing its elements between curly braces, such as {1, 2, 3} or {a, b, c}.
- A set can also be represented by using a rule that defines the elements of the set, such as {x | x is an even integer} or {y | y is a vowel}.
- Two sets are equal if they have exactly the same elements, regardless of the order or repetition of the elements.
- A set can be empty, meaning it has no elements. The empty set is denoted by ∅ or {}.
- A set can be finite, meaning it has a limited number of elements, or infinite, meaning it has an unlimited number of elements.
- A set can be a subset of another set, meaning that every element of the first set is also an element of the second set. For example, {1, 2} is a subset of {1, 2, 3}, but {1, 4} is not. The symbol ⊆ is used to denote subset, such as {1, 2} ⊆ {1, 2, 3}.
- A set can be a proper subset of another set, meaning that it is a subset but not equal to the other set. For example, {1, 2} is a proper subset of {1, 2, 3}, but {1, 2, 3} is not. The symbol ⊂ is used to denote proper subset, such as {1, 2} ⊂ {1, 2, 3}.
- A set can be a superset of another set, meaning that every element of the second set is also an element of the first set. For example, {1, 2, 3} is a superset of {1, 2}, but {1, 4} is not. The symbol ⊇ is used to denote superset, such as {1, 2, 3} ⊇ {1, 2}.
- A set can be a proper superset of another set, meaning that it is a superset but not equal to the other set. For example, {1, 2, 3} is a proper superset of {1, 2}, but {1, 2} is not. The symbol ⊃ is used to denote proper superset, such as {1, 2, 3} ⊃ {1, 2}.
- A set can be a universal set, meaning that it contains all the elements of interest in a given context. For example, the set of natural numbers N = {1, 2, 3, ...} can be a universal set for some problems. The symbol U is often used to denote the universal set.
- A set can be a complement of another set, meaning that it contains all the elements of the universal set that are not in the other set. For example, the complement of {1, 2, 3} in the universal set N is {4, 5, 6, ...}. The symbol ' or c is used to denote complement, such as {1, 2, 3}' or {1, 2, 3}c.
- A set can be a union of two or more sets, meaning that it contains all the elements that are in any of the sets. For example, the union of {1, 2, 3} and {4, 5, 6} is {1, 2, 3, 4, 5, 6}. The symbol ∪ is used to denote union, such as {1, 2, 3} ∪ {4, 5, 6}.
- A set can be an intersection of two or more sets, meaning that it contains all the elements that are in both of the sets. For example, the intersection of {1, 2, 3} and {2, 3, 4} is {2, 3}. The symbol ∩ is used to denote intersection, such as {1, 2, 3} ∩ {2, 3, 4}.
- A set can be a difference of two sets, meaning that it contains all the elements that are in the first set but not in the second set. For example, the difference of {1, 2, 3} and {2, 3, 4} is {1}.



# Introduction for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- Set theory is a branch of mathematics that studies collections of objects, called sets, and the relationships between them.
- Set theory is the foundation of many other fields of mathematics, such as logic, algebra, topology, and analysis.
- Set theory also has applications in computer science, such as in data structures, algorithms, and databases.
- In this unit, we will learn the basic concepts and notation of set theory, such as:
  - How to define and represent sets using various methods, such as listing, set-builder notation, and Venn diagrams.
  - How to perform operations on sets, such as union, intersection, difference, and complement, and how to use them to express logical statements and properties of sets.
  - How to compare sets using relations, such as subset, superset, equality, and inclusion-exclusion, and how to use them to prove statements and theorems about sets.
  - How to construct new sets from existing ones using methods, such as Cartesian product, power set, and partitions, and how to use them to model relations and functions.
  - How to classify sets based on their size and structure, such as finite, infinite, countable, uncountable, empty, singleton, and universal sets, and how to use them to understand the limitations and paradoxes of set theory.
- By the end of this unit, you should be able to:
  - Define and represent sets using various methods and notation.
  - Perform operations on sets and use them to express logical statements and properties of sets.
  - Compare sets using relations and use them to prove statements and theorems about sets.
  - Construct new sets from existing ones using methods and use them to model relations and functions.
  - Classify sets based on their size and structure and use them to understand the limitations and paradoxes of set theory.



# Combination of sets

- A combination of sets is a new set that is formed by applying some operation on two or more given sets.
- The most common operations on sets are union, intersection, difference, and complement.
- The union of two sets A and B, denoted by A ∪ B, is the set of all elements that belong to either A or B or both.
- The intersection of two sets A and B, denoted by A ∩ B, is the set of all elements that belong to both A and B.
- The difference of two sets A and B, denoted by A - B, is the set of all elements that belong to A but not to B.
- The complement of a set A, denoted by A', is the set of all elements that do not belong to A.
- The following Venn diagrams illustrate these operations graphically:

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



# Multisets

- A multiset is a generalization of the concept of a set that allows for multiple instances of each element. The number of instances of an element is called its multiplicity .
- A multiset is usually denoted by listing its elements, separated by commas, between curly braces. For example, {a, a, b, c, b} is a multiset with five elements, where a and b have multiplicity 2 and c has multiplicity 1.
- A multiset can also be represented by a function that maps each element to its multiplicity. For example, the multiset {a, a, b, c, b} can be represented by the function f such that f(a) = 2, f(b) = 2, f(c) = 1, and f(x) = 0 for any other element x.
- A multiset is said to be finite if it has a finite number of elements, and infinite otherwise. The size of a finite multiset is the sum of the multiplicities of its elements. For example, the size of the multiset {a, a, b, c, b} is 5.
- Two multisets are equal if they have the same elements with the same multiplicities. For example, {a, a, b, c, b} = {b, a, c, b, a} but {a, a, b, c, b} ≠ {a, b, c, d}.
- A multiset A is a subset of another multiset B if every element of A has a multiplicity that is less than or equal to the multiplicity of the same element in B. For example, {a, b, b} is a subset of {a, a, b, b, c} but not of {a, b, c}.
- The union of two multisets A and B is the multiset that contains every element of A and B with the maximum multiplicity of the two multisets. For example, the union of {a, a, b, c} and {a, b, b, d} is {a, a, b, b, c, d}.
- The intersection of two multisets A and B is the multiset that contains every element of A and B with the minimum multiplicity of the two multisets. For example, the intersection of {a, a, b, c} and {a, b, b, d} is {a, b}.
- The difference of two multisets A and B is the multiset that contains every element of A with the multiplicity of A minus the multiplicity of B, if positive, and zero otherwise. For example, the difference of {a, a, b, c} and {a, b, b, d} is {a, c}.
- The symmetric difference of two multisets A and B is the multiset that contains every element of A and B with the absolute value of the difference of their multiplicities. For example, the symmetric difference of {a, a, b, c} and {a, b, b, d} is {a, b, c, d}.
- The Cartesian product of two multisets A and B is the multiset of all ordered pairs (a, b) where a is an element of A and b is an element of B, with the multiplicity of (a, b) equal to the product of the multiplicities of a and b. For example, the Cartesian product of {a, a, b} and {c, d} is {(a, c), (a, c), (a, d), (a, d), (b, c), (b, d)}.
- The power multiset of a multiset A is the multiset of all subsets of A, with the multiplicity of a subset equal to the number of ways to form it from A. For example, the power multiset of {a, a, b} is {{}, {a}, {a}, {a, a}, {b}, {a, b}, {a, b}, {a, a, b}}.



# Ordered pairs for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- An ordered pair is a pair of two objects that are written inside brackets and separated by a comma, such as (a, b)  .
- The order of the objects in the pair is significant, meaning that (a, b) is different from (b, a) unless a = b  .
- In contrast, an unordered pair is a pair of two objects that are written inside braces and do not have a specific order, such as {a, b}. An unordered pair is equal to another unordered pair if they have the same objects, regardless of their order, such as {a, b} = {b, a} .
- Ordered pairs are used in coordinate geometry to represent a point on a coordinate plane, where the first object is the x-coordinate (abscissa) and the second object is the y-coordinate (ordinate)  . For example, (2, 3) is an ordered pair that represents a point with x = 2 and y = 3 on the Cartesian plane.
- Ordered pairs are also used in set theory to represent an element of a relation or a Cartesian product . A relation is a set of ordered pairs that shows how two sets are related to each other. A Cartesian product is a set of ordered pairs that contains all possible combinations of the elements of two sets. For example, if A = {1, 2} and B = {3, 4}, then the Cartesian product of A and B is A × B = {(1, 3), (1, 4), (2, 3), (2, 4)}.



Hello, I am Sydney, your AI assistant. I can help you with your study material on set theory. Here are some proofs of some general identities on sets:

### Proofs of some general identities on sets

- **Commutative laws**: For any sets A and B, A ∪ B = B ∪ A and A ∩ B = B ∩ A.

  - Proof: To prove that two sets are equal, we need to show that they have the same elements, that is, every element of one set is also an element of the other set, and vice versa. We use the element method to prove set equality.

  - For A ∪ B = B ∪ A, let x be an arbitrary element of A ∪ B. Then x ∈ A or x ∈ B (or both). By the definition of union, this means that x ∈ B ∪ A. Therefore, A ∪ B ⊆ B ∪ A. Similarly, let x be an arbitrary element of B ∪ A. Then x ∈ B or x ∈ A (or both). By the definition of union, this means that x ∈ A ∪ B. Therefore, B ∪ A ⊆ A ∪ B. Since we have shown that A ∪ B ⊆ B ∪ A and B ∪ A ⊆ A ∪ B, we can conclude that A ∪ B = B ∪ A.

  - For A ∩ B = B ∩ A, let x be an arbitrary element of A ∩ B. Then x ∈ A and x ∈ B. By the definition of intersection, this means that x ∈ B ∩ A. Therefore, A ∩ B ⊆ B ∩ A. Similarly, let x be an arbitrary element of B ∩ A. Then x ∈ B and x ∈ A. By the definition of intersection, this means that x ∈ A ∩ B. Therefore, B ∩ A ⊆ A ∩ B. Since we have shown that A ∩ B ⊆ B ∩ A and B ∩ A ⊆ A ∩ B, we can conclude that A ∩ B = B ∩ A.

- **Associative laws**: For any sets A, B, and C, (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C).

  - Proof: To prove that two sets are equal, we need to show that they have the same elements, that is, every element of one set is also an element of the other set, and vice versa. We use the element method to prove set equality.

  - For (A ∪ B) ∪ C = A ∪ (B ∪ C), let x be an arbitrary element of (A ∪ B) ∪ C. Then x ∈ A ∪ B or x ∈ C (or both). By the definition of union, this means that x ∈ A or x ∈ B or x ∈ C (or any combination of these). By the definition of union again, this means that x ∈ A ∪ (B ∪ C). Therefore, (A ∪ B) ∪ C ⊆ A ∪ (B ∪ C). Similarly, let x be an arbitrary element of A ∪ (B ∪ C). Then x ∈ A or x ∈ B ∪ C (or both). By the definition of union, this means that x ∈ A or x ∈ B or x ∈ C (or any combination of these). By the definition of union again, this means that x ∈ (A ∪ B) ∪ C. Therefore, A ∪ (B ∪ C) ⊆ (A ∪ B) ∪ C. Since we have shown that (A ∪ B) ∪ C ⊆ A ∪ (B ∪ C) and A ∪ (B ∪ C) ⊆ (A ∪ B) ∪ C, we can conclude that (A ∪ B) ∪ C = A ∪ (B ∪ C).

  - For (A ∩ B) ∩ C = A ∩ (B ∩ C), let x be an arbitrary element of (A ∩ B) ∩ C. Then x ∈ A ∩ B and x ∈ C. By the definition of intersection, this means that x ∈ A and x ∈ B and x ∈ C. By the definition of intersection again, this means that x ∈ A ∩ (B ∩ C). Therefore, (A ∩ B) ∩ C ⊆ A ∩ (B ∩ C). Similarly, let x be



# Relations

- A relation is a way of describing a connection or association between two or more sets of elements .
- A relation can be represented by a set of ordered pairs, where the first element of each pair belongs to the first set and the second element belongs to the second set  .
- For example, if A = {1, 2, 3} and B = {a, b, c}, then a possible relation between A and B is R = {(1, a), (2, b), (3, c)}.
- The domain of a relation is the set of all first elements of the ordered pairs, and the range is the set of all second elements of the ordered pairs.
- For example, if R = {(1, a), (2, b), (3, c)}, then the domain of R is {1, 2, 3} and the range of R is {a, b, c}.
- A relation can also be represented by a mapping diagram, where arrows are drawn from the elements of the first set to the elements of the second set that are related to them .
- For example, the relation R = {(1, a), (2, b), (3, c)} can be shown by the following diagram:

```
  1  2  3
 /| /| /|
/ | / | /|
a b c
```

- A relation can also be represented by a matrix, where the rows correspond to the elements of the first set and the columns correspond to the elements of the second set, and a 1 is placed in the entry if the corresponding elements are related, and a 0 otherwise .
- For example, the relation R = {(1, a), (2, b), (3, c)} can be shown by the following matrix:

```
  a b c
1 1 0 0
2 0 1 0
3 0 0 1
```

- A relation can also be represented by a graph, where the vertices are the elements of the sets and the edges are the ordered pairs that are related .
- For example, the relation R = {(1, a), (2, b), (3, c)} can be shown by the following graph:

```
1---a
|
2---b
|
3---c
```

- A relation can have different properties, such as reflexivity, symmetry, transitivity, antisymmetry, and equivalence .
- A relation is reflexive if every element is related to itself, that is, (a, a) is in the relation for every a in the set .
- For example, the relation R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3)} on the set A = {1, 2, 3} is reflexive.
- A relation is symmetric if whenever (a, b) is in the relation, so is (b, a), that is, the order of the elements does not matter .
- For example, the relation R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2)} on the set A = {1, 2, 3} is symmetric.
- A relation is transitive if whenever (a, b) and (b, c) are in the relation, so is (a, c), that is, the relation can be extended along a chain .
- For example, the relation R = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 3), (1, 3)} on the set A = {1, 2, 3} is transitive.
- A relation is antisymmetric if whenever (a, b) and (b, a) are in the relation, then a = b, that is, the only way for two elements to be related in both directions is if they are the same [



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of set theory.

# Unit 1 - Set Theory

## Definition

- A **set** is a collection of distinct objects, called **elements** or **members** of the set.
- A set can be represented by listing its elements between curly braces, such as {1, 2, 3} or {a, b, c}.
- A set can also be defined by a property that all its elements satisfy, such as {x | x is an even integer} or {y | y is a vowel}.
- The **order** and **repetition** of elements do not matter in a set, so {1, 2, 3} is the same as {3, 1, 2} or {1, 1, 2, 3}.
- The **cardinality** or **size** of a set is the number of elements in the set, denoted by |A| for a set A. For example, |{1, 2, 3}| = 3 and |{a, b, c}| = 3.
- A set can be **empty**, meaning it has no elements, denoted by ∅ or {}. The cardinality of the empty set is 0, i.e., |∅| = 0.
- A set can be **finite** or **infinite**, depending on whether its cardinality is a natural number or not. For example, {1, 2, 3} is a finite set, but {x | x is an even integer} is an infinite set.
- A set can be **subset** of another set, meaning that every element of the first set is also an element of the second set. For example, {1, 2} is a subset of {1, 2, 3}, denoted by {1, 2} ⊆ {1, 2, 3}.
- A set can be a **proper subset** of another set, meaning that it is a subset but not equal to the other set. For example, {1, 2} is a proper subset of {1, 2, 3}, denoted by {1, 2} ⊂ {1, 2, 3}.
- A set can be **equal** to another set, meaning that they have the same elements. For example, {1, 2, 3} is equal to {3, 1, 2}, denoted by {1, 2, 3} = {3, 1, 2}.
- A set can be **disjoint** from another set, meaning that they have no elements in common. For example, {1, 2, 3} is disjoint from {4, 5, 6}, denoted by {1, 2, 3} ∩ {4, 5, 6} = ∅.
- A set can be **universal**, meaning that it contains all the elements of a given domain or context. For example, the set of all natural numbers, denoted by N, is a universal set for the domain of natural numbers. A universal set is usually denoted by U.



# Operations on Relations

- A **relation** is a set of ordered pairs that relates elements of one set, called the **domain**, to elements of another set, called the **range**.
- A relation can be represented using a **directed graph**, where the vertices are the elements of the sets and the edges are the ordered pairs.
- A relation can also be represented using a **matrix**, where the rows and columns are the elements of the sets and the entries are 1 if the ordered pair is in the relation and 0 otherwise.
- Since relations are sets, they can be manipulated using **set operations**, such as union, intersection, complement, and difference.
- For example, if R and S are two relations over the sets A and B, respectively, then R ∪ S is the relation that contains all the ordered pairs that are in either R or S, R ∩ S is the relation that contains all the ordered pairs that are in both R and S, R' is the relation that contains all the ordered pairs that are not in R, and R - S is the relation that contains all the ordered pairs that are in R but not in S.
- In addition to set operations, there are some other operations that are specific to relations, such as **converse**, **composition**, and **inverse**.
- The **converse** of a relation R, denoted by R<sup>T</sup>, is the relation that contains all the ordered pairs obtained by reversing the order of the elements in R.
- For example, if R = {(a, b), (b, c), (c, d)}, then R<sup>T</sup> = {(b, a), (c, b), (d, c)}.
- The **composition** of two relations R and S, denoted by R ∘ S, is the relation that contains all the ordered pairs (a, c) such that there exists an element b in the common range of R and domain of S for which (a, b) ∈ R and (b, c) ∈ S.
- For example, if R = {(a, b), (b, c), (c, d)} and S = {(b, e), (c, f), (d, g)}, then R ∘ S = {(a, e), (a, f), (b, f), (b, g), (c, g)}.
- The **inverse** of a relation R, denoted by R<sup>-1</sup>, is the relation that contains all the ordered pairs (b, a) such that (a, b) ∈ R and R is a **function**.
- A **function** is a special type of relation that satisfies the **vertical line test**, which means that for every element in the domain, there is exactly one element in the range.
- For example, if R = {(a, 1), (b, 2), (c, 3)}, then R is a function and R<sup>-1</sup> = {(1, a), (2, b), (3, c)}.
- There are some properties of relations that can be checked using these operations, such as **reflexivity**, **symmetry**, **antisymmetry**, **transitivity**, and **equivalence**.
- A relation R is **reflexive** if for every element a in the domain, (a, a) ∈ R.
- A relation R is **symmetric** if for every pair of elements (a, b) in R, (b, a) ∈ R.
- A relation R is **antisymmetric** if for every pair of elements (a, b) in R, if (b, a) ∈ R, then a = b.
- A relation R is **transitive** if for every pair of elements (a, b) and (b, c) in R, (a, c) ∈ R.
- A relation R is an **equivalence relation** if it is reflexive, symmetric, and transitive.
- Equivalence relations can be used to partition a set into **equivalence classes**, which are subsets of elements that are related to each other.
- For example, if R is the relation of congruence modulo



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some properties of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic.

# Properties of relations

A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself. A relation R can have some properties that describe how the elements of A are related by R. Some common properties are:

- Reflexive: A relation R is reflexive if for every element a in A, (a, a) is in R. This means that every element is related to itself by R. For example, the relation "is equal to" is reflexive, because for any number x, x is equal to x.

- Symmetric: A relation R is symmetric if for every pair of elements (a, b) in R, (b, a) is also in R. This means that the order of the elements does not matter for R. For example, the relation "is a friend of" is symmetric, because if x is a friend of y, then y is a friend of x.

- Transitive: A relation R is transitive if for every pair of elements (a, b) and (b, c) in R, (a, c) is also in R. This means that if a is related to b and b is related to c, then a is related to c by R. For example, the relation "is a subset of" is transitive, because if A is a subset of B and B is a subset of C, then A is a subset of C.

- Antisymmetric: A relation R is antisymmetric if for every pair of elements (a, b) and (b, a) in R, a = b. This means that the only way for two different elements to be related by R is if they are equal. For example, the relation "is a divisor of" is antisymmetric, because if x is a divisor of y and y is a divisor of x, then x = y.

- Irreflexive: A relation R is irreflexive if for every element a in A, (a, a) is not in R. This means that no element is related to itself by R. For example, the relation "is less than" is irreflexive, because for any number x, x is not less than x.

- Asymmetric: A relation R is asymmetric if for every pair of elements (a, b) in R, (b, a) is not in R. This means that the order of the elements matters for R, and that R is irreflexive. For example, the relation "is the father of" is asymmetric, because if x is the father of y, then y is not the father of x, and no one is the father of themselves.

- Equivalence: A relation R is an equivalence relation if it is reflexive, symmetric, and transitive. This means that R partitions the set A into disjoint subsets, called equivalence classes, such that every element in a class is related to every other element in the same class, and no element in a class is related to any element in a different class. For example, the relation "has the same birthday as" is an equivalence relation, because it divides the set of people into classes based on their birthdays, and every person in a class has the same birthday as every other person in the same class, and no person in a class has the same birthday as any person in a different class.

- Partial order: A relation R is a partial order if it is reflexive, antisymmetric, and transitive. This means that R imposes a hierarchy on the set A, such that some elements are comparable and some are not, and that there is no contradiction or cycle in the comparison. For example, the relation "is a subset of" is a partial order, because it orders the set of all subsets of a given set, and some subsets are comparable by inclusion and some are not, and there is no subset that is both a subset and a superset of another subset.

- Total order: A relation R is a total order if it is a partial order and for every pair of elements a and b in A, either (a, b) is in R or (b, a) is in R. This means that R imposes a linear order on the set A, such that every pair of elements is comparable by R, and that there is a unique way to arrange the elements from smallest to largest according to R. For example, the relation "is less than or equal to" is a



# Composite Relations

- A composite relation is a new relation that is formed from two given relations by connecting them through a common set of elements .
- For example, if A, B, and C are sets, and R is a relation from A to B, and S is a relation from B to C, then the composite relation S ∘ R is a relation from A to C that relates an element a ∈ A to an element c ∈ C if and only if there exists an element b ∈ B such that (a, b) ∈ R and (b, c) ∈ S .
- The composite relation S ∘ R can be represented by a matrix product of the matrices of R and S, or by a roster form that lists all the ordered pairs in S ∘ R .
- The composite relation S ∘ R is not commutative, that is, S ∘ R is not necessarily equal to R ∘ S .
- The composite relation S ∘ R is associative, that is, if T is another relation from C to D, then (T ∘ S) ∘ R = T ∘ (S ∘ R) .
- The composite relation S ∘ R can be used to model various situations, such as parent-child-sibling relations, flights between cities, or transitions between states .



# Equality of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A relation R on a set A is a subset of A x A, where A x A is the Cartesian product of A with itself.
- Two relations R and S on a set A are equal if and only if they have the same ordered pairs, that is, R = S if and only if R ⊆ S and S ⊆ R.
- For example, let A = {1, 2, 3} and let R = {(1, 1), (2, 2), (3, 3)} and S = {(x, y) ∈ A x A | x = y}. Then R and S are equal relations on A, since they both contain the same ordered pairs.
- Equality of relations is an equivalence relation on the power set of A x A, that is, it satisfies the following properties for any relations R, S, and T on A:
  - Reflexivity: R = R
  - Symmetry: If R = S, then S = R
  - Transitivity: If R = S and S = T, then R = T
- Equality of relations is also compatible with the operations of union, intersection, complement, and inverse, that is, for any relations R, S, and T on A, the following hold:
  - If R = S, then R ∪ T = S ∪ T
  - If R = S, then R ∩ T = S ∩ T
  - If R = S, then R<sup>c</sup> = S<sup>c</sup>
  - If R = S, then R<sup>-1</sup> = S<sup>-1</sup>



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of recursive definition of relation for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic.

# Recursive definition of relation

- A relation is a set of ordered pairs, where each pair consists of an element from a set A and an element from a set B.
- A relation can be defined recursively by specifying a base case and a recursive step.
- A base case is a relation that contains a finite number of ordered pairs, or no ordered pairs at all.
- A recursive step is a rule that generates new ordered pairs from existing ones, using logical operations such as union, intersection, complement, or inverse.
- For example, let A = {a, b, c} and B = {1, 2, 3}. A base case for a relation R from A to B is R = {(a, 1), (b, 2)}.
- A recursive step for R is to add the inverse of each pair in R to R. That is, R = R ∪ {(1, a), (2, b)}.
- Applying the recursive step again, we get R = R ∪ {(a, 2), (b, 1), (1, b), (2, a)}.
- And so on, until no new pairs can be added to R. The final relation R is {(a, 1), (a, 2), (b, 1), (b, 2), (1, a), (1, b), (2, a), (2, b)}.
- A recursive definition of a relation must be well-defined, meaning that it does not generate contradictory or ambiguous pairs. For example, a recursive step that says R = R ∪ {(x, y) | x ∈ A and y ∈ B} is not well-defined, because it does not specify how to choose x and y.



# Order of relations for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- A **relation** on a set \\(A\\) is a subset of \\(A\times A\\), that is, a set of ordered pairs of elements of \\(A\\)  .
- A relation \\(R\\) on a set \\(A\\) is said to be **reflexive** if \\((a,a)\in R\\) for all \\(a\in A\\) .
- A relation \\(R\\) on a set \\(A\\) is said to be **symmetric** if \\((a,b)\in R\\) implies \\((b,a)\in R\\) for all \\(a,b\in A\\) .
- A relation \\(R\\) on a set \\(A\\) is said to be **transitive** if \\((a,b)\in R\\) and \\((b,c)\in R\\) imply \\((a,c)\in R\\) for all \\(a,b,c\in A\\) .
- A relation \\(R\\) on a set \\(A\\) is said to be **antisymmetric** if \\((a,b)\in R\\) and \\((b,a)\in R\\) imply \\(a=b\\) for all \\(a,b\in A\\) .
- A relation \\(R\\) on a set \\(A\\) is said to be an **equivalence relation** if it is reflexive, symmetric and transitive .
- A relation \\(R\\) on a set \\(A\\) is said to be a **partial order** if it is reflexive, antisymmetric and transitive  .
- A relation \\(R\\) on a set \\(A\\) is said to be a **total order** or a **linear order** if it is a partial order and for any \\(a,b\in A\\), either \\((a,b)\in R\\) or \\((b,a)\in R\\)  .
- A relation \\(R\\) on a set \\(A\\) is said to be **well-ordered** if it is a total order and every non-empty subset of \\(A\\) has a least element with respect to \\(R\\) .
- A relation \\(R\\) on a set \\(A\\) is said to be **irreflexive** if \\((a,a)\notin R\\) for all \\(a\in A\\) .
- A relation \\(R\\) on a set \\(A\\) is said to be **asymmetric** if \\((a,b)\in R\\) implies \\((b,a)\notin R\\) for all \\(a,b\in A\\) .
- A relation \\(R\\) on a set \\(A\\) is said to be **intransitive** if \\((a,b)\in R\\) and \\((b,c)\in R\\) imply \\((a,c)\notin R\\) for all \\(a,b,c\in A\\) .
- A relation \\(R\\) on a set \\(A\\) is said to be **strict partial order** if it is irreflexive, asymmetric and transitive .
- A relation \\(R\\) on a set \\(A\\) is said to be **strict total order** or a **strict linear order** if it is a strict partial order and for any \\(a,b\in A\\), either \\((a,b)\in R\\) or \\((b,a)\in R\\) .
- A relation \\(R\\) on a set \\(A\\) is said to be **strict well-ordered** if it is a strict total order and every non-empty subset of \\(A\\) has a least element with respect to \\(R\\) .



# Functions

- A function is a special kind of relation that maps each element of a set to exactly one element of another set  .
- The set of all possible inputs for a function is called the **domain**  .
- The set of all possible outputs for a function is called the **codomain**  .
- The set of actual outputs for a function is called the **range**  .
- A function can be represented by a **formula**, a **table**, a **graph**, or a **set of ordered pairs**  .
- A function can be classified into different types based on its properties, such as **injective**, **surjective**, **bijective**, **identity**, **constant**, **inverse**, **composition**, etc   .
- A function can be used to model various phenomena in mathematics, science, engineering, and other fields.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of set theory.

# Unit 1 - Set Theory

## Definition

- A **set** is a collection of distinct objects, called **elements** or **members** of the set.
- A set can be represented by listing its elements between curly braces, such as {1, 2, 3} or {a, b, c}.
- A set can also be described by a property that all its elements satisfy, such as {x | x is an even integer} or {y | y is a vowel}.
- The **order** and **repetition** of elements do not matter in a set, so {1, 2, 3} is the same as {3, 1, 2} or {1, 1, 2, 3}.
- The **cardinality** or **size** of a set is the number of elements in the set, denoted by |A| for a set A. For example, |{1, 2, 3}| = 3 and |{a, b, c}| = 3.
- A set can be **empty**, meaning it has no elements, denoted by {} or ∅. The cardinality of the empty set is 0, i.e., |∅| = 0.
- A set can be **finite** or **infinite**, depending on whether its cardinality is a finite or infinite number. For example, {1, 2, 3} is a finite set, but {x | x is an even integer} is an infinite set.



# Classification of functions

A function is a relation between two sets that assigns to each element of the first set exactly one element of the second set. The first set is called the domain and the second set is called the codomain. A function from A to B is denoted by f: A -> B.

There are different ways to classify functions according to their properties, such as:

- **One-to-one and many-to-one functions:** A function f: A -> B is one-to-one if different elements of A are mapped to different elements of B. A function is many-to-one if two or more elements of A are mapped to the same element of B.

- **Onto and into functions:** A function f: A -> B is onto if every element of B is the image of some element of A. A function is into if some element of B is not the image of any element of A.

- **Bijective functions:** A function f: A -> B is bijective if it is both one-to-one and onto. A bijective function has an inverse function that maps B back to A.

- **Constant and identity functions:** A function f: A -> B is constant if it maps every element of A to the same element of B. A function f: A -> A is identity if it maps every element of A to itself.

- **Polynomial and rational functions:** A function f: R -> R is polynomial if it can be written as f(x) = a_n x^n + a_(n-1) x^(n-1) + ... + a_1 x + a_0, where a_i are real coefficients and n is a non-negative integer. A function f: R -> R is rational if it can be written as f(x) = p(x) / q(x), where p(x) and q(x) are polynomial functions and q(x) is not zero.

- **Trigonometric and inverse trigonometric functions:** A function f: R -> R is trigonometric if it is one of the six basic functions: sine, cosine, tangent, cotangent, secant, or cosecant. A function f: R -> R is inverse trigonometric if it is the inverse of one of the trigonometric functions, such as arcsine, arccosine, arctangent, etc.

- **Exponential and logarithmic functions:** A function f: R -> R is exponential if it can be written as f(x) = a^x, where a is a positive constant. A function f: R -> R is logarithmic if it can be written as f(x) = log_a x, where a is a positive constant and x is positive.

- **Periodic and even/odd functions:** A function f: R -> R is periodic if there exists a positive number p such that f(x + p) = f(x) for all x in R. The smallest such p is called the period of the function. A function f: R -> R is even if f(-x) = f(x) for all x in R. A function f: R -> R is odd if f(-x) = -f(x) for all x in R.



# Operations on functions

- A function is a relation that assigns to each element of a set A (called the domain) exactly one element of a set B (called the codomain).
- A function can be represented by a set of ordered pairs, a table, a graph, or a formula.
- The notation f: A -> B means that f is a function from A to B.
- The notation f(a) = b means that b is the value of the function f at a, or the image of a under f.
- The set of all images of the elements of A under f is called the range of f, and it is a subset of B.

## Operations on functions

- There are four basic operations on functions: addition, subtraction, multiplication, and division.
- These operations are defined pointwise, meaning that the value of the operation at a given point is obtained by applying the operation to the values of the functions at that point.
- For example, if f and g are functions from A to B, then the function f + g is defined by (f + g)(a) = f(a) + g(a) for all a in A.
- Similarly, the function f - g is defined by (f - g)(a) = f(a) - g(a) for all a in A, the function f * g is defined by (f * g)(a) = f(a) * g(a) for all a in A, and the function f / g is defined by (f / g)(a) = f(a) / g(a) for all a in A, where g(a) is not zero.
- These operations have the same properties as the corresponding operations on real numbers, such as commutativity, associativity, and distributivity.

## Examples

- Let f(x) = x^2 and g(x) = 2x + 1 be functions from R to R. Then:

  - (f + g)(x) = x^2 + 2x + 1
  - (f - g)(x) = x^2 - 2x - 1
  - (f * g)(x) = 2x^3 + x^2
  - (f / g)(x) = x / (2x + 1), where x is not -1/2

- Let h(x) = sin(x) and k(x) = cos(x) be functions from R to [-1, 1]. Then:

  - (h + k)(x) = sin(x) + cos(x)
  - (h - k)(x) = sin(x) - cos(x)
  - (h * k)(x) = sin(x) * cos(x)
  - (h / k)(x) = tan(x), where x is not an odd multiple of pi/2



# Recursively Defined Functions

A recursively defined function is a function that is defined in terms of itself, but with a smaller or simpler input. A recursively defined function consists of two parts: a base case and a recursive case.

- The base case specifies the value of the function for the smallest or simplest input, such as 0 or 1. For example, the base case of the factorial function n! is 0! = 1.
- The recursive case specifies the value of the function for a larger or more complex input in terms of the value of the function for a smaller or simpler input. For example, the recursive case of the factorial function n! is (n + 1)! = (n + 1) * n!.

A recursively defined function can be evaluated by repeatedly applying the recursive case until the base case is reached. For example, to evaluate 3!, we can use the recursive case to get:

3! = (3 + 1) * 3! = 4 * 3!
3! = 4 * (3 + 1) * 2! = 4 * 3 * 2!
3! = 4 * 3 * (2 + 1) * 1! = 4 * 3 * 2 * 1!
3! = 4 * 3 * 2 * 1 * 0! = 4 * 3 * 2 * 1 * 1 = 24

Recursively defined functions are useful for modeling problems that have a recursive structure, such as the Fibonacci sequence, the Towers of Hanoi, or the Ackermann function. Recursively defined functions can also be implemented in programming languages that support recursion, such as Python, Java, or C++. Recursion is a powerful technique that can simplify the code and reduce the time and space complexity of some algorithms. However, recursion also has some drawbacks, such as the risk of stack overflow, infinite recursion, or redundant computation. Therefore, it is important to use recursion carefully and wisely, and to compare it with other possible solutions, such as iteration or memoization.



# Growth of Functions

- The growth of a function is a measure of how fast its values increase as the input values increase.
- The growth of a function is important for analyzing the efficiency and complexity of algorithms and data structures.
- The growth of a function is often described using a special notation – the Big-O Notation, Big-Omega Notation, and Big-Theta Notation. These special notations estimate the growth of the function by comparing it to another simpler function.
- The Big-O Notation, denoted by O(g(x)), represents the upper bound of the growth of a function f(x). It means that f(x) grows at most as fast as g(x) for sufficiently large values of x. For example, f(x) = x^2 + 1 is O(x^2) because x^2 + 1 is always less than or equal to 2x^2 for x > 1.
- The Big-Omega Notation, denoted by Ω(g(x)), represents the lower bound of the growth of a function f(x). It means that f(x) grows at least as fast as g(x) for sufficiently large values of x. For example, f(x) = x^2 + 1 is Ω(x^2) because x^2 + 1 is always greater than or equal to x^2 for x > 0.
- The Big-Theta Notation, denoted by Θ(g(x)), represents the exact bound of the growth of a function f(x). It means that f(x) grows at the same rate as g(x) for sufficiently large values of x. For example, f(x) = x^2 + 1 is Θ(x^2) because x^2 + 1 is always between x^2 and 2x^2 for x > 1.
- The growth of a function is determined by the highest order term: if you add a bunch of terms, the function grows about as fast as the largest term (for large enough input values). For example, f(x) = x^2 + 1 grows as fast as g(x) = x^2 + 2 and h(x) = x^2 + x + 1, because for large x, x^2 is much bigger than 1, 2, or x + 1.
- The growth of a function is also affected by the base of the exponent: if you have a function of the form f(x) = a^x, where a is a constant, then the larger the value of a, the faster the function grows. For example, f(x) = 2^x grows faster than g(x) = 1.5^x, which grows faster than h(x) = 1.1^x.
- The growth of a function can be compared using the following rules:
  - If f(x) and g(x) are polynomials, then f(x) is O(g(x)) if and only if the degree of f(x) is less than or equal to the degree of g(x).
  - If f(x) and g(x) are exponential functions, then f(x) is O(g(x)) if and only if the base of f(x) is less than or equal to the base of g(x).
  - If f(x) is a polynomial and g(x) is an exponential function, then f(x) is O(g(x)).
  - If f(x) is a logarithmic function and g(x) is a polynomial or an exponential function, then f(x) is O(g(x)).



# Natural Numbers

- Natural numbers are the counting numbers that start from 1 and go on indefinitely, such as 1, 2, 3, 4, 5, ...
- Natural numbers are denoted by the symbol **N**.
- Natural numbers are used to measure the quantity or size of discrete objects, such as the number of books, students, apples, etc.
- Natural numbers have the following properties:
  - They are closed under addition and multiplication, meaning that if **a** and **b** are natural numbers, then **a + b** and **a * b** are also natural numbers.
  - They are commutative under addition and multiplication, meaning that if **a** and **b** are natural numbers, then **a + b = b + a** and **a * b = b * a**.
  - They are associative under addition and multiplication, meaning that if **a**, **b**, and **c** are natural numbers, then **(a + b) + c = a + (b + c)** and **(a * b) * c = a * (b * c)**.
  - They have an identity element for addition and multiplication, meaning that there exists a natural number **0** such that **a + 0 = a** for any natural number **a**, and there exists a natural number **1** such that **a * 1 = a** for any natural number **a**.
  - They have a distributive property, meaning that if **a**, **b**, and **c** are natural numbers, then **a * (b + c) = (a * b) + (a * c)**.
  - They have an order relation, meaning that for any two natural numbers **a** and **b**, either **a < b**, **a = b**, or **a > b**, where **<** and **>** denote the less than and greater than relations, respectively.
  - They have a well-ordering principle, meaning that any non-empty subset of natural numbers has a least element, that is, an element that is smaller than or equal to all other elements in the subset.



# Introduction for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- Set theory is a branch of mathematics that studies collections of objects, called sets, and the relationships between them.
- A set is a well-defined collection of distinct objects, which can be anything such as numbers, letters, symbols, or even other sets.
- The objects in a set are called elements or members of the set. We use curly braces { } to enclose the elements of a set, and commas to separate them. For example, {1, 2, 3} is a set with three elements: 1, 2, and 3.
- We can also use a rule or a description to define a set, as long as it is clear and unambiguous. For example, {x | x is an even integer} is a set of all even integers, and {x | x is a vowel} is a set of all vowels.
- We can use the symbol ∈ to denote that an object is an element of a set, and the symbol ∉ to denote that an object is not an element of a set. For example, 2 ∈ {1, 2, 3} and 4 ∉ {1, 2, 3}.
- We can use the symbol = to denote that two sets have exactly the same elements, and the symbol ≠ to denote that two sets have at least one different element. For example, {1, 2, 3} = {3, 2, 1} and {1, 2, 3} ≠ {1, 2, 4}.
- We can use the symbol ⊆ to denote that a set is a subset of another set, meaning that every element of the first set is also an element of the second set. For example, {1, 2} ⊆ {1, 2, 3} and {1, 2, 3} ⊆ {1, 2, 3}.
- We can use the symbol ⊂ to denote that a set is a proper subset of another set, meaning that it is a subset but not equal to the other set. For example, {1, 2} ⊂ {1, 2, 3} and {1, 2, 3} ⊂ {1, 2, 3, 4}.
- We can use the symbol ⊇ to denote that a set is a superset of another set, meaning that every element of the second set is also an element of the first set. For example, {1, 2, 3} ⊇ {1, 2} and {1, 2, 3} ⊇ {1, 2, 3}.
- We can use the symbol ⊃ to denote that a set is a proper superset of another set, meaning that it is a superset but not equal to the other set. For example, {1, 2, 3} ⊃ {1, 2} and {1, 2, 3, 4} ⊃ {1, 2, 3}.
- We can use the symbol ∅ to denote the empty set, which is a set that has no elements. For example, ∅ ⊆ {1, 2, 3} and ∅ ≠ {1, 2, 3}.
- We can use the symbol U to denote the universal set, which is a set that contains all the objects of interest in a given context. For example, if we are studying natural numbers, then U = {0, 1, 2, 3, ...}.
- We can use the symbol ∩ to denote the intersection of two sets, which is a set that contains all the elements that are common to both sets. For example, {1, 2, 3} ∩ {2, 3, 4} = {2, 3}.
- We can use the symbol ∪ to denote the union of two sets, which is a set that contains all the elements that are in either set or both sets. For example, {1, 2, 3} ∪ {2, 3, 4} = {1, 2, 3, 4}.
- We can use the symbol - to denote the difference of two sets, which is a set that contains all the elements that are in the first set but not in the second set. For example, {1, 2, 3} - {2, 3, 4} = {1}.
- We can use the symbol ' to denote the complement of



# Mathematical Induction

- Mathematical induction is a method for proving that a statement is true for every natural number, that is, that the infinitely many cases all hold.
- Mathematical induction is based on the principle of mathematical induction, which states that if a statement is true for some initial value and remains true after a certain step is applied, then it is true for all values that can be reached by applying the step repeatedly.
- Mathematical induction consists of two steps: the base case and the induction step.
  - The base case is to verify that the statement is true for some initial value, usually the smallest or simplest one.
  - The induction step is to assume that the statement is true for some arbitrary value, and then show that it is also true for the next value in the sequence.
- Mathematical induction can be used to prove various properties of natural numbers, such as divisibility, summation, factorial, and Fibonacci sequence.
- Mathematical induction can also be generalized to other types of sequences, such as arithmetic or geometric progressions, or to other domains, such as sets, graphs, or trees.
- Mathematical induction is an inference rule used in formal proofs, and is the foundation of most correctness proofs for computer programs.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of variants of induction for the unit 1 - set theory in the subject of discrete structures and theory of logic.

# Variants of Induction

Induction is a method of mathematical proof that is based on the principle of mathematical induction. The principle of mathematical induction states that if a statement P(n) is true for some base case n = b, and if P(k) implies P(k+1) for any k ≥ b, then P(n) is true for all n ≥ b.

There are different variants of induction that can be used to prove different kinds of statements. Some of the common variants are:

- **Strong induction**: This is a variant of induction where the inductive step assumes that P(n) is true for all n ≤ k, instead of just P(k), and then proves P(k+1). This can be useful when the statement P(n) depends on more than one previous case.

- **Complete induction**: This is another name for strong induction.

- **Structural induction**: This is a variant of induction where the statement P(x) is defined for some structure x, such as a set, a graph, a tree, etc. The base case is usually P(∅) or P(some simple structure), and the inductive step assumes that P(x) is true for all substructures of x, and then proves P(x). This can be useful when the statement P(x) depends on the structure of x.

- **Course-of-values induction**: This is a variant of induction where the statement P(n) is defined for some natural number n, and the base case is usually P(0) or P(1). The inductive step assumes that P(n) is true for all n < k, where k is some function of n, such as k = n/2, k = n-1, k = n^2, etc., and then proves P(k). This can be useful when the statement P(n) depends on some function of n.

- **Transfinite induction**: This is a variant of induction where the statement P(α) is defined for some ordinal number α, which is a generalization of natural numbers. The base case is usually P(0), and the inductive step assumes that P(α) is true for all α < β, and then proves P(β). This can be useful when the statement P(α) depends on the order type of α.

- **Well-founded induction**: This is a generalization of induction where the statement P(x) is defined for some element x of a well-founded set, which is a set that has no infinite descending chains. The base case is usually P(x) for some minimal element x, and the inductive step assumes that P(x) is true for all y < x, where < is some well-founded relation on the set, and then proves P(x). This can be useful when the statement P(x) depends on some relation on the set.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Discrete Structures & Theory of Logic. Here is the content for the topic of Induction with Nonzero Base cases:

# Induction with Nonzero Base cases

- Induction is a method of mathematical proof that is used to show that a statement is true for all natural numbers, or for a subset of natural numbers.
- The basic idea of induction is to prove the statement for a base case, and then assume that it is true for some arbitrary natural number k, and show that it implies that the statement is also true for k+1. This is called the inductive step.
- The base case is usually the smallest natural number for which the statement makes sense, such as 0 or 1. However, sometimes the statement is only true for natural numbers that are greater than or equal to some nonzero value, such as 2 or 3. In such cases, we need to modify the induction method to use a nonzero base case.
- For example, suppose we want to prove that for all natural numbers n ≥ 2, the inequality 2^n > n^2 holds. We cannot use 0 or 1 as the base case, because the inequality does not hold for them. Instead, we use 2 as the base case, and show that 2^2 > 2^2 is true. Then, we assume that the inequality is true for some k ≥ 2, and show that it implies that 2^(k+1) > (k+1)^2 is also true. This completes the inductive step, and by the principle of mathematical induction, the statement is true for all natural numbers n ≥ 2.
- The general form of induction with nonzero base cases is as follows:

  - Let P(n) be a statement involving a natural number n, and let b be a nonzero natural number such that P(b) is true.
  - Prove that P(b) is true. This is the base case.
  - Let k be an arbitrary natural number such that k ≥ b, and assume that P(k) is true. This is the induction hypothesis.
  - Prove that P(k+1) is true, using the induction hypothesis. This is the inductive step.
  - By the principle of mathematical induction, P(n) is true for all natural numbers n ≥ b.

- Induction with nonzero base cases is useful when the statement we want to prove is not defined or not true for some small natural numbers, but becomes true for larger natural numbers. It is also useful when the statement involves a function or a sequence that has a nonzero initial value or term.



# Proof Methods

A proof is a logical argument that establishes the validity of a mathematical statement. A proof consists of a sequence of statements that are either axioms, definitions, or logical consequences of previous statements. The goal of a proof is to show that the final statement, called the conclusion, follows from the initial statement, called the hypothesis.

There are different methods of proof that can be used depending on the type of statement and the level of rigor required. Some of the common proof methods are:

- Direct proof: A direct proof is a proof that starts from the hypothesis and uses logical rules to derive the conclusion. A direct proof is usually the simplest and most straightforward way to prove a statement.

- Indirect proof: An indirect proof is a proof that assumes the negation of the conclusion and shows that it leads to a contradiction with the hypothesis or a known fact. An indirect proof is also called a proof by contradiction or a reductio ad absurdum.

- Contrapositive proof: A contrapositive proof is a proof that uses the logical equivalence of the statement and its contrapositive. The contrapositive of a statement of the form "if p, then q" is "if not q, then not p". A contrapositive proof is a type of indirect proof that starts from the negation of the conclusion and derives the negation of the hypothesis.

- Proof by cases: A proof by cases is a proof that divides the hypothesis into several mutually exclusive and exhaustive cases and proves the conclusion for each case separately. A proof by cases is also called a proof by exhaustion or a proof by disjunction.

- Proof by induction: A proof by induction is a proof that establishes the validity of a statement for all natural numbers or a subset of natural numbers. A proof by induction consists of two steps: the base case and the induction step. The base case proves the statement for the smallest or initial value of the natural number. The induction step assumes the statement is true for some natural number k and proves it for the next natural number k+1. By the principle of mathematical induction, the statement is true for all natural numbers or the subset of natural numbers.

- Proof by contradiction: A proof by contradiction is a proof that assumes the negation of the statement and shows that it leads to a contradiction with a known fact or a logical rule. A proof by contradiction is also called an indirect proof or a reductio ad absurdum.

- Proof by contraposition: A proof by contraposition is a proof that uses the logical equivalence of the statement and its contrapositive. The contrapositive of a statement of the form "if p, then q" is "if not q, then not p". A proof by contraposition is a type of indirect proof that starts from the negation of the conclusion and derives the negation of the hypothesis.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of proof by counter-example for the notes of the unit 1 - set theory in the subject of discrete structures and theory of logic.

# Proof by counter-example

- A proof by counter-example is a method of disproving a statement by showing that there exists a specific case where the statement is false.
- A counter-example is a specific instance of the general case that contradicts the statement.
- To prove by counter-example, we need to find one counter-example that makes the statement false. We do not need to check all possible cases.
- A proof by counter-example can only be used to disprove a statement, not to prove it. If we cannot find a counter-example, it does not mean that the statement is true.
- A proof by counter-example is also known as a proof by contradiction or a reductio ad absurdum.

## Example

- Consider the statement: "For any two sets A and B, A ∩ B = A ∪ B".
- To disprove this statement, we need to find two sets A and B such that A ∩ B is not equal to A ∪ B.
- One possible counter-example is A = {1, 2, 3} and B = {4, 5, 6}.
- Then A ∩ B = {} and A ∪ B = {1, 2, 3, 4, 5, 6}.
- Clearly, A ∩ B ≠ A ∪ B, so the statement is false.
- Therefore, we have proved by counter-example that the statement is false.



# Proof by contradiction

- Proof by contradiction is a method of proving a statement by assuming that it is false and deriving a contradiction from that assumption.
- The contradiction can be either a logical inconsistency or a violation of a known fact or theorem.
- The basic form of proof by contradiction is:

  - Suppose that P is the statement we want to prove, and Q is some statement that leads to a contradiction.
  - Assume that P is false, or equivalently, that not P is true.
  - Using logical rules and known facts, show that not P implies Q.
  - Show that Q is false, or equivalently, that not Q is true.
  - Conclude that not P implies not Q, which is a contradiction, since Q and not Q cannot both be true.
  - Therefore, the assumption that P is false must be wrong, and P must be true.

- An example of proof by contradiction is:

  - Suppose we want to prove that √2 is irrational, that is, it cannot be written as a ratio of two integers.
  - Assume that √2 is rational, that is, √2 = a/b, where a and b are integers with no common factors.
  - Squaring both sides, we get 2 = a^2/b^2, or 2b^2 = a^2.
  - This implies that a^2 is even, since it is divisible by 2.
  - By a known fact, if a^2 is even, then a is even, that is, a = 2k for some integer k.
  - Substituting a = 2k into 2b^2 = a^2, we get 2b^2 = 4k^2, or b^2 = 2k^2.
  - This implies that b^2 is even, and by the same fact, b is even, that is, b = 2l for some integer l.
  - But then, a and b have a common factor of 2, which contradicts the assumption that they have no common factors.
  - Therefore, the assumption that √2 is rational must be false, and √2 must be irrational.



## Unit 2 - Algebraic Structures

- An algebraic structure is a set of elements with one or more operations defined on it that satisfy certain properties or axioms.
- Examples of algebraic structures are groups, rings, fields, vector spaces, matrices, etc.
- The most basic algebraic structure is a group, which consists of a set G and a binary operation * that satisfies the following properties:
  - Closure: For any a, b in G, a * b is also in G.
  - Associativity: For any a, b, c in G, (a * b) * c = a * (b * c).
  - Identity: There exists an element e in G such that for any a in G, a * e = e * a = a. This element is called the identity element of G.
  - Inverse: For any a in G, there exists an element b in G such that a * b = b * a = e. This element is called the inverse of a and is denoted by a^-1.
- A group is called abelian or commutative if it also satisfies the following property:
  - Commutativity: For any a, b in G, a * b = b * a.
- Examples of groups are the integers Z with addition as the operation, the nonzero rational numbers Q* with multiplication as the operation, the set of symmetries of a regular polygon with composition as the operation, etc.
- A ring is an algebraic structure that consists of a set R and two binary operations, usually denoted by + and *, that satisfy the following properties:
  - (R, +) is an abelian group.
  - * is associative and has an identity element, usually denoted by 1.
  - * is distributive over +, that is, for any a, b, c in R, a * (b + c) = (a * b) + (a * c) and (a + b) * c = (a * c) + (b * c).
- A ring is called commutative if * is also commutative.
- Examples of rings are the integers Z, the polynomials Z[x] with coefficients in Z, the matrices M_n(Z) with entries in Z and size n x n, etc.
- A field is a commutative ring that satisfies the following additional property:
  - Every nonzero element of R has a multiplicative inverse, that is, for any a in R, a != 0, there exists b in R such that a * b = b * a = 1.
- Examples of fields are the rational numbers Q, the real numbers R, the complex numbers C, the finite fields Z_p with p a prime number, etc.
- A vector space is an algebraic structure that consists of a set V and two operations, usually denoted by + and *, that satisfy the following properties:
  - (V, +) is an abelian group.
  - * is a scalar multiplication, that is, it takes an element of a field F, called a scalar, and an element of V, called a vector, and produces another vector in V.
  - * is distributive over both + operations, that is, for any a, b in F and u, v in V, a * (u + v) = (a * u) + (a * v) and (a + b) * u = (a * u) + (b * u).
  - * is compatible with the field multiplication, that is, for any a, b in F and u in V, (a * b) * u = a * (b * u).
  - * has an identity element, usually denoted by 1, such that for any u in V, 1 * u = u.
- Examples of vector spaces are the set of n-tuples of elements of a field F, denoted by F^n, the set of polynomials of degree less than or equal to n with coefficients in a field F, denoted by F[x]_n, the set of continuous functions from a closed interval [a, b] to a field F, denoted by C[a, b], etc.



# Definition for the notes of the Unit 2 - Algebraic Structures in the subject of Discrete Structures & Theory of Logic

- Discrete mathematics is the branch of mathematics that deals with finite or discrete objects, such as integers, graphs, logic, and codes.
- An algebraic structure is a set with one or more operations defined on it that satisfy certain properties or axioms.
- Examples of algebraic structures are groups, rings, fields, vector spaces, lattices, and Boolean algebras.
- An algebraic system is a pair (A, F) where A is a nonempty set and F is a set of operations on A .
- An operation on a set A is a function that maps some elements of A to another element of A.
- An operation can be unary (one input), binary (two inputs), ternary (three inputs), or n-ary (n inputs) depending on the number of inputs it takes.
- A binary operation on a set A is usually denoted by a symbol, such as +, *, or ∨, and written as a * b, where a and b are elements of A.
- A unary operation on a set A is usually denoted by a symbol, such as -, ~, or ¬, and written as -a, ~a, or ¬a, where a is an element of A.
- Some common properties or axioms of operations are commutativity, associativity, identity, inverse, distributivity, and closure.
- An operation * on a set A is commutative if a * b = b * a for all a, b in A.
- An operation * on a set A is associative if (a * b) * c = a * (b * c) for all a, b, c in A.
- An operation * on a set A has an identity element e if a * e = e * a = a for all a in A.
- An operation * on a set A has an inverse element for a if there exists b in A such that a * b = b * a = e, where e is the identity element.
- An operation * on a set A is distributive over another operation + on A if a * (b + c) = (a * b) + (a * c) and (b + c) * a = (b * a) + (c * a) for all a, b, c in A.
- An operation * on a set A is closed if a * b is in A for all a, b in A.
- A set A with a binary operation * is called a group if * is associative, has an identity element, and has an inverse element for every element in A.
- A group is called abelian or commutative if * is also commutative.
- A set A with two binary operations + and * is called a ring if + and * are associative, + is commutative, * is distributive over +, and + has an identity element and an inverse element for every element in A.
- A ring is called commutative if * is also commutative.
- A ring is called a field if * also has an identity element and an inverse element for every nonzero element in A.
- A set A with a binary operation + and a scalar multiplication operation * is called a vector space if + is associative, commutative, has an identity element, and has an inverse element for every element in A, and * satisfies certain properties such as distributivity, associativity, and identity.
- A set A with a partial order relation ≤ is called a lattice if for any two elements a and b in A, there exist a least upper bound (lub) and a greatest lower bound (glb) of a and b in A.
- A lattice is called a Boolean algebra if it also has two binary operations + and * that are commutative, associative, distributive, and satisfy certain identities such as a + a = a, a * a = a, a + 1 = 1, a * 0 = 0, and a + ¬a = 1, where 1 and 0 are the maximum and minimum elements of the



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of groups for the unit 2 - algebraic structures in the subject of discrete structures and theory of logic.

# Groups

A group is a set G together with a binary operation * that satisfies the following four properties:

- **Closure**: For all a, b in G, a * b is also in G.
- **Associativity**: For all a, b, c in G, (a * b) * c = a * (b * c).
- **Identity**: There exists an element e in G such that for all a in G, e * a = a * e = a. This element is called the identity element of G.
- **Inverse**: For each a in G, there exists an element b in G such that a * b = b * a = e, where e is the identity element of G. This element b is called the inverse of a in G.

Some examples of groups are:

- The set of integers Z with the operation of addition (+).
- The set of nonzero rational numbers Q* with the operation of multiplication (×).
- The set of invertible n × n matrices with real entries, denoted by GL(n, R), with the operation of matrix multiplication.
- The set of symmetries of a regular polygon, denoted by Dn, with the operation of composition.

Some properties of groups are:

- The identity element of a group is unique.
- The inverse of each element of a group is unique.
- For any a, b, c in a group G, if a * b = a * c, then b = c. Similarly, if b * a = c * a, then b = c. This is called the cancellation law.
- For any a, b in a group G, (a * b)^-1 = b^-1 * a^-1, where x^-1 denotes the inverse of x in G.
- A group G is called **abelian** or **commutative** if for all a, b in G, a * b = b * a. All the examples of groups given above are abelian, except for GL(n, R) and Dn (for n > 2).



# Subgroups and order

- A **subgroup** is a subset of a group that satisfies the four group requirements: closure, associativity, identity, and inverse .
- A subgroup must contain the identity element of the group.
- A subgroup of a group is denoted by or sometimes .
- A subgroup that does not include the entire group itself is called a **proper subgroup**, denoted by or .
- The **order** of a subgroup is the number of elements in the subgroup.
- The order of any subgroup of a group of order must be a divisor of . This is known as **Lagrange's theorem**.
- A subgroup of a group is called a **normal subgroup** if for all .
- A subgroup is normal if and only if it is the kernel of a homomorphism.
- A subgroup is normal if and only if it is invariant under conjugation by any element of the group.
- A subgroup is normal if and only if its left and right cosets are equal.
- A subgroup is normal if and only if it is a union of conjugacy classes.
- A subgroup is called a **cyclic subgroup** if it is generated by a single element .
- A cyclic subgroup is normal in any group that contains it.
- A cyclic subgroup of order is isomorphic to the additive group of integers modulo .
- A cyclic group has exactly one subgroup of each order dividing the order of the group.
- A cyclic group is abelian.
- A group is cyclic if and only if it has exactly one generator.
- A group is cyclic if and only if it is isomorphic to a cyclic subgroup of the group of complex roots of unity.



# Cyclic Groups

- A group (G, ∘) is called a cyclic group if there exists an element a∈G such that G is generated by a. In other words, every element of G can be written as a power of a (or a multiple of a if the operation is additive)   .
- The element a is called a generator or a primitive element of the cyclic group G. A cyclic group may have more than one generator. For example, the group (Z, +) is cyclic and both 1 and -1 are generators   .
- The order of a cyclic group G is equal to the order of the generator a, denoted by |a|. The order of a is the smallest positive integer n such that a^n = e (or a + a + ... + a (n times) = 0 if the operation is additive), where e is the identity element of G  .
- A cyclic group can be finite or infinite. A finite cyclic group has a finite order, while an infinite cyclic group has an infinite order. For example, the group (Z, +) is an infinite cyclic group, while the group (Z_n, +) is a finite cyclic group of order n   .
- A cyclic group is always abelian, since a^m ∘ a^n = a^(m+n) = a^(n+m) = a^n ∘ a^m for any m, n ∈ Z (or similarly for additive notation)   .
- A cyclic group has exactly one subgroup of each order that divides the order of the group. For example, the group (Z_12, +) has subgroups of order 1, 2, 3, 4, 6, and 12, and each subgroup is cyclic   .
- A subgroup of a cyclic group is also cyclic. For example, the subgroup {0, 3, 6, 9} of (Z_12, +) is cyclic and generated by 3   .
- A cyclic group of prime order has no proper subgroups, since the only divisors of a prime number are 1 and itself. For example, the group (Z_5, +) has no proper subgroups   .
- Two cyclic groups of the same order are isomorphic. For example, the groups (Z_6, +) and (Z_7^*, ×) are isomorphic, where Z_7^* is the set of positive integers less than 7 that are relatively prime to 7   .
- A direct product of cyclic groups is cyclic if and only if their orders are relatively prime. For example, the direct product (Z_2, +) × (Z_3, +) is cyclic, but the direct product (Z_2, +) × (Z_4, +) is not   .

: https://www.mathstoon.com/cyclic-group/
: http://dictionary.sensagent.com/Cyclic%20group/en-en/
: https://math.libretexts.org/Courses/SUNY_Schenectady_County_Community_College/Discrete_Structures/14%3A_Group_Theory_and_Applications/14.01%3A_Cyclic_Groups



# Cosets

- A **coset** of a subgroup H of a group G is a subset of G obtained by multiplying H with elements of G from left or right.
- For example, if H = {e, a, a^2} is a subgroup of G = {e, a, a^2, b, ab, a^2b}, then Ha = {a, a^2, e} and bH = {b, ba, ba^2} are cosets of H in G.
- Depending on the multiplication from left or right, we can classify cosets as **left cosets** or **right cosets**.
- For example, Ha is a left coset of H in G, and bH is a right coset of H in G.
- The notation for left and right cosets is usually Hg and gH, respectively, where g is any element of G.
- Cosets are mainly used to decompose a group G into equal-sized disjoint subsets of G. They play an important role in many topics in group theory, such as normal subgroups, Lagrange's theorem, quotient groups, etc.
- Some properties of cosets are:
  - The number of left cosets of H in G is equal to the number of right cosets of H in G, and is called the **index** of H in G, denoted by [G : H].
  - The size of any left coset of H in G is equal to the size of H, and is called the **order** of H, denoted by |H|.
  - The size of any right coset of H in G is also equal to the size of H.
  - Two left cosets Hg and Hg' are either equal or disjoint, and similarly for right cosets.
  - The union of all left cosets of H in G is equal to G, and similarly for right cosets.
  - A subgroup H of G is called a **normal subgroup** if every left coset of H in G is also a right coset of H in G, and vice versa. In other words, Hg = gH for all g in G. Normal subgroups are important because they allow us to define quotient groups, which are groups formed by the cosets of a normal subgroup.
  - Lagrange's theorem states that for any finite group G and any subgroup H of G, the order of G is equal to the product of the order of H and the index of H in G, i.e., |G| = |H| [G : H]. This implies that the order of any subgroup and any coset of G divides the order of G.



# Lagrange's Theorem

- Lagrange's theorem is one of the central theorems of abstract algebra .
- It states that in group theory, for any finite group say G, the order of subgroup H of group G divides the order of G .
- The order of the group represents the number of elements .
- Mathematically, if G is a finite group and H is a subgroup of G, then |H| divides |G|, where |H| and |G| denote the orders of H and G respectively  .
- The quotient |G|/|H| is called the index of H in G, and it is equal to the number of distinct left or right cosets of H in G  .
- A coset of H in G is a subset of G that is obtained by multiplying all the elements of H by a fixed element of G .
- The left cosets of H in G are of the form gH = {gh : h ∈ H} for some g ∈ G .
- The right cosets of H in G are of the form Hg = {hg : h ∈ H} for some g ∈ G .
- Lagrange's theorem implies that every coset of H in G has the same size as H, and that the cosets of H in G partition G into disjoint subsets .
- Lagrange's theorem can be used to prove many important results in group theory, such as the Euler's theorem, Fermat's little theorem, Wilson's theorem, and Cauchy's theorem .



# Normal Subgroups

- A normal subgroup H of a group G is a subgroup of G that is invariant under conjugation by members of the group. In other words, for every element g in G and every element h in H, we have g h g^-1 in H. The usual notation for this relation is H ≤ N G.
- Equivalently, a normal subgroup H of a group G is a subgroup of G such that every left coset and right coset corresponding to an element g are the same, that is, g H = H g.
- Normal subgroups are important because they allow us to define quotient groups, which are groups obtained by dividing a group by a normal subgroup. Quotient groups are useful for studying the structure and properties of groups.
- Some properties of normal subgroups are:

  - The trivial subgroup {e} and the whole group G are always normal subgroups of G.
  - The intersection of any collection of normal subgroups of G is a normal subgroup of G.
  - The product of any collection of normal subgroups of G is a normal subgroup of G, if the collection is finite or if G is abelian.
  - If H and K are normal subgroups of G such that H ∩ K = {e}, then H K is isomorphic to H × K.
  - If H is a normal subgroup of G and K is a subgroup of G, then H K is a subgroup of G and K / (H ∩ K) is isomorphic to H K / H.
  - If H is a normal subgroup of G and K is a normal subgroup of H, then K is a normal subgroup of G if and only if H K = K H.
  - If H is a normal subgroup of G and g is an element of G, then g H g^-1 is a normal subgroup of G and isomorphic to H.
  - If H is a normal subgroup of G and N is a normal subgroup of H, then N is a normal subgroup of G if and only if g N g^-1 = N for all g in G.
  - If H is a normal subgroup of G and N is a normal subgroup of G, then H N is a normal subgroup of G and H ∩ N is a normal subgroup of H and N. Moreover, H / (H ∩ N) is isomorphic to H N / N.
  - If H is a normal subgroup of G and N is a normal subgroup of G, then H / N is a normal subgroup of G / N if and only if H contains N.
  - If H is a normal subgroup of G and N is a normal subgroup of G, then H / N is a normal subgroup of G / N if and only if H N = N H.
  - If H is a subgroup of G and [G : H] = 2, then H is a normal subgroup of G.
  - If H is a subgroup of G and G is abelian, then H is a normal subgroup of G.
  - If H is a subgroup of G and G is cyclic, then H is a normal subgroup of G.
  - If H is a subgroup of G and H is abelian, then H is not necessarily a normal subgroup of G.
  - A group G is simple if it has no normal subgroups other than {e} and G.



# Permutation and Symmetric Groups

## Permutation

- A permutation is a bijective function from a set to itself, that is, a function that maps each element of the set to a unique element of the set.
- A permutation can also be seen as a rearrangement of the elements of a set in a certain order.
- A permutation can be represented in different ways, such as a two-row notation, a cycle notation, or a matrix notation.
- For example, let S = {1, 2, 3, 4}. A permutation of S is a function f: S -> S such that f is bijective. One possible permutation is f(1) = 2, f(2) = 4, f(3) = 1, f(4) = 3. This can be written as:

  - Two-row notation: (1 2 3 4) (2 4 1 3)
  - Cycle notation: (1 2 4 3)
  - Matrix notation: | 1 2 3 4 | | 2 4 1 3 |

## Symmetric Group

- A symmetric group on a set X is the set of all permutations on X, denoted by Sym(X) or S_n, where n is the cardinality of X .
- A symmetric group is a group under the operation of function composition, that is, applying one permutation after another .
- For example, let S = {1, 2, 3, 4} and Sym(S) = S_4. Then S_4 has 4! = 24 elements, each of which is a permutation of S. The group operation is denoted by a dot, such as f.g, which means applying g first and then f. The identity element of S_4 is the permutation that maps each element to itself, denoted by e or (1)(2)(3)(4). The inverse of a permutation f is the permutation that undoes the effect of f, denoted by f^-1^.
- A symmetric group has some important properties, such as:

  - It is non-abelian, meaning that the order of applying permutations matters, that is, f.g is not necessarily equal to g.f.
  - It is finite, meaning that it has a finite number of elements, equal to n! for S_n.
  - It is the largest permutation group on n elements, meaning that any subgroup of S_n is also a permutation group.
  - It is isomorphic to the group of invertible n x n matrices under matrix multiplication, denoted by GL(n, R).

## Permutation Group

- A permutation group on a set X is a subgroup of the symmetric group on X, that is, a subset of Sym(X) that is also a group under function composition .
- A permutation group can also be defined as a group that acts on a set X, meaning that there is a homomorphism from the group to Sym(X) that preserves the group structure .
- For example, let S = {1, 2, 3, 4} and G = {(1), (1 2)(3 4), (1 3)(2 4), (1 4)(2 3)}. Then G is a permutation group on S, as it is a subgroup of S_4. It is also a group that acts on S, as there is a homomorphism from G to S_4 that maps each element of G to itself.
- A permutation group has some important properties, such as:

  - It is a subgroup of a symmetric group, meaning that it inherits some properties of the symmetric group, such as being finite and non-abelian.
  - It is isomorphic to a group of symmetries of some object, meaning that there is a one-to-one correspondence between the elements of the group and the ways of transforming the object without changing its shape or size .
  - It is determined by its generators, meaning that any element of the group can be obtained by applying a finite sequence of some fixed elements of the group, called generators .



# Group Homomorphisms

- A group homomorphism is a function that maps one group to another group and preserves the group operation. That is, if $G$ and $H$ are groups with operations $\ast$ and $\cdot$, respectively, then a function $h:G\to H$ is a group homomorphism if
$$h(x\ast y) = h(x)\cdot h(y)$$
for all $x,y\in G$  .
- A group homomorphism has the following properties:
  - It maps the identity element of $G$ to the identity element of $H$. That is, $h(e_G) = e_H$ .
  - It maps the inverse of any element in $G$ to the inverse of its image in $H$. That is, $h(x^{-1}) = h(x)^{-1}$ for all $x\in G$ .
  - It preserves the order of any element in $G$. That is, if $x\in G$ has order $n$, then $h(x)\in H$ has order $n$ or $1$.
- A group homomorphism can be classified into different types based on its injectivity and surjectivity:
  - An injective homomorphism is one that maps distinct elements of $G$ to distinct elements of $H$. That is, $h(x) = h(y)$ implies $x=y$ for all $x,y\in G$ .
  - A surjective homomorphism is one that maps $G$ onto $H$. That is, for any $h\in H$, there exists $x\in G$ such that $h(x) = h$ .
  - A bijective homomorphism is one that is both injective and surjective. It is also called an isomorphism of groups. It implies that $G$ and $H$ are essentially the same group, just with different names for the elements and the operation  .
- A group homomorphism can be used to study the properties and structure of groups. Some important concepts related to group homomorphisms are:
  - The kernel of a homomorphism is the set of all elements in $G$ that are mapped to the identity element of $H$. That is, $\ker h = \{x\in G \mid h(x) = e_H\}$   .
  - The image of a homomorphism is the set of all elements in $H$ that are mapped from some element in $G$. That is, $\operatorname{im} h = \{h(x) \mid x\in G\}$   .
  - The kernel and the image of a homomorphism are both subgroups of $G$ and $H$, respectively   .
  - The first isomorphism theorem states that if $h:G\to H$ is a homomorphism, then $G/\ker h \cong \operatorname{im} h$, where $G/\ker h$ is the quotient group of $G$ by the kernel of $h$   .
  - The second isomorphism theorem states that if $h:G\to H$ is a homomorphism and $K$ is a subgroup of $G$ that contains $\ker h$, then $K/\ker h \cong h(K)$, where $h(K)$ is the image of $K$ under $h$   .
  - The third isomorphism theorem states that if $h:G\to H$ is a homomorphism and $K$ and $L$ are subgroups of $G$ that contain $\ker h$, then $(K/L)/h(L) \cong h(K)/h(L)$, where $K/L$ and $h(K)/h(L)$ are the quotient groups of $



# Definition and elementary properties of Rings and Fields

## Rings

- A ring is a set R together with two binary operations, usually called addition (+) and multiplication (·), that satisfy the following properties :

  - (R,+) is an abelian group, i.e., addition is associative, commutative, has an identity element (denoted by 0), and every element has an additive inverse.
  - Multiplication is associative and has an identity element (denoted by 1).
  - Multiplication distributes over addition, i.e., for any a, b, c in R, we have a · (b + c) = (a · b) + (a · c) and (a + b) · c = (a · c) + (b · c).

- Examples of rings are the set of integers (Z), the set of polynomials (Z[x]), and the set of matrices (Mn(Z)) with integer entries .
- A ring is called commutative if multiplication is also commutative, i.e., for any a, b in R, we have a · b = b · a . All the examples above are commutative rings.
- A ring is called a field if every nonzero element has a multiplicative inverse, i.e., for any a in R, a ≠ 0, there exists b in R such that a · b = b · a = 1 . A field is also a commutative ring.

## Fields

- A field is a set F together with two binary operations, usually called addition (+) and multiplication (·), that satisfy the following properties :

  - (F,+) is an abelian group, i.e., addition is associative, commutative, has an identity element (denoted by 0), and every element has an additive inverse.
  - (F \ {0}, ·) is an abelian group, i.e., multiplication is associative, commutative, has an identity element (denoted by 1), and every nonzero element has a multiplicative inverse.
  - Multiplication distributes over addition, i.e., for any a, b, c in F, we have a · (b + c) = (a · b) + (a · c) and (a + b) · c = (a · c) + (b · c).

- Examples of fields are the set of rational numbers (Q), the set of real numbers (R), and the set of complex numbers (C) .
- A field is a special case of a ring, where every nonzero element is a unit, i.e., has a multiplicative inverse .
- A field is also a vector space over itself, i.e., it has a scalar multiplication that is compatible with the field operations .



# Unit 3 - Lattices

- A lattice is a partially ordered set (L, ≤) in which every pair of elements has a least upper bound and a greatest lower bound .
- A least upper bound of a pair {a, b} is an element c such that a ≤ c and b ≤ c, and there is no other element d such that a ≤ d and b ≤ d and d ≤ c. It is denoted by a ∨ b or lub(a, b).
- A greatest lower bound of a pair {a, b} is an element c such that c ≤ a and c ≤ b, and there is no other element d such that d ≤ a and d ≤ b and c ≤ d. It is denoted by a ∧ b or glb(a, b).
- A lattice is also an algebraic structure with two binary, commutative and associative operations ∨ and ∧ that satisfy the absorption laws: a ∨ (a ∧ b) = a and a ∧ (a ∨ b) = a for all elements a and b.
- A lattice can be represented by a Hasse diagram, which is a graphical representation of the partial order relation. The elements are drawn as points, and a line segment is drawn between two elements a and b if a ≤ b and there is no other element c such that a ≤ c and c ≤ b. The lower elements are drawn below the higher elements.
- A lattice is called bounded if it has a least element 0 and a greatest element 1, such that 0 ≤ a and a ≤ 1 for all elements a. The least and greatest elements are also called the bottom and the top of the lattice, respectively.
- A lattice is called distributive if it satisfies the distributive laws: a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) and a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) for all elements a, b and c. A lattice is distributive if and only if it does not contain a sublattice isomorphic to M3 or N5, where M3 and N5 are the following lattices:

M3 and N5

- A lattice is called complemented if every element a has a complement a', such that a ∨ a' = 1 and a ∧ a' = 0. A complemented lattice is called uniquely complemented if every element has a unique complement. A lattice is uniquely complemented if and only if it is distributive and bounded.
- A lattice is called modular if it satisfies the modular law: a ≤ c implies a ∨ (b ∧ c) = (a ∨ b) ∧ c for all elements a, b and c. A modular lattice is also called a Dedekind lattice. A modular lattice is distributive if and only if it does not contain a sublattice isomorphic to M3.
- A lattice is called complete if every subset of L has a least upper bound and a greatest lower bound. A complete lattice is bounded, and every bounded lattice is complete if it is finite. A complete lattice is distributive if and only if it satisfies the infinite distributive laws: ∨ S ∧ T = ∧ {∨ {s, t} | s ∈ S, t ∈ T} and ∧ S ∨ T = ∨ {∧ {s, t} | s ∈ S, t ∈ T} for all subsets S and T of L.
- A lattice is called a Boolean algebra if it is a distributive, complemented and bounded lattice. A Boolean algebra is also a complete lattice, and every complete lattice is a Boolean algebra if it is finite. A Boolean algebra has the following properties:
  - a ∨ 0 = a and a ∧ 1 = a for all elements a (identity laws).
  - a ∨ a = a and a ∧ a = a for all elements a (idempotent laws).
  - a ∨ b = b ∨ a and a ∧ b = b ∧ a for all elements a and b (commutative laws).
  - a ∨ (b ∨ c) = (a ∨ b) ∨ c and a ∧ (b ∧ c) = (



# Definition for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a **greatest lower bound** and a **least upper bound** .
- A greatest lower bound of two elements a and b in a poset is an element c such that c ≤ a and c ≤ b, and there is no other element d that is lower than c and also satisfies d ≤ a and d ≤ b. It is denoted by a ∧ b or glb(a, b).
- A least upper bound of two elements a and b in a poset is an element c such that a ≤ c and b ≤ c, and there is no other element d that is higher than c and also satisfies a ≤ d and b ≤ d. It is denoted by a ∨ b or lub(a, b).
- The greatest lower bound and the least upper bound of two elements in a lattice are also called the **meet** and the **join** of the elements, respectively.
- The meet and the join of two elements in a lattice are **unique**, if they exist.
- A lattice can be represented by a **Hasse diagram**, which is a graphical representation of the partial order relation. In a Hasse diagram, the elements of the lattice are represented by points, and the partial order relation is represented by lines connecting the points. The lines are drawn such that if a ≤ b, then a is below b, and there is no other element c between a and b such that a ≤ c ≤ b.
- A lattice can also be defined as an **algebraic structure** with two binary operations, called meet and join, that satisfy certain properties. A lattice is denoted by [L; ∧, ∨], where L is the set of elements and ∧ and ∨ are the meet and join operations.
- The properties of the meet and join operations in a lattice are:

  - **Commutativity**: a ∧ b = b ∧ a and a ∨ b = b ∨ a for all a, b ∈ L.
  - **Associativity**: a ∧ (b ∧ c) = (a ∧ b) ∧ c and a ∨ (b ∨ c) = (a ∨ b) ∨ c for all a, b, c ∈ L.
  - **Idempotency**: a ∧ a = a and a ∨ a = a for all a ∈ L.
  - **Absorption**: a ∧ (a ∨ b) = a and a ∨ (a ∧ b) = a for all a, b ∈ L.
  - **Distributivity**: a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c) and a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c) for all a, b, c ∈ L.

- A lattice is called a **distributive lattice** if it satisfies the distributivity property, and a **non-distributive lattice** otherwise.
- A lattice is called a **bounded lattice** if it has a **greatest element** and a **least element**. A greatest element of a lattice is an element that is greater than or equal to every other element in the lattice. A least element of a lattice is an element that is less than or equal to every other element in the lattice. A greatest element is denoted by 1 or T, and a least element is denoted by 0 or F.
- A lattice is called a **complete lattice** if every subset of the lattice has a greatest lower bound and a least upper bound. A complete lattice is always a bounded lattice, since the greatest lower bound of the empty set is the greatest element, and the least upper bound of the empty set is the least element.
- A lattice is called a **modular lattice** if it satisfies the following property: a ≤ c implies a ∨ (b ∧ c) = (a ∨ b) ∧ c for all a, b, c ∈ L. A modular lattice is always a distributive lattice, but the converse is not true.
- A lattice is called a **complemented lattice** if every element in the lattice has a **complement**. A complement of an element a



# Properties of lattices – Bounded

- A lattice is a poset (L, ⪯) for which every pair of elements has a greatest lower bound and least upper bound.
- A bounded lattice is a lattice that additionally has a greatest element (also called maximum, or top element, and denoted by 1, or by ⊤) and a least element (also called minimum, or bottom, and denoted by 0, or by ⊥), which satisfy:
  - for all x in L, x ∧ 1 = x and x ∨ 1 = 1
  - for all x in L, x ∧ 0 = 0 and x ∨ 0 = x
- The element 1 is called the upper bound, or top of L and the element 0 is called the lower bound or bottom of L.
- A bounded lattice is also called a complete lattice, since it has a least upper bound and a greatest lower bound for any subset of L.
- A complemented lattice is a bounded lattice in which every element is complemented. Namely, the complement of 1 is 0, and the complement of 0 is 1.
- A distributive lattice is a lattice in which for all elements in the poset the distributive property holds:
  - x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z)
  - x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)
- Every finite lattice L = {a 1,a 2,a 3....a n} is bounded. This can be proved by taking the least upper bound and the greatest lower bound of all the elements in L.



# Complemented for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **bounded lattice** is a lattice that has a minimum element (denoted by 0) and a maximum element (denoted by 1).
- A **complemented lattice** is a bounded lattice in which every element has a **complement**, that is, an element such that their lub is 1 and their glb is 0.
- A **distributive lattice** is a lattice that satisfies the **distributive laws**, that is, for any elements x, y, and z in the lattice, x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z) and x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z), where ∧ and ∨ denote the glb and lub operations, respectively.
- A **Boolean algebra** is a distributive complemented lattice. It is also called a **Boolean lattice** or a **two-element algebra**.
- A **sublattice** of a lattice L is a subset of L that is also a lattice under the same glb and lub operations.
- A **homomorphism** between two lattices L and M is a function f : L → M that preserves the glb and lub operations, that is, for any elements x and y in L, f(x ∧ y) = f(x) ∧ f(y) and f(x ∨ y) = f(x) ∨ f(y).
- An **isomorphism** between two lattices L and M is a bijective homomorphism f : L → M. Two lattices are **isomorphic** if there exists an isomorphism between them.
- A **lattice diagram** is a graphical representation of a lattice, in which the elements are represented by points and the partial order relation is represented by lines connecting the points. The lub and glb of two elements are shown by the lowest and highest points that are reachable from both elements, respectively.
- A **Hasse diagram** is a simplified lattice diagram, in which only the **covering relations** are shown, that is, the lines connecting two elements x and y such that x < y and there is no element z in the lattice such that x < z < y. The lub and glb of two elements are shown by the lowest and highest points that are directly connected to both elements, respectively.



# Modular and Complete Lattice

- A **lattice** is a partially ordered set (poset) in which every two elements have a unique least upper bound (called their **join** or **supremum**) and a unique greatest lower bound (called their **meet** or **infimum**).
- A lattice is **complete** if every subset of the lattice has a join and a meet, not just every pair of elements. Equivalently, a lattice is complete if it has a **top** element (the join of the empty set) and a **bottom** element (the meet of the empty set).
- A lattice is **modular** if it satisfies the following self-dual condition, called the **modular law**:

  - For any elements a, b, and x in the lattice, if a ≤ b, then a ∨ (x ∧ b) = (a ∨ x) ∧ b.

- The modular law states that if a is below b, then the join of a and the meet of x and b is equal to the meet of the join of a and x and b. In other words, the order of operations of join and meet does not matter when a is below b.
- A modular lattice is a special case of a **distributive lattice**, which satisfies the stronger **distributive laws**:

  - For any elements a, b, and x in the lattice, a ∨ (x ∧ b) = (a ∨ x) ∧ (a ∨ b) and a ∧ (x ∨ b) = (a ∧ x) ∨ (a ∧ b).

- The distributive laws state that the join and meet operations distribute over each other, regardless of the order of the elements. Every distributive lattice is modular, but not every modular lattice is distributive.
- An example of a modular lattice that is not distributive is the **pentagon lattice**, which has five elements: a top element, a bottom element, and three elements in between that form a cycle. The pentagon lattice violates the distributive laws, but satisfies the modular law.
- An example of a complete lattice that is not modular is the **power set lattice**, which has the power set of a given set as its elements, ordered by inclusion. The power set lattice is complete, since every subset of the power set has a join (the union of the subsets) and a meet (the intersection of the subsets). However, the power set lattice is not modular, unless the given set has at most two elements.



# Boolean Algebra

- Boolean algebra is a branch of mathematics that deals with operations on logical values with binary variables  .
- The Boolean variables are represented as binary numbers to represent truths: 1 = true and 0 = false .
- Elementary algebra deals with numerical operations whereas Boolean algebra deals with logical operations.
- Boolean algebra traces its origins to an 1854 book by mathematician George Boole.
- The basic operations of Boolean algebra are the logical operations AND, OR and NOT .
- AND is denoted by ∧, OR by ∨ and NOT by ¬.
- AND returns 1 if both operands are 1, otherwise 0.
- OR returns 1 if either operand is 1, otherwise 0.
- NOT returns 1 if the operand is 0, otherwise 0.
- For example, 1 ∧ 0 = 0, 1 ∨ 0 = 1, ¬1 = 0.
- Boolean algebra follows certain laws or rules that govern the operations and simplify the expressions.
- Some of the common laws are:

  - Commutative law: a ∧ b = b ∧ a, a ∨ b = b ∨ a.
  - Associative law: (a ∧ b) ∧ c = a ∧ (b ∧ c), (a ∨ b) ∨ c = a ∨ (b ∨ c).
  - Distributive law: a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c), a ∨ (b ∧ c) = (a ∨ b) ∧ (a ∨ c).
  - Identity law: a ∧ 1 = a, a ∨ 0 = a.
  - Complement law: a ∧ ¬a = 0, a ∨ ¬a = 1.
  - Idempotent law: a ∧ a = a, a ∨ a = a.
  - De Morgan's law: ¬(a ∧ b) = ¬a ∨ ¬b, ¬(a ∨ b) = ¬a ∧ ¬b.

- Boolean algebra can be used to model and manipulate logical expressions, circuits, sets, functions, relations and more .
- A Boolean algebra is any set with binary operations ∧ and ∨ and a unary operation ¬ thereon satisfying the Boolean laws.
- For the purposes of this definition it is irrelevant how the operations came to satisfy the laws, whether by fiat or proof.
- A Boolean algebra can also be defined as a complemented distributive lattice.
- A lattice is a partially ordered set in which every pair of elements has a unique least upper bound and a unique greatest lower bound.
- A distributive lattice is a lattice that satisfies the distributive law.
- A complemented lattice is a lattice in which every element has a unique complement, that is, an element such that their meet is the bottom element and their join is the top element of the lattice.
- A Boolean algebra is a special case of a Boolean ring, which is a ring that satisfies the identity x + x = 0 for all x.
- A Boolean ring is also a special case of a Boolean algebra over a field, which is a vector space over a field of characteristic 2 with a bilinear product that satisfies the identity x * x = x for all x.



# Introduction for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- A **lattice** is a partially ordered set (poset) in which every pair of elements has a unique least upper bound (lub) and a unique greatest lower bound (glb).
- A **least upper bound** of a pair of elements x and y is an element z such that x ≤ z and y ≤ z, and there is no other element w that is smaller than z and satisfies x ≤ w and y ≤ w.
- A **greatest lower bound** of a pair of elements x and y is an element z such that z ≤ x and z ≤ y, and there is no other element w that is larger than z and satisfies w ≤ x and w ≤ y.
- The least upper bound of x and y is also called the **join** of x and y, denoted by x ∨ y.
- The greatest lower bound of x and y is also called the **meet** of x and y, denoted by x ∧ y.
- A lattice can be represented by a **Hasse diagram**, which is a graphical representation of the partial order relation. In a Hasse diagram, each element is represented by a node, and there is an edge from x to y if and only if x < y and there is no element z such that x < z < y. The edges are drawn so that the higher nodes are above the lower nodes.
- A lattice is said to be **bounded** if it has a least element and a greatest element. The least element is denoted by 0 and the greatest element by 1. A bounded lattice is also called a **complete lattice**.
- A lattice is said to be **distributive** if it satisfies the following two distributive laws for all elements x, y, and z:

  - x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z)
  - x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z)

- A lattice is said to be **complemented** if every element has a **complement**, which is an element y such that x ∨ y = 1 and x ∧ y = 0. A complemented lattice is also called a **Boolean algebra**.



# Axioms and Theorems of Boolean Algebra

Boolean algebra is a branch of mathematics that deals with the manipulation of logical expressions and variables. It is used to design and analyze digital circuits and systems. Boolean algebra is based on a set of axioms and theorems that define the properties and rules of logic operations.

## Axioms of Boolean Algebra

An axiom is a statement that is accepted as true without proof. It is also called a postulate. Axioms are used to define the basic logic operations of AND, OR and NOT. The following are the axioms of Boolean algebra:

- Commutative laws: These laws state that the order of operands does not affect the result of the logic operations.

  - A + B = B + A
  - A * B = B * A

- Associative laws: These laws state that the grouping of operands does not affect the result of the logic operations.

  - (A + B) + C = A + (B + C)
  - (A * B) * C = A * (B * C)

- Distributive laws: These laws state that the logic operations can be distributed over each other.

  - A * (B + C) = (A * B) + (A * C)
  - A + (B * C) = (A + B) * (A + C)

- Identity laws: These laws state that there are two special values, 0 and 1, that act as identities for the logic operations.

  - A + 0 = A
  - A * 1 = A

- Complement laws: These laws state that there is a unary operation, called complement or NOT, that reverses the value of a variable.

  - A + A' = 1
  - A * A' = 0

- Idempotent laws: These laws state that repeating a variable in a logic operation does not change the result.

  - A + A = A
  - A * A = A

- Absorption laws: These laws state that a variable can be absorbed by another variable in a logic operation.

  - A + (A * B) = A
  - A * (A + B) = A

- De Morgan's laws: These laws state that the complement of a logic operation is equal to the logic operation of the complements with the opposite operator.

  - (A + B)' = A' * B'
  - (A * B)' = A' + B'

## Theorems of Boolean Algebra

A theorem is a statement that can be derived or proved from the axioms or other theorems. Theorems are used to simplify and manipulate logic expressions and variables. The following are some of the theorems of Boolean algebra:

- Zero and one laws: These laws state that there are two special values, 0 and 1, that have unique effects on the logic operations.

  - A + 1 = 1
  - A * 0 = 0

- Involution law: This law states that the complement of a complement is equal to the original variable.

  - (A')' = A

- Redundancy laws: These laws state that some variables or terms can be eliminated from a logic expression without changing the result.

  - A + (A * B) = A
  - A * (A + B) = A

- Consensus law: This law states that a term can be removed from a logic expression if it is implied by another term.

  - A * B + A' * C + B * C = A * B + A' * C

- Adjacency law: This law states that two adjacent terms with the same variable can be combined into one term.

  - A * B + A * B' = A

- Simplification laws: These laws state that some logic expressions can be simplified by applying the axioms and theorems of Boolean algebra.

  - A + A * B = A
  - A * (A + B) = A

- Duality principle: This principle states that every axiom and theorem of Boolean algebra has a dual form that can be obtained by interchanging the operators and the identities.

  - A + B = B + A (dual of A * B = B * A)
  - A + 0 = A (dual of A * 1 = A)
  - A + A' = 1 (dual of A * A' = 0)



# Algebraic Manipulation of Boolean Expressions

- Algebraic manipulation of boolean expressions is an approach where you can transform one boolean expression into an equivalent expression by applying the postulates and theorems of boolean algebra.
- This is important if you want to convert a given expression to a canonical form (a standardized form) or if you want to minimize the number of literals (primed or unprimed variables) or terms in an expression.
- Boolean algebra is a branch of mathematics that deals with the manipulation of variables which can have only two values: true (1) or false (0). It is based on a set of axioms and rules that define the operations of AND, OR and NOT.
- Some of the basic postulates and theorems of boolean algebra are:

  - Identity laws: A + 0 = A, A . 1 = A
  - Null laws: A + 1 = 1, A . 0 = 0
  - Idempotent laws: A + A = A, A . A = A
  - Commutative laws: A + B = B + A, A . B = B . A
  - Associative laws: (A + B) + C = A + (B + C), (A . B) . C = A . (B . C)
  - Distributive laws: A . (B + C) = (A . B) + (A . C), A + (B . C) = (A + B) . (A + C)
  - Complement laws: A + A' = 1, A . A' = 0, (A')' = A
  - De Morgan's laws: (A + B)' = A' . B', (A . B)' = A' + B'
  - Absorption laws: A + (A . B) = A, A . (A + B) = A
  - Involution law: (A')' = A

- To perform algebraic manipulation of boolean expressions, you can use the following steps:

  - Identify the given expression and the desired form (canonical or minimized).
  - Apply the appropriate postulates and theorems of boolean algebra to simplify or expand the expression.
  - Check if the resulting expression is equivalent to the given expression by using a truth table or a logic diagram.
  - Repeat the steps until you obtain the desired form or the simplest expression possible.

- Here are some examples of algebraic manipulation of boolean expressions:

  - Example 1: Simplify the expression F = A + AB + BC + AC using boolean algebra.

    - Solution: We can use the distributive law and the absorption law to simplify the expression as follows:

      - F = A + AB + BC + AC
      - F = A(1 + B) + BC + AC (distributive law)
      - F = A + BC + AC (absorption law)
      - F = A + C(B + A) (distributive law)
      - F = A + C (absorption law)

    - We can verify that the simplified expression is equivalent to the original expression by using a truth table or a logic diagram.

  - Example 2: Convert the expression F = A' + B' + C' to a product of sums form using boolean algebra.

    - Solution: We can use the De Morgan's law and the complement law to convert the expression as follows:

      - F = A' + B' + C'
      - F = (A . B . C)' (De Morgan's law)
      - F = (A + B + C) . (A + B + C)' (complement law)
      - F = (A + B + C) . (A' . B' . C') (De Morgan's law)

    - We can verify that the converted expression is equivalent to the original expression by using a truth table or a logic diagram.



# Simplification of Boolean Functions

- A boolean function is a function that takes one or more boolean variables as inputs and produces a single boolean output.
- The output of a boolean function depends on the logical operations performed on the inputs, such as AND, OR, NOT, etc.
- The algebraic expression of a boolean function can be written using boolean variables, constants (0 or 1), and operators (+, ., ', etc.).
- The process of simplifying the algebraic expression of a boolean function is called minimization.
- Minimization is important since it reduces the cost and complexity of the associated circuit .
- For example, the function F = A.B + A.B + B.C can be minimized to F = A + B.C using the theorems of boolean algebra.
- There are different methods for minimizing boolean functions, such as algebraic method, Karnaugh map method, Quine-McCluskey method, etc.
- In this unit, we will focus on the algebraic method of minimization, which uses the following boolean identities:

  - Identity law: A + 0 = A, A . 1 = A
  - Idempotent law: A + A = A, A . A = A
  - Commutative law: A + B = B + A, A . B = B . A
  - Associative law: (A + B) + C = A + (B + C), (A . B) . C = A . (B . C)
  - Distributive law: A . (B + C) = A . B + A . C, A + (B . C) = (A + B) . (A + C)
  - Complement law: A + A' = 1, A . A' = 0
  - De Morgan's law: (A + B)' = A' . B', (A . B)' = A' + B'
  - Absorption law: A + A . B = A, A . (A + B) = A
  - Involution law: (A')' = A
  - Consensus law: A . B + A' . C + B . C = A . B + A' . C

- To simplify a boolean function using the algebraic method, we apply the above identities in a systematic way until we obtain the simplest expression possible.
- The order of applying the identities is not fixed, but we can follow some general guidelines, such as:

  - Eliminate the redundant terms or literals using the idempotent law, the complement law, or the absorption law.
  - Apply the distributive law to expand the expression and create more opportunities for simplification.
  - Apply the De Morgan's law to simplify the complements of sums or products.
  - Apply the consensus law to eliminate the common terms in a sum of products or a product of sums.
  - Apply the identity law, the commutative law, or the associative law to rearrange the terms or literals as needed.

- For example, to simplify the function F ( A, B, C) = A' . B + B . C' + B . C + A . B' . C', we can follow these steps:

  - Step 1: Eliminate the redundant term B . C' + B . C using the idempotent law: F = A' . B + B + A . B' . C'
  - Step 2: Apply the distributive law to expand the expression: F = A' . B + B . 1 + A . B' . C' = A' . B + B . (A + A') + A . B' . C'
  - Step 3: Apply the complement law to simplify the term A + A': F = A' . B + B . 1 + A . B' . C' = A' . B + B + A . B' . C'
  - Step 4: Apply the consensus law to eliminate the common term A' . B: F = A' . B + B + A . B' . C' = B + A . B' . C'
  - Step 5: Rearrange the terms using the commutative law: F = B + A . B' . C' = A . B' . C' + B

- The final expression F = A .



# Karnaugh maps

- A Karnaugh map (K-map) is a method of simplifying Boolean algebra expressions .
- It is a visual method that uses a grid of cells to represent all the possible combinations of input variables and their corresponding output values.
- It helps to determine the minimum expressions in the form of sum-of-products (SOP) or product-of-sums (POS) that are equivalent to the given Boolean function .
- It also helps to detect and eliminate race conditions in logic circuits.

## Working of K-maps

- To use a K-map, the following steps are followed:
  - Select a K-map according to the number of input variables. For example, for a two-variable function, a 2x2 K-map is used; for a three-variable function, a 2x4 K-map is used; and for a four-variable function, a 4x4 K-map is used.
  - Identify the minterms or maxterms as given in the problem. A minterm is a product term that contains all the input variables in either complemented or uncomplemented form. A maxterm is a sum term that contains all the input variables in either complemented or uncomplemented form.
  - Fill the grid of the K-map with 0s and 1s according to the minterms or maxterms. For a SOP expression, place 1s for the minterms and 0s for the rest. For a POS expression, place 0s for the maxterms and 1s for the rest.
  - Group the adjacent cells that contain the same value (either 1 or 0) in the largest possible power of two (such as 1, 2, 4, 8, etc.). The groups can wrap around the edges of the K-map. Each group represents a simplified term in the final expression.
  - Write the simplified expression by combining the common variables in each group. For a SOP expression, use OR operation to join the terms. For a POS expression, use AND operation to join the terms.

## Rules of K-maps

- The following rules should be followed while using K-maps:
  - The groups should be as large as possible, but they should not contain any cell with a different value.
  - The groups should be rectangular in shape and the number of cells in each group should be a power of two.
  - The groups can overlap with each other, but the overlapping cells should not be counted twice in the final expression.
  - The groups can be formed horizontally, vertically, or diagonally, but they should not break the continuity of the K-map.
  - The groups should cover all the cells with 1s for a SOP expression and all the cells with 0s for a POS expression.

## Example Problems

- Consider the following Boolean function:

  F(A, B, C) = ∑(0, 2, 4, 5, 6)

  This is a SOP expression with three input variables and five minterms.

- To simplify this function using a K-map, we follow these steps:

  - Select a 2x4 K-map for three input variables A, B, and C. Label the rows with A and the columns with BC.
  - Fill the K-map with 1s for the minterms and 0s for the rest. The minterms are 0, 2, 4, 5, and 6, which correspond to the binary values 000, 010, 100, 101, and 110 respectively.
  - Group the adjacent cells with 1s in the largest possible power of two. In this case, we can form two groups of four cells each, as shown below.

  | A\BC | 00 | 01 | 11 | 10 |
  | ---- | -- | -- | -- | -- |
  | 0    | 1  | 0  | 0  | 1  |
  | 1    | 1  | 1  | 0  | 1  |

  The groups are marked with different colors.

  - Write the simplified expression by combining the common variables in each group. For the red group, the common variable is A'. For the blue group, the common variable is B'. The final expression is:

  F(A, B, C) = A' + B'



# Logic gates

- A logic gate is an idealized or physical device that performs a Boolean function, a logical operation performed on one or more binary inputs that produces a single binary output.
- Logic gates can be made using various types of devices, such as pneumatic, mechanical, molecular, or electronic.
- There are three basic types of logic gates: AND, OR, and NOT.
- An AND gate outputs 1 only if both inputs are 1, otherwise it outputs 0.
- An OR gate outputs 1 if either or both inputs are 1, otherwise it outputs 0.
- A NOT gate outputs the opposite of its input, i.e., 1 if the input is 0, and 0 if the input is 1.
- Logic gates can be combined to form logic circuits, which enable computers to perform more complex operations than they could with just a single gate .
- A logic circuit is a chain of logic gates, where the output of one gate is used as the input to another gate.
- Some common logic circuits are NAND, NOR, XOR, and XNOR, which are derived from the basic gates using the De Morgan's laws.
- A NAND gate outputs 0 only if both inputs are 1, otherwise it outputs 1. It is equivalent to an AND gate followed by a NOT gate.
- A NOR gate outputs 1 only if both inputs are 0, otherwise it outputs 0. It is equivalent to an OR gate followed by a NOT gate.
- An XOR gate outputs 1 if the inputs are different, otherwise it outputs 0. It is equivalent to an OR gate followed by a NAND gate.
- An XNOR gate outputs 0 if the inputs are different, otherwise it outputs 1. It is equivalent to an XOR gate followed by a NOT gate.
- Logic gates and circuits can be represented using truth tables, which show the output for every possible combination of inputs .
- Logic gates and circuits can also be represented using symbols, which show the inputs, outputs, and the type of gate .
- Here are some examples of truth tables and symbols for the basic and derived gates:

| AND | 0 | 1 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 1 |

| OR | 0 | 1 |
| --- | --- | --- |
| 0 | 0 | 1 |
| 1 | 1 | 1 |

| NOT | 0 | 1 |
| --- | --- | --- |
| | 1 | 0 |

| NAND | 0 | 1 |
| --- | --- | --- |
| 0 | 1 | 1 |
| 1 | 1 | 0 |

| NOR | 0 | 1 |
| --- | --- | --- |
| 0 | 1 | 0 |
| 1 | 0 | 0 |

| XOR | 0 | 1 |
| --- | --- | --- |
| 0 | 0 | 1 |
| 1 | 1 | 0 |

| XNOR | 0 | 1 |
| --- | --- | --- |
| 0 | 1 | 0 |
| 1 | 0 | 1 |

| Symbol | Gate |
| --- | --- |
| AND | AND |
| OR | OR |
| NOT | NOT |
| NAND | NAND |
| ![NOR](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/NOR_ANSI_Labelled.svg/1200px-N



# Digital Circuits and Boolean Algebra

- Digital circuits are electronic devices that process information in binary form, using only two voltage levels to represent 0 and 1.
- Boolean algebra is a branch of mathematics that deals with binary variables and logical operations, such as AND, OR, and NOT.
- Boolean algebra can be used to model the behavior of digital circuits, and to simplify and analyze them.
- The basic elements of digital circuits are logic gates, which perform Boolean operations on one or more inputs and produce one output.
- The most common logic gates are AND, OR, and NOT gates, which have the following truth tables:

| A | B | A AND B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 1       |

| A | B | A OR B |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |

| A | NOT A |
|---|-------|
| 0 | 1     |
| 1 | 0     |

- Other logic gates, such as NAND, NOR, XOR, and XNOR, can be derived from the basic gates by combining them in different ways.
- The symbols and truth tables for these gates are:

| A | B | A NAND B |
|---|---|----------|
| 0 | 0 | 1        |
| 0 | 1 | 1        |
| 1 | 0 | 1        |
| 1 | 1 | 0        |

| A | B | A NOR B |
|---|---|---------|
| 0 | 0 | 1       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 0       |

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 0       |

| A | B | A XNOR B |
|---|---|----------|
| 0 | 0 | 1        |
| 0 | 1 | 0        |
| 1 | 0 | 0        |
| 1 | 1 | 1        |

- A logic expression is a combination of variables and operators that represents the output of a logic circuit.
- For example, the expression A AND B OR NOT C represents the output of the following circuit:

A AND B OR NOT C

- A logic expression can be simplified using the rules of Boolean algebra, such as:

| Rule | Name | Example |
|------|------|---------|
| A + 0 = A | Identity | A OR 0 = A |
| A + 1 = 1 | Annihilation | A OR 1 = 1 |
| A + A = A | Idempotence | A OR A = A |
| A + B = B + A | Commutativity | A OR B = B OR A |
| (A + B) + C = A + (B + C) | Associativity | (A OR B) OR C = A OR (B OR C) |
| A + (B * C) = (A + B) * (A + C) | Distributivity | A OR (B AND C) = (A OR B) AND (A OR C) |
| A + A * B = A | Absorption | A OR (A AND B) = A |
| A + A' = 1 | Complement | A OR NOT A = 1 |
| (A + B)' = A' * B' | De Morgan's | NOT (A OR B) = NOT A AND NOT B |
| A * 0 = 0 | Identity | A AND 0 = 0 |
| A * 1 = A | Annihilation | A AND 1 = A |
| A * A = A | Idempotence | A AND A = A |
| A * B =



## Unit 4 - Propositional Logic

- Propositional logic is a branch of logic that deals with propositions, which are statements that can be either true or false.
- Propositional logic uses symbols and connectives to represent propositions and their logical relations.
- The basic symbols of propositional logic are:
  - **Propositional variables**: lowercase letters (p, q, r, ...) that stand for arbitrary propositions.
  - **Logical constants**: uppercase letters (T, F) that stand for the truth values true and false.
  - **Logical connectives**: symbols that combine propositional variables or constants to form complex propositions. The main logical connectives are:
    - **Negation**: ¬p, which means "not p" or "it is not the case that p".
    - **Conjunction**: p ∧ q, which means "p and q" or "both p and q".
    - **Disjunction**: p ∨ q, which means "p or q" or "either p or q".
    - **Implication**: p → q, which means "p implies q" or "if p then q".
    - **Equivalence**: p ↔ q, which means "p is equivalent to q" or "p if and only if q".
- The meaning of a proposition is determined by its truth value, which is either true or false. The truth value of a proposition depends on the truth values of its components and the logical connectives that join them.
- A **truth table** is a table that shows the truth value of a proposition for every possible combination of truth values of its components. A truth table has one column for each component and one column for the proposition. Each row of the table corresponds to a possible assignment of truth values to the components. The truth value of the proposition in each row is calculated by applying the rules of the logical connectives.
- The rules of the logical connectives are:
  - ¬p is true if and only if p is false.
  - p ∧ q is true if and only if both p and q are true.
  - p ∨ q is true if and only if at least one of p and q is true.
  - p → q is true if and only if either p is false or q is true.
  - p ↔ q is true if and only if p and q have the same truth value.
- Here are some examples of truth tables:

| p | q | ¬p | p ∧ q | p ∨ q | p → q | p ↔ q |
|---|---|----|-------|-------|-------|-------|
| T | T | F  | T     | T     | T     | T     |
| T | F | F  | F     | T     | F     | F     |
| F | T | T  | F     | T     | T     | F     |
| F | F | T  | F     | F     | T     | T     |

- A proposition is **tautology** if it is always true, regardless of the truth values of its components. For example, p ∨ ¬p is a tautology, because it is true for both p = T and p = F.
- A proposition is **contradiction** if it is always false, regardless of the truth values of its components. For example, p ∧ ¬p is a contradiction, because it is false for both p = T and p = F.
- A proposition is **contingency** if it is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its components. For example, p ∧ q is a contingency, because it is true for p = T and q = T, but false for any other combination of truth values.
- Two propositions are **logically equivalent** if they have the same truth value for every possible assignment of truth values to their components. For example, p → q and ¬p ∨ q are logically equivalent, because they have the same truth value in every row of their truth tables. Logical equivalence is denoted by ≡, so we can write p → q ≡ ¬p ∨ q.
- Two propositions are **logically consistent** if there is at least one assignment of truth values to their components that makes them both true. For example, p and q are logically consistent, because they are both true for p = T and q = T. Logical consistency is denoted by ⊨, so we can write p ⊨ q.
- Two propositions are **logically inconsistent** if there is no assignment of truth values to their components that makes them both true. For example, p and ¬p are



Hello, I am Sydney, your AI assistant. I can help you with your notes for Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic. Here is a possible outline of the notes:

# Unit 4 - Propositional Logic

## Introduction
- Propositional logic is a branch of logic that deals with statements that can be true or false.
- A statement is a declarative sentence that has a truth value, either true (T) or false (F).
- A proposition is the meaning or content of a statement, regardless of the words or symbols used to express it.
- Propositional logic uses symbols and rules to manipulate and analyze propositions and their truth values.

## Propositional Variables and Connectives
- A propositional variable is a symbol that represents a proposition, such as p, q, r, etc.
- A propositional connective is a symbol that combines one or more propositions to form a new proposition, such as ¬ (negation), ∧ (conjunction), ∨ (disjunction), → (implication), and ↔ (equivalence).
- The truth value of a compound proposition depends on the truth values of its components and the connective used.
- A truth table is a table that shows the truth value of a proposition for all possible combinations of truth values of its variables.

## Logical Equivalence and Tautology
- Two propositions are logically equivalent if they have the same truth value for every possible assignment of truth values to their variables. We write p ≡ q to denote that p and q are logically equivalent.
- A logical equivalence can be proven by showing that the truth tables of the two propositions are identical, or by using logical laws and rules of inference.
- A tautology is a proposition that is always true, regardless of the truth values of its variables. For example, p ∨ ¬p is a tautology.
- A contradiction is a proposition that is always false, regardless of the truth values of its variables. For example, p ∧ ¬p is a contradiction.
- A contingency is a proposition that is neither a tautology nor a contradiction, meaning that it can be true or false depending on the truth values of its variables. For example, p ∧ q is a contingency.

## Normal Forms and Simplification
- A normal form is a standard way of writing a proposition using a specific set of connectives and rules.
- A disjunctive normal form (DNF) is a proposition that is a disjunction of one or more conjunctions of literals, where a literal is a variable or its negation. For example, (p ∧ q) ∨ (¬p ∧ r) is a DNF.
- A conjunctive normal form (CNF) is a proposition that is a conjunction of one or more disjunctions of literals. For example, (p ∨ ¬q) ∧ (¬p ∨ r) is a CNF.
- Every proposition can be converted to an equivalent DNF or CNF using the laws of propositional logic, such as De Morgan's laws, distributive laws, etc.
- A proposition can be simplified by eliminating redundant or contradictory literals or clauses, or by applying logical identities, such as p ∨ T ≡ T, p ∧ F ≡ F, etc.

## Logical Implication and Inference
- A proposition p logically implies another proposition q if q is true whenever p is true. We write p ⇒ q to denote that p logically implies q.
- A logical implication can be proven by showing that the truth table of p → q is a tautology, or by using logical laws and rules of inference.
- A rule of inference is a valid argument form that allows us to deduce a new proposition from one or more given propositions. For example, modus ponens is a rule of inference that states that if p and p → q are true, then q is true.
- A proof is a sequence of propositions that starts with one or more premises and ends with a conclusion, where each proposition is either a premise or follows from previous propositions by a rule of inference.
- A proof method is a systematic way of constructing a proof, such as direct proof, indirect proof, proof by contradiction, proof by cases, etc.



# Well Formed Formula

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
  - ((p ↔ q) ↔ r)
- Examples of non-WFFs are:
  - p ∧
  - (p ∨
  - p q
  - (p → q) ∧
  - (p ↔ q r)



# Truth tables for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A truth table is a mathematical table used in logic that shows the truth values of logical expressions for each possible combination of values taken by their logical variables.
- A truth table can be used to solve various problems in propositional logic, such as showing the semantics of logical operators, proving equivalences, solving satisfiability problems, etc.
- A truth table has one column for each logical variable and one column for the logical expression. The rows of the table correspond to all possible assignments of truth values to the variables. The truth value of the expression for each row is calculated using the rules of propositional logic.
- The following table shows the basic logical operators and their truth tables:

| Operator | Symbol | Example | Truth table |
|:--------:|:------:|:-------:|:-----------:|
| Negation | ¬, ~, ! | ¬p | p | ¬p |
| | | | T | F |
| | | | F | T |
| Conjunction | ∧, /\\, & | p ∧ q | p | q | p ∧ q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | F |
| | | | F | F | F |
| Disjunction | ∨, \\/, \| | p ∨ q | p | q | p ∨ q |
| | | | T | T | T |
| | | | T | F | T |
| | | | F | T | T |
| | | | F | F | F |
| Implication | →, ->, => | p → q | p | q | p → q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | T |
| | | | F | F | T |
| Equivalence | ↔, <->, <=> | p ↔ q | p | q | p ↔ q |
| | | | T | T | T |
| | | | T | F | F |
| | | | F | T | F |
| | | | F | F | T |

- To construct a truth table for a complex expression, we can use the following steps:
  - Identify all the logical variables and operators in the expression and assign a column for each of them.
  - Write down all possible combinations of truth values for the variables in the rows of the table. A common method is to use binary counting, starting from all F's and ending with all T's.
  - Fill in the truth values for the operators, starting from the innermost parentheses and working outwards. Use the rules of propositional logic to calculate the truth values for each row.
  - The final column of the table will show the truth values of the whole expression.

- For example, to construct a truth table for the expression (p ∧ q) → (p ∨ q), we can follow these steps:

| Step | Expression | Truth table |
|:----:|:----------:|:-----------:|
| 1 | (p ∧ q) → (p ∨ q) | p | q | (p ∧ q) | (p ∨ q) | (p ∧ q) → (p ∨ q) |
| 2 | (p ∧ q) → (p ∨ q) | p | q | (p ∧ q) | (p ∨ q) | (p ∧ q) → (p ∨ q) |
| | | F | F | | | |
| | | F | T | | | |
| | | T | F | | | |
| | | T | T | | | |
| 3 | (p ∧ q) → (p ∨ q) | p | q | (p ∧ q) | (p ∨ q) | (p ∧ q) → (p ∨ q) |
| | | F | F | F | F | |
| | | F | T | F | T | |
| | | T | F | F | T | |
| | | T | T | T | T | |
| 4 | (p ∧ q) → (p ∨ q) | p | q | (p ∧ q) | (p ∨ q) | (p ∧ q) → (p



# Tautology for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A **tautology** is a propositional formula that is **true under any possible Boolean valuation of its propositional variables** .
- A tautology is also called a **logically valid formula** or a **tautological consequence**.
- A tautology can be recognized by using a **truth table** that shows all the possible combinations of truth values for the propositional variables and the formula .
- A tautology is true in every row of the truth table, regardless of the truth values of the propositional variables .
- A tautology can also be recognized by using **logical equivalences** or **rules of inference** that simplify the formula to a single propositional variable or a constant .
- A tautology can be used to **prove the validity of an argument** by showing that the conclusion follows from the premises by logical necessity .
- A tautology can also be used to **derive new formulas** from existing ones by applying logical rules or equivalences .
- Some examples of tautologies are :

  - p ∨ ¬p (law of excluded middle)
  - p → p (law of identity)
  - (p → q) ∨ (q → p) (material implication)
  - (p ∧ q) → p (simplification)
  - p ↔ p (law of biconditional)
  - (p ∧ (p ∨ q)) ↔ p (absorption)
  - (p ∨ q) ↔ (¬p → q) (implication)
  - ¬(p ∧ ¬p) (law of non-contradiction)



# Satisfiability for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- Satisfiability is a semantic property of a propositional formula or a set of propositional formulas that indicates whether there exists a truth assignment that makes the formula or the set of formulas true .
- A propositional formula is satisfiable if there is a 1-assignment for it; a set of propositional formulas is satisfiable if there is a simultaneous 1-assignment for its elements.
- A propositional formula is unsatisfiable if there is no truth assignment that makes it true; a set of propositional formulas is unsatisfiable if there is no simultaneous truth assignment that makes all of them true .
- A propositional formula is valid if it is true for every truth assignment; a set of propositional formulas is valid if every truth assignment that makes all of them true also makes the conclusion true .
- The propositional satisfiability problem (often called SAT) is the problem of determining whether a set of sentences in propositional logic is satisfiable .
- SAT is a fundamental problem in computer science and logic, as many other problems can be reduced to it, such as circuit design, planning, theorem proving, and cryptography  .
- SAT is also a computationally hard problem, as it belongs to the class of NP-complete problems, which means that there is no known efficient algorithm that can solve it in polynomial time  .
- However, there are various methods and heuristics that can solve SAT for many practical instances, such as backtracking, resolution, local search, and stochastic algorithms  .
- SAT can be extended to other logics, such as first-order logic, modal logic, and temporal logic, by adding more symbols and rules to the syntax and semantics of propositional logic.



# Contradiction for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- A contradiction is an assertion of propositional logic that is false in all situations; that is, it is false for all possible values of its variables .
- For example, the assertion A ∨ B is true when A is true (or B is true), but it is false when A and B are both false.
- A contradiction can be expressed as a compound proposition that is logically equivalent to F, the false constant.
- For example, the proposition A ∧ ¬A is a contradiction, because it is always false regardless of the value of A.
- A contradiction can also be expressed as a negation of a tautology, which is a proposition that is true in all situations.
- For example, the proposition ¬(A ∨ ¬A) is a contradiction, because it is the negation of a tautology A ∨ ¬A.
- A contradiction can be used as a tool to detect disingenuous beliefs and bias, by showing that a proposition conflicts either with itself or established fact.
- For example, the proposition "All men are mortal and some men are immortal" is a contradiction, because it conflicts with itself.
- A contradiction can also be used as a form of proof by contradiction, which is a method of establishing the truth or validity of a proposition by showing that assuming the proposition to be false leads to a contradiction.
- For example, to prove that √2 is irrational, we can assume that it is rational and write it as a fraction a/b in lowest terms, then show that this leads to a contradiction that a and b are both even, which contradicts the assumption that a/b is in lowest terms.



# Algebra of Proposition

- Algebra of proposition is the subbranch of mathematical logic that studies propositions and logical operators.
- A proposition is a declarative sentence that has a truth value, either true or false.
- A logical operator is a symbol that defines a new proposition from one or more given propositions.
- The most common logical operators are negation (NOT), conjunction (AND), disjunction (OR), implication (IF ... THEN), and equivalence (IF AND ONLY IF).
- Each logical operator has a truth table that shows the truth value of the new proposition for every possible combination of truth values of the given propositions.
- For example, the truth table for the conjunction operator (AND) is:

| p | q | p AND q |
|---|---|---------|
| T | T | T       |
| T | F | F       |
| F | T | F       |
| F | F | F       |

- This means that p AND q is true only when both p and q are true, and false otherwise.
- Algebra of proposition also studies the properties and rules of logical operators, such as commutativity, associativity, distributivity, identity, complement, idempotence, absorption, De Morgan's laws, etc .
- For example, the commutative property states that p AND q is equivalent to q AND p, and p OR q is equivalent to q OR p.
- Algebra of proposition also uses logical equivalence and logical implication to compare and simplify propositions .
- Two propositions are logically equivalent if they have the same truth value for every possible assignment of truth values to their variables .
- For example, p AND q is logically equivalent to NOT (NOT p OR NOT q), as shown by the following truth table:

| p | q | p AND q | NOT p | NOT q | NOT p OR NOT q | NOT (NOT p OR NOT q) |
|---|---|---------|-------|-------|-----------------|----------------------|
| T | T | T       | F     | F     | F               | T                    |
| T | F | F       | F     | T     | T               | F                    |
| F | T | F       | T     | F     | T               | F                    |
| F | F | F       | T     | T     | T               | F                    |

- Logical equivalence can be used to transform a proposition into a simpler or more convenient form without changing its meaning.
- A proposition p logically implies a proposition q if q is true whenever p is true .
- For example, p OR q logically implies p, as shown by the following truth table:

| p | q | p OR q | p OR q implies p |
|---|---|--------|------------------|
| T | T | T      | T                |
| T | F | T      | T                |
| F | T | T      | F                |
| F | F | F      | T                |

- Logical implication can be used to deduce new propositions from existing ones or to prove the validity of arguments .
- Algebra of proposition is useful for analyzing and manipulating logical expressions, such as those used in computer programming, circuit design, cryptography, artificial intelligence, etc .



# Theory of Inference for the notes of the Unit 4 - Propositional Logic in the subject of Discrete Structures & Theory of Logic

- **Propositional logic** is the branch of logic that studies ways of combining or altering statements or propositions to form more complicated statements or propositions.
- **Inference** is the process of deriving new statements or propositions from given statements or propositions using rules of logic.
- **Rules of inference** are the logical principles that allow us to draw valid conclusions from given premises.
- **Validity** is the property of an argument that guarantees that the conclusion follows from the premises, regardless of the truth or falsity of the premises.
- **Soundness** is the property of an argument that guarantees that the conclusion is true, if the premises are true and the argument is valid.
- **Modus ponens** is a rule of inference that states that if p implies q and p is true, then q is true. Symbolically, it can be written as (p -> q) ^ p => q.
- **Modus tollens** is a rule of inference that states that if p implies q and q is false, then p is false. Symbolically, it can be written as (p -> q) ^ ~q => ~p.
- **Contraposition** is a rule of inference that states that if p implies q, then not q implies not p. Symbolically, it can be written as (p -> q) => (~q -> ~p).
- **Conjunction** is a rule of inference that states that if p and q are both true, then p ^ q is true. Symbolically, it can be written as p ^ q => p ^ q.
- **Simplification** is a rule of inference that states that if p ^ q is true, then p is true and q is true. Symbolically, it can be written as p ^ q => p and p ^ q => q.
- **Addition** is a rule of inference that states that if p is true, then p v q is true for any q. Symbolically, it can be written as p => p v q.
- **Disjunctive syllogism** is a rule of inference that states that if p v q is true and p is false, then q is true. Symbolically, it can be written as (p v q) ^ ~p => q.
- **Hypothetical syllogism** is a rule of inference that states that if p implies q and q implies r, then p implies r. Symbolically, it can be written as (p -> q) ^ (q -> r) => (p -> r).
- **Dilemma** is a rule of inference that states that if p implies q and r implies s, and either p or r is true, then either q or s is true. Symbolically, it can be written as (p -> q) ^ (r -> s) ^ (p v r) => (q v s).
- **Resolution** is a rule of inference that states that if p v q and ~p v r are true, then q v r is true. Symbolically, it can be written as (p v q) ^ (~p v r) => (q v r).
- **De Morgan's laws** are rules of inference that state that the negation of a conjunction is equivalent to the disjunction of the negations, and the negation of a disjunction is equivalent to the conjunction of the negations. Symbolically, they can be written as ~(p ^ q) <=> ~p v ~q and ~(p v q) <=> ~p ^ ~q.
- **Double negation** is a rule of inference that states that the negation of a negation is equivalent to the original statement. Symbolically, it can be written as ~~p <=> p.
- **Commutation** is a rule of inference that states that the order of the operands in a conjunction or a disjunction does not affect the truth value of the statement. Symbolically, it can be written as p ^ q <=> q ^ p and p v q <=> q v p.
- **Association** is a rule of inference that states that the grouping of the operands in a conjunction or a disjunction does not affect the truth value of the statement. Symbolically, it can be written as (p ^ q) ^ r <=> p ^ (q ^ r) and (p v q) v r <=> p v (q v r).
- **Distribution** is a rule of inference



## Unit 5 - Predicate Logic

Predicate logic is a branch of logic that deals with predicates, quantifiers, and variables. Predicate logic is more expressive than propositional logic, as it can capture the structure and meaning of natural language sentences more accurately.

### Predicate Logic Syntax

The syntax of predicate logic consists of the following elements:

- **Predicates**: Predicates are symbols that represent properties or relations of objects. For example, `P(x)` means that object `x` has property `P`, and `Q(x,y)` means that objects `x` and `y` are related by relation `Q`.
- **Constants**: Constants are symbols that represent specific objects in the domain of discourse. For example, `a`, `b`, and `c` can be constants that denote Alice, Bob, and Charlie, respectively.
- **Variables**: Variables are symbols that can stand for any object in the domain of discourse. For example, `x`, `y`, and `z` can be variables that range over all possible objects.
- **Quantifiers**: Quantifiers are symbols that indicate how many objects satisfy a given predicate. There are two main types of quantifiers: universal (`∀`) and existential (`∃`). For example, `∀x P(x)` means that all objects have property `P`, and `∃x Q(x,a)` means that there exists some object that is related to `a` by relation `Q`.
- **Connectives**: Connectives are symbols that combine predicates or quantified formulas into more complex formulas. The connectives of predicate logic are the same as those of propositional logic: negation (`¬`), conjunction (`∧`), disjunction (`∨`), implication (`→`), and equivalence (`↔`).
- **Parentheses**: Parentheses are symbols that group formulas together and indicate the scope of quantifiers and connectives. For example, `(∀x P(x)) → Q(a)` means that if all objects have property `P`, then `a` has property `Q`.

### Predicate Logic Semantics

The semantics of predicate logic defines how to assign truth values to predicate logic formulas based on a given interpretation. An interpretation consists of the following components:

- **Domain**: The domain is the set of all possible objects that the constants, variables, and predicates refer to. For example, the domain can be the set of all people, or the set of all natural numbers, or the set of all animals, etc.
- **Assignment**: The assignment is a function that maps each constant to a specific object in the domain, and each variable to an arbitrary object in the domain. For example, the assignment can map `a` to Alice, `b` to Bob, `c` to Charlie, `x` to Alice, `y` to Bob, and `z` to Charlie.
- **Interpretation**: The interpretation is a function that maps each predicate to a set of tuples of objects in the domain that satisfy the predicate. For example, the interpretation can map `P` to the set of all people who are happy, and `Q` to the set of all pairs of people who are friends.

The truth value of a predicate logic formula is determined by the following rules:

- A predicate formula `P(t1,...,tn)` is true if and only if the tuple of objects denoted by the terms `t1,...,tn` belongs to the set mapped by the predicate `P` in the interpretation. A term can be either a constant or a variable. For example, `P(a)` is true if and only if Alice is happy, and `Q(x,y)` is true if and only if `x` and `y` are friends.
- A negated formula `¬φ` is true if and only if `φ` is false.
- A conjunctive formula `φ ∧ ψ` is true if and only if both `φ` and `ψ` are true.
- A disjunctive formula `φ ∨ ψ` is true if and only if either `φ` or `ψ` is true.
- An implication formula `φ → ψ` is true if and only if either `φ` is false or `ψ` is true.
- An equivalence formula `φ ↔ ψ` is true if and only if `φ` and `ψ` have the same truth value.
- A universally quantified formula `∀x φ` is true if and only if `φ` is true for every possible value of `x` in the domain. For example, `∀x P(x)` is true if and only if everyone is happy.
- An existentially quantified formula `∃x φ`



# First order predicate logic

- First order predicate logic is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Predicates are symbols that represent properties or relations of objects in a domain of discourse.
- Variables are symbols that can take any value from a domain of discourse.
- Quantifiers are symbols that express how many objects in a domain of discourse satisfy a predicate.
- The two most common quantifiers are the universal quantifier (∀) and the existential quantifier (∃).
- The universal quantifier (∀) means "for all" or "every". For example, ∀x P(x) means "P(x) is true for every x in the domain of discourse".
- The existential quantifier (∃) means "there exists" or "some". For example, ∃x P(x) means "there is some x in the domain of discourse such that P(x) is true".
- First order predicate logic can express more complex and nuanced propositions than propositional logic, which lacks quantifiers.
- For example, propositional logic cannot express the difference between "All humans are mortal" and "Some humans are mortal", but first order predicate logic can, using the predicates H(x) for "x is human" and M(x) for "x is mortal".
- The first proposition can be written as ∀x (H(x) → M(x)), meaning "for every x, if x is human, then x is mortal".
- The second proposition can be written as ∃x (H(x) ∧ M(x)), meaning "there is some x such that x is human and x is mortal".
- First order predicate logic is the standard for the formalization of mathematics into axioms, and is studied in the foundations of mathematics.
- Peano arithmetic and Zermelo–Fraenkel set theory are axiomatizations of number theory and set theory, respectively, into first order predicate logic.
- First order predicate logic is also known as first-order logic, quantificational logic, and first-order predicate calculus.



# Well Formed Formula of Predicate Logic

- A well formed formula (WFF) of predicate logic is a string of symbols that can be interpreted as a meaningful expression in predicate logic.
- A WFF can be either a **closed formula** or an **open formula**.
- A closed formula (also called a **sentence** or a **proposition**) is a WFF that does not contain any free variables. It can be evaluated as true or false in a given interpretation.
- An open formula (also called a **sentential function** or a **propositional function**) is a WFF that contains at least one free variable. It cannot be evaluated as true or false by itself, but only when the free variables are assigned values from a domain.
- The rules for constructing WFFs of predicate logic are as follows :
  - Any predicate letter followed by any constant or variable is a WFF. For example: `Pq`, `Qx`, `Rab`.
  - The result of prefixing any WFF with `~` (negation) is a WFF. For example: `~Pq`, `~(Qx ∨ Ry)`.
  - The result of joining any two WFFs with `•` (conjunction), `∨` (disjunction), `⊃` (implication), or `≡` (equivalence) and enclosing the result in parentheses is a WFF. For example: `(Pq • Qx)`, `(Qx ⊃ Ry)`, `(Pq ≡ ~Qx)`.
  - The result of prefixing any WFF with `∀x` (universal quantification) or `∃x` (existential quantification), where `x` is any variable, is a WFF. For example: `∀xPx`, `∃yQy`, `∀x(Qx ⊃ ∃yRxy)`.
  - Nothing else is a WFF. For example: `P`, `QxRy`, `∀Pq`, `(Pq ∨)`.
- The order of precedence of the logical operators is as follows: `~`, `∀`, `∃`, `•`, `∨`, `⊃`, `≡`. Parentheses can be used to override the order of precedence. For example: `~∀xPx` means `~(∀xPx)`, not `(~∀x)Px`.
- The scope of a quantifier is the part of the WFF that it affects. The scope of a quantifier is the WFF that immediately follows it, unless parentheses indicate otherwise. For example: in `∀x(Px ∨ Qx)`, the scope of `∀x` is `(Px ∨ Qx)`; in `∀xPx ∨ Qx`, the scope of `∀x` is `Px`.
- A variable is **bound** in a WFF if it occurs within the scope of a quantifier that uses the same variable. A variable is **free** in a WFF if it is not bound. For example: in `∀xPx ∨ Qx`, `x` is bound and `y` is free; in `Px ∨ Qy`, both `x` and `y` are free.
- A WFF is **valid** if it is true in every possible interpretation. A WFF is **satisfiable** if it is true in at least one possible interpretation. A WFF is **unsatisfiable** if it is false in every possible interpretation. For example: `∀xPx ⊃ ∃xPx` is valid; `∀xPx ∨ ∃x~Px` is satisfiable but not valid; `∀xPx • ∃x~Px` is unsatisfiable.



# Quantifiers

Quantifiers are symbols that indicate how many instances of a variable make a predicate true. They are used in predicate logic to express the scope and extent of a predicate over a range of elements. There are two main types of quantifiers: universal and existential.

## Universal Quantifier

The universal quantifier, denoted by the symbol ∀, states that the statements within its scope are true for every value of the specific variable. For example, the statement ∀x P(x) means that P(x) is true for all values of x in the domain. The universal quantifier is also called the "for all" or "for every" quantifier.

## Existential Quantifier

The existential quantifier, denoted by the symbol ∃, states that the statements within its scope are true for at least one value of the specific variable. For example, the statement ∃x P(x) means that P(x) is true for some value of x in the domain. The existential quantifier is also called the "there exists" or "for some" quantifier.

## Examples

- The statement "Every natural number is even or odd" can be written in predicate logic as ∀x (N(x) → (E(x) ∨ O(x))), where N(x) is the predicate "x is a natural number", E(x) is the predicate "x is even", and O(x) is the predicate "x is odd".
- The statement "Some prime numbers are odd" can be written in predicate logic as ∃x (P(x) ∧ O(x)), where P(x) is the predicate "x is a prime number" and O(x) is the predicate "x is odd".
- The statement "There is no largest natural number" can be written in predicate logic as ¬∃x ∀y (N(x) ∧ N(y) → x ≥ y), where N(x) is the predicate "x is a natural number" and x ≥ y is the relation "x is greater than or equal to y".



# Inference Theory of Predicate Logic

- Predicate logic, also known as first-order logic or quantified logic, is a formal language in which propositions are expressed in terms of predicates, variables and quantifiers.
- Predicates are functions that take one or more arguments and return a truth value. For example, P(x) means "x is prime".
- Variables are symbols that can represent any object in the domain of discourse. For example, x, y, z, etc.
- Quantifiers are operators that specify the scope of a variable. For example, ∀x means "for all x" and ∃x means "there exists x".
- Inference theory of predicate logic is a set of rules that allow us to derive valid conclusions from quantified statements .
- There are four main rules of inference for predicate logic :
  - Universal specification (US): From ∀x P(x), one can conclude P(y) for any y in the domain.
  - Universal generalization (UG): From P(y) for any y in the domain, one can conclude ∀x P(x).
  - Existential specification (ES): From ∃x P(x), one can conclude P(y) for some y in the domain.
  - Existential generalization (EG): From P(y) for some y in the domain, one can conclude ∃x P(x).
- These rules can be used to construct valid arguments in predicate logic. For example, given the premises:
  - ∀x (P(x) → Q(x))
  - ∃x P(x)
  - We can use US to infer P(a) for some a in the domain.
  - We can use modus ponens (a rule of propositional logic) to infer Q(a) from P(a) and ∀x (P(x) → Q(x)).
  - We can use EG to infer ∃x Q(x) from Q(a).
  - Therefore, the conclusion ∃x Q(x) follows from the premises by the rules of inference.



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
  - Red-black tree: A balanced binary search tree where every node is either red or black, and the following rules are satisfied:
    - The root is black.
    - Every leaf is black.
    - If a node is red, then both its children are black.
    - Every simple path from a node to a descendant leaf has the same number of black nodes.
  - B-tree: A tree where each node has a variable number of children, and the following rules are satisfied:
    - The root has at least two children, unless it is the only node in the tree.
    - Every node except the root and the leaves has at least `t` children and at most `2t` children, where `t` is a fixed positive integer.
    - Every leaf has the same depth, which is the height of the tree.
    - Each node contains `n` keys, where `n` is the number of children minus one, and the keys are sorted in ascending order.
    - The keys of a node act as separators for the subtrees. For example, if a node has keys `k1, k2, k3`, and children `c1, c2, c3, c4`, then all the keys in `c1` are less than `k1`, all the keys in `c2` are between `k1` and `k2`, all the keys in `c3` are between `k2` and `k3`, and all the keys in `c4` are greater than `k3`.
  - Trie: A tree where each node represents a prefix of a string, and the children of a node are the possible characters that can extend the prefix. The root represents the empty string. A node is marked as a terminal node if it represents a complete string.
- Some common operations on trees are:
  - Traversal: Visiting every node in the tree in a specific order. There are three types of traversal for binary trees:
    - Preorder: Visit the root, then the left subtree, then the right subtree.
    - Inorder: Visit the left subtree, then the root, then the right subtree.
    - Postorder: Visit the left subtree, then the right subtree, then the root.
  - Search: Finding a node with a given value or key in the tree. The search algorithm depends on the type of the tree. For example, for a binary search tree, we can compare the value with the root, and recursively search in the left or right subtree depending on the result of the comparison.
  - Insertion: Adding a new node with a given value or key to the tree. The insertion algorithm depends on the type of the tree. For example, for a binary search tree, we can search for the value, and insert the new node as a leaf at the appropriate position.
  - Deletion: Removing a node with a given value or key from the tree. The deletion algorithm depends on the type of the tree. For example, for a binary search tree, we can search for the value, and replace the node with its successor or predecessor, or with a leaf if it has no children.
  - Height: Finding the length of the longest path from the root to a leaf in the tree. The height of an empty tree is -1, and the height of a tree with one node is 0.
  - Size: Finding the number of nodes in the tree. The size of an empty tree is 0, and the size of a tree with one node is 1



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some definitions for the notes of the Unit 6 - Trees in the subject of Discrete Structures & Theory of Logic.

# Unit 6 - Trees

## Definition 1: Tree
- A tree is a connected, undirected graph that has no cycles.
- A tree with n vertices has n-1 edges.
- A tree is also called a free tree or a simple graph.

## Definition 2: Rooted Tree
- A rooted tree is a tree in which one vertex is designated as the root.
- The root is the only vertex with no parent.
- The root has zero or more children, which are the vertices adjacent to it.
- Each child of the root has zero or more children of its own, and so on.
- The vertices that have no children are called leaves.

## Definition 3: Ordered Tree
- An ordered tree is a rooted tree in which the children of each vertex are ordered from left to right.
- An ordered tree is also called a plane tree or a labeled tree.

## Definition 4: Binary Tree
- A binary tree is an ordered tree in which each vertex has at most two children, called the left child and the right child.
- A binary tree is also called a 2-tree or a full binary tree.

## Definition 5: Height and Depth of a Tree
- The height of a tree is the length of the longest path from the root to a leaf.
- The height of a vertex in a tree is the length of the longest path from that vertex to a leaf.
- The depth of a vertex in a tree is the length of the path from the root to that vertex.
- The depth of the root is zero.



# Binary tree

- A binary tree is a **tree data structure** where each node has up to **two child nodes**, creating the branches of the tree  .
- The two children are usually called the **left and right nodes** .
- A binary tree is also a **rooted tree** that is also an **ordered tree** (a.k.a. plane tree) in which every node has at most two children.
- A rooted tree naturally imparts a notion of **levels** (distance from the root), thus for every node a notion of **children** may be defined as the nodes connected to it a level below.
- A binary tree is either:
  - An **empty tree** (a tree consisting of no vertices), or
  - A **non-empty tree** consisting of a **root node** and two subtrees that are both binary trees, called the **left subtree** and the **right subtree** of the root.
- A binary tree is called a **full binary tree** (sometimes referred to as a proper or plane or strict binary tree) if every node has either 0 or 2 children .
- A binary tree is called a **complete binary tree** if all levels are completely filled except possibly the last level and the last level has all keys as left as possible.
- A binary tree is called a **balanced binary tree** if the height of the tree is O(log n) where n is the number of nodes.
- A binary tree is called a **perfect binary tree** if all internal nodes have two children and all leaves are at the same level.
- A binary tree is called a **degenerate (or pathological) binary tree** if every internal node has one child. Such trees are performance-wise same as linked list.
- A binary tree is called a **skewed binary tree** if all nodes have only one child, either left or right.
- A binary tree is called a **binary search tree** if for every node, the value of all the nodes in the left subtree is lesser or equal and the value of all the nodes in the right subtree is greater or equal.
- A binary tree is called a **binary heap** if it is a complete binary tree and satisfies the heap property, which states that the value of a node is greater than or equal to (max-heap) or less than or equal to (min-heap) the value of its parent.
- A binary tree is called a **binary expression tree** if it is a binary tree that represents an arithmetic expression. Each internal node corresponds to an operator and each leaf node corresponds to an operand.
- A binary tree is called a **Huffman tree** if it is a binary tree that is used for optimal prefix coding. It is a full binary tree where each leaf node represents a character and its frequency, and the weight of each internal node is the sum of the weights of its children.



# Binary tree traversal

Binary tree traversal is a process of visiting each node in a binary tree exactly once in a defined order. A binary tree is a non-linear data structure that consists of nodes, each having at most two children: left child and right child. The topmost node is called the root node, and the nodes with no children are called leaf nodes.

There are three common types of binary tree traversal: inorder, preorder and postorder. Each type of traversal defines a different order of visiting the nodes, based on the following rules:

- Inorder traversal: visit the left subtree, then the root, then the right subtree.
- Preorder traversal: visit the root, then the left subtree, then the right subtree.
- Postorder traversal: visit the left subtree, then the right subtree, then the root.

The following diagram shows an example of a binary tree and its inorder, preorder and postorder traversal.

Binary tree traversal

The inorder traversal of the binary tree is: D B E A F C
The preorder traversal of the binary tree is: A B D E C F
The postorder traversal of the binary tree is: D E B F C A

The binary tree traversal can be implemented using recursion or iteration. The recursive approach is simpler and more intuitive, but it may cause stack overflow if the tree is very deep. The iterative approach uses a stack or a queue to store the nodes that need to be visited, and it is more efficient in terms of space and time complexity.

The following pseudocode shows the recursive and iterative implementations of the inorder traversal of a binary tree.

## Recursive inorder traversal

```
procedure inorder(node)
  if node is not null then
    inorder(node.left) // visit the left subtree
    print node.data // visit the root
    inorder(node.right) // visit the right subtree
  end if
end procedure
```

## Iterative inorder traversal

```
procedure inorder(root)
  create an empty stack S
  initialize current node as root
  while current node is not null or stack is not empty do
    while current node is not null do
      push current node to S // store the node for later visit
      current node = current node.left // move to the left child
    end while
    current node = pop from S // retrieve the node from the stack
    print current node.data // visit the node
    current node = current node.right // move to the right child
  end while
end procedure
```



# Binary Search Tree

A binary search tree (BST) is a data structure that stores values in a hierarchical order. It has the following properties  :

- A BST is a rooted binary tree, which means it has a single node called the root at the top, and each node has at most two children, called the left child and the right child.
- Each node in a BST has a key (and an optional value) that can be compared with other keys using a total order relation, such as less than, equal to, or greater than.
- The key of any node is greater than all the keys in its left subtree, and less than all the keys in its right subtree. This is called the binary search property, and it allows for efficient search, insertion, and deletion operations.
- A BST can be empty, which means it has no nodes.

Here is an example of a BST with seven nodes:

```
    8
   / \
  3   10
 / \    \
1   6    14
   / \   /
  4   7 13
```

The root node has the key 8, and it has two children: the left child has the key 3, and the right child has the key 10. The node with the key 3 has two children: the left child has the key 1, and the right child has the key 6. The node with the key 10 has one child: the right child has the key 14. The node with the key 6 has two children: the left child has the key 4, and the right child has the key 7. The node with the key 14 has one child: the left child has the key 13. The nodes with the keys 1, 4, 7, and 13 have no children, and they are called the leaf nodes.

The binary search property is satisfied for every node in this BST. For example, the key of the node with the key 6 is greater than the key of its left child (4), and less than the key of its right child (7). The key of the node with the key 10 is greater than all the keys in its left subtree (8, 3, 1, 6, 4, 7), and less than all the keys in its right subtree (14, 13).

A BST can have different shapes depending on the order of insertion and deletion of the nodes. For example, if we insert the nodes with the keys 1, 2, 3, 4, 5, 6, 7 in that order, we get a BST that looks like a linked list:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
           \
            7
```

This BST is called a skewed BST, and it has the worst performance for search, insertion, and deletion operations, because they take linear time in the number of nodes. On the other hand, if we insert the nodes with the keys 4, 2, 6, 1, 3, 5, 7 in that order, we get a BST that looks like a balanced tree:

```
    4
   / \
  2   6
 / \ / \
1  3 5  7
```

This BST is called a balanced BST, and it has the best performance for search, insertion, and deletion operations, because they take logarithmic time in the number of nodes. A balanced BST is also called a height-balanced BST, because the difference between the heights of the left and right subtrees of any node is at most one. The height of a BST is the length of the longest path from the root to a leaf node.

There are different ways to implement a BST, such as using arrays, linked lists, or pointers. The most common way is to use a node class that has three attributes: a key, a value, and two pointers to the left and right children. Here is an example of a node class in Python:

```python
class Node:
  def __init__(self, key, value=None):
    self.key = key
    self.value = value
    self.left = None
    self.right = None
```

To create a BST, we can use a tree class that has a root attribute, and methods for search, insertion, and



## Unit 7 - Graphs

A graph is a collection of vertices (or nodes) and edges (or links) that connect some pairs of vertices. Graphs are used to model various types of networks, such as social networks, communication networks, transportation networks, etc.

Some basic concepts and terminology related to graphs are:

- A vertex is an entity that can have a name, a value, or some other attributes. Vertices are also called nodes or points.
- An edge is a connection between two vertices. Edges are also called links or lines.
- A path is a sequence of edges that connects two vertices. A path can be simple (no repeated vertices) or non-simple (some vertices are repeated).
- A cycle is a path that starts and ends at the same vertex. A cycle can be simple (no repeated edges) or non-simple (some edges are repeated).
- A graph is connected if there is a path between any two vertices. A graph is disconnected if there are some pairs of vertices that have no path between them.
- A subgraph is a graph that consists of some vertices and edges of another graph. A subgraph can be proper (not equal to the original graph) or improper (equal to the original graph).
- A graph is complete if there is an edge between every pair of vertices. A complete graph with n vertices has n(n-1)/2 edges.
- A graph is bipartite if its vertices can be divided into two sets such that there is no edge between vertices in the same set. A bipartite graph can be complete if there is an edge between every pair of vertices in different sets.
- A graph is weighted if each edge has a numerical value associated with it. The value of an edge is also called its weight or cost.
- A graph is directed if each edge has a direction, indicating the source and the destination of the edge. A directed edge is also called an arc or an arrow.
- A graph is undirected if each edge has no direction, meaning that it can be traversed in either direction. An undirected edge is also called a line or a link.
- A graph is simple if it has no loops (edges that connect a vertex to itself) and no multiple edges (more than one edge between the same pair of vertices).
- A graph is multigraph if it has loops or multiple edges.
- A graph is mixed if it has both directed and undirected edges.
- A graph is planar if it can be drawn on a plane without any edges crossing each other. A graph is non-planar if it cannot be drawn on a plane without any edges crossing each other.
- A graph is regular if every vertex has the same degree. The degree of a vertex is the number of edges incident to it. The degree of a vertex in a directed graph is the sum of its in-degree (the number of edges coming into it) and its out-degree (the number of edges going out of it).
- A graph is Eulerian if it has a cycle that contains every edge exactly once. A graph is Hamiltonian if it has a cycle that contains every vertex exactly once.
- A graph is a tree if it is connected and has no cycles. A tree is a special type of graph that has a hierarchical structure. A tree has a root (a vertex with no incoming edges), leaves (vertices with no outgoing edges), and internal nodes (vertices with both incoming and outgoing edges).
- A graph is a forest if it is a collection of trees. A forest is a special type of graph that has no cycles. A forest can be disconnected or connected. A connected forest is also called a spanning tree.



# Unit 7 - Graphs

## Definition and terminology

- A **graph** is a mathematical structure that consists of a set of **vertices** (or nodes) and a set of **edges** (or links) that connect pairs of vertices.
- A graph can be represented by a diagram, where vertices are drawn as points or circles, and edges are drawn as lines or curves connecting the vertices.
- A graph can also be represented by an **adjacency matrix**, where each row and column corresponds to a vertex, and each entry indicates whether there is an edge between the corresponding vertices or not.
- A graph can be **directed** or **undirected**, depending on whether the edges have a direction or not. A directed edge is drawn as an arrow pointing from one vertex to another, while an undirected edge is drawn as a line without arrows.
- A graph can be **weighted** or **unweighted**, depending on whether the edges have a numerical value or not. A weighted edge is drawn with a label indicating its value, while an unweighted edge has no label.
- A graph can be **simple** or **non-simple**, depending on whether it has multiple edges or loops or not. A multiple edge is an edge that connects the same pair of vertices more than once, while a loop is an edge that connects a vertex to itself. A simple graph has no multiple edges or loops, while a non-simple graph may have them.
- A graph can be **connected** or **disconnected**, depending on whether there is a path between any pair of vertices or not. A path is a sequence of edges that connects a sequence of vertices, where each edge is adjacent to the previous and next vertex in the sequence. A connected graph has a path between any pair of vertices, while a disconnected graph may have some pairs of vertices that are not connected by any path.
- A graph can be **cyclic** or **acyclic**, depending on whether it has a cycle or not. A cycle is a path that starts and ends at the same vertex, and does not repeat any other vertex or edge. A cyclic graph has at least one cycle, while an acyclic graph has no cycles.
- A graph can be **complete** or **incomplete**, depending on whether it has all possible edges or not. A complete graph has an edge between every pair of distinct vertices, while an incomplete graph may have some pairs of vertices that are not connected by any edge.
- A graph can be **bipartite** or **non-bipartite**, depending on whether it can be partitioned into two sets of vertices such that no edge connects two vertices in the same set. A bipartite graph can be drawn with the vertices in two distinct regions, such that all edges cross the boundary between the regions, while a non-bipartite graph cannot be drawn in this way.



# Representation of graphs

- A graph is a mathematical structure that consists of a set of vertices and a set of edges that connect pairs of vertices.
- A graph can be represented in different ways, such as using an adjacency matrix, an adjacency list, or an incidence matrix.
- An adjacency matrix is a square matrix of size n x n, where n is the number of vertices in the graph. The entry in the i-th row and j-th column of the matrix is 1 if there is an edge between vertex i and vertex j, and 0 otherwise.
- An adjacency list is a collection of lists, one for each vertex in the graph. The list for vertex i contains the names or indices of the vertices that are adjacent to i, i.e., that share an edge with i.
- An incidence matrix is a rectangular matrix of size n x m, where n is the number of vertices and m is the number of edges in the graph. The entry in the i-th row and j-th column of the matrix is 1 if vertex i is incident to edge j, and 0 otherwise.
- An example of a graph and its different representations is shown below:

graph

- The adjacency matrix of the graph is:

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 1 | 0 | 1 | 0 |
| B | 1 | 0 | 1 | 0 | 1 |
| C | 0 | 1 | 0 | 1 | 0 |
| D | 1 | 0 | 1 | 0 | 1 |
| E | 0 | 1 | 0 | 1 | 0 |

- The adjacency list of the graph is:

| Vertex | Adjacent vertices |
|--------|-------------------|
| A      | B, D              |
| B      | A, C, E           |
| C      | B, D              |
| D      | A, C, E           |
| E      | B, D              |

- The incidence matrix of the graph is:

|   | e1 | e2 | e3 | e4 | e5 | e6 |
|---|----|----|----|----|----|----|
| A | 1  | 0  | 0  | 1  | 0  | 0  |
| B | 1  | 1  | 0  | 0  | 1  | 0  |
| C | 0  | 1  | 1  | 0  | 0  | 0  |
| D | 0  | 0  | 1  | 1  | 0  | 1  |
| E | 0  | 0  | 0  | 0  | 1  | 1  |

- The choice of representation depends on the type and size of the graph, and the operations that need to be performed on it. For example, adjacency matrices are easy to use for checking the existence of an edge, but they require more space and time for adding or deleting vertices or edges. Adjacency lists are more efficient for sparse graphs, where the number of edges is much less than the number of possible edges, but they require more time for searching for an edge. Incidence matrices are useful for representing bipartite graphs, where the vertices can be divided into two disjoint sets, but they require more space than adjacency matrices or lists.



# Multigraphs

- A **multigraph** is a graph that allows **multiple edges** (also called parallel edges) between the same pair of vertices. A multigraph does not allow **loops**, which are edges that connect a vertex to itself .
- A multigraph can be represented by a **pair** of sets: G = (V, E), where V is the set of vertices and E is a **multiset** of unordered pairs of vertices, called edges .
- A multigraph can also be represented by an **adjacency matrix**, which is a square matrix A of size n x n, where n is the number of vertices. The entry A[i][j] is the number of edges between vertices i and j. The matrix is **symmetric** since the graph is undirected.
- A multigraph can be **visualized** by drawing the vertices as points and the edges as curves connecting the vertices. If there are multiple edges between two vertices, they are drawn as separate curves. The order and shape of the curves do not matter .
- A multigraph is a **generalization** of a simple graph, which is a graph that does not allow multiple edges or loops. A simple graph is a special case of a multigraph where the multiset E is a set, i.e., no repeated elements .
- A multigraph can be **converted** to a simple graph by removing the extra edges between any pair of vertices. This process may result in a loss of information about the original multigraph.
- A multigraph can be **used** to model situations where there are different types of relationships or connections between the same entities, such as roads, flights, or communication channels .



# Bipartite Graphs

- A **bipartite graph** is a graph whose vertices can be divided into two disjoint and independent sets, such that every edge connects a vertex in one set to a vertex in the other set .
- The two sets are usually called the **parts** of the graph, and are denoted by and .
- A bipartite graph can also be defined as a graph that is **two-colorable**, meaning that the vertices can be colored with two colors such that no two adjacent vertices have the same color .
- A bipartite graph is a special case of a **k-partite graph** with .
- A **complete bipartite graph** is a bipartite graph where every vertex in one part is adjacent to every vertex in the other part. It is denoted by , where and are the sizes of the two parts.
- A **bipartite matching** is a set of edges in a bipartite graph such that no two edges share a common vertex. A **maximum bipartite matching** is a bipartite matching with the largest possible number of edges.
- A **perfect matching** is a bipartite matching that covers all the vertices of the graph. A bipartite graph has a perfect matching if and only if it satisfies the **Hall's condition**, which states that for every subset of vertices in one part, the number of neighbors in the other part is at least as large as the size of the subset.
- Bipartite graphs are mostly used in modeling relationships, especially between two entire separate classes of object. For example, a bipartite graph can represent the preferences of students and schools in a college admission problem, or the assignments of workers and tasks in a scheduling problem.



# Planar Graphs

- A **planar graph** is a graph that can be drawn on a plane (a flat surface) such that no two edges cross each other.
- A **plane graph** is a planar graph with a specific drawing on a plane.
- A plane graph divides the plane into regions called **faces**.
- The **boundary** of a face is the cycle of edges that enclose it.
- The **degree** of a face is the number of edges on its boundary.
- The **outer face** of a plane graph is the unbounded region that contains the infinite part of the plane.
- A **planar embedding** of a graph is a mapping that assigns a point in the plane to each vertex and a curve in the plane to each edge, such that the curves do not intersect except at their endpoints.
- A graph is planar if and only if it has a planar embedding.
- A graph that is not planar is called **non-planar**.
- A **subgraph** of a graph is a graph whose vertices and edges are subsets of the original graph.
- A **minor** of a graph is a graph that can be obtained from a subgraph by contracting edges, i.e., replacing two adjacent vertices with a single vertex and removing any parallel edges.
- A **homeomorphism** of a graph is a graph that can be obtained from the original graph by subdividing edges, i.e., replacing an edge with a path of two or more edges.
- Two graphs are **homeomorphic** if they can be obtained from each other by homeomorphisms.
- A **Kuratowski subgraph** of a graph is a subgraph that is homeomorphic to either K<sub>5</sub> (the complete graph on five vertices) or K<sub>3,3</sub> (the complete bipartite graph on six vertices).
- **Kuratowski's theorem** states that a graph is planar if and only if it does not contain a Kuratowski subgraph.
- A **planar separator theorem** is a theorem that states that any planar graph can be divided into smaller parts by removing a small number of vertices.
- A **dual graph** of a plane graph is a graph that has a vertex for each face of the original graph and an edge for each pair of faces that share an edge on their boundary.
- A **Euler's formula** states that for any connected plane graph with n vertices, e edges, and f faces, n - e + f = 2.
- A **Platonic solid** is a convex polyhedron (a solid with flat faces) that is regular, i.e., all its faces are congruent regular polygons and all its vertices have the same degree.
- There are exactly five Platonic solids: the tetrahedron, the cube, the octahedron, the dodecahedron, and the icosahedron.
- The **dual** of a Platonic solid is another Platonic solid that has a vertex for each face of the original solid and a face for each vertex of the original solid.
- The **Four color theorem** states that any plane graph can be colored with at most four colors such that no two adjacent vertices have the same color.
- The **Five color theorem** states that any plane graph can be colored with at most five colors such that no two adjacent vertices have the same color.
- The **Six color theorem** states that any planar graph can be colored with at most six colors such that no two adjacent vertices have the same color.
- The **chromatic number** of a graph is the minimum number of colors needed to color the graph such that no two adjacent vertices have the same color.
- The **chromatic polynomial** of a graph is a polynomial that counts the number of ways to color the graph with k colors for any positive integer k.
- The **girth** of a graph is the length of the shortest cycle in the graph.
- The **outerplanar graph** is a graph that can be drawn on a plane such that all the vertices are on the outer face.
- The



# Isomorphism and Homeomorphism of graphs

## Isomorphism

- Two graphs G and H are **isomorphic** if there is a **bijection** (one-to-one and onto) f from the vertex set of G to the vertex set of H such that two vertices u and v are adjacent in G if and only if f(u) and f(v) are adjacent in H.
- Isomorphism preserves the **structure** and **properties** of graphs, such as the number of vertices, the number of edges, the degree sequence, the connectivity, the cycles, etc.
- Isomorphic graphs are **equivalent** in terms of graph theory, and they are often denoted by G ≅ H.
- To check if two graphs are isomorphic, we can try to find an isomorphism f by **matching** the vertices of G and H according to their degrees and neighborhoods, or by using some **invariants** (properties that are preserved under isomorphism) to rule out the possibility of isomorphism.
- For example, the following two graphs are isomorphic, and one possible isomorphism is f(a) = 1, f(b) = 2, f(c) = 3, f(d) = 4, f(e) = 5.

isomorphic graphs

## Homeomorphism

- A **subdivision** of a graph G is a graph obtained by replacing each edge of G by a path of one or more edges, such that no new vertices are introduced except on edges.
- A **smoothing** of a graph G is an inverse operation of subdivision, that is, removing a vertex of degree 2 and replacing the two edges incident to it by a single edge.
- Two graphs G and H are **homeomorphic** if there is a graph isomorphism from some subdivision of G to some subdivision of H.
- Homeomorphism is a weaker notion of equivalence than isomorphism, as it allows the graphs to have different numbers of vertices and edges, as long as they have the same **topological** shape.
- Homeomorphic graphs have the same **Euler characteristic**, **genus**, **crossing number**, and **planarity**.
- To check if two graphs are homeomorphic, we can try to find a homeomorphism by **subdividing** or **smoothing** the edges of G and H until they have the same structure, or by using some **invariants** (properties that are preserved under homeomorphism) to rule out the possibility of homeomorphism.
- For example, the following two graphs are homeomorphic, and one possible homeomorphism is obtained by subdividing the edge bd in G and the edge 24 in H, and then matching the vertices as follows: f(a) = 1, f(b) = 2, f(c) = 3, f(d) = 4, f(e) = 5, f(x) = y.

homeomorphic graphs

: Isomorphism and Homeomorphism of graphs - tutorialspoint.com
: Homeomorphism (graph theory) - Wikipedia



# Euler and Hamiltonian paths

- Euler and Hamiltonian paths are two types of paths in graphs that have different properties and applications.
- A **path** in a graph is a sequence of vertices connected by edges, such that no vertex is repeated.
- A **cycle** in a graph is a path that starts and ends at the same vertex, such that no other vertex is repeated.

## Euler paths and cycles

- An **Euler path** is a path that passes through every **edge** exactly once. If it ends at the initial vertex then it is an **Euler cycle**.
- For example, the graph below has an Euler path from A to D, and an Euler cycle from A to A.

Euler path and cycle

- An Euler path or cycle can exist both in a directed and undirected graph, as long as the graph is connected and has no isolated vertices.
- A necessary and sufficient condition for the existence of an Euler path or cycle in a graph is based on the degrees of the vertices.
  - A graph has an Euler cycle if and only if every vertex has an **even degree**.
  - A graph has an Euler path but not an Euler cycle if and only if exactly two vertices have an **odd degree**, and these are the endpoints of the path.
  - A graph has no Euler path or cycle if and only if more than two vertices have an **odd degree**.

## Hamiltonian paths and cycles

- A **Hamiltonian path** is a path that passes through every **vertex** exactly once. If it ends at the initial vertex then it is a **Hamiltonian cycle**.
- For example, the graph below has a Hamiltonian path from A to E, and a Hamiltonian cycle from A to A.

Hamiltonian path and cycle

- A Hamiltonian path or cycle can exist both in a directed and undirected graph, as long as the graph is connected and has no isolated vertices.
- Unlike Euler paths and cycles, there is no simple necessary and sufficient condition for the existence of a Hamiltonian path or cycle in a graph. However, there are some sufficient conditions that can be used to check if a graph has a Hamiltonian path or cycle, such as the following:
  - If a graph has **n** vertices and the degree of every vertex is at least **n/2**, then the graph has a Hamiltonian cycle. This is known as **Dirac's theorem**.
  - If a graph has **n** vertices and the sum of the degrees of any two non-adjacent vertices is at least **n**, then the graph has a Hamiltonian cycle. This is known as **Ore's theorem**.
  - If a graph is **complete**, meaning that every pair of vertices is connected by an edge, then the graph has a Hamiltonian cycle. This is a special case of Dirac's theorem.

## Applications of Euler and Hamiltonian paths and cycles

- Euler and Hamiltonian paths and cycles have various applications in different fields, such as computer science, mathematics, engineering, biology, and more. Some examples are:
  - The **traveling salesman problem** is a famous optimization problem that asks for the shortest Hamiltonian cycle in a weighted graph, where the weights represent the distances or costs between the vertices. This problem has applications in logistics, scheduling, routing, and more.
  - The **Chinese postman problem** is another optimization problem that asks for the shortest Euler cycle or path in a weighted graph, where the weights represent the distances or costs between the edges. This problem has applications in mail delivery, garbage collection, street sweeping, and more.
  - The **de Bruijn sequence** is a cyclic sequence of symbols that contains every possible subsequence of a given length exactly once. For example, the de Bruijn sequence of length 2 over the alphabet {0, 1} is 00110. This sequence can be constructed by finding an Euler cycle in a de Bruijn graph, which is a directed graph where the vertices are all possible subsequences of a given length, and the edges are labeled by the symbols that extend the subsequences. This sequence has applications in coding theory, cryptography, combinatorics, and more.
  - The **genome assembly problem** is a problem in bioinformatics that asks for the reconstruction of a DNA sequence from a set of overlapping fragments. This problem can be modeled by finding a Hamiltonian path in a de Bruijn



# Graph coloring

- Graph coloring is the procedure of assigning colors to each vertex of a graph such that no two adjacent vertices have the same color .
- The objective is to minimize the number of colors while coloring a graph .
- The smallest number of colors required to color a graph is called its chromatic number    .
- The chromatic number of a graph is denoted by χ(G) .
- A graph that can be colored with k colors is called k-colorable .
- A graph that can be colored with two colors is called bipartite .
- A proper coloring of a graph is a coloring that uses the minimum number of colors possible  .
- A graph that has a proper coloring with k colors is called k-chromatic .
- Graph coloring is closely related to the concept of an independent set .
- An independent set of a graph is a set of vertices that are not adjacent to each other .
- If a graph is properly colored, the vertices that are assigned a particular color form an independent set .
- Graph coloring has many applications in scheduling, map coloring, register allocation, etc  .
- There are different algorithms for graph coloring, such as greedy algorithm, backtracking algorithm, Welsh-Powell algorithm, etc   .



## Unit 8 - Recurrence Relation & Generating function

- A **recurrence relation** is an equation that defines a sequence recursively: each term of the sequence is defined as a function of the preceding terms.
- A **generating function** is a formal power series that encodes the information of a sequence: the coefficient of x^n in the generating function is the n-th term of the sequence.
- Recurrence relations and generating functions are useful tools for analyzing and solving problems involving sequences, such as counting, combinatorics, recurrence, and algorithms.

### Examples of recurrence relations and generating functions

- The **Fibonacci sequence** is defined by the recurrence relation F_n = F_(n-1) + F_(n-2), with initial conditions F_0 = 0 and F_1 = 1. The generating function for the Fibonacci sequence is F(x) = x/(1-x-x^2).
- The **factorial sequence** is defined by the recurrence relation n! = n * (n-1)!, with initial condition 0! = 1. The generating function for the factorial sequence is F(x) = e^x / (1-x).
- The **binomial coefficients** are defined by the recurrence relation C(n,k) = C(n-1,k-1) + C(n-1,k), with initial conditions C(n,0) = C(n,n) = 1. The generating function for the binomial coefficients is F(x) = (1+x)^n.

### Methods for solving recurrence relations and finding generating functions

- To solve a recurrence relation, one can try to find a **closed-form expression** for the n-th term of the sequence, or a **general formula** that involves some parameters. Some common methods for finding closed-form expressions are:
  - **Guess and verify**: make an educated guess based on some patterns or observations, and then prove it by induction or substitution.
  - **Characteristic equation**: transform the recurrence relation into a polynomial equation, and then find its roots and use them to construct the solution.
  - **Generating function**: multiply both sides of the recurrence relation by x^n and sum over all n, and then manipulate the resulting equation to find the generating function, and then use partial fractions, Taylor series, or other techniques to find the coefficients.
- To find a generating function for a sequence, one can try to find a **pattern** or a **formula** for the coefficients, and then use some properties or operations of generating functions to construct the power series. Some common properties and operations of generating functions are:
  - **Linearity**: if F(x) and G(x) are generating functions for sequences a_n and b_n, respectively, then F(x) + G(x) is the generating function for a_n + b_n, and c * F(x) is the generating function for c * a_n, where c is a constant.
  - **Shift**: if F(x) is the generating function for a_n, then x * F(x) is the generating function for a_(n+1), and x^k * F(x) is the generating function for a_(n+k), where k is a positive integer.
  - **Differentiation**: if F(x) is the generating function for a_n, then F'(x) is the generating function for n * a_n, and F^(k)(x) is the generating function for n! / (n-k)! * a_n, where k is a non-negative integer.
  - **Multiplication**: if F(x) and G(x) are generating functions for sequences a_n and b_n, respectively, then F(x) * G(x) is the generating function for the **convolution** of a_n and b_n, which is defined as c_n = sum_(i=0)^n a_i * b_(n-i).
  - **Composition**: if F(x) and G(x) are generating functions for sequences a_n and b_n, respectively, then F(G(x)) is the generating function for the **composition** of a_n and b_n, which is defined as c_n = sum_(i=0)^n a_i * b_n^i.



# Recursive definition of functions

- A recursive definition of a function is a way of defining the value of a function for some inputs in terms of the values of the same function for other inputs, usually smaller or simpler.
- A recursive definition of a function consists of two parts: a base case and a recursive step.
- The base case specifies the value of the function for some simple or initial inputs, without referring to the function itself.
- The recursive step specifies the value of the function for any other input in terms of the values of the function for smaller or simpler inputs, using the function itself.
- A recursive definition of a function is valid if it is well-defined, meaning that every input has a unique value and there is no infinite recursion.
- A recursive definition of a function is useful for describing functions that have a natural or intuitive structure, such as the factorial function, the Fibonacci sequence, the Ackermann function, etc  .
- A recursive definition of a function can be converted into an iterative or non-recursive definition using a loop or a stack.
- A recursive definition of a function can also be used to define sets, sequences, relations, algorithms, grammars, etc.

: Recursive definition - Wikipedia
: Recursive Functions - Stanford Encyclopedia of Philosophy
: Recursive function | mathematics | Britannica



# Recursive algorithms

A recursive algorithm is an algorithm that calls itself, either directly or indirectly, to solve a smaller instance of the same problem. A recursive algorithm must have a base case, which is a condition that terminates the recursion, and a recursive step, which is a rule that reduces the problem size and makes a recursive call.

## Examples of recursive algorithms

Some examples of problems that can be solved easily by recursive algorithms are:

- Factorial: The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. The factorial of 0 is defined to be 1. A recursive algorithm to compute n! is:

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
    return merge(left, right) # merge the two sorted halves
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

## Advantages and disadvantages of recursive algorithms

Some advantages of recursive algorithms are:

- They are simple and elegant, and can reduce the complexity of the code.
- They can handle dynamic data structures such as trees and graphs easily.
- They can express some mathematical concepts and patterns naturally.

Some disadvantages of recursive algorithms are:

- They may cause stack overflow, which is an error that occurs when the call stack exceeds its limit due to too many recursive calls.
- They may have a high time and space complexity, which means they can be slower and consume more memory than iterative algorithms.
- They may be difficult to debug and understand, especially for complex problems.



# Method of solving recurrences

A recurrence relation is an equation that defines a sequence recursively, that is, each term of the sequence is expressed in terms of previous terms. Recurrence relations are often used to model the time complexity of recursive algorithms, such as divide and conquer algorithms.

There are several methods of solving recurrence relations, such as:

- **Forward substitution**: This method involves solving the recurrence relation for n = 0, 1, 2, ... until a pattern is observed. Then, a guess is made for the general form of the solution and verified by induction.
- **Recursion tree**: This method involves converting the recurrence relation into a tree, where each node represents the cost incurred at each level of recursion. The total cost is then obtained by summing up the costs of all the nodes .
- **Master theorem**: This method is applicable for a special class of divide and conquer recurrences of the form T(n) = aT(n/b) + f(n), where a, b, and f(n) are constants or functions. The master theorem provides a formula for the asymptotic behavior of T(n) based on the comparison of f(n) and n^(log_b a).
- **Akra-Bazzi method**: This method is a generalization of the master theorem that can handle more general forms of divide and conquer recurrences, such as T(n) = g(n) + a_1T(n/b_1) + ... + a_kT(n/b_k), where g(n) and a_i are constants or functions and b_i are constants.
- **Generating functions**: This method involves finding a function that generates the terms of the sequence as its coefficients, and then manipulating the function algebraically or analytically to obtain a closed-form expression for the sequence .



## Unit 9 - Combinatorics

Combinatorics is the branch of mathematics that studies the ways of counting, arranging, and selecting objects from a given set or collection. Some of the topics covered in this unit are:

- **Factorial notation**: The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120. The factorial of 0 is defined to be 1, that is, 0! = 1.
- **Permutations**: A permutation of a set of objects is an ordered arrangement of those objects. For example, the permutations of the set {a, b, c} are abc, acb, bac, bca, cab, and cba. The number of permutations of n distinct objects is n!. The number of permutations of n objects taken r at a time, denoted by P(n, r), is n! / (n - r)!. For example, P(5, 3) = 5! / (5 - 3)! = 60.
- **Combinations**: A combination of a set of objects is an unordered selection of those objects. For example, the combinations of the set {a, b, c} taken 2 at a time are ab, ac, and bc. The number of combinations of n objects taken r at a time, denoted by C(n, r) or (n r), is n! / (r! (n - r)!). For example, C(5, 3) = 5! / (3! 2!) = 10.
- **Binomial theorem**: The binomial theorem is a formula that gives the expansion of a binomial expression raised to a positive integer power. For example, (x + y)^3 = x^3 + 3x^2y + 3xy^2 + y^3. The general form of the binomial theorem is:

  (x + y)^n = C(n, 0)x^n + C(n, 1)x^(n-1)y + C(n, 2)x^(n-2)y^2 + ... + C(n, n)y^n

  where C(n, r) are the binomial coefficients that can be arranged in a triangular pattern called Pascal's triangle.
- **Counting principles**: The counting principles are rules that help us to find the number of possible outcomes of a compound event. Some of the counting principles are:

  - **Multiplication principle**: If an event can occur in m ways and another event can occur in n ways, then the number of ways that both events can occur is m x n.
  - **Addition principle**: If an event can occur in m ways and another event can occur in n ways, and the two events are mutually exclusive, then the number of ways that either event can occur is m + n.
  - **Inclusion-exclusion principle**: If an event can occur in m ways and another event can occur in n ways, and the two events are not mutually exclusive, then the number of ways that either event can occur is m + n - k, where k is the number of ways that both events can occur.



# Introduction for the notes of the Unit 9 - Combinatorics in the subject of Discrete Structures & Theory of Logic

- Combinatorics is the branch of mathematics that studies finite or countable discrete structures.
- Combinatorics can be used to analyze many problems in computer science, such as cryptography, coding theory, graph algorithms, and complexity theory.
- Combinatorics can also be applied to other fields, such as biology, chemistry, physics, and social sciences.
- Some of the main topics in combinatorics are:

  - Counting principles: How to count the number of possible outcomes or arrangements of a given situation, such as permutations, combinations, binomial coefficients, and inclusion-exclusion principle.
  - Recurrence relations: How to define a sequence or a function by relating its terms or values to previous ones, such as Fibonacci numbers, Catalan numbers, and generating functions.
  - Pigeonhole principle: How to show that a certain condition must hold when there are more objects than containers, such as the birthday paradox, Ramsey theory, and Dirichlet's box principle.
  - Combinatorial proofs: How to prove a mathematical statement by using combinatorial arguments, such as double counting, bijections, induction, and combinatorial identities.
  - Combinatorial designs: How to construct and analyze finite arrangements of objects that satisfy certain properties or constraints, such as Latin squares, block designs, and error-correcting codes.



# Counting Techniques for the notes of the Unit 9 - Combinatorics in the subject of Discrete Structures & Theory of Logic

- Combinatorics is the branch of mathematics that deals with the study of finite or countable discrete structures, such as sets, graphs, permutations, combinations, etc. 
- Combinatorics helps us to count the number of objects in a set quickly, to estimate the complexity of algorithms, to solve problems in discrete probability, and to analyze various combinatorial structures.  
- Counting techniques are the methods that we use to find the number of possible outcomes or arrangements of a given situation or problem. 
- Some of the basic counting techniques are:

  - The Rule of Products: If there are $n_1$ ways to do task 1, and $n_2$ ways to do task 2, and so on, then there are $n_1 \times n_2 \times \cdots \times n_k$ ways to do all the tasks in sequence. 
  - The Rule of Sums: If there are $n_1$ ways to do task 1, and $n_2$ ways to do task 2, and so on, and the tasks are mutually exclusive, then there are $n_1 + n_2 + \cdots + n_k$ ways to do any one of the tasks. 
  - The Rule of Exponents: If there are $n$ ways to do a task, and the task is repeated $k$ times, then there are $n^k$ ways to do the task $k$ times. 
  - Factorials: The number of ways to arrange $n$ distinct objects in a row is $n! = n \times (n-1) \times \cdots \times 2 \times 1$. 
  - Permutations: The number of ways to choose and arrange $k$ objects out of $n$ distinct objects is $P(n,k) = n!/(n-k)!$. 
  - Combinations: The number of ways to choose $k$ objects out of $n$ distinct objects, without regard to order, is $C(n,k) = n!/(k!(n-k)!)$. 
  - Binomial Coefficients: The number of ways to choose $k$ objects out of $n$ identical objects, without regard to order, is ${n \choose k} = (n+k-1)!/(k!(n-1)!)$. 
  - Generalized Permutations and Combinations: The number of ways to choose and arrange $k$ objects out of $n$ objects, where some of the objects are identical, is $P(n,k) = n!/(n_1!n_2!\cdots n_r!)$, where $n_1, n_2, \cdots, n_r$ are the number of identical objects of each type. The number of ways to choose $k$ objects out of $n$ objects, where some of the objects are identical, without regard to order, is $C(n,k) = (n+k-1)!/(n_1!n_2!\cdots n_r!k!)$, where $n_1, n_2, \cdots, n_r$ are the number of identical objects of each type. 
  - The Pigeonhole Principle: If $n$ objects are placed into $k$ boxes, where $n > k$, then there is at least one box that contains more than one object. 

- Some examples of counting problems are:

  - How many different license plates can be made using three letters followed by three digits? 
    - Answer: By the rule of products, there are $26 \times 26 \times 26 \times 10 \times 10 \times 10 = 17576000$ ways.
  - How many different ways can a committee of 5 people be chosen from a group of 10 people? 
    - Answer: By the formula for combinations, there are $C(10,5) = 10!/(5!5!) = 252$ ways.
  - How many different ways can 10 balls be distributed



# Pigeonhole Principle

The pigeonhole principle is a simple but powerful idea that can be used to prove the existence of certain mathematical facts. The principle states that if n items are put into m containers, with n > m, then at least one container must contain more than one item. The items are called pigeons and the containers are called pigeonholes.

The principle can be illustrated by a simple example. Suppose you have 10 pigeons and 9 pigeonholes. How can you distribute the pigeons into the pigeonholes? No matter how you do it, you will end up with at least one pigeonhole that has more than one pigeon. This is because 10 is greater than 9, so there are more pigeons than pigeonholes.

The principle can also be applied to other situations, such as colors, numbers, shapes, etc. For example, suppose you have a drawer with 10 socks, 5 of them are red and 5 of them are blue. How many socks do you need to pull out of the drawer to guarantee that you have a matching pair? Using the pigeonhole principle (m = 2 socks, using one pigeonhole per color), you need to pull only three socks from the drawer (n = 3 items). Either you have three of one color, or you have two of one color and one of the other.

The pigeonhole principle has many generalizations and applications in mathematics, such as combinatorics, number theory, geometry, graph theory, etc. Here are some examples of the pigeonhole principle in action:

- If you have n pigeons in k holes, and (n/k) is not an integer, then some hole must have strictly more than (n/k) pigeons. For example, if you have 16 pigeons in 5 holes, then some hole must have at least 4 pigeons.
- If you have n points in a unit square, then some pair of points must be at most \\sqrt{2}/n apart. This is because you can divide the square into n equal segments, and use each segment as a pigeonhole for the points. The pigeonhole principle implies that at least one segment must have two points, which guarantees that no two points can be farther apart than \\sqrt{2}/n.
- If you have 13 people in a room, then at least two of them must have the same birthday (ignoring leap years). This is because there are only 12 possible months for a birthday, and 13 people are more than 12 months. The pigeonhole principle implies that at least one month must have two or more people with the same birthday.

