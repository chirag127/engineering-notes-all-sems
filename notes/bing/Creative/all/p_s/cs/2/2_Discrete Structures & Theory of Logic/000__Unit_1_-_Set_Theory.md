## Unit 1 - Set Theory

- Set theory is the branch of mathematical logic that studies sets, which can be informally described as collections of objects.
- Objects of any kind can be collected into a set, but set theory is mostly concerned with those that are relevant to mathematics as a whole.
- Set theory deals with the properties of well-defined collections of objects, such as numbers or functions.
- Set theory is the true study of infinity and the foundation for the rest of mathematics.

### Basic concepts and notation

- A set is a collection of distinct objects, called elements or members of the set .
- A set can be specified by listing its elements within curly braces, such as {1, 2, 3} or {a, b, c} .
- A set can also be defined by a property that all its elements satisfy, such as {x | x is an even integer} or {y | y is a vowel} .
- The order and repetition of elements do not matter in a set, so {1, 2, 3} is the same as {3, 2, 1} or {1, 1, 2, 3} .
- The symbol ∈ means "is an element of" and the symbol ∉ means "is not an element of" . For example, 2 ∈ {1, 2, 3} and 4 ∉ {1, 2, 3} .
- The symbol ⊆ means "is a subset of" and the symbol ⊂ means "is a proper subset of" . A set A is a subset of a set B if every element of A is also an element of B . A set A is a proper subset of a set B if A is a subset of B and A is not equal to B . For example, {1, 2} ⊆ {1, 2, 3} and {1, 2} ⊂ {1, 2, 3} .
- The symbol ∅ denotes the empty set, which is the set that has no elements . The empty set is a subset of every set .
- The symbol U denotes the universal set, which is the set that contains all the elements under consideration . For example, if we are talking about natural numbers, then U = {0, 1, 2, 3, ...} .
- The symbol |A| denotes the cardinality of a set A, which is the number of elements in A . For example, |{1, 2, 3}| = 3 and |∅| = 0 .
- The symbol P(A) denotes the power set of a set A, which is the set of all subsets of A . For example, P({1, 2}) = {∅, {1}, {2}, {1, 2}} .

### Set operations

- The union of two sets A and B, denoted by A ∪ B, is the set of all elements that are in A or in B or in both . For example, {1, 2, 3} ∪ {2, 4, 6} = {1, 2, 3, 4, 6} .
- The intersection of two sets A and B, denoted by A ∩ B, is the set of all elements that are in both A and B . For example, {1, 2, 3} ∩ {2, 4, 6} = {2} .
- The difference of two sets A and B, denoted by A \ B, is the set of all elements that are in

A but not in B . For example, {1, 2, 3} \ {2, 4, 6} = {1, 3} .
- The complement of a set A, denoted by A', is the set of all elements that are in the universal set U but not in A . For example, if U = {1, 2, 3, 4, 5, 6}, then {1, 2, 3}' = {4, 5, 6} .
- The Cartesian product of two sets A and B, denoted by A × B, is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B . For example, {1, 2} × {3, 4} = {(1, 3), (1, 4), (2, 3), (2, 4)} .

### Set relations

- Two sets A and B are equal, denoted by A = B, if they have the same elements . For example, {1, 2, 3} = {3, 2, 1} .
- Two sets A and B are disjoint, denoted by A ∩ B = ∅, if they have no common elements . For example, {1, 3, 5} and {2, 4, 6} are disjoint .
- A set A is a partition of a set B, denoted by A ⊢ B, if A is a collection of non-empty subsets of B such that every element of B belongs to exactly one subset of A . For example, {{1, 2}, {3, 4}, {5, 6}} is a partition of {1, 2, 3, 4, 5, 6} .

### Set functions

- A function f from a set A to a set B, denoted by f: A → B, is a rule that assigns to each element of A exactly one element of B . For example, f: {1, 2, 3} → {a, b, c} defined by f(1) = a, f(2) = b, f(3) = c is a function .
- The domain of a function f, denoted by dom(f), is the set of all elements of A that are mapped by f . For example, dom(f) = {1, 2, 3} .
- The codomain of a function f, denoted by codom(f), is the set B that f maps to . For example, codom(f) = {a, b, c} .
- The range of a function f, denoted by ran(f), is the set of all elements of B that are mapped by f . For example, ran(f) = {a, b, c} .
- A function f is injective (or one-to-one), denoted by f: A ↣ B, if different elements of A are mapped to different elements of B . For example, f: {1, 2, 3} ↣ {a, b, c} defined by f(1) = a, f(2) = b, f(3) = c is injective .
- A function f is surjective (or onto), denoted by f: A ↠ B, if every element of B is mapped by some element of A . For example, f: {1, 2, 3} ↠ {a, b, c} defined by f(1) = a, f(2) = b, f(3) = c is surjective .
- A function f is bijective (or one-to-one and onto