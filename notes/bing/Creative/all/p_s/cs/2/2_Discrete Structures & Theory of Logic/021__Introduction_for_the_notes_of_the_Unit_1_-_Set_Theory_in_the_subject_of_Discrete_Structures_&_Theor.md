### Introduction

- Set theory is the branch of mathematics that studies sets, which are collections of objects, such as {blue, white, red} or the (infinite) set of all prime numbers.
- Set theory is one of the foundations of discrete mathematics, as it provides the language and tools to deal with finite and discrete structures, such as logic, algorithms, graphs, cryptography, etc.
- Set theory can be developed in a rigorous and axiomatic way, to avoid the contradictions and paradoxes that arise from naive set theory.
- Some of the basic concepts and operations of set theory are:

  - A set is denoted by listing its elements within curly braces, such as {a, b, c} or {1, 2, 3, 4, 5}.
  - The order and repetition of elements in a set do not matter, so {a, b, c} = {c, a, b} = {a, a, b, c}.
  - An element x belongs to a set A if x is one of the objects in A, denoted by x ∈ A. Otherwise, x does not belong to A, denoted by x ∉ A.
  - A set A is a subset of another set B if every element of A is also an element of B, denoted by A ⊆ B. If A is a subset of B but not equal to B, then A is a proper subset of B, denoted by A ⊂ B.
  - The empty set is the set that has no elements, denoted by ∅ or {}.
  - The universal set is the set that contains all the elements under consideration, denoted by U.
  - The cardinality of a set A is the number of elements in A, denoted by |A| or n(A).
  - The power set of a set A is the set of all subsets of A, denoted by P(A).
  - The union of two sets A and B is the set of all elements that belong to either A or B, denoted by A ∪ B.
  - The intersection of two sets A and B is the set of all elements that belong to both A and B, denoted by A ∩ B.
  - The difference of two sets A and B is the set of all elements that belong to A but not to B, denoted by A - B or A \ B.
  - The complement of a set A is the set of all elements that do not belong to A, denoted by A' or A^c.
  - Two sets A and B are disjoint if they have no elements in common, i.e., A ∩ B = ∅.
  - Two sets A and B are equal if they have the same elements, i.e., A ⊆ B and B ⊆ A, denoted by A = B.
  - The Cartesian product of two sets A and B is the set of all ordered pairs (a, b) where a ∈ A and b ∈ B, denoted by A × B.

- Some examples of sets and operations are:

  - {1, 2, 3} ∪ {3, 4, 5} = {1, 2, 3, 4, 5}
  - {1, 2, 3} ∩ {3, 4, 5} = {3}
  - {1, 2, 3} - {3, 4, 5} = {1, 2}
  - {1, 2, 3}' = {x | x ∉ {1, 2, 3}}
  - P({1, 2, 3}) = {∅, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
  - |{1, 2, 3}| = 3
  - {1, 2, 3} × {a, b} = {(1, a), (1, b), (2, a), (2, b), (3, a), (3, b)}

- Some applications of set theory in discrete mathematics are:

  - Logic: Sets can be used to represent propositions, truth values, and logical connectives.
  - Relations: Sets can be used to define relations, such as equivalence, order, and function.
  - Graphs

Some possible mnemonics and learning tricks for the topic are:

- To remember the symbols for union, intersection, and difference, think of the shapes of the letters U, I, and D. U looks like a cup that can hold more elements, so it represents union. I looks like a line that can only hold common elements, so it represents intersection. D looks like a dash that can remove elements, so it represents difference.
- To remember the symbols for subset, proper subset, and equal, think of the shapes of the symbols ⊆, ⊂, and =. ⊆ looks like a container that can hold another set, so it represents subset. ⊂ looks like a container that is smaller than another set, so it represents proper subset. = looks like a balance that shows two sets are the same, so it represents equal.
- To remember the formula for the cardinality of the union of two sets, think of the word "inclusion-exclusion". |A ∪ B| = |A| + |B| - |A ∩ B|. The formula includes the cardinalities of A and B, but excludes the cardinality of their intersection, to avoid double counting.