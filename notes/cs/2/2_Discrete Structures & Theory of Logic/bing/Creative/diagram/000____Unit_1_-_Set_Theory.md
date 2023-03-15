## Unit 1 - Set Theory

- A **set** is a collection of distinct objects, called **elements** or **members** of the set.
- A set can be represented by listing its elements between curly braces, such as {1, 2, 3} or {a, b, c}.
- A set can also be described by a property that its elements satisfy, such as {x | x is an even integer} or {y | y is a vowel}.
- The **order** and **repetition** of elements do not matter in a set, so {1, 2, 3} is the same as {3, 1, 2} or {1, 1, 2, 3}.
- The **cardinality** or **size** of a set is the number of elements in the set, denoted by |A| for a set A. For example, |{1, 2, 3}| = 3 and |{a, b, c}| = 3.
- A set can be **empty**, meaning it has no elements, denoted by ∅ or {}. The cardinality of the empty set is 0, so |∅| = 0.
- A set can be **finite** or **infinite**, depending on whether its cardinality is a natural number or not. For example, {1, 2, 3} is finite, but {x | x is an even integer} is infinite.
- Two sets are **equal** if they have the same elements, regardless of how they are represented. For example, {1, 2, 3} = {3, 1, 2} and {x | x is an even integer} = {2n | n is an integer}.
- A set A is a **subset** of another set B, denoted by A ⊆ B, if every element of A is also an element of B. For example, {1, 2} ⊆ {1, 2, 3} and {a, e, i, o, u} ⊆ {y | y is a vowel}.
- A set A is a **proper subset** of another set B, denoted by A ⊂ B, if A ⊆ B and A ≠ B. For example, {1, 2} ⊂ {1, 2, 3} and {a, e, i, o, u} ⊂ {y | y is a vowel}.
- A set A is **disjoint** from another set B if they have no elements in common, meaning A ∩ B = ∅. For example, {1, 2, 3} and {4, 5, 6} are disjoint, but {1, 2, 3} and {2, 4, 6} are not.
- The **union** of two sets A and B, denoted by A ∪ B, is the set of all elements that belong to either A or B or both. For example, {1, 2, 3} ∪ {2, 4, 6} = {1, 2, 3, 4, 6}.
- The **intersection** of two sets A and B, denoted by A ∩ B, is the set of all elements that belong to both A and B. For example, {1, 2, 3} ∩ {2, 4, 6} = {2}.
- The **difference** of two sets A and B, denoted by A \ B, is the set of all elements that belong to A but not to B. For example, {1, 2, 3} \ {2, 4, 6} = {1, 3}.
- The **complement** of a set A, denoted by A<sup>c</sup> or A', is the set of all elements that do not belong to A. The complement of a set is relative to a **universal set** U, which is the set of all possible elements under consideration. For example, if U = {1, 2, 3, 4, 5, 6}, then {1, 2, 3}<sup>c</sup> = {4, 5, 6}.
- The **power set** of a set A, denoted by P(A), is the set of all subsets of A, including the empty set and A itself. For example, P({1, 2, 3}) = {∅, {1}, {2}, {3}, {