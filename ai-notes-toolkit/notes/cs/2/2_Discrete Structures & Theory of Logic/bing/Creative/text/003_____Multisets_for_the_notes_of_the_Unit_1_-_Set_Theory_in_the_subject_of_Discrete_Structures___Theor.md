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