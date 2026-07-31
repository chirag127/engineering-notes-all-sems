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