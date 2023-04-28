

## Unit 1 - Set Theory

Set theory is a branch of mathematical logic that studies sets, which informally are collections of objects. Although any type of object can be collected into a set, set theory is applied most often to objects that are relevant to mathematics.

Some important concepts in set theory include:

1. **Set:** A set is a collection of distinct objects, considered as an object in its own right. For example, the numbers 1, 2, and 3 are distinct objects when considered separately, but when they are considered collectively they form a single set of size three, written {1, 2, 3}.
2. **Element:** An element is an object that is a member of a set. For example, 1 is an element of the set {1, 2, 3}.
3. **Subset:** A set A is a subset of a set B if every element of A is also an element of B. For example, {1, 2} is a subset of {1, 2, 3}.
4. **Union:** The union of two sets A and B is the set of all elements that are in A, in B, or in both. For example, the union of {1, 2} and {2, 3} is {1, 2, 3}.
5. **Intersection:** The intersection of two sets A and B is the set of all elements that are in both A and B. For example, the intersection of {1, 2} and {2, 3} is {2}.
6. **Complement:** The complement of a set A is the set of all elements that are not in A. For example, if the universal set is {1, 2, 3, 4}, then the complement of {1, 2} is {3, 4}.
7. **Cardinality:** The cardinality of a set A is the number of elements in A. For example, the cardinality of {1, 2, 3} is 3.




### Introduction for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic

- Set theory is a branch of mathematical logic that studies sets, which informally are collections of objects.
- It is the foundation of most of mathematics and is used to define and study the properties of sets and their elements.
- Set theory is used to define and study the properties of mathematical objects such as numbers, functions, and relations.
- The basic concepts of set theory include sets, elements, subsets, and operations on sets such as union, intersection, and difference.
- Set theory is also used to study the properties of infinite sets and the concept of cardinality.
- In the subject of Discrete Structures & Theory of Logic, set theory is used to study the logical foundations of mathematics and to develop formal systems for reasoning about mathematical objects.



# Combination of Sets

In the study of set theory, the combination of sets refers to the process of creating new sets by combining the elements of two or more existing sets. There are several ways to combine sets, including union, intersection, and Cartesian product.

1. **Union**: The union of two sets A and B, denoted by A ∪ B, is the set of all elements that are in A, or in B, or in both. In other words, it is the set of all elements that are in at least one of the two sets. For example, if A = {1, 2, 3} and B = {2, 3, 4}, then A ∪ B = {1, 2, 3, 4}.

2. **Intersection**: The intersection of two sets A and B, denoted by A ∩ B, is the set of all elements that are in both A and B. In other words, it is the set of all elements that are common to both sets. For example, if A = {1, 2, 3} and B = {2, 3, 4}, then A ∩ B = {2, 3}.

3. **Cartesian Product**: The Cartesian product of two sets A and B, denoted by A × B, is the set of all ordered pairs (a, b) where a is an element of A and b is an element of B. For example, if A = {1, 2} and B = {3, 4}, then A × B = {(1, 3), (1, 4), (2, 3), (2, 4)}.

These are some of the ways to combine sets in set theory. Each method has its own properties and uses, and they are commonly used in various fields of mathematics and computer science. It is important to understand these concepts and how to apply them when studying set theory and related subjects.



# Multisets

A multiset is a generalization of a set that allows multiple instances of the same element. It is also known as a bag or mset.

- Unlike a set, a multiset can have multiple instances of the same element. For example, the multiset {a, a, b} is different from the set {a, b}.
- The order of elements in a multiset does not matter, just like in a set. For example, the multisets {a, a, b} and {a, b, a} are considered the same.
- The number of times an element appears in a multiset is called its multiplicity. In the multiset {a, a, b}, the multiplicity of a is 2 and the multiplicity of b is 1.
- Multisets can be represented using set notation with the addition of a function that specifies the multiplicity of each element. For example, the multiset {a, a, b} can be represented as {a:2, b:1}.
- Operations on multisets include union, intersection, and difference. These operations are similar to the corresponding set operations, but take into account the multiplicities of the elements.
- Multisets have applications in various fields, including computer science, statistics, and combinatorics.




# Unit 1 - Set Theory: Ordered Pairs

