 Here are the notes on Relations for Unit 1 - Set Theory in Discrete Structures & Theory of Logic:

### Relations

- A relation is a set of ordered pairs that connects two sets. It describes how elements in one set are connected to elements in another set.
- For sets A and B, a relation from A to B is a subset of A x B (the cartesian product of A and B).
- The elements of the ordered pairs are denoted as (a, b) where a is from set A and b is from set B.
- Example: Let A = {1, 2, 3} and B = {4, 5, 6}. Then a possible relation from A to B is R = {(1, 4), (2, 5), (3, 6)}. This connects each element in A to one element in B.
- Some types of relations:
-- Function - Every element in the first set is connected to exactly one element in the second set.
-- One-to-one - No two distinct elements in the first set are connected to the same element in the second set.
-- Onto - Every element in the second set is connected to at least one element in the first set.
-- Bijective - A relation that is both one-to-one and onto.

- Properties of relations:
-- Reflexive - Every element is connected to itself (a, a)
-- Symmetric - If a is connected to b, then b is also connected to a
-- Transitive - If a is connected to b and b is connected to c, then a is connected to c
-- Antisymmetric - Two distinct elements cannot be connected to each other

- Closure properties under set operations:
-- Union - (R U S) contains ordered pairs that are in either R or S (or both)
-- Intersection - (R N S) contains only ordered pairs that are in both R and S
-- Complement - (R') contains ordered pairs (a, b) such that (a, b) is not in R
-- Composition - (R o S) takes an ordered pair in R and pairs its second element with the element in S that corresponds to the second element in R.