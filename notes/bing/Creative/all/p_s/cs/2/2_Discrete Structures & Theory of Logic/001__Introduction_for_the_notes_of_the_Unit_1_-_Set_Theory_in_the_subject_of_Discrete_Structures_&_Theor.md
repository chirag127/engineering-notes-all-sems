### Introduction

- Set theory is the branch of mathematics that studies sets, which are collections of objects, such as {blue, white, red} or the (infinite) set of all prime numbers.
- Sets are fundamental objects in discrete mathematics, as they can be used to model many other discrete structures, such as graphs, relations, functions, logic, etc.
- Some basic concepts and operations on sets are:

  - A set is said to contain its elements. For example, 4 is an element of the set {2,4,17,23}, and we write 4 ∈ {2,4,17,23}. If an object is not an element of a set, we write ∈. For example, 5 ∉ {2,4,17,23}.
  - Two sets are equal if they have exactly the same elements. For example, {2,4,17,23} = {17,4,23,2}, but {2,4,17,23} ≠ {2,4,17}.
  - A set is a subset of another set if every element of the first set is also an element of the second set. For example, {2,4} is a subset of {2,4,17,23}, and we write {2,4} ⊆ {2,4,17,23}. Every set is a subset of itself, and the empty set {} is a subset of any set.
  - A set is a proper subset of another set if it is a subset of the second set and not equal to it. For example, {2,4} is a proper subset of {2,4,17,23}, and we write {2,4} ⊂ {2,4,17,23}. The empty set is a proper subset of any non-empty set.
  - The union of two sets is the set of all elements that belong to either set. For example, {2,4,17,23} ∪ {5,17,23,42} = {2,4,5,17,23,42}. The union of a set and itself is the same set, and the union of a set and the empty set is the same set.
  - The intersection of two sets is the set of all elements that belong to both sets. For example, {2,4,17,23} ∩ {5,17,23,42} = {17,23}. The intersection of a set and itself is the same set, and the intersection of a set and the empty set is the empty set.
  - The complement of a set is the set of all elements that do not belong to the set. For example, if the universal set U is {1,2,3,4,5,6}, then the complement of {2,4,17,23} is {1,3,5,6}. The complement of a set is denoted by a bar over the set, such as {2,4,17,23}.
  - The difference of two sets is the set of all elements that belong to the first set but not to the second set. For example, {2,4,17,23} - {5,17,23,42} = {2,4}. The difference of a set and itself is the empty set, and the difference of a set and the empty set is the same set.
  - The symmetric difference of two sets is the set of all elements that belong to exactly one of the sets. For example, {2,4,17,23} Δ {5,17,23,42} = {2,4,5,42}. The symmetric difference of a set and itself is the empty set, and the symmetric difference of a set and the empty set is the same set.
  - The power set of a set is the set of all subsets of the set. For example, the power set of {2,4,17,23} is {{}, {2}, {4}, {17}, {23}, {2,4}, {2,17}, {2,23}, {4,17}, {4,23}, {17,23}, {2,4,17}, {2,4,23}, {2,17,23}, {4,17,23}, {2,4,17,23}}. The power set of a set is denoted by P(set), such as P({2,4,17,23}).
  - The cardinal

- Some possible mnemonics and learning tricks for the topic are:

  - To remember the symbols for union, intersection, complement, difference and symmetric difference, you can use the following phrases:

    - Union is U-shaped: ∪
    - Intersection is an X: ∩
    - Complement is a C with a bar: 
    - Difference is a minus sign: -
    - Symmetric difference is a triangle: Δ

  - To remember the properties of set operations, you can use the following acronyms:

    - Commutative: C for Change. You can change the order of the sets without changing the result. For example, A ∪ B = B ∪ A and A ∩ B = B ∩ A.
    - Associative: A for Arrange. You can arrange the parentheses without changing the result. For example, (A ∪ B) ∪ C = A ∪ (B ∪ C) and (A ∩ B) ∩ C = A ∩ (B ∩ C).
    - Distributive: D for Distribute. You can distribute one operation over another. For example, A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C).
    - Identity: I for Identity. There is an identity element for each operation that does not change the result. For example, A ∪ {} = A and A ∩ U = A, where U is the universal set.
    - Complement: C for Complement. The complement of a set is the opposite of the set. For example, A ∪  = U and A ∩  = {}.
    - De Morgan's: D for Double. You can double negate a set expression and switch the operations. For example,  (A ∪ B) =  ∩  and  (A ∩ B) =  ∪ .

  - To remember the formula for the cardinality of the union of two sets, you can use the following rhyme:

    - To find the union, add them all
    - But subtract the intersection, or you'll fall
    - For example, |A ∪ B| = |A| + |B| - |A ∩ B|, where |set| means the number of elements in the set.