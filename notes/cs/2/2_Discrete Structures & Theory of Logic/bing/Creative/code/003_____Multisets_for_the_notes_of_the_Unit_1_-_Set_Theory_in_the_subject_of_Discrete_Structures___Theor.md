# Multisets

- A multiset is a generalization of the concept of a set that allows for multiple instances of each element .
- The number of instances of an element in a multiset is called its multiplicity .
- A multiset is usually denoted by listing its elements, separated by commas, between curly braces, such as {a, a, b, c, b}.
- A multiset can also be represented by a function that maps each element to its multiplicity, such as f(a) = 2, f(b) = 2, f(c) = 1.
- A multiset is said to be finite if it has a finite number of elements, and infinite otherwise.
- The size of a finite multiset is the sum of the multiplicities of its elements, such as |{a, a, b, c, b}| = 5 .
- Two multisets are equal if they have the same elements with the same multiplicities, such as {a, b, b, c} = {b, a, c, b} .
- A multiset A is a subset of another multiset B if every element of A has a multiplicity less than or equal to that of B, such as {a, b, b} ⊆ {a, a, b, b, c} .
- The union of two multisets A and B is the multiset that contains every element of A and B with the maximum multiplicity, such as {a, b, b} ∪ {a, c, c} = {a, a, b, b, c, c} .
- The intersection of two multisets A and B is the multiset that contains every element of A and B with the minimum multiplicity, such as {a, b, b} ∩ {a, c, c} = {a} .
- The difference of two multisets A and B is the multiset that contains every element of A with the multiplicity reduced by that of B, such as {a, b, b} - {a, c, c} = {b, b} .
- The symmetric difference of two multisets A and B is the multiset that contains every element of A and B that does not belong to their intersection, such as {a, b, b} ⊕ {a, c, c} = {b, b, c, c} .
- The Cartesian product of two multisets A and B is the multiset of all ordered pairs (a, b) where a ∈ A and b ∈ B, such as {a, b} × {c, c, d} = {(a, c), (a, c), (a, d), (b, c), (b, c), (b, d)} .
- The power multiset of a multiset A is the multiset of all possible subsets of A, such as P({a, b, b}) = {{}, {a}, {b}, {b}, {a, b}, {a, b}, {b, b}, {a, b, b}} .
- The cardinality of a multiset A is the number of distinct elements in A, such as |{a, b, b, c}| = 3.
- The sum of two multisets A and B is the multiset that contains every element of A and B with the sum of their multiplicities, such as {a, b, b} + {a, c, c} = {a, a, a, b, b, c, c}.
- The complement of a multiset A with respect to a universal multiset U is the multiset that contains every element of U with the multiplicity reduced by that of A, such as {a, b, b}' = {c, c, d, d} if U = {a, b, c, c, d, d}.