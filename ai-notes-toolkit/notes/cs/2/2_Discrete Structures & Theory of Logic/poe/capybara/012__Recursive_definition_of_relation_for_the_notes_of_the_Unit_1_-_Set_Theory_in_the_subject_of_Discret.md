### Recursive definition of relation for the notes of the Unit 1 - Set Theory in the subject of Discrete Structures & Theory of Logic.

In the study of discrete structures, set theory plays an important role. One of the key concepts in set theory is the definition of relations. In this topic, we will discuss the recursive definition of relations.

A relation between two sets A and B is a subset of the Cartesian product of A and B. The Cartesian product of A and B is defined as the set of all ordered pairs (a, b), where a is an element of A and b is an element of B.

A relation R between sets A and B can be defined recursively in the following way:

1. Base case: The empty set is a relation between any two sets A and B.

2. Recursive case: Suppose R is a relation between sets A and B. Then, we can define a new relation R' between sets A and B by adding a new ordered pair (a, b) to R if and only if some condition P(a, b) is satisfied. This condition can be any logical statement involving the elements a and b of A and B, respectively.

3. Repeat the recursive case: We can apply the recursive case as many times as needed to build up a relation between A and B.

For example, suppose we want to define a relation R between the sets A = {1, 2, 3} and B = {4, 5, 6}. We can define R recursively as follows:

- Base case: The empty set is a relation between A and B.

- Recursive case: Suppose R is a relation between A and B. Then, we can define a new relation R' between A and B by adding a new ordered pair (a, b) to R' if and only if a + b is even.

We can apply the recursive case as many times as needed to build up the relation R between A and B. Here is the resulting relation R:

R = {(1, 4), (1, 6), (2, 5), (3, 4), (3, 6)}

In summary, the recursive definition of relations is a powerful tool for defining relations between sets. It allows us to define complex relations by building them up from simpler ones using logical conditions.