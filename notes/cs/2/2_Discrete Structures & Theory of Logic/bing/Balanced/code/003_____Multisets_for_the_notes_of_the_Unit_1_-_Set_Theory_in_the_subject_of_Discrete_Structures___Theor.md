### Multisets

- A multiset is a generalization of the concept of a set that allows for multiple instances of each element. The number of instances of an element is called its multiplicity .
- A multiset is usually denoted by listing its elements, separated by commas, between curly braces. For example, {a, a, b, c, b} is a multiset with five elements, where a and b have multiplicity 2 and c has multiplicity 1.
- Unlike sets, multisets are not necessarily distinct. Two multisets are equal if and only if they have the same elements with the same multiplicities . For example, {a, b, c, b, a} = {a, a, b, b, c} but {a, b, c, b, a} ≠ {a, b, c, d, a}.
- Multisets can be empty, finite, or infinite. An empty multiset has no elements and is denoted by { } or ∅. A finite multiset has a finite number of elements. An infinite multiset has an infinite number of elements or an element with infinite multiplicity . For example, {a, a, a, ...} is an infinite multiset with one element of infinite multiplicity.
- Multisets can be operated on by various operations, such as union, intersection, difference, and sum. These operations are defined by adding or subtracting the multiplicities of the elements in the multisets . For example, if A = {a, a, b, c} and B = {b, b, c, d}, then:

  - A ∪ B = {a, a, b, b, c, c, d}, the union of A and B, which contains all the elements of A and B with the maximum multiplicity of each element.
  - A ∩ B = {b, c}, the intersection of A and B, which contains the elements that are common to A and B with the minimum multiplicity of each element.
  - A \ B = {a, a}, the difference of A and B, which contains the elements that are in A but not in B with the multiplicity of each element in A minus the multiplicity of each element in B.
  - A + B = {a, a, a, a, b, b, b, c, c, c, d}, the sum of A and B, which contains all the elements of A and B with the sum of the multiplicities of each element.