- An ordered pair is a pair of elements where the order in which the elements are listed matters.
- The ordered pair (a, b) is different from the ordered pair (b, a) unless a = b.
- Ordered pairs are used to represent points in a Cartesian plane, where the first element represents the x-coordinate and the second element represents the y-coordinate.
- The set of all ordered pairs (x, y) where x and y are elements of two sets A and B, respectively, is called the Cartesian product of A and B, denoted by A × B.
- The Cartesian product of two sets A and B is defined as A × B = {(a, b) | a ∈ A and b ∈ B}.
- The number of elements in the Cartesian product of two finite sets A and B is equal to the product of the number of elements in A and the number of elements in B, i.e., |A × B| = |A| × |B|.
- The Cartesian product is not commutative, i.e., A × B is not necessarily equal to B × A.
- The Cartesian product is not associative, i.e., (A × B) × C is not necessarily equal to A × (B × C).
- The Cartesian product distributes over union, i.e., A × (B ∪ C) = (A × B) ∪ (A × C).
- The Cartesian product distributes over intersection, i.e., A × (B ∩ C) = (A × B) ∩ (A × C).




# Proofs of some general identities on sets

Here are some general identities on sets and their proofs:

1. **Commutative Laws**: For any sets A and B, A ∪ B = B ∪ A and A ∩ B = B ∩ A.

Proof: Let x ∈ A ∪ B. Then x ∈ A or x ∈ B. This means that x ∈ B or x ∈ A, which implies that x ∈ B ∪ A. Hence, A ∪ B ⊆ B ∪ A. Similarly, B ∪ A ⊆ A ∪ B, so A ∪ B = B ∪ A. The proof for A ∩ B = B ∩ A is similar.

2. **Associative Laws**: For any sets A, B, and C, (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C).

Proof: Let x ∈ (A ∪ B) ∪ C. Then x ∈ A ∪ B or x ∈ C. If x ∈ A ∪ B, then x ∈ A or x ∈ B. In either case, x ∈ A or x ∈ B ∪ C, which implies that x ∈ A ∪ (B ∪ C). If x ∈ C, then x ∈ B ∪ C, which implies that x ∈ A ∪ (B ∪ C). Hence, (A ∪ B) ∪ C ⊆ A ∪ (B ∪ C). Similarly, A ∪ (B ∪ C) ⊆ (A ∪ B) ∪ C, so (A ∪ B) ∪ C = A ∪ (B ∪ C). The proof for (A ∩ B) ∩ C = A ∩ (B ∩ C) is similar.

3. **Distributive Laws**: For any sets A, B, and C, A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).

Proof: Let x ∈ A ∪ (B ∩ C). Then x ∈ A or x ∈ B ∩ C. If x ∈ A, then x ∈ A ∪ B and x ∈ A ∪ C, which implies that x ∈ (A ∪ B) ∩ (A ∪ C). If x ∈ B ∩ C, then x ∈ B and x ∈ C, which implies that x ∈ A ∪ B and x ∈ A ∪ C, and hence x ∈ (A ∪ B) ∩ (A ∪ C). Hence, A ∪ (B ∩ C) ⊆ (A ∪ B) ∩ (A ∪ C). Similarly, (A ∪ B) ∩ (A ∪ C) ⊆ A ∪ (B ∩ C), so A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C). The proof for A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) is similar.




# Relations

Relations are a fundamental concept in set theory and discrete mathematics. A relation is a way to associate elements of one set with elements of another set. Here are some key points to remember about relations:

1. A relation is a subset of the Cartesian product of two sets. For example, if we have two sets A and B, a relation R from A to B is a subset of A x B.

2. A relation can be represented using an arrow diagram, where the elements of the first set are drawn on the left, the elements of the second set are drawn on the right, and arrows are drawn from elements of the first set to elements of the second set to indicate the pairs in the relation.

3. The domain of a relation is the set of all first elements of the ordered pairs in the relation. The range of a relation is the set of all second elements of the ordered pairs in the relation.

4. A relation can have various properties, such as being reflexive, symmetric, transitive, or antisymmetric. These properties are defined in terms of the ordered pairs in the relation.

5. Relations can be composed, meaning that if we have a relation R from A to B and a relation S from B to C, we can define a new relation T from A to C by composing R and S.

6. Relations can also be inverted, meaning that if we have a relation R from A to B, we can define a new relation S from B to A by inverting the ordered pairs in R.

7. Relations are a powerful tool for modeling many different types of relationships between elements of sets, and are widely used in mathematics, computer science, and other fields.




# Unit 1 - Set Theory

## Definition

- A **set** is a collection of distinct objects, considered as an object in its own right.
- Sets are usually denoted by capital letters, such as A, B, or C.
- The objects in a set are called **elements** or **members** of the set.
- The notation `a ∈ A` means that `a` is an element of the set `A`.
- The notation `b ∉ B` means that `b` is not an element of the set `B`.
- Two sets are considered **equal** if and only if they have exactly the same elements.
- The **empty set** is the set with no elements, denoted by `{}` or `∅`.
- A set can have any number of elements, including zero, one, or infinitely many.
- Sets can contain elements of any type, including numbers, letters, other sets, or even abstract concepts.


